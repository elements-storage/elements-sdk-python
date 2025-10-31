# JobDetailUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_definitions** | [**[JobVariableDefinition]**](JobVariableDefinition.md) |  | 
**name** | **str** |  | 
**schedules** | [**[ScheduleReference]**](ScheduleReference.md) |  | [optional] 
**subtasks** | [**[SubtaskReference]**](SubtaskReference.md) |  | [optional] 
**allow_users** | [**[ElementsUserReference]**](ElementsUserReference.md) |  | [optional] 
**allow_groups** | [**[ElementsGroupReference]**](ElementsGroupReference.md) |  | [optional] 
**media_roots** | **[int]** |  | [optional] 
**workflow** | **int, none_type** |  | [optional] 
**special_type** | **int, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**allow_others_to_start** | **bool** |  When &#x60;allow_users&#x60; is an empty array, this flag allows users with the \&quot;tasks:start\&quot; permission to run this job, even without the \&quot;tasks:manage\&quot; permission. Otherwise, only users specified in &#x60;allow_users&#x60; and belonging to &#x60;allow_groups&#x60; can start the job (irrespective of permissions \&quot;tasks:start\&quot; and \&quot;tasks:manage\&quot;).  | [optional] 
**allow_client_to_start** | **bool** |  | [optional] 
**show_as_button** | **bool** |  | [optional] 
**input_type** | **str, none_type** |  | [optional] 
**add_to_new_media_roots** | **bool** |  | [optional] 
**hook** | **str, none_type** |  | [optional] 
**webhook_secret** | **str, none_type** |  | [optional] 
**elements_release** | **str** |  | [optional] 
**security_context** | **int, none_type** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


