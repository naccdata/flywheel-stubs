"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class ModifyUserInput:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, firstname=..., lastname=..., email=..., avatars=..., avatar=..., roles=..., disabled=..., preferences=..., root=..., password=..., central_revision=...) -> None:
        """ModifyUserInput - a model defined in Swagger"""
        ...
    
    @property
    def firstname(self): # -> None:
        """Gets the firstname of this ModifyUserInput.


        :return: The firstname of this ModifyUserInput.
        :rtype: str
        """
        ...
    
    @firstname.setter
    def firstname(self, firstname): # -> None:
        """Sets the firstname of this ModifyUserInput.


        :param firstname: The firstname of this ModifyUserInput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def lastname(self): # -> None:
        """Gets the lastname of this ModifyUserInput.


        :return: The lastname of this ModifyUserInput.
        :rtype: str
        """
        ...
    
    @lastname.setter
    def lastname(self, lastname): # -> None:
        """Sets the lastname of this ModifyUserInput.


        :param lastname: The lastname of this ModifyUserInput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def email(self): # -> None:
        """Gets the email of this ModifyUserInput.


        :return: The email of this ModifyUserInput.
        :rtype: str
        """
        ...
    
    @email.setter
    def email(self, email): # -> None:
        """Sets the email of this ModifyUserInput.


        :param email: The email of this ModifyUserInput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def avatars(self): # -> None:
        """Gets the avatars of this ModifyUserInput.


        :return: The avatars of this ModifyUserInput.
        :rtype: Avatars
        """
        ...
    
    @avatars.setter
    def avatars(self, avatars): # -> None:
        """Sets the avatars of this ModifyUserInput.


        :param avatars: The avatars of this ModifyUserInput.  # noqa: E501
        :type: Avatars
        """
        ...
    
    @property
    def avatar(self): # -> None:
        """Gets the avatar of this ModifyUserInput.


        :return: The avatar of this ModifyUserInput.
        :rtype: str
        """
        ...
    
    @avatar.setter
    def avatar(self, avatar): # -> None:
        """Sets the avatar of this ModifyUserInput.


        :param avatar: The avatar of this ModifyUserInput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def roles(self): # -> None:
        """Gets the roles of this ModifyUserInput.


        :return: The roles of this ModifyUserInput.
        :rtype: list[RoleType]
        """
        ...
    
    @roles.setter
    def roles(self, roles): # -> None:
        """Sets the roles of this ModifyUserInput.


        :param roles: The roles of this ModifyUserInput.  # noqa: E501
        :type: list[RoleType]
        """
        ...
    
    @property
    def disabled(self): # -> None:
        """Gets the disabled of this ModifyUserInput.


        :return: The disabled of this ModifyUserInput.
        :rtype: bool
        """
        ...
    
    @disabled.setter
    def disabled(self, disabled): # -> None:
        """Sets the disabled of this ModifyUserInput.


        :param disabled: The disabled of this ModifyUserInput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def preferences(self): # -> None:
        """Gets the preferences of this ModifyUserInput.


        :return: The preferences of this ModifyUserInput.
        :rtype: UserPreferences
        """
        ...
    
    @preferences.setter
    def preferences(self, preferences): # -> None:
        """Sets the preferences of this ModifyUserInput.


        :param preferences: The preferences of this ModifyUserInput.  # noqa: E501
        :type: UserPreferences
        """
        ...
    
    @property
    def root(self): # -> None:
        """Gets the root of this ModifyUserInput.


        :return: The root of this ModifyUserInput.
        :rtype: bool
        """
        ...
    
    @root.setter
    def root(self, root): # -> None:
        """Sets the root of this ModifyUserInput.


        :param root: The root of this ModifyUserInput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def password(self): # -> None:
        """Gets the password of this ModifyUserInput.


        :return: The password of this ModifyUserInput.
        :rtype: str
        """
        ...
    
    @password.setter
    def password(self, password): # -> None:
        """Sets the password of this ModifyUserInput.


        :param password: The password of this ModifyUserInput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def central_revision(self): # -> None:
        """Gets the central_revision of this ModifyUserInput.


        :return: The central_revision of this ModifyUserInput.
        :rtype: int
        """
        ...
    
    @central_revision.setter
    def central_revision(self, central_revision): # -> None:
        """Sets the central_revision of this ModifyUserInput.


        :param central_revision: The central_revision of this ModifyUserInput.  # noqa: E501
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
    


