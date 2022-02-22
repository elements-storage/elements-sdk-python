# Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**subtasks** | [**list[SubtaskReference]**](SubtaskReference.md) |  | [optional] 
**schedules** | [**list[ScheduleReference]**](ScheduleReference.md) |  | [optional] 
**allow_users** | [**list[ElementsUserReference]**](ElementsUserReference.md) |  | [optional] 
**allow_groups** | [**list[ElementsGroupReference]**](ElementsGroupReference.md) |  | [optional] 
**startable** | **bool** |  | [optional] [readonly] 
**variable_definitions** | **list[dict(str, object)]** |  | [optional] 
**media_roots** | **list[int]** |  | [optional] 
**webhook_url** | **str** |  | [optional] [readonly] 
**special_type** | **int** |  | [optional] 
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**allow_others_to_start** | **bool** |  | [optional] 
**allow_client_to_start** | **bool** |  | [optional] 
**show_as_button** | **bool** |  | [optional] 
**input_type** | **str** |  | [optional] 
**hook** | **str** |  | [optional] 
**webhook_secret** | **str** |  | [optional] 
**security_context** | **int** |  | [optional] 
**part_of_workflow_for** | **int** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


