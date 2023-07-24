# MediaRootDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**volume** | [**VolumeReference**](VolumeReference.md) |  | 
**full_path** | **str** |  | [readonly] 
**workflow_jobs** | [**[Job]**](Job.md) |  | [readonly] 
**name** | **str** |  | 
**custom_fields** | [**[CustomFieldReference]**](CustomFieldReference.md) |  | [optional] 
**workflow** | **{str: (str, none_type)}, none_type** |  | [optional] 
**resolved_permissions** | [**[MediaRootPermission]**](MediaRootPermission.md) |  | [optional] [readonly] 
**jobs** | [**[JobReference]**](JobReference.md) |  | [optional] 
**ai_config** | **{str: (str, none_type)}, none_type** |  | [optional] 
**path** | **str** |  | [optional] 
**needs_rescan** | **bool** |  | [optional] 
**view_mode** | **str** |  | [optional] 
**view_style** | **str** |  | [optional] 
**view_default_tab** | **str** |  | [optional] 
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
**prefetch_thumbnail_strips** | **bool** |  | [optional] 
**cover** | **str, none_type** |  | [optional] 
**name_field** | **str, none_type** |  | [optional] 
**share_comments** | **bool** |  | [optional] 
**share_link_duration** | **int** |  | [optional] 
**default_proxy_profile** | **int, none_type** |  | [optional] 
**cloud_proxy_profile** | **int, none_type** |  | [optional] 
**ai_connection** | **int, none_type** |  | [optional] 
**ai_proxy_profile** | **int, none_type** |  | [optional] 
**proxy_profiles** | **[int]** |  | [optional] 
**tags** | **[int]** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


