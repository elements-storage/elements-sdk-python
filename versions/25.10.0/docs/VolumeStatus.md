# VolumeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online** | **bool, none_type** |  | 
**size_total** | **str, none_type** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty string. | [optional] [readonly] 
**size_used** | **str, none_type** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty string. | [optional] [readonly] 
**size_free** | **str, none_type** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty string. | [optional] [readonly] 
**usage** | [**VolumeUsage**](VolumeUsage.md) |  | [optional] 
**snfs** | [**VolumeSNFSStatus**](VolumeSNFSStatus.md) |  | [optional] 
**beegfs** | [**VolumeBeeGFSStatus**](VolumeBeeGFSStatus.md) |  | [optional] 
**ceph** | [**VolumeCephStatus**](VolumeCephStatus.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


