# WorkflowPartialUpdate

A Media Library workflow: a set of states and the allowed transitions between them, used to track assets through an e.g. review/approval process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | The workflow states an asset can be in. | [optional] 
**transitions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | The allowed transitions between states. | [optional] 
**roots** | **[int]** | Media Roots in which this workflow is available. | [optional] 
**name** | **str** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


