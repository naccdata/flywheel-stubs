"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class InputJobProfile:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, elapsed_time_ms=..., executor=..., preparation_time_ms=..., upload_time_ms=..., versions=...) -> None:
        """InputJobProfile - a model defined in Swagger"""
        ...
    
    @property
    def elapsed_time_ms(self): # -> None:
        """Gets the elapsed_time_ms of this InputJobProfile.


        :return: The elapsed_time_ms of this InputJobProfile.
        :rtype: int
        """
        ...
    
    @elapsed_time_ms.setter
    def elapsed_time_ms(self, elapsed_time_ms): # -> None:
        """Sets the elapsed_time_ms of this InputJobProfile.


        :param elapsed_time_ms: The elapsed_time_ms of this InputJobProfile.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def executor(self): # -> None:
        """Gets the executor of this InputJobProfile.


        :return: The executor of this InputJobProfile.
        :rtype: ExecutorInfo
        """
        ...
    
    @executor.setter
    def executor(self, executor): # -> None:
        """Sets the executor of this InputJobProfile.


        :param executor: The executor of this InputJobProfile.  # noqa: E501
        :type: ExecutorInfo
        """
        ...
    
    @property
    def preparation_time_ms(self): # -> None:
        """Gets the preparation_time_ms of this InputJobProfile.


        :return: The preparation_time_ms of this InputJobProfile.
        :rtype: int
        """
        ...
    
    @preparation_time_ms.setter
    def preparation_time_ms(self, preparation_time_ms): # -> None:
        """Sets the preparation_time_ms of this InputJobProfile.


        :param preparation_time_ms: The preparation_time_ms of this InputJobProfile.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def upload_time_ms(self): # -> None:
        """Gets the upload_time_ms of this InputJobProfile.


        :return: The upload_time_ms of this InputJobProfile.
        :rtype: int
        """
        ...
    
    @upload_time_ms.setter
    def upload_time_ms(self, upload_time_ms): # -> None:
        """Sets the upload_time_ms of this InputJobProfile.


        :param upload_time_ms: The upload_time_ms of this InputJobProfile.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def versions(self): # -> None:
        """Gets the versions of this InputJobProfile.


        :return: The versions of this InputJobProfile.
        :rtype: dict(str, str)
        """
        ...
    
    @versions.setter
    def versions(self, versions): # -> None:
        """Sets the versions of this InputJobProfile.


        :param versions: The versions of this InputJobProfile.  # noqa: E501
        :type: dict(str, str)
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
    


