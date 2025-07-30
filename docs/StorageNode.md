# StorageNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**interfaces** | [**[Interface]**](Interface.md) |  | [readonly] 
**is_log_aggregator** | **bool** |  | [readonly] 
**task_queues** | **[str]** |  | 
**unique_id** | **str, none_type** |  | 
**name** | **str** |  | 
**address** | **str** | For communication between nodes only | 
**ipmi** | **int** |  | 
**ipmi_address** | **str, none_type** |  | 
**ipmi_username** | **str** |  | 
**ipmi_password** | **str** |  | 
**proxy_queue** | **bool** |  | 
**email_queue** | **bool** |  | 
**apply_configuration_queue** | **bool** |  | 
**solr_indexer_enabled** | **bool** |  | 
**discovery_enabled** | **bool** |  | 
**discovery_address_override** | **str, none_type** |  | 
**ntp_enabled** | **bool** |  | 
**type** | **int** |  | 
**allow_root_login** | **bool** |  | 
**permission_mask** | **str** | Comma-separated list of user permissions allowed on this node | 
**address_override** | **str, none_type** | Enforces mounting from a specific address/hostname instead of the available interfaces | 
**auto_scan_interfaces** | **bool** |  | 
**volume_queues** | **[int]** | Run volume-specific tasks for selected volumes. | 
**status** | [**StorageNodeStatus**](StorageNodeStatus.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


