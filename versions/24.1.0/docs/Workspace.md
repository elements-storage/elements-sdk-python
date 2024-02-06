# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**production** | [**ProductionMiniReference**](ProductionMiniReference.md) |  | 
**current_share_name** | **str** |  | [readonly] 
**size_used** | **int, none_type** |  | [readonly] 
**size_total** | **int, none_type** |  | [readonly] 
**bookmarked** | **bool, none_type** |  | [readonly] 
**resolved_read_only** | **bool, none_type** |  | [readonly] 
**volume** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**volume_path** | **str, none_type** |  | [optional] [readonly] 
**path** | **str, none_type** |  | [optional] [readonly] 
**sharing_nfs_permissions** | [**[NFSPermission]**](NFSPermission.md) |  | [optional] 
**full_path** | **str, none_type** |  | [optional] [readonly] 
**endpoints** | [**[WorkspaceEndpoint], none_type**](WorkspaceEndpoint.md) |  | [optional] [readonly] 
**quota** | [**Quota**](Quota.md) |  | [optional] 
**quota_size_hard** | **int** |  | [optional] 
**quota_size_soft** | **int** |  | [optional] 
**resolved_permissions** | [**[WorkspaceResolvedPermission], none_type**](WorkspaceResolvedPermission.md) |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**directory** | **str, none_type** |  | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] 
**long_description** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**last_login** | **datetime, none_type** |  | [optional] [readonly] 
**active** | **bool** |  | [optional] 
**mac_protocol** | **str** |  | [optional] 
**win_protocol** | **str** |  | [optional] 
**win_drive** | **str, none_type** |  | [optional] 
**linux_protocol** | **str** |  | [optional] 
**linux_mountpoint** | **str, none_type** |  | [optional] 
**share_name** | **str, none_type** |  | [optional] 
**share_nfs** | **bool** |  | [optional] 
**share_afp** | **bool** |  | [optional] 
**sharing_hidden** | **bool** |  | [optional] 
**sharing_require_login** | **bool** |  | [optional] 
**sharing_read_only** | **bool** |  | [optional] 
**sharing_allow_execute** | **bool** |  | [optional] 
**enable_quota** | **bool** |  | [optional] 
**affinity** | **str, none_type** |  | [optional] 
**emulate_avid** | **bool** |  | [optional] 
**emulate_capture** | **bool** |  | [optional] 
**emulate_preopen** | **bool** |  | [optional] 
**emulate_ntfs_streams** | **bool** |  | [optional] 
**emulate_recycle_bin** | **bool** |  | [optional] 
**emulate_fruit** | **bool** |  | [optional] 
**smb_extra_config** | **str** |  | [optional] 
**afp_extra_config** | **str** |  | [optional] 
**recycle_bin_exclude** | **str, none_type** |  | [optional] 
**is_external** | **bool** |  | [optional] 
**external_mac_url** | **str, none_type** |  | [optional] 
**external_win_url** | **str, none_type** |  | [optional] 
**external_linux_url** | **str, none_type** |  | [optional] 
**allow_symlinks** | **bool** |  | [optional] 
**rw_permission_priority** | **bool** |  | [optional] 
**template** | **int, none_type** |  | [optional] 
**home_for** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


