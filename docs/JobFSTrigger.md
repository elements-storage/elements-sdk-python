# JobFSTrigger

A filesystem-change trigger that automatically starts a job when matching files are created, modified, renamed or deleted under a watched path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**path** | **str** | Filesystem path to watch for changes. | 
**name_glob** | **str** | Glob pattern; only files whose name matches it fire the trigger. | 
**recursive** | **bool** | Also watch subdirectories of the path. | 
**listen_for_created** | **bool** |  | 
**listen_for_modified** | **bool** |  | 
**listen_for_renamed** | **bool** |  | 
**listen_for_deleted** | **bool** |  | 
**job** | **int** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


