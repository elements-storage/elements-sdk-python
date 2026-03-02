# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**production** | [**ProductionMini**](ProductionMini.md) |  | 
**volume** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**sharing_nfs_permissions** | [**[NFSPermission]**](NFSPermission.md) |  | 
**current_share_name** | **str** |  | [readonly] 
**size_used** | **int, none_type** |  | [readonly] 
**size_total** | **int, none_type** |  | [readonly] 
**bookmarked** | **bool, none_type** |  | [readonly] 
**quota_size_hard** | **int** |  | 
**quota_size_soft** | **int** |  | 
**endpoints** | **[str]** | This is a legacy placeholder field for compatibility with previous SDK versions. It is always an empty array. | [readonly] 
**resolved_read_only** | **bool, none_type** |  | [readonly] 
**name** | **str** |  | 
**description** | **str, none_type** |  | 
**long_description** | **str** |  | 
**is_template** | **bool** |  | 
**active** | **bool** |  | 
**mac_protocol** | **str, none_type** |  | 
**win_protocol** | **str** |  | 
**win_drive** | **str, none_type** |  | 
**linux_protocol** | **str** |  | 
**linux_mountpoint** | **str, none_type** |  | 
**share_name** | **str, none_type** |  | 
**share_nfs** | **bool** |  | 
**share_afp** | **bool** |  | 
**sharing_hidden** | **bool** |  | 
**sharing_require_login** | **bool** |  | 
**sharing_read_only** | **bool** |  | 
**sharing_allow_execute** | **bool** |  | 
**enable_quota** | **bool** |  | 
**current_size** | **int, none_type** |  | 
**affinity** | **str, none_type** |  | 
**emulate_avid** | **bool** |  | 
**emulate_capture** | **bool** |  | 
**emulate_preopen** | **bool** |  | 
**emulate_alternate_data_streams** | **bool** |  | 
**emulate_recycle_bin** | **bool** |  | 
**smb_extra_config** | **str** |  | 
**afp_extra_config** | **str** |  | 
**recycle_bin_exclude** | **str, none_type** |  | 
**is_external** | **bool** |  | 
**external_mac_url** | **str, none_type** |  | 
**external_win_url** | **str, none_type** |  | 
**external_linux_url** | **str, none_type** |  | 
**allow_symlinks** | **bool** |  | 
**rw_permission_priority** | **bool** |  | 
**veto_dot_underscore** | **bool** |  | 
**is_offloaded** | **bool** |  | [readonly] 
**template** | **int, none_type** |  | 
**offload_volume** | [**VolumeMini**](VolumeMini.md) |  | [optional] 
**volume_path** | **str, none_type** |  | [optional] [readonly] 
**path** | **str, none_type** |  | [optional] [readonly] 
**full_path** | **str, none_type** |  | [optional] [readonly] 
**quota** | [**Quota**](Quota.md) |  | [optional] 
**resolved_permissions** | [**[WorkspaceResolvedPermission], none_type**](WorkspaceResolvedPermission.md) |  | [optional] [readonly] 
**transfer_status** | [**WorkspaceTransferStatus**](WorkspaceTransferStatus.md) |  | [optional] 
**directory** | **str, none_type** |  | [optional] [readonly] 
**last_login** | **datetime, none_type** |  | [optional] [readonly] 
**offload_volume_path** | **str, none_type** |  | [optional] [readonly] 
**last_offload_sync_date** | **datetime, none_type** |  | [optional] [readonly] 
**home_for** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


