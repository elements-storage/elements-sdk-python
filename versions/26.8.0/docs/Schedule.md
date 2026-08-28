# Schedule

A schedule that runs an Automation job automatically, either at a fixed interval or on a crontab expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**variables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**next_run** | **datetime** |  | [readonly] 
**type** | **int** | Scheduling mode: fixed interval (&#x60;1&#x60;, uses &#x60;every&#x60;/&#x60;period&#x60;) or a crontab expression (&#x60;2&#x60;, uses the &#x60;crontab_*&#x60; fields). | 
**enabled** | **bool** |  | 
**last_run** | **datetime, none_type** |  | 
**every** | **int** |  | 
**period** | **str** |  | 
**crontab_day_of_month** | **str** |  | 
**crontab_day_of_week** | **str** |  | 
**crontab_hour** | **str** |  | 
**crontab_minute** | **str** |  | 
**crontab_month_of_year** | **str** |  | 
**job** | **int** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


