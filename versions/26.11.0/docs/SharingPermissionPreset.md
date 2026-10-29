# SharingPermissionPreset

A reusable preset of Media Library sharing permissions that can be applied when creating share links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**allow_read** | **bool** |  | 
**allow_create** | **bool** |  | 
**allow_write_fs** | **bool** | Allow operations that would write to the filesystem | 
**allow_write_db** | **bool** | Allow operations that would write to the database, e.g. editing asset metadata (tags, custom fields, ratings, comments). | 
**allow_proxy_download** | **bool** | Allow downloading low-resolution proxy files. | 
**allow_original_download** | **bool** | Allow downloading original full-resolution source files. | 
**allow_upload** | **bool** |  | 
**allow_sharing** | **bool** |  | 
**allow_delete_fs** | **bool** | Allow deleting files from the filesystem. | 
**allow_delete_db** | **bool** | Allow removing asset records and metadata from the database. | 
**show_tags** | **bool** |  | 
**show_comments** | **bool** |  | 
**show_locations** | **bool** |  | 
**show_custom_fields** | **bool** |  | 
**show_ratings** | **bool** |  | 
**show_subclips** | **bool** |  | 
**show_subtitles** | **bool** |  | 
**show_ai_metadata** | **bool** |  | 
**show_markers** | **bool** |  | 
**show_history** | **bool** |  | 
**name** | **str** |  | 
**default** | **bool** | When true, this preset is pre-selected when creating a new link. | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


