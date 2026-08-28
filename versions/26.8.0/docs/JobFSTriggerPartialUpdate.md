# JobFSTriggerPartialUpdate

A filesystem-change trigger that automatically starts a job when matching files are created, modified, renamed or deleted under a watched path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Filesystem path to watch for changes. | [optional] 
**name_glob** | **str** | Glob pattern; only files whose name matches it fire the trigger. | [optional] 
**recursive** | **bool** | Also watch subdirectories of the path. | [optional] 
**listen_for_created** | **bool** |  | [optional] 
**listen_for_modified** | **bool** |  | [optional] 
**listen_for_renamed** | **bool** |  | [optional] 
**listen_for_deleted** | **bool** |  | [optional] 
**job** | **int** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


