"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class MoveConflict:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, move_type=..., id=..., conflict_with=..., conflict_label=..., label=..., subject_code=...) -> None:
        """MoveConflict - a model defined in Swagger"""
        ...
    
    @property
    def move_type(self): # -> None:
        """Gets the move_type of this MoveConflict.


        :return: The move_type of this MoveConflict.
        :rtype: list[ContainerType]
        """
        ...
    
    @move_type.setter
    def move_type(self, move_type): # -> None:
        """Sets the move_type of this MoveConflict.


        :param move_type: The move_type of this MoveConflict.  # noqa: E501
        :type: list[ContainerType]
        """
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this MoveConflict.


        :return: The id of this MoveConflict.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this MoveConflict.


        :param id: The id of this MoveConflict.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def conflict_with(self): # -> None:
        """Gets the conflict_with of this MoveConflict.


        :return: The conflict_with of this MoveConflict.
        :rtype: ContainerReference
        """
        ...
    
    @conflict_with.setter
    def conflict_with(self, conflict_with): # -> None:
        """Sets the conflict_with of this MoveConflict.


        :param conflict_with: The conflict_with of this MoveConflict.  # noqa: E501
        :type: ContainerReference
        """
        ...
    
    @property
    def conflict_label(self): # -> None:
        """Gets the conflict_label of this MoveConflict.


        :return: The conflict_label of this MoveConflict.
        :rtype: str
        """
        ...
    
    @conflict_label.setter
    def conflict_label(self, conflict_label): # -> None:
        """Sets the conflict_label of this MoveConflict.


        :param conflict_label: The conflict_label of this MoveConflict.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def label(self): # -> None:
        """Gets the label of this MoveConflict.


        :return: The label of this MoveConflict.
        :rtype: str
        """
        ...
    
    @label.setter
    def label(self, label): # -> None:
        """Sets the label of this MoveConflict.


        :param label: The label of this MoveConflict.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def subject_code(self): # -> None:
        """Gets the subject_code of this MoveConflict.


        :return: The subject_code of this MoveConflict.
        :rtype: str
        """
        ...
    
    @subject_code.setter
    def subject_code(self, subject_code): # -> None:
        """Sets the subject_code of this MoveConflict.


        :param subject_code: The subject_code of this MoveConflict.  # noqa: E501
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
    


