"""
This type stub file was generated by pyright.
"""

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
class DataViewFileSpec:
    swagger_types = ...
    attribute_map = ...
    rattribute_map = ...
    def __init__(self, container=..., analysis_filter=..., filter=..., zip_member=..., match=..., format=..., format_options=..., process_files=..., columns=...) -> None:
        """DataViewFileSpec - a model defined in Swagger"""
        ...
    
    @property
    def container(self): # -> None:
        """Gets the container of this DataViewFileSpec.

        The type of container (e.g. session)

        :return: The container of this DataViewFileSpec.
        :rtype: str
        """
        ...
    
    @container.setter
    def container(self, container): # -> None:
        """Sets the container of this DataViewFileSpec.

        The type of container (e.g. session)

        :param container: The container of this DataViewFileSpec.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def analysis_filter(self): # -> None:
        """Gets the analysis_filter of this DataViewFileSpec.


        :return: The analysis_filter of this DataViewFileSpec.
        :rtype: DataViewAnalysisFilterSpec
        """
        ...
    
    @analysis_filter.setter
    def analysis_filter(self, analysis_filter): # -> None:
        """Sets the analysis_filter of this DataViewFileSpec.


        :param analysis_filter: The analysis_filter of this DataViewFileSpec.  # noqa: E501
        :type: DataViewAnalysisFilterSpec
        """
        ...
    
    @property
    def filter(self): # -> None:
        """Gets the filter of this DataViewFileSpec.


        :return: The filter of this DataViewFileSpec.
        :rtype: DataViewNameFilterSpec
        """
        ...
    
    @filter.setter
    def filter(self, filter): # -> None:
        """Sets the filter of this DataViewFileSpec.


        :param filter: The filter of this DataViewFileSpec.  # noqa: E501
        :type: DataViewNameFilterSpec
        """
        ...
    
    @property
    def zip_member(self): # -> None:
        """Gets the zip_member of this DataViewFileSpec.


        :return: The zip_member of this DataViewFileSpec.
        :rtype: DataViewZipFilterSpec
        """
        ...
    
    @zip_member.setter
    def zip_member(self, zip_member): # -> None:
        """Sets the zip_member of this DataViewFileSpec.


        :param zip_member: The zip_member of this DataViewFileSpec.  # noqa: E501
        :type: DataViewZipFilterSpec
        """
        ...
    
    @property
    def match(self): # -> None:
        """Gets the match of this DataViewFileSpec.

        If multiple file matches are encountered, which file to choose. Default is first

        :return: The match of this DataViewFileSpec.
        :rtype: str
        """
        ...
    
    @match.setter
    def match(self, match): # -> None:
        """Sets the match of this DataViewFileSpec.

        If multiple file matches are encountered, which file to choose. Default is first

        :param match: The match of this DataViewFileSpec.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def format(self): # -> None:
        """Gets the format of this DataViewFileSpec.

        The expected data file format, default is auto-detect

        :return: The format of this DataViewFileSpec.
        :rtype: str
        """
        ...
    
    @format.setter
    def format(self, format): # -> None:
        """Sets the format of this DataViewFileSpec.

        The expected data file format, default is auto-detect

        :param format: The format of this DataViewFileSpec.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def format_options(self): # -> None:
        """Gets the format_options of this DataViewFileSpec.


        :return: The format_options of this DataViewFileSpec.
        :rtype: object
        """
        ...
    
    @format_options.setter
    def format_options(self, format_options): # -> None:
        """Sets the format_options of this DataViewFileSpec.


        :param format_options: The format_options of this DataViewFileSpec.  # noqa: E501
        :type: object
        """
        ...
    
    @property
    def process_files(self): # -> None:
        """Gets the process_files of this DataViewFileSpec.

        Set to false to skip file reading, and return file attributes instead

        :return: The process_files of this DataViewFileSpec.
        :rtype: bool
        """
        ...
    
    @process_files.setter
    def process_files(self, process_files): # -> None:
        """Sets the process_files of this DataViewFileSpec.

        Set to false to skip file reading, and return file attributes instead

        :param process_files: The process_files of this DataViewFileSpec.  # noqa: E501
        :type: bool
        """
        ...
    
    @property
    def columns(self): # -> None:
        """Gets the columns of this DataViewFileSpec.


        :return: The columns of this DataViewFileSpec.
        :rtype: list[DataViewColumnSpec]
        """
        ...
    
    @columns.setter
    def columns(self, columns): # -> None:
        """Sets the columns of this DataViewFileSpec.


        :param columns: The columns of this DataViewFileSpec.  # noqa: E501
        :type: list[DataViewColumnSpec]
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
    


