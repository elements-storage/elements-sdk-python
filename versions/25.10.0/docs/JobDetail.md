# JobDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**schedules** | [**[Schedule]**](Schedule.md) |  | 
**startable** | **bool** |  | [readonly] 
**variable_definitions** | [**[JobVariableDefinition]**](JobVariableDefinition.md) |  | 
**webhook_url** | **str, none_type** |  | [readonly] 
**needs_compatibility_check** | **bool** |  | [readonly] 
**subtasks** | [**[Subtask]**](Subtask.md) |  | 
**allow_users** | [**[ElementsUser]**](ElementsUser.md) |  | 
**allow_groups** | [**[ElementsGroup]**](ElementsGroup.md) |  | 
**media_roots** | **[int]** |  | 
**workflow** | **int, none_type** |  | 
**fs_triggers** | [**[JobFSTrigger]**](JobFSTrigger.md) |  | [readonly] 
**special_type** | **int, none_type** |  | 
**name** | **str** |  | 
**description** | **str, none_type** |  | 
**enabled** | **bool** |  | 
**allow_others_to_start** | **bool** |  When &#x60;allow_users&#x60; is an empty array, this flag allows users with the \&quot;tasks:start\&quot; permission to run this job, even without the \&quot;tasks:manage\&quot; permission. Otherwise, only users specified in &#x60;allow_users&#x60; and belonging to &#x60;allow_groups&#x60; can start the job (irrespective of permissions \&quot;tasks:start\&quot; and \&quot;tasks:manage\&quot;).  | 
**allow_client_to_start** | **bool** |  | 
**show_as_button** | **bool** |  | 
**input_type** | **str, none_type** |  | 
**add_to_new_media_roots** | **bool** |  | 
**hook** | **str, none_type** |  | 
**webhook_secret** | **str, none_type** |  | 
**elements_release** | **str** |  | 
**security_context** | **int, none_type** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


