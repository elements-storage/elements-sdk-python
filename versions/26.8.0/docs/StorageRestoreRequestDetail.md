# StorageRestoreRequestDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restore_tier** | **str** | Provider-specific retrieval tier to use (e.g. expedited, standard or bulk), trading off speed against cost. | 
**restore_type** | **str** | Whether to temporarily make the data available in place (&#x60;MAKE_AVAILABLE&#x60;) or copy it to a target path (&#x60;RESTORE_TO_PATH&#x60;). | 
**target_path** | **str, none_type** | Destination path when restore_type is &#x60;RESTORE_TO_PATH&#x60;. | [optional] 
**days** | **int** | Number of days to keep the restored copy available before it expires. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


