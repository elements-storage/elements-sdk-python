# FilesystemPermissionPartialUpdate

A low-level grant of filesystem access to an ELEMENTS WebUI user or group for a path, useful e.g. for granting additional access to paths for Automation jobs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Filesystem path this permission grants access to. | [optional] 
**read_only** | **bool** | When true, grant read-only access; otherwise read-write. | [optional] 
**user** | **int, none_type** |  | [optional] 
**group** | **int, none_type** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


