# StorageRestoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**media_file** | [**MediaFileMini**](MediaFileMini.md) |  | 
**user** | [**ElementsUserMini**](ElementsUserMini.md) |  | 
**cloud_account** | [**CloudAccountMini**](CloudAccountMini.md) |  | 
**items_total** | **int** |  | [readonly] 
**items_processed** | **int** |  | [readonly] 
**created** | **datetime** |  | [readonly] 
**last_polled** | **datetime, none_type** |  | 
**restore_tier** | **str** |  | 
**restore_type** | **str** |  | 
**target_path** | **str, none_type** |  | 
**target_storage_class** | **str, none_type** | Copy to same location with this storage class when restore completes | 
**status** | **str** |  | 
**task_id** | **str, none_type** |  | [optional] [readonly] 
**root** | [**MediaRootMini**](MediaRootMini.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


