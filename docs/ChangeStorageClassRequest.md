# ChangeStorageClassRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_class** | **str** | The cloud storage class to move the data to (provider-specific). | 
**force_restore** | **bool** | When true, first restore any objects currently in cold storage so the storage class change can proceed. | [optional]  if omitted the server will use the default value of False
**restore_tier** | **str, none_type** | Retrieval tier to use if a restore is needed (provider-specific, e.g. expedited, standard or bulk). | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


