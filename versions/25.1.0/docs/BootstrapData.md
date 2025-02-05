# BootstrapData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**events** | [**[Event]**](Event.md) |  | 
**sentry_config** | **{str: (str, none_type)}** |  | 
**has_wan_networks** | **bool** |  | 
**task_meta** | [**{str: (TaskType,)}**](TaskType.md) |  | 
**scanner_metadata_schema** | **[{str: (str, none_type)}]** |  | 
**media_root_permissions** | [**[MediaRootPermission]**](MediaRootPermission.md) |  | 
**shared_storage_values** | **{str: (str, none_type)}** |  | 
**user_storage_values** | **{str: (str, none_type)}** |  | 
**saml_providers** | [**[SAMLProviderMini]**](SAMLProviderMini.md) |  | 
**settings** | [**PublicSettings**](PublicSettings.md) |  | 
**kibana_enabled** | **bool** |  | 
**system_name** | **str** |  | 
**stream_proxy_url_prefix** | **str** |  | 
**has_password_policy** | **bool** |  | 
**has_filesystem_events** | **bool** |  | 
**current_node** | [**StorageNode**](StorageNode.md) |  | [optional] 
**license** | [**License**](License.md) |  | [optional] 
**parameter_values** | [**Parameters**](Parameters.md) |  | [optional] 
**identity_value** | [**ElementsUserDetail**](ElementsUserDetail.md) |  | [optional] 
**identity_value_from_cookie_session** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**active_saml_provider** | [**SAMLProviderMini**](SAMLProviderMini.md) |  | [optional] 
**tasks_summary** | [**TasksSummary**](TasksSummary.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


