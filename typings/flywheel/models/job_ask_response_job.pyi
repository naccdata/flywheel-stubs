"""
This type stub file was generated by pyright.
"""

from .mixins import JobMixin

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class JobAskResponseJob(JobMixin):
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, compute_provider_id=..., failure_reason=..., label=..., priority=..., modified=..., parents=..., produced_metadata=..., related_container_ids=..., request=..., retried=..., saved_files=..., state=..., profile=..., transitions=..., gear_id=..., gear_info=..., rule_id=..., role_id=..., inputs=..., legacy_inputs=..., destination=..., tags=..., attempt=..., previous_job_id=..., created=..., id=..., config=..., origin=..., batch=..., failed_output_accepted=..., parent_info=...) -> None:
        """JobAskResponseJob - a model defined in Swagger"""
        ...
    
    @property
    def compute_provider_id(self): # -> None:
        """Gets the compute_provider_id of this JobAskResponseJob.


        :return: The compute_provider_id of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @compute_provider_id.setter
    def compute_provider_id(self, compute_provider_id): # -> None:
        """Sets the compute_provider_id of this JobAskResponseJob.


        :param compute_provider_id: The compute_provider_id of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def failure_reason(self): # -> None:
        """Gets the failure_reason of this JobAskResponseJob.


        :return: The failure_reason of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @failure_reason.setter
    def failure_reason(self, failure_reason): # -> None:
        """Sets the failure_reason of this JobAskResponseJob.


        :param failure_reason: The failure_reason of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def label(self): # -> None:
        """Gets the label of this JobAskResponseJob.


        :return: The label of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @label.setter
    def label(self, label): # -> None:
        """Sets the label of this JobAskResponseJob.


        :param label: The label of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def priority(self): # -> None:
        """Gets the priority of this JobAskResponseJob.


        :return: The priority of this JobAskResponseJob.
        :rtype: JobPriority
        """
        ...
    
    @priority.setter
    def priority(self, priority): # -> None:
        """Sets the priority of this JobAskResponseJob.


        :param priority: The priority of this JobAskResponseJob.  # noqa: E501
        :type: JobPriority
        """
        ...
    
    @property
    def modified(self): # -> None:
        """Gets the modified of this JobAskResponseJob.


        :return: The modified of this JobAskResponseJob.
        :rtype: datetime
        """
        ...
    
    @modified.setter
    def modified(self, modified): # -> None:
        """Sets the modified of this JobAskResponseJob.


        :param modified: The modified of this JobAskResponseJob.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def parents(self): # -> None:
        """Gets the parents of this JobAskResponseJob.


        :return: The parents of this JobAskResponseJob.
        :rtype: JobParents
        """
        ...
    
    @parents.setter
    def parents(self, parents): # -> None:
        """Sets the parents of this JobAskResponseJob.


        :param parents: The parents of this JobAskResponseJob.  # noqa: E501
        :type: JobParents
        """
        ...
    
    @property
    def produced_metadata(self): # -> None:
        """Gets the produced_metadata of this JobAskResponseJob.


        :return: The produced_metadata of this JobAskResponseJob.
        :rtype: object
        """
        ...
    
    @produced_metadata.setter
    def produced_metadata(self, produced_metadata): # -> None:
        """Sets the produced_metadata of this JobAskResponseJob.


        :param produced_metadata: The produced_metadata of this JobAskResponseJob.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def related_container_ids(self): # -> None:
        """Gets the related_container_ids of this JobAskResponseJob.


        :return: The related_container_ids of this JobAskResponseJob.
        :rtype: list[str]
        """
        ...
    
    @related_container_ids.setter
    def related_container_ids(self, related_container_ids): # -> None:
        """Sets the related_container_ids of this JobAskResponseJob.


        :param related_container_ids: The related_container_ids of this JobAskResponseJob.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def request(self): # -> None:
        """Gets the request of this JobAskResponseJob.


        :return: The request of this JobAskResponseJob.
        :rtype: JobRequest
        """
        ...
    
    @request.setter
    def request(self, request): # -> None:
        """Sets the request of this JobAskResponseJob.


        :param request: The request of this JobAskResponseJob.  # noqa: E501
        :type: JobRequest
        """
        ...
    
    @property
    def retried(self): # -> None:
        """Gets the retried of this JobAskResponseJob.


        :return: The retried of this JobAskResponseJob.
        :rtype: datetime
        """
        ...
    
    @retried.setter
    def retried(self, retried): # -> None:
        """Sets the retried of this JobAskResponseJob.


        :param retried: The retried of this JobAskResponseJob.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def saved_files(self): # -> None:
        """Gets the saved_files of this JobAskResponseJob.


        :return: The saved_files of this JobAskResponseJob.
        :rtype: list[str]
        """
        ...
    
    @saved_files.setter
    def saved_files(self, saved_files): # -> None:
        """Sets the saved_files of this JobAskResponseJob.


        :param saved_files: The saved_files of this JobAskResponseJob.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def state(self): # -> None:
        """Gets the state of this JobAskResponseJob.


        :return: The state of this JobAskResponseJob.
        :rtype: JobState
        """
        ...
    
    @state.setter
    def state(self, state): # -> None:
        """Sets the state of this JobAskResponseJob.


        :param state: The state of this JobAskResponseJob.  # noqa: E501
        :type: JobState
        """
        ...
    
    @property
    def profile(self): # -> None:
        """Gets the profile of this JobAskResponseJob.


        :return: The profile of this JobAskResponseJob.
        :rtype: JobProfile
        """
        ...
    
    @profile.setter
    def profile(self, profile): # -> None:
        """Sets the profile of this JobAskResponseJob.


        :param profile: The profile of this JobAskResponseJob.  # noqa: E501
        :type: JobProfile
        """
        ...
    
    @property
    def transitions(self): # -> None:
        """Gets the transitions of this JobAskResponseJob.


        :return: The transitions of this JobAskResponseJob.
        :rtype: Transitions
        """
        ...
    
    @transitions.setter
    def transitions(self, transitions): # -> None:
        """Sets the transitions of this JobAskResponseJob.


        :param transitions: The transitions of this JobAskResponseJob.  # noqa: E501
        :type: Transitions
        """
        ...
    
    @property
    def gear_id(self): # -> None:
        """Gets the gear_id of this JobAskResponseJob.


        :return: The gear_id of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @gear_id.setter
    def gear_id(self, gear_id): # -> None:
        """Sets the gear_id of this JobAskResponseJob.


        :param gear_id: The gear_id of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def gear_info(self): # -> None:
        """Gets the gear_info of this JobAskResponseJob.


        :return: The gear_info of this JobAskResponseJob.
        :rtype: GearInfo
        """
        ...
    
    @gear_info.setter
    def gear_info(self, gear_info): # -> None:
        """Sets the gear_info of this JobAskResponseJob.


        :param gear_info: The gear_info of this JobAskResponseJob.  # noqa: E501
        :type: GearInfo
        """
        ...
    
    @property
    def rule_id(self): # -> None:
        """Gets the rule_id of this JobAskResponseJob.


        :return: The rule_id of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @rule_id.setter
    def rule_id(self, rule_id): # -> None:
        """Sets the rule_id of this JobAskResponseJob.


        :param rule_id: The rule_id of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def role_id(self): # -> None:
        """Gets the role_id of this JobAskResponseJob.


        :return: The role_id of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @role_id.setter
    def role_id(self, role_id): # -> None:
        """Sets the role_id of this JobAskResponseJob.


        :param role_id: The role_id of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def inputs(self): # -> None:
        """Gets the inputs of this JobAskResponseJob.


        :return: The inputs of this JobAskResponseJob.
        :rtype: dict(str, union[JobFileInput,ContextInput,core__models__jobs__ApiKeyInput])
        """
        ...
    
    @inputs.setter
    def inputs(self, inputs): # -> None:
        """Sets the inputs of this JobAskResponseJob.


        :param inputs: The inputs of this JobAskResponseJob.  # noqa: E501
        :type: dict(str, union[JobFileInput,ContextInput,core__models__jobs__ApiKeyInput])
        """
        ...
    
    @property
    def legacy_inputs(self): # -> None:
        """Gets the legacy_inputs of this JobAskResponseJob.


        :return: The legacy_inputs of this JobAskResponseJob.
        :rtype: list[LegacyInput]
        """
        ...
    
    @legacy_inputs.setter
    def legacy_inputs(self, legacy_inputs): # -> None:
        """Sets the legacy_inputs of this JobAskResponseJob.


        :param legacy_inputs: The legacy_inputs of this JobAskResponseJob.  # noqa: E501
        :type: list[LegacyInput]
        """
        ...
    
    @property
    def destination(self): # -> None:
        """Gets the destination of this JobAskResponseJob.


        :return: The destination of this JobAskResponseJob.
        :rtype: ContainerReference
        """
        ...
    
    @destination.setter
    def destination(self, destination): # -> None:
        """Sets the destination of this JobAskResponseJob.


        :param destination: The destination of this JobAskResponseJob.  # noqa: E501
        :type: ContainerReference
        """
        ...
    
    @property
    def tags(self): # -> None:
        """Gets the tags of this JobAskResponseJob.


        :return: The tags of this JobAskResponseJob.
        :rtype: list[str]
        """
        ...
    
    @tags.setter
    def tags(self, tags): # -> None:
        """Sets the tags of this JobAskResponseJob.


        :param tags: The tags of this JobAskResponseJob.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def attempt(self): # -> None:
        """Gets the attempt of this JobAskResponseJob.


        :return: The attempt of this JobAskResponseJob.
        :rtype: int
        """
        ...
    
    @attempt.setter
    def attempt(self, attempt): # -> None:
        """Sets the attempt of this JobAskResponseJob.


        :param attempt: The attempt of this JobAskResponseJob.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def previous_job_id(self): # -> None:
        """Gets the previous_job_id of this JobAskResponseJob.


        :return: The previous_job_id of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @previous_job_id.setter
    def previous_job_id(self, previous_job_id): # -> None:
        """Sets the previous_job_id of this JobAskResponseJob.


        :param previous_job_id: The previous_job_id of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def created(self): # -> None:
        """Gets the created of this JobAskResponseJob.


        :return: The created of this JobAskResponseJob.
        :rtype: datetime
        """
        ...
    
    @created.setter
    def created(self, created): # -> None:
        """Sets the created of this JobAskResponseJob.


        :param created: The created of this JobAskResponseJob.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this JobAskResponseJob.


        :return: The id of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this JobAskResponseJob.


        :param id: The id of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def config(self): # -> None:
        """Gets the config of this JobAskResponseJob.


        :return: The config of this JobAskResponseJob.
        :rtype: object
        """
        ...
    
    @config.setter
    def config(self, config): # -> None:
        """Sets the config of this JobAskResponseJob.


        :param config: The config of this JobAskResponseJob.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def origin(self): # -> None:
        """Gets the origin of this JobAskResponseJob.


        :return: The origin of this JobAskResponseJob.
        :rtype: Origin
        """
        ...
    
    @origin.setter
    def origin(self, origin): # -> None:
        """Sets the origin of this JobAskResponseJob.


        :param origin: The origin of this JobAskResponseJob.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def batch(self): # -> None:
        """Gets the batch of this JobAskResponseJob.


        :return: The batch of this JobAskResponseJob.
        :rtype: str
        """
        ...
    
    @batch.setter
    def batch(self, batch): # -> None:
        """Sets the batch of this JobAskResponseJob.


        :param batch: The batch of this JobAskResponseJob.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def failed_output_accepted(self): # -> None:
        """Gets the failed_output_accepted of this JobAskResponseJob.


        :return: The failed_output_accepted of this JobAskResponseJob.
        :rtype: bool
        """
        ...
    
    @failed_output_accepted.setter
    def failed_output_accepted(self, failed_output_accepted): # -> None:
        """Sets the failed_output_accepted of this JobAskResponseJob.


        :param failed_output_accepted: The failed_output_accepted of this JobAskResponseJob.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def parent_info(self): # -> None:
        """Gets the parent_info of this JobAskResponseJob.


        :return: The parent_info of this JobAskResponseJob.
        :rtype: JobDetailParentInfo
        """
        ...
    
    @parent_info.setter
    def parent_info(self, parent_info): # -> None:
        """Sets the parent_info of this JobAskResponseJob.


        :param parent_info: The parent_info of this JobAskResponseJob.  # noqa: E501
        :type: JobDetailParentInfo
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
    


