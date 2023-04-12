
from enum import Enum, unique

class DefaultBadRequestException(Exception):
    def __init__(self, errors: dict = [dict()], custom_message=None, code=None):
        self.http_status_code = 400
        self.code = code
        self.errors = errors
        if custom_message:
            self.message = custom_message
        else:
            self.message = "Invalid Api Request"
        super().__init__(self.message)
    def __str__(self) -> str:
        return f"""
        message : {self.message},
        code : {self.code}
        """

@unique
class Codes(str, Enum):
    """Generic Codes"""
    
    DATA_TYPE_ERROR = "TYPE_ERR"
    REQUIRED = "REQUIRED"


class SchemaBase:
    def __init__(self, api_body: dict, schema: dict, exception_cls=DefaultBadRequestException) -> None:
        self._api_body, self._schema = self.__valiadted_args(api_body, schema)
        self._VC = Codes
        self._exception=exception_cls
        self._message = "Invalid {0}"
        self.__check_required(self._api_body)
        self.__apply_defaults(self._api_body)
        self.__run_object_validators(self._api_body)

    def __valiadted_args(self, api_body: dict, schema: dict):
        if not isinstance(schema, dict):
            raise Exception(f"{self.__class__.__name__} : Schema should be dict")
        if not isinstance(api_body, dict):
            raise Exception(f"{self.__class__.__name__} : api_body should be dict")
        return api_body, schema

    def __type_check(self, key, value) -> None:
        CODE = self._VC.DATA_TYPE_ERROR

        SUPPORTED_PYTHON_TYPES = (int, float, str, list, tuple, set, dict, object, bool)
        info = self._schema.get(key)
        if isinstance(info, type(None)):
            # TODO : either raise error for keys that are not defined in schema .
            # TODO : or , delete that entry from the incomming dict itself
            return
        if not isinstance(info, dict):
            raise Exception(f"Invalid schema : Field[{key}] infomation should be dict")
        if "type" not in info:
            raise Exception(f"Invalid schema : type infomation of Field[{key}] missing")
        if info["type"] in SUPPORTED_PYTHON_TYPES and not isinstance(
            value, info["type"]
        ):
            raise self._exception(
                custom_message=self._message.format(key),
                code=CODE
            )

    def __run_item_validators(self, key, value) -> type(None):
        _validators = self._schema.get(key, {}).get("validators", [])
        for func in _validators:
            if callable(func):
                func(key, value)

    def __check_required(self, obj: dict) -> None:
        """Check if all required parameters present in object"""
        CODE = self._VC.REQUIRED

        required_values = self._schema.get("required", [])
        for key in required_values:
            if key in self._schema and key not in obj:
                raise self._exception(
                        custom_message=self._message.format(key),
                        code=CODE
                    )

    def __run_object_validators(self, obj: dict) -> type(None):

        _validators = self._schema.get("validators", [])
        for func in _validators:
            if callable(func):
                func(obj)

    def __apply_defaults(self, obj: dict) -> None:
        """Apply default values"""

        default_values = self._schema.get("default", {})
        for key in default_values:
            if key not in obj:
                obj[key] = default_values[key]

    def __apply_coersion(self, key, value) -> tuple:

        info = self._schema.get(key)

        if isinstance(info, type(None)):
            # TODO : either raise error for keys that are not defined in schema .
            # TODO : or , delete that entry from the incomming dict itself
            return key, value

        if not isinstance(info, dict):
            raise Exception(f"Invalid schema : Field[{key}] infomation should be dict")

        coersion_func = info.get("coerce", lambda v: v)
        coerced_value = value
        code = self._VC.DATA_TYPE_ERROR
        if callable(coersion_func):
            try:
                coerced_value = coersion_func(value)
            except Exception:
                bad_req = self._exception()
                bad_req.message = self._message.format(key)
                bad_req.code = code
                raise bad_req

        return key, coerced_value

    def initialize(self, key, value, with_coersion=False) -> tuple:
        """Run all item level validation functions"""

        if with_coersion:
            key, value = self.__apply_coersion(key, value)
            self._api_body[key] = value
        self.__type_check(key, value)
        self.__run_item_validators(key, value)

        return key, value
