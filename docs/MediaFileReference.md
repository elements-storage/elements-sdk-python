# MediaFileReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**volume** | [**VolumeMini**](VolumeMini.md) |  | [optional] 
**info** | **{str: (str, none_type)}** |  | [optional] [readonly] 
**custom_fields** | **{str: (str, none_type)}** |  | [optional] [readonly] 
**resolved_permission** | [**MediaRootPermission**](MediaRootPermission.md) |  | [optional] 
**parent_file** | **{str: (str, none_type)}** |  | [optional] [readonly] 
**root** | [**MediaRootMini**](MediaRootMini.md) |  | [optional] 
**effective_custom_fields** | **{str: (str, none_type)}** |  | [optional] [readonly] 
**modified_by** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**full_path** | **str** |  | [optional] [readonly] 
**is_shared** | **bool, none_type** |  | [optional] [readonly] 
**is_excluded** | **bool** |  | [optional] [readonly] 
**is_hardlink** | **bool** |  | [optional] [readonly] 
**is_bookmarked** | **bool, none_type** |  | [optional] [readonly] 
**child_count** | **int, none_type** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**path** | **str** |  | [optional] [readonly] 
**pathhash** | **str** |  | [optional] [readonly] 
**ancestry** | **str** |  | [optional] [readonly] 
**is_dir** | **bool** |  | [optional] [readonly] 
**total_files** | **int, none_type** |  | [optional] [readonly] 
**size** | **int** |  | [optional] [readonly] 
**mtime** | **int** |  | [optional] [readonly] 
**present** | **bool** |  | [optional] [readonly] 
**needs_rescan** | **bool** |  | [optional] [readonly] 
**is_showroom** | **bool** |  | [optional] [readonly] 
**bundle_index** | **int** |  | [optional] [readonly] 
**modified** | **datetime** |  | [optional] [readonly] 
**parent** | **int** |  | [optional] [readonly] 
**bundle** | **int** |  | [optional] [readonly] 
**bookmarked_by** | **[int]** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#models) [[Back to API list]](../README.md#api-endpoints) [[Back to README]](../README.md)


