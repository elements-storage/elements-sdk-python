# MediaRootDetail

A Media Library root — a named, permissioned part of the filesystem that is exposed in the Media Library. Carries Media Library related settings that are scoped to this path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**custom_fields** | [**[CustomField]**](CustomField.md) |  | 
**volume** | [**Volume**](Volume.md) |  | 
**full_path** | **str** | Absolute filesystem path (volume mount point joined with the root path). | [readonly] 
**workflow** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**cover** | **str, none_type** | URL to retrieve the cover image, or null if no cover has been set. | [readonly] 
**jobs** | [**[Job]**](Job.md) |  | 
**name** | **str** |  | 
**path** | **str** | Path relative to the volume root. Empty string means the volume root itself. | 
**description** | **str, none_type** |  | 
**needs_rescan** | **bool** | Deprecated | 
**view_mode** | **str** | Folder display mode in the browser UI (normal or flat). | 
**view_style** | **str** | Default layout style in the browser UI (gallery, list or compact). | 
**view_default_tab** | **str** | Default tab shown in the asset detail panel. | 
**show_tags** | **bool** |  | 
**show_comments** | **bool** |  | 
**show_locations** | **bool** |  | 
**show_custom_fields** | **bool** |  | 
**show_ratings** | **bool** |  | 
**show_subclips** | **bool** |  | 
**show_subtitles** | **bool** |  | 
**show_markers** | **bool** |  | 
**show_history** | **bool** |  | 
**show_ai_metadata** | **bool** |  | 
**prefetch_thumbnail_strips** | **bool** | Pre-generate thumbnail strip proxies for faster in-browser timeline scrubbing. | 
**name_field** | **str, none_type** | Custom metadata field whose value is shown as the file name in the UI. If unset, the actual filename is used. | 
**share_comments** | **bool** | Whether new comments should automatically be visible across Media Roots | 
**share_link_duration** | **int** |  | 
**disable_framestacks** | **bool** | Disable detection of framestacks in this Media Root. Useful if it is known that this root will contain sequential still images. | 
**default_proxy_profile** | **int, none_type** |  | 
**cloud_proxy_profile** | **int, none_type** |  | 
**proxy_profiles** | **[int]** |  | 
**tags** | **[int]** |  | 
**resolved_permissions** | [**[MediaRootPermission]**](MediaRootPermission.md) | Effective permissions for the requesting user; present only when &#x60;resolve_permissions&#x60; is set. | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


