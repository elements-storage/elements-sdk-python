# SharingPermissionPresetPartialUpdate

A reusable preset of Media Library sharing permissions that can be applied when creating share links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_read** | **bool** |  | [optional] 
**allow_create** | **bool** |  | [optional] 
**allow_write_fs** | **bool** | Allow operations that would write to the filesystem | [optional] 
**allow_write_db** | **bool** | Allow operations that would write to the database, e.g. editing asset metadata (tags, custom fields, ratings, comments). | [optional] 
**allow_proxy_download** | **bool** | Allow downloading low-resolution proxy files. | [optional] 
**allow_original_download** | **bool** | Allow downloading original full-resolution source files. | [optional] 
**allow_upload** | **bool** |  | [optional] 
**allow_sharing** | **bool** |  | [optional] 
**allow_delete_fs** | **bool** | Allow deleting files from the filesystem. | [optional] 
**allow_delete_db** | **bool** | Allow removing asset records and metadata from the database. | [optional] 
**show_tags** | **bool** |  | [optional] 
**show_comments** | **bool** |  | [optional] 
**show_locations** | **bool** |  | [optional] 
**show_custom_fields** | **bool** |  | [optional] 
**show_ratings** | **bool** |  | [optional] 
**show_subclips** | **bool** |  | [optional] 
**show_subtitles** | **bool** |  | [optional] 
**show_ai_metadata** | **bool** |  | [optional] 
**show_markers** | **bool** |  | [optional] 
**show_history** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**default** | **bool** | When true, this preset is pre-selected when creating a new link. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


