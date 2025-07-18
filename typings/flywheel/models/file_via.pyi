"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class FileVia:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., method=..., type=..., name=...) -> None:
        """FileVia - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this FileVia.


        :return: The id of this FileVia.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this FileVia.


        :param id: The id of this FileVia.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def method(self): # -> None:
        """Gets the method of this FileVia.


        :return: The method of this FileVia.
        :rtype: str
        """
        ...
    
    @method.setter
    def method(self, method): # -> None:
        """Sets the method of this FileVia.


        :param method: The method of this FileVia.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def type(self): # -> None:
        """Gets the type of this FileVia.


        :return: The type of this FileVia.
        :rtype: str
        """
        ...
    
    @type.setter
    def type(self, type): # -> None:
        """Sets the type of this FileVia.


        :param type: The type of this FileVia.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this FileVia.


        :return: The name of this FileVia.
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this FileVia.


        :param name: The name of this FileVia.  # noqa: E501
        :type: str
        """
        ...
    
    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        ...
    
    def return_value(self): # -> Self:
        """Unwraps return value from model"""
        ...
    
    def to_dict(self): # -> dict[Any, Any]:
        """Returns the model properties as a dict"""
        ...
    
    def to_str(self): # -> str:
        """Returns the string representation of the model"""
        ...
    
    def __repr__(self): # -> str:
        """For `print` and `pprint`"""
        ...
    
    def __eq__(self, other) -> bool:
        """Returns true if both objects are equal"""
        ...
    
    def __ne__(self, other) -> bool:
        """Returns true if both objects are not equal"""
        ...
    
    def __getitem__(self, key): # -> Any:
        """Returns the value of key"""
        ...
    
    def __setitem__(self, key, value): # -> None:
        """Sets the value of key"""
        ...
    
    def __contains__(self, key): # -> bool:
        """Checks if the given value is a key in this object"""
        ...
    
    def keys(self): # -> dict_keys[str, str]:
        """Returns the list of json properties in the object"""
        ...
    
    def values(self): # -> Generator[Any, Any, None]:
        """Returns the list of values in the object"""
        ...
    
    def items(self): # -> Generator[tuple[str, Any], Any, None]:
        """Returns the list of json property to value mapping"""
        ...
    
    def get(self, key, default=...): # -> Any | None:
        """Get the value of the provided json property, or default"""
        ...
    


