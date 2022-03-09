# JobReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**subtasks** | [**[SubtaskReference]**](SubtaskReference.md) |  | [optional] [readonly] 
**schedules** | [**[ScheduleReference]**](ScheduleReference.md) |  | [optional] [readonly] 
**allow_users** | [**[ElementsUserReference]**](ElementsUserReference.md) |  | [optional] [readonly] 
**allow_groups** | [**[ElementsGroupReference]**](ElementsGroupReference.md) |  | [optional] [readonly] 
**startable** | **bool** |  | [optional] [readonly] 
**variable_definitions** | **[{str: (str, none_type)}]** |  | [optional] [readonly] 
**media_roots** | **[int]** |  | [optional] [readonly] 
**webhook_url** | **str, none_type** |  | [optional] [readonly] 
**special_type** | **int, none_type** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**enabled** | **bool** |  | [optional] [readonly] 
**allow_others_to_start** | **bool** |  | [optional] [readonly] 
**allow_client_to_start** | **bool** |  | [optional] [readonly] 
**show_as_button** | **bool** |  | [optional] [readonly] 
**input_type** | **str, none_type** |  | [optional] [readonly] 
**hook** | **str, none_type** |  | [optional] [readonly] 
**webhook_secret** | **str, none_type** |  | [optional] [readonly] 
**security_context** | **int, none_type** |  | [optional] [readonly] 
**part_of_workflow_for** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


