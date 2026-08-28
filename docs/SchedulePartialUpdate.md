# SchedulePartialUpdate

A schedule that runs an Automation job automatically, either at a fixed interval or on a crontab expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**type** | **int** | Scheduling mode: fixed interval (&#x60;1&#x60;, uses &#x60;every&#x60;/&#x60;period&#x60;) or a crontab expression (&#x60;2&#x60;, uses the &#x60;crontab_*&#x60; fields). | [optional] 
**enabled** | **bool** |  | [optional] 
**last_run** | **datetime, none_type** |  | [optional] 
**every** | **int** |  | [optional] 
**period** | **str** |  | [optional] 
**crontab_day_of_month** | **str** |  | [optional] 
**crontab_day_of_week** | **str** |  | [optional] 
**crontab_hour** | **str** |  | [optional] 
**crontab_minute** | **str** |  | [optional] 
**crontab_month_of_year** | **str** |  | [optional] 
**job** | **int** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


