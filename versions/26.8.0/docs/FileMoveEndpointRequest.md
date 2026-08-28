# FileMoveEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **[str]** | Filesystem paths to operate on. | 
**destination** | **str** | Destination directory to move the inputs into. | 
**sync** | **bool** | When true, wait for the move to finish before responding instead of running it as a background task. | [optional] 
**overwrite** | **str** | How to handle a file that already exists at the destination: skip (Overwrite.SKIP), &#x60;Overwrite.WARN&#x60;, keep both by appending a &#x60;Overwrite.NUMBER&#x60; or &#x60;Overwrite.TIMESTAMP&#x60;, or &#x60;Overwrite.OVERWRITE&#x60; it. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


