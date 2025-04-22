# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**proxy_info** | **{str: (str, none_type)}** |  | [readonly] 
**custom_fields** | **{str: (str, none_type)}** |  | 
**tags** | [**[Tag]**](Tag.md) |  | 
**backups** | [**[AssetBackupMini]**](AssetBackupMini.md) |  | [readonly] 
**proxies_generated** | **bool** |  | [readonly] 
**proxies_failed** | **bool** |  | [readonly] 
**bundles** | [**[MediaFileBundleMini]**](MediaFileBundleMini.md) |  | [readonly] 
**format** | [**FormatMetadata**](FormatMetadata.md) |  | 
**info** | **{str: (str, none_type)}** |  | [readonly] 
**sync_id** | **str** |  | [readonly] 
**display_name** | **str** |  | [readonly] 
**has_files** | **bool** |  | [readonly] 
**has_backups** | **bool** |  | [readonly] 
**has_cloud_links** | **bool** |  | [readonly] 
**thumbnail_generated** | **bool** |  | [readonly] 
**workflow_state** | **int** |  | 
**is_temporary** | **bool** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**timecode** | **float, none_type** |  | 
**set_stack_order** | **int** |  | 
**proxies** | [**[Proxy]**](Proxy.md) |  | [optional] [readonly] 
**default_proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**resolved_permission** | [**MediaRootPermission**](MediaRootPermission.md) |  | [optional] 
**modified_by** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**rating** | **float, none_type** |  | [optional] [readonly] 
**checksum** | **str, none_type** |  | [optional] [readonly] 
**type** | **str, none_type** |  | [optional] [readonly] 
**matched_scanner** | **str, none_type** |  | [optional] [readonly] 
**set_stack** | **int, none_type** |  | [optional] [readonly] 
**version_stack** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


