# MediaRootMiniReference

A Media Library root — a named, permissioned part of the filesystem that is exposed in the Media Library. Carries Media Library related settings that are scoped to this path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**volume** | [**VolumeMini**](VolumeMini.md) |  | 
**name** | **str** |  | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] [readonly] 
**full_path** | **str** | Absolute filesystem path (volume mount point joined with the root path). | [optional] [readonly] 
**path** | **str** | Path relative to the volume root. Empty string means the volume root itself. | [optional] 
**prefetch_thumbnail_strips** | **bool** | Pre-generate thumbnail strip proxies for faster in-browser timeline scrubbing. | [optional] [readonly] 
**view_mode** | **str** | Folder display mode in the browser UI (normal or flat). | [optional] [readonly] 
**cover** | **str, none_type** | URL to retrieve the cover image, or null if no cover has been set. | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


