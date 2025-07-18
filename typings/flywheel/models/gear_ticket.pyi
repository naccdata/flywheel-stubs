"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class GearTicket:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., origin=..., geardoc=..., timestamp=...) -> None:
        """GearTicket - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this GearTicket.


        :return: The id of this GearTicket.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this GearTicket.


        :param id: The id of this GearTicket.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def origin(self): # -> None:
        """Gets the origin of this GearTicket.


        :return: The origin of this GearTicket.
        :rtype: Origin
        """
        ...
    
    @origin.setter
    def origin(self, origin): # -> None:
        """Sets the origin of this GearTicket.


        :param origin: The origin of this GearTicket.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def geardoc(self): # -> None:
        """Gets the geardoc of this GearTicket.


        :return: The geardoc of this GearTicket.
        :rtype: GearDocumentInput
        """
        ...
    
    @geardoc.setter
    def geardoc(self, geardoc): # -> None:
        """Sets the geardoc of this GearTicket.


        :param geardoc: The geardoc of this GearTicket.  # noqa: E501
        :type: GearDocumentInput
        """
        ...
    
    @property
    def timestamp(self): # -> None:
        """Gets the timestamp of this GearTicket.


        :return: The timestamp of this GearTicket.
        :rtype: datetime
        """
        ...
    
    @timestamp.setter
    def timestamp(self, timestamp): # -> None:
        """Sets the timestamp of this GearTicket.


        :param timestamp: The timestamp of this GearTicket.  # noqa: E501
        :type: datetime
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
    


