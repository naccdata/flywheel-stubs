"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class JupyterlabServerResponse:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., project_id=..., label=..., created=..., modified=..., last_modified_by=..., origin=..., server_state=..., external_storage_id=..., latest_version=...) -> None:
        """JupyterlabServerResponse - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this JupyterlabServerResponse.

        Unique database ID

        :return: The id of this JupyterlabServerResponse.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this JupyterlabServerResponse.

        Unique database ID

        :param id: The id of this JupyterlabServerResponse.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def project_id(self): # -> None:
        """Gets the project_id of this JupyterlabServerResponse.

        Unique database ID

        :return: The project_id of this JupyterlabServerResponse.
        :rtype: str
        """
        ...
    
    @project_id.setter
    def project_id(self, project_id): # -> None:
        """Sets the project_id of this JupyterlabServerResponse.

        Unique database ID

        :param project_id: The project_id of this JupyterlabServerResponse.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def label(self): # -> None:
        """Gets the label of this JupyterlabServerResponse.


        :return: The label of this JupyterlabServerResponse.
        :rtype: str
        """
        ...
    
    @label.setter
    def label(self, label): # -> None:
        """Sets the label of this JupyterlabServerResponse.


        :param label: The label of this JupyterlabServerResponse.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def created(self): # -> None:
        """Gets the created of this JupyterlabServerResponse.

        Creation time (automatically set)

        :return: The created of this JupyterlabServerResponse.
        :rtype: datetime
        """
        ...
    
    @created.setter
    def created(self, created): # -> None:
        """Sets the created of this JupyterlabServerResponse.

        Creation time (automatically set)

        :param created: The created of this JupyterlabServerResponse.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def modified(self): # -> None:
        """Gets the modified of this JupyterlabServerResponse.

        Last modification time (automatically updated)

        :return: The modified of this JupyterlabServerResponse.
        :rtype: datetime
        """
        ...
    
    @modified.setter
    def modified(self, modified): # -> None:
        """Sets the modified of this JupyterlabServerResponse.

        Last modification time (automatically updated)

        :param modified: The modified of this JupyterlabServerResponse.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def last_modified_by(self): # -> None:
        """Gets the last_modified_by of this JupyterlabServerResponse.


        :return: The last_modified_by of this JupyterlabServerResponse.
        :rtype: Origin
        """
        ...
    
    @last_modified_by.setter
    def last_modified_by(self, last_modified_by): # -> None:
        """Sets the last_modified_by of this JupyterlabServerResponse.


        :param last_modified_by: The last_modified_by of this JupyterlabServerResponse.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def origin(self): # -> None:
        """Gets the origin of this JupyterlabServerResponse.


        :return: The origin of this JupyterlabServerResponse.
        :rtype: Origin
        """
        ...
    
    @origin.setter
    def origin(self, origin): # -> None:
        """Sets the origin of this JupyterlabServerResponse.


        :param origin: The origin of this JupyterlabServerResponse.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def server_state(self): # -> None:
        """Gets the server_state of this JupyterlabServerResponse.


        :return: The server_state of this JupyterlabServerResponse.
        :rtype: ServerState
        """
        ...
    
    @server_state.setter
    def server_state(self, server_state): # -> None:
        """Sets the server_state of this JupyterlabServerResponse.


        :param server_state: The server_state of this JupyterlabServerResponse.  # noqa: E501
        :type: ServerState
        """
        ...
    
    @property
    def external_storage_id(self): # -> None:
        """Gets the external_storage_id of this JupyterlabServerResponse.


        :return: The external_storage_id of this JupyterlabServerResponse.
        :rtype: str
        """
        ...
    
    @external_storage_id.setter
    def external_storage_id(self, external_storage_id): # -> None:
        """Sets the external_storage_id of this JupyterlabServerResponse.


        :param external_storage_id: The external_storage_id of this JupyterlabServerResponse.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def latest_version(self): # -> None:
        """Gets the latest_version of this JupyterlabServerResponse.


        :return: The latest_version of this JupyterlabServerResponse.
        :rtype: int
        """
        ...
    
    @latest_version.setter
    def latest_version(self, latest_version): # -> None:
        """Sets the latest_version of this JupyterlabServerResponse.


        :param latest_version: The latest_version of this JupyterlabServerResponse.  # noqa: E501
        :type: int
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
    


