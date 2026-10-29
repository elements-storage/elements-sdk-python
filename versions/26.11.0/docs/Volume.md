# Volume

Volumes are the main storage locations for user content on ELEMENTS. Each volume is a mounted filesystem, clustered or not, that is made available to the clients via workspaces and shares. Volumes can be on-premise native, on-premise third-party (with a license) or cloud (with a license). Only cloud volumes may be added directly without ELEMENTS support involvement as other types require additional configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**path** | **str** | The exact server-side mountpoint path or cloud storage URI for this volume | 
**nodes** | **[int]** | Storage nodes that this volume is \&quot;native\&quot; to. These nodes will be selected for NAS connection requests | 
**display_name** | **str** |  | 
**visual_tag** | **str, none_type** | A visual label shown for this volume in the UI | 
**is_default** | **bool** | Pre-selects this volume in the UI selectors | 
**use_for_homes** | **bool** | Whether this volume can be used for user home workspace | 
**use_for_workspaces** | **bool** | Whether this volume can be used for workspaces in general | 
**type** | **str** |  | 
**snm_enabled** | **bool** |  | 
**snfs_name** | **str, none_type** |  | 
**backend** | [**Backend**](Backend.md) |  | 
**cloud_account** | **int, none_type** | For cloud volumes, the CloudAccount object containing credentials for this volume. | 
**qumulo_integration** | **int, none_type** | The Qumulo integration associated with this volume if it is a Qumulo volume. Required for Qumulo volumes and must be empty for non-Qumulo volumes. | 
**onefs_integration** | **int, none_type** | The OneFS integration associated with this volume if it is a OneFS volume. Required for OneFS volumes and must be empty for non-OneFS volumes. | 
**fs_properties** | [**FSProperties**](FSProperties.md) |  | [optional] 
**status** | [**VolumeStatus**](VolumeStatus.md) |  | [optional] 
**nfsv4_export** | **str, none_type** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty string. | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


