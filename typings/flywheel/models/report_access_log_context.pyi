"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class ReportAccessLogContext:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, group=..., project=..., subject=..., session=..., acquisition=..., file=...) -> None:
        """ReportAccessLogContext - a model defined in Swagger"""
        ...
    
    @property
    def group(self): # -> None:
        """Gets the group of this ReportAccessLogContext.


        :return: The group of this ReportAccessLogContext.
        :rtype: ReportAccessLogContextEntry
        """
        ...
    
    @group.setter
    def group(self, group): # -> None:
        """Sets the group of this ReportAccessLogContext.


        :param group: The group of this ReportAccessLogContext.  # noqa: E501
        :type: ReportAccessLogContextEntry
        """
        ...
    
    @property
    def project(self): # -> None:
        """Gets the project of this ReportAccessLogContext.


        :return: The project of this ReportAccessLogContext.
        :rtype: ReportAccessLogContextEntry
        """
        ...
    
    @project.setter
    def project(self, project): # -> None:
        """Sets the project of this ReportAccessLogContext.


        :param project: The project of this ReportAccessLogContext.  # noqa: E501
        :type: ReportAccessLogContextEntry
        """
        ...
    
    @property
    def subject(self): # -> None:
        """Gets the subject of this ReportAccessLogContext.


        :return: The subject of this ReportAccessLogContext.
        :rtype: ReportAccessLogContextEntry
        """
        ...
    
    @subject.setter
    def subject(self, subject): # -> None:
        """Sets the subject of this ReportAccessLogContext.


        :param subject: The subject of this ReportAccessLogContext.  # noqa: E501
        :type: ReportAccessLogContextEntry
        """
        ...
    
    @property
    def session(self): # -> None:
        """Gets the session of this ReportAccessLogContext.


        :return: The session of this ReportAccessLogContext.
        :rtype: ReportAccessLogContextEntry
        """
        ...
    
    @session.setter
    def session(self, session): # -> None:
        """Sets the session of this ReportAccessLogContext.


        :param session: The session of this ReportAccessLogContext.  # noqa: E501
        :type: ReportAccessLogContextEntry
        """
        ...
    
    @property
    def acquisition(self): # -> None:
        """Gets the acquisition of this ReportAccessLogContext.


        :return: The acquisition of this ReportAccessLogContext.
        :rtype: ReportAccessLogContextEntry
        """
        ...
    
    @acquisition.setter
    def acquisition(self, acquisition): # -> None:
        """Sets the acquisition of this ReportAccessLogContext.


        :param acquisition: The acquisition of this ReportAccessLogContext.  # noqa: E501
        :type: ReportAccessLogContextEntry
        """
        ...
    
    @property
    def file(self): # -> None:
        """Gets the file of this ReportAccessLogContext.


        :return: The file of this ReportAccessLogContext.
        :rtype: ReportAccessLogContextFileEntry
        """
        ...
    
    @file.setter
    def file(self, file): # -> None:
        """Sets the file of this ReportAccessLogContext.


        :param file: The file of this ReportAccessLogContext.  # noqa: E501
        :type: ReportAccessLogContextFileEntry
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
    


