# VolumeReference

Volumes are the main storage locations for user content on ELEMENTS. Each volume is a mounted filesystem, clustered or not, that is made available to the clients via workspaces and shares. Volumes can be on-premise native, on-premise third-party (with a license) or cloud (with a license). Only cloud volumes may be added directly without ELEMENTS support involvement as other types require additional configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**path** | **str** | The exact server-side mountpoint path or cloud storage URI for this volume | [optional] [readonly] 
**nodes** | **[int]** | Storage nodes that this volume is \&quot;native\&quot; to. These nodes will be selected for NAS connection requests | [optional] [readonly] 
**display_name** | **str** |  | [optional] [readonly] 
**visual_tag** | **str, none_type** | A visual label shown for this volume in the UI | [optional] [readonly] 
**is_default** | **bool** | Pre-selects this volume in the UI selectors | [optional] [readonly] 
**use_for_homes** | **bool** | Whether this volume can be used for user home workspace | [optional] [readonly] 
**use_for_workspaces** | **bool** | Whether this volume can be used for workspaces in general | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**snm_enabled** | **bool** |  | [optional] [readonly] 
**snfs_name** | **str, none_type** |  | [optional] [readonly] 
**fs_properties** | [**FSProperties**](FSProperties.md) |  | [optional] 
**backend** | [**Backend**](Backend.md) |  | [optional] 
**status** | [**VolumeStatus**](VolumeStatus.md) |  | [optional] 
**cloud_account** | **int, none_type** | For cloud volumes, the CloudAccount object containing credentials for this volume. | [optional] [readonly] 
**qumulo_integration** | **int, none_type** | The Qumulo integration associated with this volume if it is a Qumulo volume. Required for Qumulo volumes and must be empty for non-Qumulo volumes. | [optional] [readonly] 
**nfsv4_export** | **str, none_type** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty string. | [optional] [readonly] 
**onefs_integration** | **int, none_type** | The OneFS integration associated with this volume if it is a OneFS volume. Required for OneFS volumes and must be empty for non-OneFS volumes. | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


