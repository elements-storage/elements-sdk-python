# WorkflowTransitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | **int** | The workflow transition job to run on the selected assets. | 
**root** | **int** | The Media Root whose workflow the transition belongs to. | 
**bundles** | **[int]** | Bundles to transition. | [optional] 
**directories** | **[int]** | Directories whose contents to transition. | [optional] 
**variables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Variable values to pass to the transition job. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


