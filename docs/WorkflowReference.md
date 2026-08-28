# WorkflowReference

A Media Library workflow: a set of states and the allowed transitions between them, used to track assets through an e.g. review/approval process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**states** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | The workflow states an asset can be in. | [optional] [readonly] 
**transitions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | The allowed transitions between states. | [optional] [readonly] 
**roots** | **[int]** | Media Roots in which this workflow is available. | [optional] [readonly] 
**jobs** | [**[Job]**](Job.md) |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


