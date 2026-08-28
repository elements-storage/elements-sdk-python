# TasksSummary

Task status summary; present only for internal users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**running** | [**[TaskInfo]**](TaskInfo.md) | List of all currently running tasks (RUNNING (1), ABORTING (3)). | 
**recent_finished** | [**[TaskInfo]**](TaskInfo.md) | The latest five tasks that have finished (FINISHED (2), ABORTED (4), FAILED (5), WARNINGS (6), NOOP (7)) in the past hour. | 
**pending_count** | **int** | The number of tasks currently in the queue (PENDING (0), awaiting execution. | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


