# MediaFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**volume** | [**VolumeMini**](VolumeMini.md) |  | 
**effective_custom_fields** | **{str: (str, none_type)}** |  | [readonly] 
**full_path** | **str** |  | [readonly] 
**is_shared** | **bool, none_type** |  | [readonly] 
**is_excluded** | **bool** |  | [readonly] 
**is_hardlink** | **bool** |  | [readonly] 
**is_bookmarked** | **bool, none_type** |  | [readonly] 
**child_count** | **int, none_type** |  | [readonly] 
**name** | **str** |  | [readonly] 
**path** | **str** |  | [readonly] 
**pathhash** | **str** |  | [readonly] 
**ancestry** | **str** |  | [readonly] 
**is_dir** | **bool** |  | [readonly] 
**size** | **int** |  | [readonly] 
**mtime** | **int** |  | [readonly] 
**present** | **bool** |  | [readonly] 
**is_showroom** | **bool** |  | [readonly] 
**bundle_index** | **int** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**parent** | **int** |  | [readonly] 
**bundle** | **int** |  | [readonly] 
**info** | **{str: (str, none_type)}** |  | [optional] 
**custom_fields** | **{str: (str, none_type)}** |  | [optional] 
**resolved_permission** | [**MediaRootPermission**](MediaRootPermission.md) |  | [optional] 
**parent_file** | **{str: (str, none_type)}** |  | [optional] [readonly] 
**root** | [**MediaRootMini**](MediaRootMini.md) |  | [optional] 
**modified_by** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**total_files** | **int, none_type** |  | [optional] 
**needs_rescan** | **bool** |  | [optional] 
**bookmarked_by** | **[int]** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


