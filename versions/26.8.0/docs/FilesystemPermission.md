# FilesystemPermission

A low-level grant of filesystem access to an ELEMENTS WebUI user or group for a path, useful e.g. for granting additional access to paths for Automation jobs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**path** | **str** | Filesystem path this permission grants access to. | 
**read_only** | **bool** | When true, grant read-only access; otherwise read-write. | 
**user** | **int, none_type** |  | 
**group** | **int, none_type** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


