# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**info** | **{str: (str, none_type)}** |  | [readonly] 
**proxy_info** | **{str: (str, none_type)}** |  | [readonly] 
**custom_fields** | **{str: (str, none_type)}** |  | 
**tags** | **[int]** |  | 
**backups** | **str** |  | [readonly] 
**proxies_generated** | **bool** |  | [readonly] 
**proxies_failed** | **bool** |  | [readonly] 
**bundles** | [**[MediaFileBundleMini]**](MediaFileBundleMini.md) |  | [readonly] 
**format** | [**FormatMetadata**](FormatMetadata.md) |  | 
**sync_id** | **str** |  | [readonly] 
**display_name** | **str** |  | [readonly] 
**has_files** | **bool** |  | [readonly] 
**has_backups** | **bool** |  | [readonly] 
**has_cloud_links** | **bool** |  | [readonly] 
**checksum** | **str** |  | [readonly] 
**type** | **str** |  | [readonly] 
**thumbnail_generated** | **bool** |  | [readonly] 
**matched_scanner** | **str** |  | [readonly] 
**workflow_state** | **int** |  | [readonly] 
**is_temporary** | **bool** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**proxies** | [**[Proxy]**](Proxy.md) |  | [optional] [readonly] 
**default_proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**resolved_permission** | [**MediaRootPermission**](MediaRootPermission.md) |  | [optional] 
**modified_by** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**rating** | **int, none_type** |  | [optional] [readonly] 
**set** | **int, none_type** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


