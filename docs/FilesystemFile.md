# FilesystemFile

A physical file or directory on a storage volume, including its size, timestamps, ownership and permission modes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [readonly] 
**name** | **str** |  | 
**size** | **int** |  | [readonly] 
**modification_time** | **datetime** |  | [readonly] 
**is_dir** | **bool** |  | [readonly] 
**path_permissions** | [**PathPermissions**](PathPermissions.md) |  | 
**total_size** | **int** |  | [readonly] 
**parent** | **str** |  | 
**access_time** | **datetime** |  | [readonly] 
**creation_time** | **datetime** |  | [readonly] 
**mode** | **str** |  | [optional] 
**uid** | **int** |  | [optional] 
**gid** | **int** |  | [optional] 
**user** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**recursive** | **bool** | Apply the given ownership and permission modes to all existing contents recursively. | [optional] 
**affinity** | **str, none_type** | StorNext (SNFS) affinity to assign, controlling which storage pool the data is placed on. | [optional] 
**files** | [**[DirectoryEntry], none_type**](DirectoryEntry.md) |  | [optional] 
**mode_setuid** | **bool** |  | [optional] 
**mode_setgid** | **bool** |  | [optional] 
**mode_setvfx** | **bool** |  | [optional] 
**mode_user_read** | **bool** |  | [optional] 
**mode_user_write** | **bool** |  | [optional] 
**mode_user_execute** | **bool** |  | [optional] 
**mode_group_read** | **bool** |  | [optional] 
**mode_group_write** | **bool** |  | [optional] 
**mode_group_execute** | **bool** |  | [optional] 
**mode_others_read** | **bool** |  | [optional] 
**mode_others_write** | **bool** |  | [optional] 
**mode_others_execute** | **bool** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


