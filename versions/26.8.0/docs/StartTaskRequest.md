# StartTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_type** | **str** | Identifier of the task type to run. | 
**parameters** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Parameters to pass to the task, keyed by name. | 
**sync** | **bool** | When true, run the task synchronously and return only once it completes. | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


