"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class GcpCreds:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, client_email=..., client_id=..., private_key_id=..., private_key=..., client_x509_cert_url=..., project_id=..., auth_uri=..., token_uri=..., auth_provider_x509_cert_url=..., type=...) -> None:
        """GcpCreds - a model defined in Swagger"""
        ...
    
    @property
    def client_email(self): # -> None:
        """Gets the client_email of this GcpCreds.


        :return: The client_email of this GcpCreds.
        :rtype: str
        """
        ...
    
    @client_email.setter
    def client_email(self, client_email): # -> None:
        """Sets the client_email of this GcpCreds.


        :param client_email: The client_email of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def client_id(self): # -> None:
        """Gets the client_id of this GcpCreds.


        :return: The client_id of this GcpCreds.
        :rtype: str
        """
        ...
    
    @client_id.setter
    def client_id(self, client_id): # -> None:
        """Sets the client_id of this GcpCreds.


        :param client_id: The client_id of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def private_key_id(self): # -> None:
        """Gets the private_key_id of this GcpCreds.


        :return: The private_key_id of this GcpCreds.
        :rtype: str
        """
        ...
    
    @private_key_id.setter
    def private_key_id(self, private_key_id): # -> None:
        """Sets the private_key_id of this GcpCreds.


        :param private_key_id: The private_key_id of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def private_key(self): # -> None:
        """Gets the private_key of this GcpCreds.


        :return: The private_key of this GcpCreds.
        :rtype: str
        """
        ...
    
    @private_key.setter
    def private_key(self, private_key): # -> None:
        """Sets the private_key of this GcpCreds.


        :param private_key: The private_key of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def client_x509_cert_url(self): # -> None:
        """Gets the client_x509_cert_url of this GcpCreds.


        :return: The client_x509_cert_url of this GcpCreds.
        :rtype: str
        """
        ...
    
    @client_x509_cert_url.setter
    def client_x509_cert_url(self, client_x509_cert_url): # -> None:
        """Sets the client_x509_cert_url of this GcpCreds.


        :param client_x509_cert_url: The client_x509_cert_url of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def project_id(self): # -> None:
        """Gets the project_id of this GcpCreds.


        :return: The project_id of this GcpCreds.
        :rtype: str
        """
        ...
    
    @project_id.setter
    def project_id(self, project_id): # -> None:
        """Sets the project_id of this GcpCreds.


        :param project_id: The project_id of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def auth_uri(self): # -> None:
        """Gets the auth_uri of this GcpCreds.


        :return: The auth_uri of this GcpCreds.
        :rtype: str
        """
        ...
    
    @auth_uri.setter
    def auth_uri(self, auth_uri): # -> None:
        """Sets the auth_uri of this GcpCreds.


        :param auth_uri: The auth_uri of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def token_uri(self): # -> None:
        """Gets the token_uri of this GcpCreds.


        :return: The token_uri of this GcpCreds.
        :rtype: str
        """
        ...
    
    @token_uri.setter
    def token_uri(self, token_uri): # -> None:
        """Sets the token_uri of this GcpCreds.


        :param token_uri: The token_uri of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def auth_provider_x509_cert_url(self): # -> None:
        """Gets the auth_provider_x509_cert_url of this GcpCreds.


        :return: The auth_provider_x509_cert_url of this GcpCreds.
        :rtype: str
        """
        ...
    
    @auth_provider_x509_cert_url.setter
    def auth_provider_x509_cert_url(self, auth_provider_x509_cert_url): # -> None:
        """Sets the auth_provider_x509_cert_url of this GcpCreds.


        :param auth_provider_x509_cert_url: The auth_provider_x509_cert_url of this GcpCreds.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def type(self): # -> None:
        """Gets the type of this GcpCreds.


        :return: The type of this GcpCreds.
        :rtype: str
        """
        ...
    
    @type.setter
    def type(self, type): # -> None:
        """Sets the type of this GcpCreds.


        :param type: The type of this GcpCreds.  # noqa: E501
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
    


