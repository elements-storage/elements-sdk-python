# OneTimeAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**activity** | [**[OneTimeAccessTokenActivity]**](OneTimeAccessTokenActivity.md) |  | [readonly] 
**user** | [**ElementsUserMiniReference**](ElementsUserMiniReference.md) |  | 
**created_by** | [**ElementsUserMini**](ElementsUserMini.md) |  | 
**shared_bundles** | [**[OneTimeAccessTokenSharedObject]**](OneTimeAccessTokenSharedObject.md) |  | [readonly] 
**shared_directories** | [**[OneTimeAccessTokenSharedObject]**](OneTimeAccessTokenSharedObject.md) |  | [readonly] 
**full_url** | **str** |  | [readonly] 
**url** | **str** |  | 
**token** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**is_easy_sharing_for_bundle** | **int** |  | [readonly] 
**is_easy_sharing_for_directory** | **int** |  | [readonly] 
**media_root_permissions** | **str, none_type** |  | [optional] [readonly] 
**view_limit_enabled** | **bool** |  | [optional] 
**view_limit_left** | **int** |  | [optional] 
**expires** | **datetime, none_type** |  | [optional] 
**require_login** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#models) [[Back to API list]](../README.md#api-endpoints) [[Back to README]](../README.md)


