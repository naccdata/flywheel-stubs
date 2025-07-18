"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class ViewerApp:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., type=..., name=..., description=..., url=..., origin=..., options=..., files=..., containers=...) -> None:
        """ViewerApp - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this ViewerApp.


        :return: The id of this ViewerApp.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this ViewerApp.


        :param id: The id of this ViewerApp.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def type(self): # -> None:
        """Gets the type of this ViewerApp.


        :return: The type of this ViewerApp.
        :rtype: ViewerAppType
        """
        ...
    
    @type.setter
    def type(self, type): # -> None:
        """Sets the type of this ViewerApp.


        :param type: The type of this ViewerApp.  # noqa: E501
        :type: ViewerAppType
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this ViewerApp.


        :return: The name of this ViewerApp.
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this ViewerApp.


        :param name: The name of this ViewerApp.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def description(self): # -> None:
        """Gets the description of this ViewerApp.


        :return: The description of this ViewerApp.
        :rtype: str
        """
        ...
    
    @description.setter
    def description(self, description): # -> None:
        """Sets the description of this ViewerApp.


        :param description: The description of this ViewerApp.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def url(self): # -> None:
        """Gets the url of this ViewerApp.


        :return: The url of this ViewerApp.
        :rtype: str
        """
        ...
    
    @url.setter
    def url(self, url): # -> None:
        """Sets the url of this ViewerApp.


        :param url: The url of this ViewerApp.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def origin(self): # -> None:
        """Gets the origin of this ViewerApp.


        :return: The origin of this ViewerApp.
        :rtype: Origin
        """
        ...
    
    @origin.setter
    def origin(self, origin): # -> None:
        """Sets the origin of this ViewerApp.


        :param origin: The origin of this ViewerApp.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def options(self): # -> None:
        """Gets the options of this ViewerApp.


        :return: The options of this ViewerApp.
        :rtype: object
        """
        ...
    
    @options.setter
    def options(self, options): # -> None:
        """Sets the options of this ViewerApp.


        :param options: The options of this ViewerApp.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def files(self): # -> None:
        """Gets the files of this ViewerApp.


        :return: The files of this ViewerApp.
        :rtype: object
        """
        ...
    
    @files.setter
    def files(self, files): # -> None:
        """Sets the files of this ViewerApp.


        :param files: The files of this ViewerApp.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def containers(self): # -> None:
        """Gets the containers of this ViewerApp.


        :return: The containers of this ViewerApp.
        :rtype: object
        """
        ...
    
    @containers.setter
    def containers(self, containers): # -> None:
        """Sets the containers of this ViewerApp.


        :param containers: The containers of this ViewerApp.  # noqa: E501
        :type: object
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
    


