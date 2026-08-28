# FileCopyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **[str]** | Filesystem paths to operate on. | 
**destination** | **str** | Destination directory to copy the inputs into. | 
**hardlink** | **bool** | When true, create hardlinks instead of copying file data where possible. | [optional] 
**sync** | **bool** | When true, wait for the copy to finish before responding instead of running it as a background task. | [optional] 
**overwrite** | **str** | How to handle a file that already exists at the destination: skip (Overwrite.SKIP), &#x60;Overwrite.WARN&#x60;, keep both by appending a &#x60;Overwrite.NUMBER&#x60; or &#x60;Overwrite.TIMESTAMP&#x60;, or &#x60;Overwrite.OVERWRITE&#x60; it. | [optional] 
**folders** | **str** | How to handle copying folders: merge contents into existing folder (&#x60;FolderCopyBehaviour.MERGE&#x60;) or rename the new folder (&#x60;FolderCopyBehaviour.RENAME&#x60;). Note that &#x60;Overwrite.OVERWRITE&#x60; logic will still be applied to individual files in both cases. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


