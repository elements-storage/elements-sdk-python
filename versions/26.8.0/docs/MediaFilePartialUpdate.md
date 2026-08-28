# MediaFilePartialUpdate

Represents a file or folder on the filesystem that has been seen by the Media Library scanner. Files that are part of a media object are grouped in a MediaFileBundle (whether one file or multiple) and after a bundle is scanned, an Asset is created and assigned to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**custom_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**total_files** | **int, none_type** | Legacy (unused) | [optional] 
**needs_rescan** | **bool** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


