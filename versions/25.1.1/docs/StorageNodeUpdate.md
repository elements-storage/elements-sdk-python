# StorageNodeUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend** | [**Backend**](Backend.md) |  | 
**task_queues** | **[str]** |  | [optional] 
**unique_id** | **str, none_type** |  | [optional] 
**name** | **str** |  | [optional] 
**address** | **str** | For communication between nodes only | [optional] 
**ipmi** | **int** |  | [optional] 
**ipmi_address** | **str, none_type** |  | [optional] 
**ipmi_username** | **str** |  | [optional] 
**ipmi_password** | **str** |  | [optional] 
**proxy_queue** | **bool** |  | [optional] 
**email_queue** | **bool** |  | [optional] 
**apply_configuration_queue** | **bool** |  | [optional] 
**solr_indexer_enabled** | **bool** |  | [optional] 
**discovery_enabled** | **bool** |  | [optional] 
**discovery_address_override** | **str, none_type** |  | [optional] 
**ntp_enabled** | **bool** |  | [optional] 
**type** | **int** |  | [optional] 
**allow_root_login** | **bool** |  | [optional] 
**permission_mask** | **str** | Comma-separated list of user permissions allowed on this node | [optional] 
**address_override** | **str, none_type** | Enforces mounting from a specific address/hostname instead of the available interfaces | [optional] 
**auto_scan_interfaces** | **bool** |  | [optional] 
**onefs_host** | **str, none_type** |  | [optional] 
**onefs_username** | **str, none_type** |  | [optional] 
**onefs_password** | **str, none_type** |  | [optional] 
**onefs_zone** | **str, none_type** |  | [optional] 
**volume_queues** | **[int]** | Run volume-specific tasks for selected volumes. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


