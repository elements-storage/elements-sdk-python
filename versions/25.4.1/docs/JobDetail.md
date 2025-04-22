# JobDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**schedules** | [**[Schedule]**](Schedule.md) |  | 
**startable** | **bool** |  | [readonly] 
**variable_definitions** | **[{str: (str, none_type)}]** |  | 
**webhook_url** | **str, none_type** |  | [readonly] 
**needs_compatibility_check** | **bool** |  | [readonly] 
**fs_triggers** | [**[JobFSTrigger]**](JobFSTrigger.md) |  | [readonly] 
**part_of_workflow_for** | **[str]** |  | [readonly] 
**subtasks** | [**[Subtask]**](Subtask.md) |  | 
**allow_users** | [**[ElementsUser]**](ElementsUser.md) |  | 
**allow_groups** | [**[ElementsGroup]**](ElementsGroup.md) |  | 
**media_roots** | **[int]** |  | 
**workflow** | **int, none_type** |  | 
**special_type** | **int, none_type** |  | 
**name** | **str** |  | 
**description** | **str, none_type** |  | 
**enabled** | **bool** |  | 
**allow_others_to_start** | **bool** |  | 
**allow_client_to_start** | **bool** |  | 
**show_as_button** | **bool** |  | 
**input_type** | **str, none_type** |  | 
**add_to_new_media_roots** | **bool** |  | 
**hook** | **str, none_type** |  | 
**webhook_secret** | **str, none_type** |  | 
**elements_release** | **str** |  | 
**security_context** | **int, none_type** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


