# MediaRootPermission

A permission record granting a user or group access to a media root or one of its subdirectories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**group** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**full_path** | **str** | Absolute filesystem path this permission covers (root full path joined with the permission path). | [readonly] 
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
**path** | **str** | Subdirectory within the root to which this permission is scoped. Empty string grants access to the entire root. | 
**root** | **int** |  | 
**is_temporary_for_token** | **int, none_type** | If set, this permission was created for a sharing link and is removed when the link is deleted. | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


