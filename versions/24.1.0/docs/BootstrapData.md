# BootstrapData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_node** | [**StorageNode**](StorageNode.md) |  | 
**public_parameters** | [**PublicParameters**](PublicParameters.md) |  | 
**known_usernames** | **[str]** |  | 
**known_emails** | **[str]** |  | 
**impersonation_active** | **bool** |  | 
**one_time_access_token_active** | **bool** |  | 
**debug** | **bool** |  | 
**version** | [**ElementsVersion**](ElementsVersion.md) |  | 
**client_os** | **str** |  | 
**session_id** | **str** |  | 
**cloud_connections** | [**[CloudConnection]**](CloudConnection.md) |  | 
**ai_connections** | [**[AIConnection]**](AIConnection.md) |  | 
**events** | [**[Event]**](Event.md) |  | 
**sentry_config** | **{str: (str, none_type)}** |  | 
**has_wan_networks** | **bool** |  | 
**task_meta** | [**{str: (TaskType,)}**](TaskType.md) |  | 
**scanner_metadata_schema** | **[{str: (str, none_type)}]** |  | 
**media_root_permissions** | [**[MediaRootPermission]**](MediaRootPermission.md) |  | 
**shared_storage_values** | **{str: (str, none_type)}** |  | 
**user_storage_values** | **{str: (str, none_type)}** |  | 
**saml_providers** | [**[SAMLProviderMini]**](SAMLProviderMini.md) |  | 
**settings** | **{str: (str, none_type)}** |  | 
**kibana_enabled** | **bool** |  | 
**system_name** | **str** |  | 
**stream_proxy_url_prefix** | **str** |  | 
**license** | [**License**](License.md) |  | [optional] 
**parameter_values** | [**Parameters**](Parameters.md) |  | [optional] 
**identity_value** | [**ElementsUserDetail**](ElementsUserDetail.md) |  | [optional] 
**active_saml_provider** | [**SAMLProviderMini**](SAMLProviderMini.md) |  | [optional] 
**tasks_summary** | [**TasksSummary**](TasksSummary.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


