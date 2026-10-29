# Alert

A system alert, for example from the RAID controller or the filesystem fill level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**message** | **str** |  | 
**level** | **str** |  | 
**is_open** | **bool** |  | 
**node** | [**StorageNodeMini**](StorageNodeMini.md) |  | 
**opened_at** | **datetime** |  | [readonly] 
**closed_at** | **datetime, none_type** |  | 
**duration** | **float, none_type** | Duration of the alert in seconds | 
**acknowledged_by** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**silenced_by** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


