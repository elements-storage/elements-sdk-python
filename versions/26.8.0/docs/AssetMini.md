# AssetMini

Each Asset is a unique instance of media content. Assets are either singular files or groups of files comprising a single media object (for example separate video and audio files or a framestack). The relation between Asset and its individual files is through the MediaFileBundle model. Assets are checksummed and multiple copies of the same media will refer to the same Asset. Asset carries the media metadata and all user-created objects such as comments or markers will link back to the Asset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**sync_id** | **str** |  | [readonly] 
**display_name** | **str** |  | [readonly] 
**format** | [**FormatMetadata**](FormatMetadata.md) |  | 
**thumbnail_generated** | **bool** |  | [readonly] 
**proxies_failed** | **bool** |  | [readonly] 
**default_proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**type** | **str, none_type** |  | [optional] [readonly] 
**proxies** | [**[Proxy]**](Proxy.md) |  | [optional] [readonly] 
**matched_scanner** | **str, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


