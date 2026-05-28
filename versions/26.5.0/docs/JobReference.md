# JobReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**schedules** | [**[Schedule]**](Schedule.md) |  | [optional] [readonly] 
**startable** | **bool** |  | [optional] [readonly] 
**variable_definitions** | [**[JobVariableDefinition]**](JobVariableDefinition.md) |  | [optional] [readonly] 
**webhook_url** | **str, none_type** |  | [optional] [readonly] 
**needs_compatibility_check** | **bool** |  | [optional] [readonly] 
**special_type** | **int, none_type** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] [readonly] 
**enabled** | **bool** |  | [optional] [readonly] 
**allow_others_to_start** | **bool** |  When &#x60;allow_users&#x60; is an empty array, this flag allows users with the \&quot;tasks:start\&quot; permission to run this job, even without the \&quot;tasks:manage\&quot; permission. Otherwise, only users specified in &#x60;allow_users&#x60; and belonging to &#x60;allow_groups&#x60; can start the job (irrespective of permissions \&quot;tasks:start\&quot; and \&quot;tasks:manage\&quot;).  | [optional] [readonly] 
**allow_client_to_start** | **bool** |  | [optional] [readonly] 
**show_as_button** | **bool** |  | [optional] [readonly] 
**input_type** | **str, none_type** |  | [optional] [readonly] 
**add_to_new_media_roots** | **bool** |  | [optional] [readonly] 
**hook** | **str, none_type** |  | [optional] [readonly] 
**webhook_secret** | **str, none_type** |  | [optional] [readonly] 
**elements_release** | **str** |  | [optional] [readonly] 
**no_concurrency** | **bool** |  | [optional] [readonly] 
**security_context** | **int, none_type** |  | [optional] [readonly] 
**workflow** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


