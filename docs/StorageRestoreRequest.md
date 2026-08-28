# StorageRestoreRequest

A request to bring files back from cold cloud storage to readily-accessible storage, tracking the restore status of the files under the selected folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**media_file** | [**MediaFileMini**](MediaFileMini.md) |  | 
**user** | [**ElementsUserMini**](ElementsUserMini.md) |  | 
**cloud_account** | [**CloudAccountMini**](CloudAccountMini.md) |  | 
**items_total** | **int** |  | [readonly] 
**items_processed** | **int** |  | [readonly] 
**created** | **datetime** | When the request was created. | [readonly] 
**last_polled** | **datetime, none_type** | When the restore status was last checked with the storage provider. | 
**restore_tier** | **str** | Provider-specific retrieval tier requested for the restore (e.g. expedited, standard or bulk), trading off speed against cost. | 
**restore_type** | **str** | Whether the data is temporarily made available in place (&#x60;MAKE_AVAILABLE&#x60;) or copied to a target path (&#x60;RESTORE_TO_PATH&#x60;). | 
**target_path** | **str, none_type** | Destination path for the restored copy when restore_type is &#x60;RESTORE_TO_PATH&#x60;. | 
**target_storage_class** | **str, none_type** | Copy to same location with this storage class when restore completes | 
**status** | **str** | Overall status of the restore: &#x60;RUNNING&#x60; (in progress), &#x60;READY&#x60; (restored and available) or &#x60;FAILED&#x60;. | 
**task_id** | **str, none_type** |  | [optional] [readonly] 
**root** | [**MediaRootMini**](MediaRootMini.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


