# StorageNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**address** | **str** | For communication between nodes only | [optional] 
**address_override** | **str** | Enforces mounting from a specific address/hostname instead of the available interfaces | [optional] 
**backend** | [**Backend**](Backend.md) |  | [optional] 
**type** | **int** |  | [optional] 
**ipmi** | **int** |  | [optional] 
**interfaces** | [**list[Interface]**](Interface.md) |  | [optional] [readonly] 
**status** | [**StorageNodeStatus**](StorageNodeStatus.md) |  | [optional] 
**is_log_aggregator** | **bool** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


