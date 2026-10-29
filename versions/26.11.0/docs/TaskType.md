# TaskType

A registered Automation task type that can be run, with its identifier, display metadata, accepted parameters and outputs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**display_name** | **str** |  | 
**display_group** | **str** |  | 
**description** | **str, none_type** |  | 
**input_type** | **str, none_type** |  | 
**abortable** | **bool** |  | 
**arg_template** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | 
**args_schema** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | JSON Schema describing the task parameters | [readonly] 
**required_args** | **[str]** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty array. | [readonly] 
**output_names** | **{str: (str,)}** |  | 
**output_types** | [**{str: (ArgumentType,)}**](ArgumentType.md) |  | [readonly] 
**parameters_editor_component** | **str, none_type** |  | 
**superuser_only** | **bool** |  | 
**icon_class** | **str, none_type** |  | 
**is_available** | **bool** |  | [readonly] 
**allow_in_jobs** | **bool** |  | 
**required_permissions** | **[str]** |  | 
**new_since_version** | **str, none_type** |  | 
**wildcard_input** | **bool, none_type** |  | 
**license_component** | **str, none_type** |  | [readonly] 
**arg_types** | **str, none_type** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty string. | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


