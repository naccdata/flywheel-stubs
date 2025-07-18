"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class JoinOrigins:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, device=..., job=..., user=...) -> None:
        """JoinOrigins - a model defined in Swagger"""
        ...
    
    @property
    def device(self): # -> None:
        """Gets the device of this JoinOrigins.


        :return: The device of this JoinOrigins.
        :rtype: dict(str, JoinOriginDevice)
        """
        ...
    
    @device.setter
    def device(self, device): # -> None:
        """Sets the device of this JoinOrigins.


        :param device: The device of this JoinOrigins.  # noqa: E501
        :type: dict(str, JoinOriginDevice)
        """
        ...
    
    @property
    def job(self): # -> None:
        """Gets the job of this JoinOrigins.


        :return: The job of this JoinOrigins.
        :rtype: dict(str, JoinOriginJob)
        """
        ...
    
    @job.setter
    def job(self, job): # -> None:
        """Sets the job of this JoinOrigins.


        :param job: The job of this JoinOrigins.  # noqa: E501
        :type: dict(str, JoinOriginJob)
        """
        ...
    
    @property
    def user(self): # -> None:
        """Gets the user of this JoinOrigins.


        :return: The user of this JoinOrigins.
        :rtype: dict(str, JoinOriginUser)
        """
        ...
    
    @user.setter
    def user(self, user): # -> None:
        """Sets the user of this JoinOrigins.


        :param user: The user of this JoinOrigins.  # noqa: E501
        :type: dict(str, JoinOriginUser)
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
    


