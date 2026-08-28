# ElementsUserProfile

The current user's own profile: their editable preferences (display name, language, default page, file-manager bookmarks) plus read-only account info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str, none_type** |  | [readonly] 
**default_page** | **str** |  | 
**full_name** | **str, none_type** |  | 
**language** | **str, none_type** |  | 
**fm_bookmarks** | **[str]** |  | 
**id** | **int** |  | 
**username** | **str** |  | [readonly] 
**display_name** | **str** |  | [readonly] 
**effective_permissions** | **[str]** |  | [readonly] 
**has_password** | **bool** |  | [readonly] 
**allow_changing_password** | **bool** |  | [readonly] 
**allowed_fs_paths** | **[str], none_type** |  | [readonly] 
**allowed_fs_write_paths** | **[str], none_type** |  | [readonly] 
**is_cloud** | **bool** |  | [readonly] 
**is_external** | **bool** |  | [readonly] 
**totp_enabled** | **bool** |  | [readonly] 
**unix_username** | **str, none_type** |  | [optional] [readonly] 
**email** | **str, none_type** |  | [optional] [readonly] 
**ldap** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**shaper_rate** | **int, none_type** |  | [optional] [readonly] 
**shaper_ceiling** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


