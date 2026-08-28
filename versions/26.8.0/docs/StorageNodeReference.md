# StorageNodeReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**backend** | [**Backend**](Backend.md) |  | 
**interfaces** | [**[Interface]**](Interface.md) |  | [optional] [readonly] 
**status** | [**StorageNodeStatus**](StorageNodeStatus.md) |  | [optional] 
**is_log_aggregator** | **bool** |  | [optional] [readonly] 
**task_queues** | **[str]** |  | [optional] [readonly] 
**unique_id** | **str, none_type** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**address** | **str** | For communication between nodes only | [optional] [readonly] 
**ipmi** | **int** |  | [optional] [readonly] 
**ipmi_address** | **str, none_type** |  | [optional] [readonly] 
**ipmi_username** | **str** |  | [optional] [readonly] 
**ipmi_password** | **str** |  | [optional] [readonly] 
**proxy_queue** | **bool** |  | [optional] [readonly] 
**email_queue** | **bool** |  | [optional] [readonly] 
**solr_indexer_enabled** | **bool** |  | [optional] [readonly] 
**discovery_enabled** | **bool** |  | [optional] [readonly] 
**discovery_address_override** | **str, none_type** |  | [optional] [readonly] 
**ntp_enabled** | **bool** |  | [optional] [readonly] 
**type** | **int** |  | [optional] [readonly] 
**allow_root_login** | **bool** |  | [optional] [readonly] 
**permission_mask** | **str** | Comma-separated list of user permissions allowed on this node | [optional] [readonly] 
**address_override** | **str, none_type** | Enforces mounting from a specific address/hostname instead of the available interfaces | [optional] [readonly] 
**auto_scan_interfaces** | **bool** |  | [optional] [readonly] 
**onefs_host** | **str, none_type** |  | [optional] [readonly] 
**onefs_username** | **str, none_type** |  | [optional] [readonly] 
**onefs_password** | **str, none_type** |  | [optional] [readonly] 
**onefs_zone** | **str, none_type** |  | [optional] [readonly] 
**volume_queues** | **[int]** | Run volume-specific tasks for selected volumes. | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


