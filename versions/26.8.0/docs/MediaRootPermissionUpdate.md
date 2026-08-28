# MediaRootPermissionUpdate

A permission record granting a user or group access to a media root or one of its subdirectories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root** | **int** |  | 
**user** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**group** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
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
**path** | **str** | Subdirectory within the root to which this permission is scoped. Empty string grants access to the entire root. | [optional] 
**is_temporary_for_token** | **int, none_type** | If set, this permission was created for a sharing link and is removed when the link is deleted. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


