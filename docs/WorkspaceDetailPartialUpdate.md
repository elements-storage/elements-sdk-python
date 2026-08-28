# WorkspaceDetailPartialUpdate

A workspace is a logical unit and a filesystem location that holds user content. Each workspace gets automatically shared via NAS and is accessible from the ELEMENTS Client by the users that have access to it via permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**production** | [**ProductionReference**](ProductionReference.md) |  | [optional] 
**volume** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**sharing_nfs_permissions** | [**[NFSPermission]**](NFSPermission.md) |  | [optional] 
**quota_size_hard** | **int** | Hard quota limit (absolute cap for the workspace) | [optional] 
**quota_size_soft** | **int** | Soft quota limit (warning threshold) | [optional] 
**name** | **str** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**long_description** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**mac_protocol** | **str, none_type** |  | [optional] 
**win_protocol** | **str** | Defines how the workspace is mounted by the ELEMENTS Client - mapped as a disk or opened as a UNC path | [optional] 
**win_drive** | **str, none_type** | Drive letter for the ELEMENTS Client to use | [optional] 
**linux_protocol** | **str** |  | [optional] 
**linux_mountpoint** | **str, none_type** | Mountpoint for the ELEMENTS Client to use | [optional] 
**share_name** | **str, none_type** |  | [optional] 
**share_nfs** | **bool** |  | [optional] 
**share_afp** | **bool** |  | [optional] 
**sharing_hidden** | **bool** | When enabled, the share will be hidden in network browsing (e.g. SMB or AFP browse lists) | [optional] 
**sharing_require_login** | **bool** | Require authentication over SMB and AFP | [optional] 
**sharing_read_only** | **bool** |  | [optional] 
**sharing_allow_execute** | **bool** |  | [optional] 
**enable_quota** | **bool** |  | [optional] 
**current_size** | **int, none_type** | Total cached size of the workspace, if tracked by the quota system | [optional] 
**affinity** | **str, none_type** | StorNext affinity tag | [optional] 
**emulate_avid** | **bool** | Emulate Avid NEXIS storage to enable bin locking in Avid Media Composer | [optional] 
**emulate_capture** | **bool** | Set up the SMB share for ingest, disables opportunistic locks for growing file editing | [optional] 
**emulate_preopen** | **bool** | Unused (legacy) | [optional] 
**emulate_alternate_data_streams** | **bool** | Enable alternate streams and extended attributes over SMB | [optional] 
**emulate_recycle_bin** | **bool** |  | [optional] 
**smb_extra_config** | **str** | Additional raw SMB configuration to add to the share definition in smb.conf | [optional] 
**afp_extra_config** | **str** | Additional raw AFP configuration to add to the share definition in afp.conf | [optional] 
**recycle_bin_exclude** | **str, none_type** | Exclude list for Samba vfs_recycle | [optional] 
**is_external** | **bool** |  | [optional] 
**external_mac_url** | **str, none_type** |  | [optional] 
**external_win_url** | **str, none_type** |  | [optional] 
**external_linux_url** | **str, none_type** |  | [optional] 
**allow_symlinks** | **bool** |  | [optional] 
**rw_permission_priority** | **bool** | When enabled, if a user has both read-only and read-write permissions, the read-write permissions will take precedence. When disabled, the read-only permissions will take precedence. | [optional] 
**veto_dot_underscore** | **bool** | Block AppleDouble files - Prevents macOS from storing ._* and .DS_Store files in the workspace over SMB | [optional] 
**template** | **int, none_type** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


