"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class Locked:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, reason=..., timestamp=..., origin=...) -> None:
        """Locked - a model defined in Swagger"""
        ...
    
    @property
    def reason(self): # -> None:
        """Gets the reason of this Locked.


        :return: The reason of this Locked.
        :rtype: ProjectLockingReason
        """
        ...
    
    @reason.setter
    def reason(self, reason): # -> None:
        """Sets the reason of this Locked.


        :param reason: The reason of this Locked.  # noqa: E501
        :type: ProjectLockingReason
        """
        ...
    
    @property
    def timestamp(self): # -> None:
        """Gets the timestamp of this Locked.


        :return: The timestamp of this Locked.
        :rtype: datetime
        """
        ...
    
    @timestamp.setter
    def timestamp(self, timestamp): # -> None:
        """Sets the timestamp of this Locked.


        :param timestamp: The timestamp of this Locked.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def origin(self): # -> None:
        """Gets the origin of this Locked.


        :return: The origin of this Locked.
        :rtype: Origin
        """
        ...
    
    @origin.setter
    def origin(self, origin): # -> None:
        """Sets the origin of this Locked.


        :param origin: The origin of this Locked.  # noqa: E501
        :type: Origin
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
    


