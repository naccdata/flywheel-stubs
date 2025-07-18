"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class CurrentUserOutput:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., user_id=..., firstname=..., lastname=..., email=..., auth0sub=..., roles=..., root=..., api_key=..., api_keys=..., avatar=..., avatars=..., disabled=..., preferences=..., created=..., modified=..., info=..., firstlogin=..., lastlogin=..., visited_projects=...) -> None:
        """CurrentUserOutput - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this CurrentUserOutput.


        :return: The id of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this CurrentUserOutput.


        :param id: The id of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def user_id(self): # -> None:
        """Gets the user_id of this CurrentUserOutput.


        :return: The user_id of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @user_id.setter
    def user_id(self, user_id): # -> None:
        """Sets the user_id of this CurrentUserOutput.


        :param user_id: The user_id of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def firstname(self): # -> None:
        """Gets the firstname of this CurrentUserOutput.


        :return: The firstname of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @firstname.setter
    def firstname(self, firstname): # -> None:
        """Sets the firstname of this CurrentUserOutput.


        :param firstname: The firstname of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def lastname(self): # -> None:
        """Gets the lastname of this CurrentUserOutput.


        :return: The lastname of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @lastname.setter
    def lastname(self, lastname): # -> None:
        """Sets the lastname of this CurrentUserOutput.


        :param lastname: The lastname of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def email(self): # -> None:
        """Gets the email of this CurrentUserOutput.


        :return: The email of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @email.setter
    def email(self, email): # -> None:
        """Sets the email of this CurrentUserOutput.


        :param email: The email of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def auth0sub(self): # -> None:
        """Gets the auth0sub of this CurrentUserOutput.


        :return: The auth0sub of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @auth0sub.setter
    def auth0sub(self, auth0sub): # -> None:
        """Sets the auth0sub of this CurrentUserOutput.


        :param auth0sub: The auth0sub of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def roles(self): # -> None:
        """Gets the roles of this CurrentUserOutput.


        :return: The roles of this CurrentUserOutput.
        :rtype: list[str]
        """
        ...
    
    @roles.setter
    def roles(self, roles): # -> None:
        """Sets the roles of this CurrentUserOutput.


        :param roles: The roles of this CurrentUserOutput.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def root(self): # -> None:
        """Gets the root of this CurrentUserOutput.


        :return: The root of this CurrentUserOutput.
        :rtype: bool
        """
        ...
    
    @root.setter
    def root(self, root): # -> None:
        """Sets the root of this CurrentUserOutput.


        :param root: The root of this CurrentUserOutput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def api_key(self): # -> None:
        """Gets the api_key of this CurrentUserOutput.


        :return: The api_key of this CurrentUserOutput.
        :rtype: LegacyApiKeyOutput
        """
        ...
    
    @api_key.setter
    def api_key(self, api_key): # -> None:
        """Sets the api_key of this CurrentUserOutput.


        :param api_key: The api_key of this CurrentUserOutput.  # noqa: E501
        :type: LegacyApiKeyOutput
        """
        ...
    
    @property
    def api_keys(self): # -> None:
        """Gets the api_keys of this CurrentUserOutput.


        :return: The api_keys of this CurrentUserOutput.
        :rtype: list[ApiKeyOutput]
        """
        ...
    
    @api_keys.setter
    def api_keys(self, api_keys): # -> None:
        """Sets the api_keys of this CurrentUserOutput.


        :param api_keys: The api_keys of this CurrentUserOutput.  # noqa: E501
        :type: list[ApiKeyOutput]
        """
        ...
    
    @property
    def avatar(self): # -> None:
        """Gets the avatar of this CurrentUserOutput.


        :return: The avatar of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @avatar.setter
    def avatar(self, avatar): # -> None:
        """Sets the avatar of this CurrentUserOutput.


        :param avatar: The avatar of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def avatars(self): # -> None:
        """Gets the avatars of this CurrentUserOutput.


        :return: The avatars of this CurrentUserOutput.
        :rtype: Avatars
        """
        ...
    
    @avatars.setter
    def avatars(self, avatars): # -> None:
        """Sets the avatars of this CurrentUserOutput.


        :param avatars: The avatars of this CurrentUserOutput.  # noqa: E501
        :type: Avatars
        """
        ...
    
    @property
    def disabled(self): # -> None:
        """Gets the disabled of this CurrentUserOutput.


        :return: The disabled of this CurrentUserOutput.
        :rtype: bool
        """
        ...
    
    @disabled.setter
    def disabled(self, disabled): # -> None:
        """Sets the disabled of this CurrentUserOutput.


        :param disabled: The disabled of this CurrentUserOutput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def preferences(self): # -> None:
        """Gets the preferences of this CurrentUserOutput.


        :return: The preferences of this CurrentUserOutput.
        :rtype: UserPreferences
        """
        ...
    
    @preferences.setter
    def preferences(self, preferences): # -> None:
        """Sets the preferences of this CurrentUserOutput.


        :param preferences: The preferences of this CurrentUserOutput.  # noqa: E501
        :type: UserPreferences
        """
        ...
    
    @property
    def created(self): # -> None:
        """Gets the created of this CurrentUserOutput.


        :return: The created of this CurrentUserOutput.
        :rtype: datetime
        """
        ...
    
    @created.setter
    def created(self, created): # -> None:
        """Sets the created of this CurrentUserOutput.


        :param created: The created of this CurrentUserOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def modified(self): # -> None:
        """Gets the modified of this CurrentUserOutput.


        :return: The modified of this CurrentUserOutput.
        :rtype: datetime
        """
        ...
    
    @modified.setter
    def modified(self, modified): # -> None:
        """Sets the modified of this CurrentUserOutput.


        :param modified: The modified of this CurrentUserOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def info(self): # -> None:
        """Gets the info of this CurrentUserOutput.


        :return: The info of this CurrentUserOutput.
        :rtype: object
        """
        ...
    
    @info.setter
    def info(self, info): # -> None:
        """Sets the info of this CurrentUserOutput.


        :param info: The info of this CurrentUserOutput.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def firstlogin(self): # -> None:
        """Gets the firstlogin of this CurrentUserOutput.


        :return: The firstlogin of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @firstlogin.setter
    def firstlogin(self, firstlogin): # -> None:
        """Sets the firstlogin of this CurrentUserOutput.


        :param firstlogin: The firstlogin of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def lastlogin(self): # -> None:
        """Gets the lastlogin of this CurrentUserOutput.


        :return: The lastlogin of this CurrentUserOutput.
        :rtype: str
        """
        ...
    
    @lastlogin.setter
    def lastlogin(self, lastlogin): # -> None:
        """Sets the lastlogin of this CurrentUserOutput.


        :param lastlogin: The lastlogin of this CurrentUserOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def visited_projects(self): # -> None:
        """Gets the visited_projects of this CurrentUserOutput.


        :return: The visited_projects of this CurrentUserOutput.
        :rtype: list[str]
        """
        ...
    
    @visited_projects.setter
    def visited_projects(self, visited_projects): # -> None:
        """Sets the visited_projects of this CurrentUserOutput.


        :param visited_projects: The visited_projects of this CurrentUserOutput.  # noqa: E501
        :type: list[str]
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
    


