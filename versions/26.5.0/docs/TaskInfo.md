# TaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | [readonly] 
**kwargs** | **{str: (str, none_type)}** |  | [readonly] 
**outputs** | **{str: (str, none_type)}** |  | [readonly] 
**subtask** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**worker** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**user** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**workstation** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**is_running** | **bool** | True when the task is in one of the following states: RUNNING (1), ABORTING (3). | [readonly] 
**is_finished** | **bool** | True when the task is in one of the following states: FINISHED (2), ABORTED (4), FAILED (5), WARNINGS (6), NOOP (7). | [readonly] 
**name** | **str, none_type** |  | 
**task_name** | **str, none_type** |  | 
**is_private** | **bool** |  | 
**worker_name** | **str, none_type** |  | 
**queue** | **str, none_type** |  | 
**state** | **int** |  | 
**state_text** | **str, none_type** |  | 
**job_instance** | **str, none_type** |  | 
**started** | **datetime** |  | [readonly] 
**exception** | **str, none_type** |  | 
**traceback** | **str, none_type** |  | 
**related_bundle_id** | **int, none_type** |  | 
**related_proxy_id** | **int, none_type** |  | 
**schedule** | **int, none_type** |  | 
**finished** | **datetime, none_type** |  | [optional] [readonly] 
**progress** | **{str: (str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


