# MediaRootDetailPartialUpdate

A Media Library root — a named, permissioned part of the filesystem that is exposed in the Media Library. Carries Media Library related settings that are scoped to this path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**[CustomFieldReference]**](CustomFieldReference.md) |  | [optional] 
**volume** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**workflow** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**jobs** | [**[JobReference]**](JobReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** | Path relative to the volume root. Empty string means the volume root itself. | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] 
**needs_rescan** | **bool** | Deprecated | [optional] 
**view_mode** | **str** | Folder display mode in the browser UI (normal or flat). | [optional] 
**view_style** | **str** | Default layout style in the browser UI (gallery, list or compact). | [optional] 
**view_default_tab** | **str** | Default tab shown in the asset detail panel. | [optional] 
**show_tags** | **bool** |  | [optional] 
**show_comments** | **bool** |  | [optional] 
**show_locations** | **bool** |  | [optional] 
**show_custom_fields** | **bool** |  | [optional] 
**show_ratings** | **bool** |  | [optional] 
**show_subclips** | **bool** |  | [optional] 
**show_subtitles** | **bool** |  | [optional] 
**show_markers** | **bool** |  | [optional] 
**show_history** | **bool** |  | [optional] 
**show_ai_metadata** | **bool** |  | [optional] 
**prefetch_thumbnail_strips** | **bool** | Pre-generate thumbnail strip proxies for faster in-browser timeline scrubbing. | [optional] 
**name_field** | **str, none_type** | Custom metadata field whose value is shown as the file name in the UI. If unset, the actual filename is used. | [optional] 
**share_comments** | **bool** | Whether new comments should automatically be visible across Media Roots | [optional] 
**share_link_duration** | **int** |  | [optional] 
**disable_framestacks** | **bool** | Disable detection of framestacks in this Media Root. Useful if it is known that this root will contain sequential still images. | [optional] 
**default_proxy_profile** | **int, none_type** |  | [optional] 
**cloud_proxy_profile** | **int, none_type** |  | [optional] 
**proxy_profiles** | **[int]** |  | [optional] 
**tags** | **[int]** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


