# we'll need a server to demonstrate an api validation
# Hence , using Flask in this case.
# One can use any python server/framework for this purpose .
from flask import Flask, request


app = Flask(__name__)
from validation_base import SchemaBase, DefaultBadRequestException

# NOTE : Your REST server must have a GLOBAL EXCEPTION HANDLER .
# since we are using Flask , we are defining a Global Exception Handler on
# the name of `DefaultBadRequestException`

@app.errorhandler(DefaultBadRequestException)
def bad_request_handler(bad_request_obj: DefaultBadRequestException):
    """400(BAD REQUEST) Exception Handler"""

    return {
        "message": bad_request_obj.message,
        "code": bad_request_obj.code
    }, 400

# This is a common check :
def check_iterable_not_emplty(key, value):
    """a simple item level validation"""
    code, message = 'EMPTY', f'Invalid {key}'
    if hasattr(value, '__len__') and len(value) < 1:
        raise DefaultBadRequestException(custom_message=message, code=code)
schema: dict = {
        "metrics": {
            "type": list,
            "validators": (check_iterable_not_emplty,),
        },
        "submission_frequency": {
            "type": str,
            "validators": (check_iterable_not_emplty,),
        },
        "submission_type": {
            "type": str,
            "validators": (check_iterable_not_emplty,),
        },
        "submission_for": {
            "type": str,
            "validators": (check_iterable_not_emplty,),
        },
        "submission_period_id": {
            "type": int,
            "validators": tuple(),
            "coerce": lambda v: int(v) if isinstance(v, (float, str)) else v,
        },
        "active": {"type": bool},
        "week_number": {"type": int, "validators":tuple()},
        "required": tuple(
            ["metrics", "submission_frequency", "submission_type", "submission_for"]
        ),
        "default": {"active": True,},
    }

class Validations(SchemaBase):...

@app.route('/test-api', methods=['POST'])
def test():
    data = request.json or {}
    validator = Validations(data, schema)
    for item in data.items():
        item = validator.initialize(*item, with_coersion=True)
        # validate each item here ...
        key, value = (*item,)
        # for e.g :-
        if key == 'metrics' and len(value) < 2:
            raise DefaultBadRequestException(
                custom_message=validator._message.format(key),
                code='MIN_METRIC_COUNT_VIOLATION'
            )
    # validate data manually here ...
    # for e.g :-
    if data["submission_frequency"] == 'WEEKLY' and data["submission_type"] != 'NORMAL':
        raise DefaultBadRequestException(
                custom_message="Invalid submission_frequency and submission_type",
                code='INVALID_COMBINATION'
            )
    return {
        "message": "validated sucessfully",
        "code": None
    }
if __name__ == '__main__':
    app.run()
