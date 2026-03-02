# MediaFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**volume** | [**VolumeMiniWithCloudAccount**](VolumeMiniWithCloudAccount.md) |  | 
**info** | **{str: (str, none_type)}** |  | 
**custom_fields** | **{str: (str, none_type)}** |  | 
**full_path** | **str** |  | [readonly] 
**path_permissions** | [**PathPermissions**](PathPermissions.md) |  | 
**is_shared** | **bool, none_type** |  | [readonly] 
**is_hardlink** | **bool** |  | [readonly] 
**is_bookmarked** | **bool, none_type** |  | [readonly] 
**exclusion_info** | [**MediaFileExclusionInfo**](MediaFileExclusionInfo.md) |  | 
**child_count** | **int, none_type** |  | [readonly] 
**name** | **str** |  | [readonly] 
**path** | **str** |  | [readonly] 
**pathhash** | **str** |  | [readonly] 
**ancestry** | **str** |  | [readonly] 
**is_dir** | **bool** |  | [readonly] 
**total_files** | **int, none_type** |  | 
**size** | **int** |  | [readonly] 
**mtime** | **int** |  | [readonly] 
**present** | **bool** |  | [readonly] 
**archived** | **bool** |  | [readonly] 
**needs_rescan** | **bool** |  | 
**is_showroom** | **bool** |  | [readonly] 
**bundle_index** | **int** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**resolved_permission** | [**MediaRootPermission**](MediaRootPermission.md) |  | [optional] 
**parent_file** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] [readonly] 
**root** | [**MediaRootMini**](MediaRootMini.md) |  | [optional] 
**effective_custom_fields** | **{str: (str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_by** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**storage_class** | **str, none_type** |  | [optional] [readonly] 
**restore_expires_at** | **datetime, none_type** |  | [optional] [readonly] 
**parent** | **int, none_type** |  | [optional] [readonly] 
**bundle** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


