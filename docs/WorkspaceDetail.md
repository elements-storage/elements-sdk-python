# WorkspaceDetail

A workspace is a logical unit and a filesystem location that holds user content. Each workspace gets automatically shared via NAS and is accessible from the ELEMENTS Client by the users that have access to it via permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**production** | [**Production**](Production.md) |  | 
**volume** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**sharing_nfs_permissions** | [**[NFSPermission]**](NFSPermission.md) |  | 
**current_share_name** | **str** |  | [readonly] 
**size_used** | **int, none_type** | Deprecated, do not use | [readonly] 
**size_total** | **int, none_type** | Deprecated, do not use | [readonly] 
**bookmarked** | **bool, none_type** |  | [readonly] 
**quota_size_hard** | **int** | Hard quota limit (absolute cap for the workspace) | 
**quota_size_soft** | **int** | Soft quota limit (warning threshold) | 
**resolved_read_only** | **bool, none_type** |  | [readonly] 
**recycle_bin_path** | **str, none_type** |  | [readonly] 
**name** | **str** |  | 
**description** | **str, none_type** |  | 
**long_description** | **str** |  | 
**is_template** | **bool** |  | 
**active** | **bool** |  | 
**mac_protocol** | **str, none_type** |  | 
**win_protocol** | **str** | Defines how the workspace is mounted by the ELEMENTS Client - mapped as a disk or opened as a UNC path | 
**win_drive** | **str, none_type** | Drive letter for the ELEMENTS Client to use | 
**linux_protocol** | **str** |  | 
**linux_mountpoint** | **str, none_type** | Mountpoint for the ELEMENTS Client to use | 
**share_name** | **str, none_type** |  | 
**share_nfs** | **bool** |  | 
**share_afp** | **bool** |  | 
**sharing_hidden** | **bool** | When enabled, the share will be hidden in network browsing (e.g. SMB or AFP browse lists) | 
**sharing_require_login** | **bool** | Require authentication over SMB and AFP | 
**sharing_read_only** | **bool** |  | 
**sharing_allow_execute** | **bool** |  | 
**enable_quota** | **bool** |  | 
**current_size** | **int, none_type** | Total cached size of the workspace, if tracked by the quota system | 
**affinity** | **str, none_type** | StorNext affinity tag | 
**emulate_avid** | **bool** | Emulate Avid NEXIS storage to enable bin locking in Avid Media Composer | 
**emulate_capture** | **bool** | Set up the SMB share for ingest, disables opportunistic locks for growing file editing | 
**emulate_preopen** | **bool** | Unused (legacy) | 
**emulate_alternate_data_streams** | **bool** | Enable alternate streams and extended attributes over SMB | 
**emulate_recycle_bin** | **bool** |  | 
**smb_extra_config** | **str** | Additional raw SMB configuration to add to the share definition in smb.conf | 
**afp_extra_config** | **str** | Additional raw AFP configuration to add to the share definition in afp.conf | 
**recycle_bin_exclude** | **str, none_type** | Exclude list for Samba vfs_recycle | 
**is_external** | **bool** |  | 
**external_mac_url** | **str, none_type** |  | 
**external_win_url** | **str, none_type** |  | 
**external_linux_url** | **str, none_type** |  | 
**allow_symlinks** | **bool** |  | 
**rw_permission_priority** | **bool** | When enabled, if a user has both read-only and read-write permissions, the read-write permissions will take precedence. When disabled, the read-only permissions will take precedence. | 
**veto_dot_underscore** | **bool** | Block AppleDouble files - Prevents macOS from storing ._* and .DS_Store files in the workspace over SMB | 
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


