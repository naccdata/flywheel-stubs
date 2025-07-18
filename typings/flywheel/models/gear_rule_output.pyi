"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class GearRuleOutput:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., project_id=..., gear_id=..., role_id=..., name=..., config=..., fixed_inputs=..., priority=..., auto_update=..., revision=..., any=..., all=..., _not=..., created=..., modified=..., disabled=..., compute_provider_id=..., last_modified_by=..., triggering_input=...) -> None:
        """GearRuleOutput - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this GearRuleOutput.


        :return: The id of this GearRuleOutput.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this GearRuleOutput.


        :param id: The id of this GearRuleOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def project_id(self): # -> None:
        """Gets the project_id of this GearRuleOutput.


        :return: The project_id of this GearRuleOutput.
        :rtype: str
        """
        ...
    
    @project_id.setter
    def project_id(self, project_id): # -> None:
        """Sets the project_id of this GearRuleOutput.


        :param project_id: The project_id of this GearRuleOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def gear_id(self): # -> None:
        """Gets the gear_id of this GearRuleOutput.


        :return: The gear_id of this GearRuleOutput.
        :rtype: str
        """
        ...
    
    @gear_id.setter
    def gear_id(self, gear_id): # -> None:
        """Sets the gear_id of this GearRuleOutput.


        :param gear_id: The gear_id of this GearRuleOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def role_id(self): # -> None:
        """Gets the role_id of this GearRuleOutput.


        :return: The role_id of this GearRuleOutput.
        :rtype: str
        """
        ...
    
    @role_id.setter
    def role_id(self, role_id): # -> None:
        """Sets the role_id of this GearRuleOutput.


        :param role_id: The role_id of this GearRuleOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this GearRuleOutput.


        :return: The name of this GearRuleOutput.
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this GearRuleOutput.


        :param name: The name of this GearRuleOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def config(self): # -> None:
        """Gets the config of this GearRuleOutput.


        :return: The config of this GearRuleOutput.
        :rtype: object
        """
        ...
    
    @config.setter
    def config(self, config): # -> None:
        """Sets the config of this GearRuleOutput.


        :param config: The config of this GearRuleOutput.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def fixed_inputs(self): # -> None:
        """Gets the fixed_inputs of this GearRuleOutput.


        :return: The fixed_inputs of this GearRuleOutput.
        :rtype: list[FixedInput]
        """
        ...
    
    @fixed_inputs.setter
    def fixed_inputs(self, fixed_inputs): # -> None:
        """Sets the fixed_inputs of this GearRuleOutput.


        :param fixed_inputs: The fixed_inputs of this GearRuleOutput.  # noqa: E501
        :type: list[FixedInput]
        """
        ...
    
    @property
    def priority(self): # -> None:
        """Gets the priority of this GearRuleOutput.


        :return: The priority of this GearRuleOutput.
        :rtype: JobPriority
        """
        ...
    
    @priority.setter
    def priority(self, priority): # -> None:
        """Sets the priority of this GearRuleOutput.


        :param priority: The priority of this GearRuleOutput.  # noqa: E501
        :type: JobPriority
        """
        ...
    
    @property
    def auto_update(self): # -> None:
        """Gets the auto_update of this GearRuleOutput.


        :return: The auto_update of this GearRuleOutput.
        :rtype: bool
        """
        ...
    
    @auto_update.setter
    def auto_update(self, auto_update): # -> None:
        """Sets the auto_update of this GearRuleOutput.


        :param auto_update: The auto_update of this GearRuleOutput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def revision(self): # -> None:
        """Gets the revision of this GearRuleOutput.


        :return: The revision of this GearRuleOutput.
        :rtype: int
        """
        ...
    
    @revision.setter
    def revision(self, revision): # -> None:
        """Sets the revision of this GearRuleOutput.


        :param revision: The revision of this GearRuleOutput.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def any(self): # -> None:
        """Gets the any of this GearRuleOutput.


        :return: The any of this GearRuleOutput.
        :rtype: list[GearRuleCondition]
        """
        ...
    
    @any.setter
    def any(self, any): # -> None:
        """Sets the any of this GearRuleOutput.


        :param any: The any of this GearRuleOutput.  # noqa: E501
        :type: list[GearRuleCondition]
        """
        ...
    
    @property
    def all(self): # -> None:
        """Gets the all of this GearRuleOutput.


        :return: The all of this GearRuleOutput.
        :rtype: list[GearRuleCondition]
        """
        ...
    
    @all.setter
    def all(self, all): # -> None:
        """Sets the all of this GearRuleOutput.


        :param all: The all of this GearRuleOutput.  # noqa: E501
        :type: list[GearRuleCondition]
        """
        ...
    
    @property
    def created(self): # -> None:
        """Gets the created of this GearRuleOutput.


        :return: The created of this GearRuleOutput.
        :rtype: datetime
        """
        ...
    
    @created.setter
    def created(self, created): # -> None:
        """Sets the created of this GearRuleOutput.


        :param created: The created of this GearRuleOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def modified(self): # -> None:
        """Gets the modified of this GearRuleOutput.


        :return: The modified of this GearRuleOutput.
        :rtype: datetime
        """
        ...
    
    @modified.setter
    def modified(self, modified): # -> None:
        """Sets the modified of this GearRuleOutput.


        :param modified: The modified of this GearRuleOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def disabled(self): # -> None:
        """Gets the disabled of this GearRuleOutput.


        :return: The disabled of this GearRuleOutput.
        :rtype: bool
        """
        ...
    
    @disabled.setter
    def disabled(self, disabled): # -> None:
        """Sets the disabled of this GearRuleOutput.


        :param disabled: The disabled of this GearRuleOutput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def compute_provider_id(self): # -> None:
        """Gets the compute_provider_id of this GearRuleOutput.


        :return: The compute_provider_id of this GearRuleOutput.
        :rtype: str
        """
        ...
    
    @compute_provider_id.setter
    def compute_provider_id(self, compute_provider_id): # -> None:
        """Sets the compute_provider_id of this GearRuleOutput.


        :param compute_provider_id: The compute_provider_id of this GearRuleOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def last_modified_by(self): # -> None:
        """Gets the last_modified_by of this GearRuleOutput.


        :return: The last_modified_by of this GearRuleOutput.
        :rtype: Origin
        """
        ...
    
    @last_modified_by.setter
    def last_modified_by(self, last_modified_by): # -> None:
        """Sets the last_modified_by of this GearRuleOutput.


        :param last_modified_by: The last_modified_by of this GearRuleOutput.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def triggering_input(self): # -> None:
        """Gets the triggering_input of this GearRuleOutput.


        :return: The triggering_input of this GearRuleOutput.
        :rtype: str
        """
        ...
    
    @triggering_input.setter
    def triggering_input(self, triggering_input): # -> None:
        """Sets the triggering_input of this GearRuleOutput.


        :param triggering_input: The triggering_input of this GearRuleOutput.  # noqa: E501
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
    


