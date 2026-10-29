# BaseTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_limit** | **int, none_type** | Maximum transfer rate in bytes per second. Null means no limit. | 
**enqueue_at_front** | **bool** | When true, place the task at the front of its queue so it runs before other already-queued tasks instead of at the back. | 
**force_sync** | **bool** | When true, bypass the safety check that aborts the sync when an unexpectedly large fraction of files at the destination would be deleted | 
**priority** | **str** | Scheduling priority of the transfer task relative to other tasks in the queue. | [optional]  if omitted the server will use the default value of "interactive"

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


