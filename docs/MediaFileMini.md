# MediaFileMini

Represents a file or folder on the filesystem that has been seen by the Media Library scanner. Files that are part of a media object are grouped in a MediaFileBundle (whether one file or multiple) and after a bundle is scanned, an Asset is created and assigned to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [readonly] 
**full_path** | **str** |  | [readonly] 
**custom_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**is_dir** | **bool** |  | [readonly] 
**is_hardlink** | **bool** |  | [readonly] 
**mtime** | **int** |  | [readonly] 
**path** | **str** |  | [readonly] 
**path_permissions** | [**PathPermissions**](PathPermissions.md) |  | 
**present** | **bool** |  | [readonly] 
**archived** | **bool** |  | [readonly] 
**size** | **int** |  | [readonly] 
**volume** | [**VolumeMiniWithCloudAccount**](VolumeMiniWithCloudAccount.md) |  | 
**bundle** | **int, none_type** |  | [optional] [readonly] 
**parent** | **int, none_type** |  | [optional] [readonly] 
**parent_file** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] [readonly] 
**restore_expires_at** | **datetime, none_type** |  | [optional] [readonly] 
**storage_class** | **str, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


