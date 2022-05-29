# JobReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**subtasks** | [**list[SubtaskReference]**](SubtaskReference.md) |  | [optional] [readonly] 
**schedules** | [**list[ScheduleReference]**](ScheduleReference.md) |  | [optional] [readonly] 
**allow_users** | [**list[ElementsUserReference]**](ElementsUserReference.md) |  | [optional] [readonly] 
**allow_groups** | [**list[ElementsGroupReference]**](ElementsGroupReference.md) |  | [optional] [readonly] 
**startable** | **bool** |  | [optional] [readonly] 
**variable_definitions** | **list[dict(str, str)]** |  | [optional] [readonly] 
**media_roots** | **list[int]** |  | [optional] [readonly] 
**webhook_url** | **str** |  | [optional] [readonly] 
**special_type** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**enabled** | **bool** |  | [optional] [readonly] 
**allow_others_to_start** | **bool** |  | [optional] [readonly] 
**allow_client_to_start** | **bool** |  | [optional] [readonly] 
**show_as_button** | **bool** |  | [optional] [readonly] 
**input_type** | **str** |  | [optional] [readonly] 
**hook** | **str** |  | [optional] [readonly] 
**webhook_secret** | **str** |  | [optional] [readonly] 
**security_context** | **int** |  | [optional] [readonly] 
**part_of_workflow_for** | **int** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


