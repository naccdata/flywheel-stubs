"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class CVATSettingsInput:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, enabled=..., tags=..., export_formats=..., cvat_organization_id=..., cvat_project_id=...) -> None:
        """CVATSettingsInput - a model defined in Swagger"""
        ...
    
    @property
    def enabled(self): # -> None:
        """Gets the enabled of this CVATSettingsInput.


        :return: The enabled of this CVATSettingsInput.
        :rtype: bool
        """
        ...
    
    @enabled.setter
    def enabled(self, enabled): # -> None:
        """Sets the enabled of this CVATSettingsInput.


        :param enabled: The enabled of this CVATSettingsInput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def tags(self): # -> None:
        """Gets the tags of this CVATSettingsInput.


        :return: The tags of this CVATSettingsInput.
        :rtype: list[str]
        """
        ...
    
    @tags.setter
    def tags(self, tags): # -> None:
        """Sets the tags of this CVATSettingsInput.


        :param tags: The tags of this CVATSettingsInput.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def export_formats(self): # -> None:
        """Gets the export_formats of this CVATSettingsInput.


        :return: The export_formats of this CVATSettingsInput.
        :rtype: list[str]
        """
        ...
    
    @export_formats.setter
    def export_formats(self, export_formats): # -> None:
        """Sets the export_formats of this CVATSettingsInput.


        :param export_formats: The export_formats of this CVATSettingsInput.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def cvat_organization_id(self): # -> None:
        """Gets the cvat_organization_id of this CVATSettingsInput.


        :return: The cvat_organization_id of this CVATSettingsInput.
        :rtype: str
        """
        ...
    
    @cvat_organization_id.setter
    def cvat_organization_id(self, cvat_organization_id): # -> None:
        """Sets the cvat_organization_id of this CVATSettingsInput.


        :param cvat_organization_id: The cvat_organization_id of this CVATSettingsInput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def cvat_project_id(self): # -> None:
        """Gets the cvat_project_id of this CVATSettingsInput.


        :return: The cvat_project_id of this CVATSettingsInput.
        :rtype: str
        """
        ...
    
    @cvat_project_id.setter
    def cvat_project_id(self, cvat_project_id): # -> None:
        """Sets the cvat_project_id of this CVATSettingsInput.


        :param cvat_project_id: The cvat_project_id of this CVATSettingsInput.  # noqa: E501
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
    


