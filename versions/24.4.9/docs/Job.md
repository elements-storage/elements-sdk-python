# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**startable** | **bool** |  | [readonly] 
**webhook_url** | **str, none_type** |  | [readonly] 
**needs_compatibility_check** | **bool** |  | [readonly] 
**subtasks** | **[str]** |  | [readonly] 
**allow_users** | **[str]** |  | [readonly] 
**allow_groups** | **[str]** |  | [readonly] 
**media_roots** | **[str]** |  | [readonly] 
**name** | **str** |  | 
**schedules** | [**[ScheduleReference]**](ScheduleReference.md) |  | [optional] 
**variable_definitions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**special_type** | **int, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**allow_others_to_start** | **bool** |  | [optional] 
**allow_client_to_start** | **bool** |  | [optional] 
**show_as_button** | **bool** |  | [optional] 
**input_type** | **str, none_type** |  | [optional] 
**add_to_new_media_roots** | **bool** |  | [optional] 
**hook** | **str, none_type** |  | [optional] 
**webhook_secret** | **str, none_type** |  | [optional] 
**elements_release** | **str** |  | [optional] 
**security_context** | **int, none_type** |  | [optional] 
**part_of_workflow_for** | **int, none_type** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)

