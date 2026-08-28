# Workflow

A Media Library workflow: a set of states and the allowed transitions between them, used to track assets through an e.g. review/approval process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**states** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | The workflow states an asset can be in. | 
**transitions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | The allowed transitions between states. | 
**roots** | **[int]** | Media Roots in which this workflow is available. | 
**jobs** | [**[Job]**](Job.md) |  | [readonly] 
**name** | **str** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


