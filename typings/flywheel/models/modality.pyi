"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class Modality:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., classification=..., description=..., active=...) -> None:
        """Modality - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this Modality.

        Unique database ID

        :return: The id of this Modality.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this Modality.

        Unique database ID

        :param id: The id of this Modality.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def classification(self): # -> None:
        """Gets the classification of this Modality.


        :return: The classification of this Modality.
        :rtype: CommonClassification
        """
        ...
    
    @classification.setter
    def classification(self, classification): # -> None:
        """Sets the classification of this Modality.


        :param classification: The classification of this Modality.  # noqa: E501
        :type: CommonClassification
        """
        ...
    
    @property
    def description(self): # -> None:
        """Gets the description of this Modality.


        :return: The description of this Modality.
        :rtype: str
        """
        ...
    
    @description.setter
    def description(self, description): # -> None:
        """Sets the description of this Modality.


        :param description: The description of this Modality.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def active(self): # -> None:
        """Gets the active of this Modality.


        :return: The active of this Modality.
        :rtype: bool
        """
        ...
    
    @active.setter
    def active(self, active): # -> None:
        """Sets the active of this Modality.


        :param active: The active of this Modality.  # noqa: E501
        :type: bool
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
    


