"""User Documentation

    This is Just a implementation scheme :-
        - to organize api validations at a single place ,
        - to provide full control to developer ,
        - to iterate the api-body only once .
    **
        [x] := required to be specified
        [ ] := not required to be specified

    # == Defining Schema Specification == #
                                                                            [Copy-Paste]
    schema : dict = {
        "parameter_name" : {
            "type" : <int | float | str | list | tuple | dict | set> [x]
            "validators" : <Iterable [ list[ callables] | tuple[ callables] | set[ callables] ]> [ ]
        },
    "validators" : <Iterable [ list[ callables] | tuple[ callables] | set[ callables] ]> [ ],
    "required" : <Iterable [ list[ str< parameter_names>] | tuple[ str< parameter_names>] | set[ str< parameter_names>] ]> [ ],
    "default" : <dict < parameter_name:default_value>>,
    }
    *you may copy this above example schema template & paste in your file . modify it & use .
    NOTE :
        - if :parameter_name specified in "required" is also specified in "default",
            then "default" value for the :parameter_name won't take effect .
        - if :parameter_name specified in "required" / "default" schema specification is
            not present as `key` in schema dict, then No error is raised .

    # == Usage == #
                                                                            [Copy-Paste]
    class Validation-Class-Name(SchemaBase):
        def __init__(self, api_body: dict, schema: dict) -> type(None):
            super().__init__(api_body, schema)

        def check_Your-Function-Name(self, key, value) -> type(None):
            # Item level validation function
            # access to :-
                # self._exception | raise this exception on violation
                # self._message | format this message & pass to exception
                # self._VC | select a code from these codes & pass to exception
            pass
        def check_Your-Function-Name(self, obj:dict) -> type(None):
            # Oject(dict) level validation function
            # access to :-
                # self._exception | raise this exception on violation
                # self._message | format this message & pass to exception
                # self._VC | select a code from these codes & pass to exception
            pass
    *you may copy this above example template & paste in your file . modify it & use .
    NOTE :
        - Replace Validation-Class-Name To ClassName of your choice .
        - Replace Your-Function-Name To FunctionName of your choice .

    # == Performing Validations == #
                                                                            [Copy-Paste]
    def Your-Validation-Function-Name(api_body: dict, **kwargs) -> type(None):
        # write all your api validations here .

        # -- this is the outer scope -- #
        validator = Validation-Class-Name(api_body,schema)
        for item in api_body.items():
            validator.initialize(*item)
            # -- this is the inner scope -- #
            # ... freely call your custom validator functions here .
            # ... write your custom validation code here .
    *you may copy this above example template & paste in your file . modify it & use .
"""
