# OneTimeAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**activity** | [**[OneTimeAccessTokenActivity]**](OneTimeAccessTokenActivity.md) |  | [readonly] 
**user** | [**ElementsUserMiniReference**](ElementsUserMiniReference.md) |  | 
**shared_bundles** | [**[OneTimeAccessTokenSharedObject]**](OneTimeAccessTokenSharedObject.md) |  | [readonly] 
**shared_directories** | [**[OneTimeAccessTokenSharedObject]**](OneTimeAccessTokenSharedObject.md) |  | [readonly] 
**full_url** | **str** |  | [readonly] 
**has_password** | **bool** |  | [readonly] 
**url** | **str** |  | 
**token** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**created_by** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**media_root_permissions** | **str, none_type** |  | [optional] [readonly] 
**view_limit_enabled** | **bool** |  | [optional] 
**view_limit_left** | **int** |  | [optional] 
**expires** | **datetime, none_type** |  | [optional] 
**require_login** | **bool** |  | [optional] 
**is_easy_sharing_for_bundle** | **int, none_type** |  | [optional] [readonly] 
**is_easy_sharing_for_directory** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


