"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class SessionModify:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, timestamp=..., project=..., subject=..., timezone=..., label=..., info=..., tags=..., permissions=..., age=..., weight=..., operator=..., project_has_template=...) -> None:
        """SessionModify - a model defined in Swagger"""
        ...
    
    @property
    def timestamp(self): # -> None:
        """Gets the timestamp of this SessionModify.


        :return: The timestamp of this SessionModify.
        :rtype: datetime
        """
        ...
    
    @timestamp.setter
    def timestamp(self, timestamp): # -> None:
        """Sets the timestamp of this SessionModify.


        :param timestamp: The timestamp of this SessionModify.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def project(self): # -> None:
        """Gets the project of this SessionModify.


        :return: The project of this SessionModify.
        :rtype: str
        """
        ...
    
    @project.setter
    def project(self, project): # -> None:
        """Sets the project of this SessionModify.


        :param project: The project of this SessionModify.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def subject(self): # -> None:
        """Gets the subject of this SessionModify.


        :return: The subject of this SessionModify.
        :rtype: union[str,SessionEmbeddedSubject]
        """
        ...
    
    @subject.setter
    def subject(self, subject): # -> None:
        """Sets the subject of this SessionModify.


        :param subject: The subject of this SessionModify.  # noqa: E501
        :type: union[str,SessionEmbeddedSubject]
        """
        ...
    
    @property
    def timezone(self): # -> None:
        """Gets the timezone of this SessionModify.


        :return: The timezone of this SessionModify.
        :rtype: str
        """
        ...
    
    @timezone.setter
    def timezone(self, timezone): # -> None:
        """Sets the timezone of this SessionModify.


        :param timezone: The timezone of this SessionModify.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def label(self): # -> None:
        """Gets the label of this SessionModify.


        :return: The label of this SessionModify.
        :rtype: str
        """
        ...
    
    @label.setter
    def label(self, label): # -> None:
        """Sets the label of this SessionModify.


        :param label: The label of this SessionModify.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def info(self): # -> None:
        """Gets the info of this SessionModify.


        :return: The info of this SessionModify.
        :rtype: object
        """
        ...
    
    @info.setter
    def info(self, info): # -> None:
        """Sets the info of this SessionModify.


        :param info: The info of this SessionModify.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def tags(self): # -> None:
        """Gets the tags of this SessionModify.


        :return: The tags of this SessionModify.
        :rtype: list[str]
        """
        ...
    
    @tags.setter
    def tags(self, tags): # -> None:
        """Sets the tags of this SessionModify.


        :param tags: The tags of this SessionModify.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def permissions(self): # -> None:
        """Gets the permissions of this SessionModify.


        :return: The permissions of this SessionModify.
        :rtype: list[RolePermission]
        """
        ...
    
    @permissions.setter
    def permissions(self, permissions): # -> None:
        """Sets the permissions of this SessionModify.


        :param permissions: The permissions of this SessionModify.  # noqa: E501
        :type: list[RolePermission]
        """
        ...
    
    @property
    def age(self): # -> None:
        """Gets the age of this SessionModify.


        :return: The age of this SessionModify.
        :rtype: int
        """
        ...
    
    @age.setter
    def age(self, age): # -> None:
        """Sets the age of this SessionModify.


        :param age: The age of this SessionModify.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def weight(self): # -> None:
        """Gets the weight of this SessionModify.


        :return: The weight of this SessionModify.
        :rtype: float
        """
        ...
    
    @weight.setter
    def weight(self, weight): # -> None:
        """Sets the weight of this SessionModify.


        :param weight: The weight of this SessionModify.  # noqa: E501
        :type: float
        """
        ...
    
    @property
    def operator(self): # -> None:
        """Gets the operator of this SessionModify.


        :return: The operator of this SessionModify.
        :rtype: str
        """
        ...
    
    @operator.setter
    def operator(self, operator): # -> None:
        """Sets the operator of this SessionModify.


        :param operator: The operator of this SessionModify.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def project_has_template(self): # -> None:
        """Gets the project_has_template of this SessionModify.


        :return: The project_has_template of this SessionModify.
        :rtype: bool
        """
        ...
    
    @project_has_template.setter
    def project_has_template(self, project_has_template): # -> None:
        """Sets the project_has_template of this SessionModify.


        :param project_has_template: The project_has_template of this SessionModify.  # noqa: E501
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
    


