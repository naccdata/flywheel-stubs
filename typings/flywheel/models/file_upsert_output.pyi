"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class FileUpsertOutput:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, id=..., name=..., type=..., file_id=..., version=..., mimetype=..., modality=..., deid_log_id=..., deid_log_skip_reason=..., classification=..., tags=..., provider_id=..., parent_ref=..., parents=..., restored_from=..., restored_by=..., path=..., reference=..., origin=..., virus_scan=..., created=..., modified=..., replaced=..., deleted=..., size=..., hash=..., client_hash=..., info=..., info_exists=..., cvat=..., zip_member_count=..., gear_info=..., copy_of=..., original_copy_of=..., revision=..., file_group=..., upsert_result=...) -> None:
        """FileUpsertOutput - a model defined in Swagger"""
        ...
    
    @property
    def id(self): # -> None:
        """Gets the id of this FileUpsertOutput.

        Hyphen-separated universally unique identifier

        :return: The id of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @id.setter
    def id(self, id): # -> None:
        """Sets the id of this FileUpsertOutput.

        Hyphen-separated universally unique identifier

        :param id: The id of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this FileUpsertOutput.

        The name of the file on disk

        :return: The name of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this FileUpsertOutput.

        The name of the file on disk

        :param name: The name of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def type(self): # -> None:
        """Gets the type of this FileUpsertOutput.

        A descriptive file type (e.g. dicom, image, document, ...)

        :return: The type of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @type.setter
    def type(self, type): # -> None:
        """Sets the type of this FileUpsertOutput.

        A descriptive file type (e.g. dicom, image, document, ...)

        :param type: The type of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def file_id(self): # -> None:
        """Gets the file_id of this FileUpsertOutput.


        :return: The file_id of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @file_id.setter
    def file_id(self, file_id): # -> None:
        """Sets the file_id of this FileUpsertOutput.


        :param file_id: The file_id of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def version(self): # -> None:
        """Gets the version of this FileUpsertOutput.


        :return: The version of this FileUpsertOutput.
        :rtype: int
        """
        ...
    
    @version.setter
    def version(self, version): # -> None:
        """Sets the version of this FileUpsertOutput.


        :param version: The version of this FileUpsertOutput.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def mimetype(self): # -> None:
        """Gets the mimetype of this FileUpsertOutput.

        A MIME Content-Type of the file

        :return: The mimetype of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @mimetype.setter
    def mimetype(self, mimetype): # -> None:
        """Sets the mimetype of this FileUpsertOutput.

        A MIME Content-Type of the file

        :param mimetype: The mimetype of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def modality(self): # -> None:
        """Gets the modality of this FileUpsertOutput.

        The type of instrument that originated the file (e.g. MR, CT, ...)

        :return: The modality of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @modality.setter
    def modality(self, modality): # -> None:
        """Sets the modality of this FileUpsertOutput.

        The type of instrument that originated the file (e.g. MR, CT, ...)

        :param modality: The modality of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def deid_log_id(self): # -> None:
        """Gets the deid_log_id of this FileUpsertOutput.

        The UUID of the de-id log

        :return: The deid_log_id of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @deid_log_id.setter
    def deid_log_id(self, deid_log_id): # -> None:
        """Sets the deid_log_id of this FileUpsertOutput.

        The UUID of the de-id log

        :param deid_log_id: The deid_log_id of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def deid_log_skip_reason(self): # -> None:
        """Gets the deid_log_skip_reason of this FileUpsertOutput.


        :return: The deid_log_skip_reason of this FileUpsertOutput.
        :rtype: DeidLogSkipReason
        """
        ...
    
    @deid_log_skip_reason.setter
    def deid_log_skip_reason(self, deid_log_skip_reason): # -> None:
        """Sets the deid_log_skip_reason of this FileUpsertOutput.


        :param deid_log_skip_reason: The deid_log_skip_reason of this FileUpsertOutput.  # noqa: E501
        :type: DeidLogSkipReason
        """
        ...
    
    @property
    def classification(self): # -> None:
        """Gets the classification of this FileUpsertOutput.


        :return: The classification of this FileUpsertOutput.
        :rtype: dict(str, list[str])
        """
        ...
    
    @classification.setter
    def classification(self, classification): # -> None:
        """Sets the classification of this FileUpsertOutput.


        :param classification: The classification of this FileUpsertOutput.  # noqa: E501
        :type: dict(str, list[str])
        """
        ...
    
    @property
    def tags(self): # -> None:
        """Gets the tags of this FileUpsertOutput.


        :return: The tags of this FileUpsertOutput.
        :rtype: list[str]
        """
        ...
    
    @tags.setter
    def tags(self, tags): # -> None:
        """Sets the tags of this FileUpsertOutput.


        :param tags: The tags of this FileUpsertOutput.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def provider_id(self): # -> None:
        """Gets the provider_id of this FileUpsertOutput.

        Unique database ID

        :return: The provider_id of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @provider_id.setter
    def provider_id(self, provider_id): # -> None:
        """Sets the provider_id of this FileUpsertOutput.

        Unique database ID

        :param provider_id: The provider_id of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def parent_ref(self): # -> None:
        """Gets the parent_ref of this FileUpsertOutput.


        :return: The parent_ref of this FileUpsertOutput.
        :rtype: ContainerReference
        """
        ...
    
    @parent_ref.setter
    def parent_ref(self, parent_ref): # -> None:
        """Sets the parent_ref of this FileUpsertOutput.


        :param parent_ref: The parent_ref of this FileUpsertOutput.  # noqa: E501
        :type: ContainerReference
        """
        ...
    
    @property
    def parents(self): # -> None:
        """Gets the parents of this FileUpsertOutput.


        :return: The parents of this FileUpsertOutput.
        :rtype: FileParents
        """
        ...
    
    @parents.setter
    def parents(self, parents): # -> None:
        """Sets the parents of this FileUpsertOutput.


        :param parents: The parents of this FileUpsertOutput.  # noqa: E501
        :type: FileParents
        """
        ...
    
    @property
    def restored_from(self): # -> None:
        """Gets the restored_from of this FileUpsertOutput.


        :return: The restored_from of this FileUpsertOutput.
        :rtype: int
        """
        ...
    
    @restored_from.setter
    def restored_from(self, restored_from): # -> None:
        """Sets the restored_from of this FileUpsertOutput.


        :param restored_from: The restored_from of this FileUpsertOutput.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def restored_by(self): # -> None:
        """Gets the restored_by of this FileUpsertOutput.


        :return: The restored_by of this FileUpsertOutput.
        :rtype: Origin
        """
        ...
    
    @restored_by.setter
    def restored_by(self, restored_by): # -> None:
        """Sets the restored_by of this FileUpsertOutput.


        :param restored_by: The restored_by of this FileUpsertOutput.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def path(self): # -> None:
        """Gets the path of this FileUpsertOutput.


        :return: The path of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @path.setter
    def path(self, path): # -> None:
        """Sets the path of this FileUpsertOutput.


        :param path: The path of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def reference(self): # -> None:
        """Gets the reference of this FileUpsertOutput.


        :return: The reference of this FileUpsertOutput.
        :rtype: bool
        """
        ...
    
    @reference.setter
    def reference(self, reference): # -> None:
        """Sets the reference of this FileUpsertOutput.


        :param reference: The reference of this FileUpsertOutput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def origin(self): # -> None:
        """Gets the origin of this FileUpsertOutput.


        :return: The origin of this FileUpsertOutput.
        :rtype: Origin
        """
        ...
    
    @origin.setter
    def origin(self, origin): # -> None:
        """Sets the origin of this FileUpsertOutput.


        :param origin: The origin of this FileUpsertOutput.  # noqa: E501
        :type: Origin
        """
        ...
    
    @property
    def virus_scan(self): # -> None:
        """Gets the virus_scan of this FileUpsertOutput.


        :return: The virus_scan of this FileUpsertOutput.
        :rtype: VirusScan
        """
        ...
    
    @virus_scan.setter
    def virus_scan(self, virus_scan): # -> None:
        """Sets the virus_scan of this FileUpsertOutput.


        :param virus_scan: The virus_scan of this FileUpsertOutput.  # noqa: E501
        :type: VirusScan
        """
        ...
    
    @property
    def created(self): # -> None:
        """Gets the created of this FileUpsertOutput.


        :return: The created of this FileUpsertOutput.
        :rtype: datetime
        """
        ...
    
    @created.setter
    def created(self, created): # -> None:
        """Sets the created of this FileUpsertOutput.


        :param created: The created of this FileUpsertOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def modified(self): # -> None:
        """Gets the modified of this FileUpsertOutput.


        :return: The modified of this FileUpsertOutput.
        :rtype: datetime
        """
        ...
    
    @modified.setter
    def modified(self, modified): # -> None:
        """Sets the modified of this FileUpsertOutput.


        :param modified: The modified of this FileUpsertOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def replaced(self): # -> None:
        """Gets the replaced of this FileUpsertOutput.


        :return: The replaced of this FileUpsertOutput.
        :rtype: datetime
        """
        ...
    
    @replaced.setter
    def replaced(self, replaced): # -> None:
        """Sets the replaced of this FileUpsertOutput.


        :param replaced: The replaced of this FileUpsertOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def deleted(self): # -> None:
        """Gets the deleted of this FileUpsertOutput.


        :return: The deleted of this FileUpsertOutput.
        :rtype: datetime
        """
        ...
    
    @deleted.setter
    def deleted(self, deleted): # -> None:
        """Sets the deleted of this FileUpsertOutput.


        :param deleted: The deleted of this FileUpsertOutput.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def size(self): # -> None:
        """Gets the size of this FileUpsertOutput.


        :return: The size of this FileUpsertOutput.
        :rtype: int
        """
        ...
    
    @size.setter
    def size(self, size): # -> None:
        """Sets the size of this FileUpsertOutput.


        :param size: The size of this FileUpsertOutput.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def hash(self): # -> None:
        """Gets the hash of this FileUpsertOutput.


        :return: The hash of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @hash.setter
    def hash(self, hash): # -> None:
        """Sets the hash of this FileUpsertOutput.


        :param hash: The hash of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def client_hash(self): # -> None:
        """Gets the client_hash of this FileUpsertOutput.


        :return: The client_hash of this FileUpsertOutput.
        :rtype: str
        """
        ...
    
    @client_hash.setter
    def client_hash(self, client_hash): # -> None:
        """Sets the client_hash of this FileUpsertOutput.


        :param client_hash: The client_hash of this FileUpsertOutput.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def info(self): # -> None:
        """Gets the info of this FileUpsertOutput.

        Free-form information storage

        :return: The info of this FileUpsertOutput.
        :rtype: object
        """
        ...
    
    @info.setter
    def info(self, info): # -> None:
        """Sets the info of this FileUpsertOutput.

        Free-form information storage

        :param info: The info of this FileUpsertOutput.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def info_exists(self): # -> None:
        """Gets the info_exists of this FileUpsertOutput.


        :return: The info_exists of this FileUpsertOutput.
        :rtype: bool
        """
        ...
    
    @info_exists.setter
    def info_exists(self, info_exists): # -> None:
        """Sets the info_exists of this FileUpsertOutput.


        :param info_exists: The info_exists of this FileUpsertOutput.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def cvat(self): # -> None:
        """Gets the cvat of this FileUpsertOutput.


        :return: The cvat of this FileUpsertOutput.
        :rtype: CVATInfo
        """
        ...
    
    @cvat.setter
    def cvat(self, cvat): # -> None:
        """Sets the cvat of this FileUpsertOutput.


        :param cvat: The cvat of this FileUpsertOutput.  # noqa: E501
        :type: CVATInfo
        """
        ...
    
    @property
    def zip_member_count(self): # -> None:
        """Gets the zip_member_count of this FileUpsertOutput.

        Number of entries in the zip archive

        :return: The zip_member_count of this FileUpsertOutput.
        :rtype: int
        """
        ...
    
    @zip_member_count.setter
    def zip_member_count(self, zip_member_count): # -> None:
        """Sets the zip_member_count of this FileUpsertOutput.

        Number of entries in the zip archive

        :param zip_member_count: The zip_member_count of this FileUpsertOutput.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def gear_info(self): # -> None:
        """Gets the gear_info of this FileUpsertOutput.


        :return: The gear_info of this FileUpsertOutput.
        :rtype: FileGearInfo
        """
        ...
    
    @gear_info.setter
    def gear_info(self, gear_info): # -> None:
        """Sets the gear_info of this FileUpsertOutput.


        :param gear_info: The gear_info of this FileUpsertOutput.  # noqa: E501
        :type: FileGearInfo
        """
        ...
    
    @property
    def copy_of(self): # -> None:
        """Gets the copy_of of this FileUpsertOutput.


        :return: The copy_of of this FileUpsertOutput.
        :rtype: FileVersionCopyOf
        """
        ...
    
    @copy_of.setter
    def copy_of(self, copy_of): # -> None:
        """Sets the copy_of of this FileUpsertOutput.


        :param copy_of: The copy_of of this FileUpsertOutput.  # noqa: E501
        :type: FileVersionCopyOf
        """
        ...
    
    @property
    def original_copy_of(self): # -> None:
        """Gets the original_copy_of of this FileUpsertOutput.


        :return: The original_copy_of of this FileUpsertOutput.
        :rtype: FileVersion
        """
        ...
    
    @original_copy_of.setter
    def original_copy_of(self, original_copy_of): # -> None:
        """Sets the original_copy_of of this FileUpsertOutput.


        :param original_copy_of: The original_copy_of of this FileUpsertOutput.  # noqa: E501
        :type: FileVersion
        """
        ...
    
    @property
    def revision(self): # -> None:
        """Gets the revision of this FileUpsertOutput.


        :return: The revision of this FileUpsertOutput.
        :rtype: int
        """
        ...
    
    @revision.setter
    def revision(self, revision): # -> None:
        """Sets the revision of this FileUpsertOutput.


        :param revision: The revision of this FileUpsertOutput.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def file_group(self): # -> None:
        """Gets the file_group of this FileUpsertOutput.


        :return: The file_group of this FileUpsertOutput.
        :rtype: FileGroup
        """
        ...
    
    @file_group.setter
    def file_group(self, file_group): # -> None:
        """Sets the file_group of this FileUpsertOutput.


        :param file_group: The file_group of this FileUpsertOutput.  # noqa: E501
        :type: FileGroup
        """
        ...
    
    @property
    def upsert_result(self): # -> None:
        """Gets the upsert_result of this FileUpsertOutput.


        :return: The upsert_result of this FileUpsertOutput.
        :rtype: UpsertResult
        """
        ...
    
    @upsert_result.setter
    def upsert_result(self, upsert_result): # -> None:
        """Sets the upsert_result of this FileUpsertOutput.


        :param upsert_result: The upsert_result of this FileUpsertOutput.  # noqa: E501
        :type: UpsertResult
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
    


