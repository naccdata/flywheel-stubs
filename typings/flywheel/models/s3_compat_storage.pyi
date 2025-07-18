"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class S3CompatStorage:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, region=..., bucket=..., path=..., endpoint_url=..., verify_certs=..., signed_urls=..., config_type=..., config_class=..., addressing_style=...) -> None:
        """S3CompatStorage - a model defined in Swagger"""
        ...
    
    @property
    def region(self): # -> None:
        """Gets the region of this S3CompatStorage.


        :return: The region of this S3CompatStorage.
        :rtype: str
        """
        ...
    
    @region.setter
    def region(self, region): # -> None:
        """Sets the region of this S3CompatStorage.


        :param region: The region of this S3CompatStorage.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def bucket(self): # -> None:
        """Gets the bucket of this S3CompatStorage.


        :return: The bucket of this S3CompatStorage.
        :rtype: str
        """
        ...
    
    @bucket.setter
    def bucket(self, bucket): # -> None:
        """Sets the bucket of this S3CompatStorage.


        :param bucket: The bucket of this S3CompatStorage.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def path(self): # -> None:
        """Gets the path of this S3CompatStorage.


        :return: The path of this S3CompatStorage.
        :rtype: str
        """
        ...
    
    @path.setter
    def path(self, path): # -> None:
        """Sets the path of this S3CompatStorage.


        :param path: The path of this S3CompatStorage.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def endpoint_url(self): # -> None:
        """Gets the endpoint_url of this S3CompatStorage.


        :return: The endpoint_url of this S3CompatStorage.
        :rtype: str
        """
        ...
    
    @endpoint_url.setter
    def endpoint_url(self, endpoint_url): # -> None:
        """Sets the endpoint_url of this S3CompatStorage.


        :param endpoint_url: The endpoint_url of this S3CompatStorage.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def verify_certs(self): # -> None:
        """Gets the verify_certs of this S3CompatStorage.


        :return: The verify_certs of this S3CompatStorage.
        :rtype: bool
        """
        ...
    
    @verify_certs.setter
    def verify_certs(self, verify_certs): # -> None:
        """Sets the verify_certs of this S3CompatStorage.


        :param verify_certs: The verify_certs of this S3CompatStorage.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def signed_urls(self): # -> None:
        """Gets the signed_urls of this S3CompatStorage.


        :return: The signed_urls of this S3CompatStorage.
        :rtype: bool
        """
        ...
    
    @signed_urls.setter
    def signed_urls(self, signed_urls): # -> None:
        """Sets the signed_urls of this S3CompatStorage.


        :param signed_urls: The signed_urls of this S3CompatStorage.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def config_type(self): # -> None:
        """Gets the config_type of this S3CompatStorage.


        :return: The config_type of this S3CompatStorage.
        :rtype: str
        """
        ...
    
    @config_type.setter
    def config_type(self, config_type): # -> None:
        """Sets the config_type of this S3CompatStorage.


        :param config_type: The config_type of this S3CompatStorage.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def config_class(self): # -> None:
        """Gets the config_class of this S3CompatStorage.


        :return: The config_class of this S3CompatStorage.
        :rtype: str
        """
        ...
    
    @config_class.setter
    def config_class(self, config_class): # -> None:
        """Sets the config_class of this S3CompatStorage.


        :param config_class: The config_class of this S3CompatStorage.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def addressing_style(self): # -> None:
        """Gets the addressing_style of this S3CompatStorage.


        :return: The addressing_style of this S3CompatStorage.
        :rtype: S3AddressingStyle
        """
        ...
    
    @addressing_style.setter
    def addressing_style(self, addressing_style): # -> None:
        """Sets the addressing_style of this S3CompatStorage.


        :param addressing_style: The addressing_style of this S3CompatStorage.  # noqa: E501
        :type: S3AddressingStyle
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
    


