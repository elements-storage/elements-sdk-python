# ELEMENTS Python SDK

- API version: 2
- Python 2.7 and 3.4+
- Latest build: 3.3.0

## Installation & Usage

```sh
pip install elements-sdk
```

Then import the package:
```python
import elements_sdk
```

## Example
```python
from elements_sdk import ApiClient, Configuration, StorageApi, Share, Volume

config = Configuration(
    host='http://elements.local',
    api_key={'Authorization': 'Bearer your-api-token'},
)
config.debug = True

with ApiClient(config) as api_client:
    storage_api = StorageApi(api_client)

    volume: Volume = storage_api.get_all_volumes()[0]
    share: Share = storage_api.create_share(dict(
        name='test',
        volume=volume,
        path='foo/bar'
    ))
    print(share)
    storage_api.delete_share(share.id)
```

## API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AWSApi* | [**create_aws_account**](docs/AWSApi#create_aws_account) | **POST** `/api/2/aws-accounts` | 
*AWSApi* | [**delete_aws_account**](docs/AWSApi#delete_aws_account) | **DELETE** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**get_all_aws_accounts**](docs/AWSApi#get_all_aws_accounts) | **GET** `/api/2/aws-accounts` | 
*AWSApi* | [**get_aws_account**](docs/AWSApi#get_aws_account) | **GET** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**get_aws_account_buckets**](docs/AWSApi#get_aws_account_buckets) | **GET** `/api/2/aws-accounts/{id}/buckets` | 
*AWSApi* | [**get_aws_account_sns_topics**](docs/AWSApi#get_aws_account_sns_topics) | **GET** `/api/2/aws-accounts/{id}/sns/topics` | 
*AWSApi* | [**patch_aws_account**](docs/AWSApi#patch_aws_account) | **PATCH** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**test_aws_account_credentials**](docs/AWSApi#test_aws_account_credentials) | **POST** `/api/2/aws-accounts/test-credentials` | 
*AWSApi* | [**update_aws_account**](docs/AWSApi#update_aws_account) | **PUT** `/api/2/aws-accounts/{id}` | 
*AuthApi* | [**check_auth_ticket**](docs/AuthApi#check_auth_ticket) | **POST** `/api/2/auth/ticket/check` | 
*AuthApi* | [**create_auth_ticket**](docs/AuthApi#create_auth_ticket) | **POST** `/api/2/auth/ticket` | 
*AuthApi* | [**delete_access_token**](docs/AuthApi#delete_access_token) | **DELETE** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**generate_password**](docs/AuthApi#generate_password) | **POST** `/api/2/auth/generate-password` | 
*AuthApi* | [**get_access_token**](docs/AuthApi#get_access_token) | **GET** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**get_all_access_tokens**](docs/AuthApi#get_all_access_tokens) | **GET** `/api/2/auth/access-tokens` | 
*AuthApi* | [**login**](docs/AuthApi#login) | **POST** `/api/2/auth/login` | 
*AuthApi* | [**logout**](docs/AuthApi#logout) | **POST** `/api/2/auth/logout` | 
*AuthApi* | [**reset_password**](docs/AuthApi#reset_password) | **POST** `/api/2/auth/reset-password` | 
*AuthApi* | [**send_access_token_email_notification**](docs/AuthApi#send_access_token_email_notification) | **POST** `/api/2/auth/access-tokens/{id}/email` | 
*AuthApi* | [**start_impersonation**](docs/AuthApi#start_impersonation) | **POST** `/api/2/auth/impersonation` | 
*AuthApi* | [**stop_impersonation**](docs/AuthApi#stop_impersonation) | **POST** `/api/2/auth/impersonation/stop` | 
*AutomationApi* | [**abort_task**](docs/AutomationApi#abort_task) | **POST** `/api/2/tasks/{id}/abort` | 
*AutomationApi* | [**create_job**](docs/AutomationApi#create_job) | **POST** `/api/2/jobs` | 
*AutomationApi* | [**create_schedule**](docs/AutomationApi#create_schedule) | **POST** `/api/2/schedules` | 
*AutomationApi* | [**create_subtask**](docs/AutomationApi#create_subtask) | **POST** `/api/2/subtasks` | 
*AutomationApi* | [**delete_finished_tasks**](docs/AutomationApi#delete_finished_tasks) | **DELETE** `/api/2/tasks/finished` | 
*AutomationApi* | [**delete_job**](docs/AutomationApi#delete_job) | **DELETE** `/api/2/jobs/{id}` | 
*AutomationApi* | [**delete_schedule**](docs/AutomationApi#delete_schedule) | **DELETE** `/api/2/schedules/{id}` | 
*AutomationApi* | [**delete_subtask**](docs/AutomationApi#delete_subtask) | **DELETE** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**delete_task**](docs/AutomationApi#delete_task) | **DELETE** `/api/2/tasks/{id}` | 
*AutomationApi* | [**download_all_task_logs**](docs/AutomationApi#download_all_task_logs) | **GET** `/api/2/tasks/logs/download` | 
*AutomationApi* | [**download_task_log**](docs/AutomationApi#download_task_log) | **GET** `/api/2/tasks/{id}/log/download` | 
*AutomationApi* | [**get_all_events**](docs/AutomationApi#get_all_events) | **GET** `/api/2/events` | 
*AutomationApi* | [**get_all_jobs**](docs/AutomationApi#get_all_jobs) | **GET** `/api/2/jobs` | 
*AutomationApi* | [**get_all_schedules**](docs/AutomationApi#get_all_schedules) | **GET** `/api/2/schedules` | 
*AutomationApi* | [**get_all_subtasks**](docs/AutomationApi#get_all_subtasks) | **GET** `/api/2/subtasks` | 
*AutomationApi* | [**get_all_task_queues**](docs/AutomationApi#get_all_task_queues) | **GET** `/api/2/tasks/queues` | 
*AutomationApi* | [**get_all_task_types**](docs/AutomationApi#get_all_task_types) | **GET** `/api/2/tasks/types` | 
*AutomationApi* | [**get_all_tasks**](docs/AutomationApi#get_all_tasks) | **GET** `/api/2/tasks` | 
*AutomationApi* | [**get_event**](docs/AutomationApi#get_event) | **GET** `/api/2/events/{id}` | 
*AutomationApi* | [**get_finished_tasks**](docs/AutomationApi#get_finished_tasks) | **GET** `/api/2/tasks/finished` | 
*AutomationApi* | [**get_job**](docs/AutomationApi#get_job) | **GET** `/api/2/jobs/{id}` | 
*AutomationApi* | [**get_pending_tasks**](docs/AutomationApi#get_pending_tasks) | **GET** `/api/2/tasks/pending` | 
*AutomationApi* | [**get_python_environments**](docs/AutomationApi#get_python_environments) | **GET** `/api/2/python/environments` | 
*AutomationApi* | [**get_schedule**](docs/AutomationApi#get_schedule) | **GET** `/api/2/schedules/{id}` | 
*AutomationApi* | [**get_subtask**](docs/AutomationApi#get_subtask) | **GET** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**get_task**](docs/AutomationApi#get_task) | **GET** `/api/2/tasks/{id}` | 
*AutomationApi* | [**get_task_log**](docs/AutomationApi#get_task_log) | **GET** `/api/2/tasks/{id}/log` | 
*AutomationApi* | [**get_task_type**](docs/AutomationApi#get_task_type) | **GET** `/api/2/tasks/types/{type}` | 
*AutomationApi* | [**get_tasks_summary**](docs/AutomationApi#get_tasks_summary) | **GET** `/api/2/tasks/summary` | 
*AutomationApi* | [**kill_all_pending_tasks**](docs/AutomationApi#kill_all_pending_tasks) | **DELETE** `/api/2/tasks/pending` | 
*AutomationApi* | [**kill_task**](docs/AutomationApi#kill_task) | **POST** `/api/2/tasks/{id}/kill` | 
*AutomationApi* | [**patch_job**](docs/AutomationApi#patch_job) | **PATCH** `/api/2/jobs/{id}` | 
*AutomationApi* | [**patch_schedule**](docs/AutomationApi#patch_schedule) | **PATCH** `/api/2/schedules/{id}` | 
*AutomationApi* | [**patch_subtask**](docs/AutomationApi#patch_subtask) | **PATCH** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**restart_task**](docs/AutomationApi#restart_task) | **POST** `/api/2/tasks/{id}/restart` | 
*AutomationApi* | [**start_job**](docs/AutomationApi#start_job) | **POST** `/api/2/jobs/{id}/start` | 
*AutomationApi* | [**start_task**](docs/AutomationApi#start_task) | **POST** `/api/2/tasks/start` | 
*AutomationApi* | [**update_job**](docs/AutomationApi#update_job) | **PUT** `/api/2/jobs/{id}` | 
*AutomationApi* | [**update_schedule**](docs/AutomationApi#update_schedule) | **PUT** `/api/2/schedules/{id}` | 
*AutomationApi* | [**update_subtask**](docs/AutomationApi#update_subtask) | **PUT** `/api/2/subtasks/{id}` | 
*IntegrationsApi* | [**delete_slack_connection**](docs/IntegrationsApi#delete_slack_connection) | **DELETE** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**delete_teams_connection**](docs/IntegrationsApi#delete_teams_connection) | **DELETE** `/api/2/integrations/teams/{id}` | 
*IntegrationsApi* | [**get_all_slack_connections**](docs/IntegrationsApi#get_all_slack_connections) | **GET** `/api/2/integrations/slack` | 
*IntegrationsApi* | [**get_all_teams_connections**](docs/IntegrationsApi#get_all_teams_connections) | **GET** `/api/2/integrations/teams` | 
*IntegrationsApi* | [**get_slack_channels**](docs/IntegrationsApi#get_slack_channels) | **GET** `/api/2/integrations/slack/{id}/channels` | 
*IntegrationsApi* | [**get_slack_connection**](docs/IntegrationsApi#get_slack_connection) | **GET** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**get_slack_emoji**](docs/IntegrationsApi#get_slack_emoji) | **GET** `/api/2/integrations/slack/{id}/emoji` | 
*IntegrationsApi* | [**get_slack_users**](docs/IntegrationsApi#get_slack_users) | **GET** `/api/2/integrations/slack/{id}/users` | 
*IntegrationsApi* | [**get_teams_channels**](docs/IntegrationsApi#get_teams_channels) | **GET** `/api/2/integrations/teams/{id}/channels` | 
*IntegrationsApi* | [**get_teams_connection**](docs/IntegrationsApi#get_teams_connection) | **GET** `/api/2/integrations/teams/{id}` | 
*IntegrationsApi* | [**get_teams_users**](docs/IntegrationsApi#get_teams_users) | **GET** `/api/2/integrations/teams/{id}/users` | 
*IntegrationsApi* | [**patch_slack_connection**](docs/IntegrationsApi#patch_slack_connection) | **PATCH** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**patch_teams_connection**](docs/IntegrationsApi#patch_teams_connection) | **PATCH** `/api/2/integrations/teams/{id}` | 
*IntegrationsApi* | [**send_slack_message**](docs/IntegrationsApi#send_slack_message) | **POST** `/api/2/integrations/slack/{id}/message` | 
*IntegrationsApi* | [**send_teams_message**](docs/IntegrationsApi#send_teams_message) | **POST** `/api/2/integrations/teams/{id}/send-message` | 
*IntegrationsApi* | [**start_slack_connection_flow**](docs/IntegrationsApi#start_slack_connection_flow) | **GET** `/api/2/integrations/slack/connect` | 
*IntegrationsApi* | [**start_slack_connection_token_refresh_flow**](docs/IntegrationsApi#start_slack_connection_token_refresh_flow) | **GET** `/api/2/integrations/slack/{id}/refresh-token` | 
*IntegrationsApi* | [**start_teams_connection_flow**](docs/IntegrationsApi#start_teams_connection_flow) | **GET** `/api/2/integrations/teams/connect` | 
*IntegrationsApi* | [**start_teams_connection_token_refresh_flow**](docs/IntegrationsApi#start_teams_connection_token_refresh_flow) | **GET** `/api/2/integrations/teams/{id}/refresh-token` | 
*IntegrationsApi* | [**update_slack_connection**](docs/IntegrationsApi#update_slack_connection) | **PUT** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**update_teams_connection**](docs/IntegrationsApi#update_teams_connection) | **PUT** `/api/2/integrations/teams/{id}` | 
*MainApi* | [**apply_configuration**](docs/MainApi#apply_configuration) | **POST** `/api/2/configuration/apply` | 
*MainApi* | [**beep**](docs/MainApi#beep) | **POST** `/api/2/system/beep` | 
*MainApi* | [**check_chunk_uploaded**](docs/MainApi#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
*MainApi* | [**check_internet_connectivity**](docs/MainApi#check_internet_connectivity) | **POST** `/api/2/system/check-connectivity` | 
*MainApi* | [**check_stor_next_license**](docs/MainApi#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
*MainApi* | [**collect_diagnostics**](docs/MainApi#collect_diagnostics) | **POST** `/api/2/system/collect-diagnostics` | 
*MainApi* | [**create_archive**](docs/MainApi#create_archive) | **POST** `/api/2/download-archive/create` | 
*MainApi* | [**create_group**](docs/MainApi#create_group) | **POST** `/api/2/groups` | 
*MainApi* | [**create_home_workspace**](docs/MainApi#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
*MainApi* | [**create_ntp_server**](docs/MainApi#create_ntp_server) | **POST** `/api/2/system/time/servers` | 
*MainApi* | [**create_user**](docs/MainApi#create_user) | **POST** `/api/2/users` | 
*MainApi* | [**create_workstation**](docs/MainApi#create_workstation) | **POST** `/api/2/workstations` | 
*MainApi* | [**delete_download_archive**](docs/MainApi#delete_download_archive) | **DELETE** `/api/2/download-archive/{id}` | 
*MainApi* | [**delete_group**](docs/MainApi#delete_group) | **DELETE** `/api/2/groups/{id}` | 
*MainApi* | [**delete_home_workspace**](docs/MainApi#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
*MainApi* | [**delete_ntp_server**](docs/MainApi#delete_ntp_server) | **DELETE** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**delete_user**](docs/MainApi#delete_user) | **DELETE** `/api/2/users/{id}` | 
*MainApi* | [**delete_workstation**](docs/MainApi#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
*MainApi* | [**disable_user_totp**](docs/MainApi#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
*MainApi* | [**enable_user_totp**](docs/MainApi#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
*MainApi* | [**finish_upload**](docs/MainApi#finish_upload) | **POST** `/api/2/uploads/finish` | 
*MainApi* | [**fix_ldap_group_memberships**](docs/MainApi#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
*MainApi* | [**get_all_download_archives**](docs/MainApi#get_all_download_archives) | **GET** `/api/2/download-archive` | 
*MainApi* | [**get_all_downloads**](docs/MainApi#get_all_downloads) | **GET** `/api/2/downloads` | 
*MainApi* | [**get_all_groups**](docs/MainApi#get_all_groups) | **GET** `/api/2/groups` | 
*MainApi* | [**get_all_ldap_servers**](docs/MainApi#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
*MainApi* | [**get_all_ntp_servers**](docs/MainApi#get_all_ntp_servers) | **GET** `/api/2/system/time/servers` | 
*MainApi* | [**get_all_storage_nodes**](docs/MainApi#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
*MainApi* | [**get_all_users**](docs/MainApi#get_all_users) | **GET** `/api/2/users` | 
*MainApi* | [**get_all_workstations**](docs/MainApi#get_all_workstations) | **GET** `/api/2/workstations` | 
*MainApi* | [**get_client_download_file**](docs/MainApi#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
*MainApi* | [**get_client_downloads**](docs/MainApi#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
*MainApi* | [**get_current_workstation**](docs/MainApi#get_current_workstation) | **GET** `/api/2/workstations/current` | 
*MainApi* | [**get_download**](docs/MainApi#get_download) | **GET** `/api/2/downloads/{id}` | 
*MainApi* | [**get_download_archive**](docs/MainApi#get_download_archive) | **GET** `/api/2/download-archive/{id}` | 
*MainApi* | [**get_download_archive_file**](docs/MainApi#get_download_archive_file) | **GET** `/api/2/download-archive/{id}/download` | 
*MainApi* | [**get_download_file**](docs/MainApi#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
*MainApi* | [**get_download_icon**](docs/MainApi#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
*MainApi* | [**get_group**](docs/MainApi#get_group) | **GET** `/api/2/groups/{id}` | 
*MainApi* | [**get_home_workspace**](docs/MainApi#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
*MainApi* | [**get_ipmi_configuration**](docs/MainApi#get_ipmi_configuration) | **GET** `/api/2/nodes/{id}/ipmi` | 
*MainApi* | [**get_ldap_server**](docs/MainApi#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
*MainApi* | [**get_ldap_server_groups**](docs/MainApi#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
*MainApi* | [**get_ldap_server_users**](docs/MainApi#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
*MainApi* | [**get_license**](docs/MainApi#get_license) | **GET** `/api/2/license` | 
*MainApi* | [**get_local_time**](docs/MainApi#get_local_time) | **GET** `/api/2/system/time` | 
*MainApi* | [**get_log**](docs/MainApi#get_log) | **GET** `/api/2/system/log/{path}` | 
*MainApi* | [**get_node_ipmi_sensors**](docs/MainApi#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
*MainApi* | [**get_node_stats**](docs/MainApi#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
*MainApi* | [**get_ntp_server**](docs/MainApi#get_ntp_server) | **GET** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**get_parameters**](docs/MainApi#get_parameters) | **GET** `/api/2/parameters` | 
*MainApi* | [**get_profile**](docs/MainApi#get_profile) | **GET** `/api/2/users/me` | 
*MainApi* | [**get_release_notes**](docs/MainApi#get_release_notes) | **GET** `/api/2/release-notes` | 
*MainApi* | [**get_service_status**](docs/MainApi#get_service_status) | **GET** `/api/2/nodes/{id}/services/{service}` | 
*MainApi* | [**get_smtp_configuration**](docs/MainApi#get_smtp_configuration) | **GET** `/api/2/system/smtp` | 
*MainApi* | [**get_stor_next_license**](docs/MainApi#get_stor_next_license) | **GET** `/api/2/stornext-license` | 
*MainApi* | [**get_storage_node**](docs/MainApi#get_storage_node) | **GET** `/api/2/nodes/{id}` | 
*MainApi* | [**get_system_info**](docs/MainApi#get_system_info) | **GET** `/api/2/system/info` | 
*MainApi* | [**get_user**](docs/MainApi#get_user) | **GET** `/api/2/users/{id}` | 
*MainApi* | [**get_workstation**](docs/MainApi#get_workstation) | **GET** `/api/2/workstations/{id}` | 
*MainApi* | [**install_stor_next_license**](docs/MainApi#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
*MainApi* | [**patch_current_workstation**](docs/MainApi#patch_current_workstation) | **PATCH** `/api/2/workstations/current` | 
*MainApi* | [**patch_download_archive**](docs/MainApi#patch_download_archive) | **PATCH** `/api/2/download-archive/{id}` | 
*MainApi* | [**patch_group**](docs/MainApi#patch_group) | **PATCH** `/api/2/groups/{id}` | 
*MainApi* | [**patch_ntp_server**](docs/MainApi#patch_ntp_server) | **PATCH** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**patch_profile**](docs/MainApi#patch_profile) | **PATCH** `/api/2/users/me` | 
*MainApi* | [**patch_user**](docs/MainApi#patch_user) | **PATCH** `/api/2/users/{id}` | 
*MainApi* | [**patch_workstation**](docs/MainApi#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
*MainApi* | [**preview_user**](docs/MainApi#preview_user) | **POST** `/api/2/users/preview` | 
*MainApi* | [**reboot**](docs/MainApi#reboot) | **POST** `/api/2/system/reboot` | 
*MainApi* | [**register_upload**](docs/MainApi#register_upload) | **POST** `/api/2/uploads/register` | 
*MainApi* | [**render_email_template_preview**](docs/MainApi#render_email_template_preview) | **POST** `/api/2/system/smtp/preview` | 
*MainApi* | [**reset_user_password**](docs/MainApi#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
*MainApi* | [**run_service_operation**](docs/MainApi#run_service_operation) | **POST** `/api/2/nodes/{id}/services/{service}/{operation}` | 
*MainApi* | [**set_ipmi_configuration**](docs/MainApi#set_ipmi_configuration) | **PUT** `/api/2/nodes/{id}/ipmi` | 
*MainApi* | [**set_local_time**](docs/MainApi#set_local_time) | **POST** `/api/2/system/time` | 
*MainApi* | [**set_my_password**](docs/MainApi#set_my_password) | **POST** `/api/2/users/me/password` | 
*MainApi* | [**set_user_password**](docs/MainApi#set_user_password) | **POST** `/api/2/users/{id}/password` | 
*MainApi* | [**shutdown**](docs/MainApi#shutdown) | **POST** `/api/2/system/shutdown` | 
*MainApi* | [**start_solr_reindex**](docs/MainApi#start_solr_reindex) | **POST** `/api/2/system/solr/reindex` | 
*MainApi* | [**start_support_session**](docs/MainApi#start_support_session) | **POST** `/api/2/system/support-session/start` | 
*MainApi* | [**start_system_backup**](docs/MainApi#start_system_backup) | **POST** `/api/2/system/backup/start` | 
*MainApi* | [**sync_ldap_group**](docs/MainApi#sync_ldap_group) | **POST** `/api/2/groups/{id}/ldap-sync` | 
*MainApi* | [**sync_ldap_users**](docs/MainApi#sync_ldap_users) | **POST** `/api/2/ldap-servers/{id}/sync-users` | 
*MainApi* | [**sync_time**](docs/MainApi#sync_time) | **POST** `/api/2/system/time/sync` | 
*MainApi* | [**sync_user_totp**](docs/MainApi#sync_user_totp) | **PUT** `/api/2/users/{id}/totp` | 
*MainApi* | [**test_smtp_configuration**](docs/MainApi#test_smtp_configuration) | **POST** `/api/2/system/smtp/test` | 
*MainApi* | [**update_current_workstation**](docs/MainApi#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
*MainApi* | [**update_download_archive**](docs/MainApi#update_download_archive) | **PUT** `/api/2/download-archive/{id}` | 
*MainApi* | [**update_group**](docs/MainApi#update_group) | **PUT** `/api/2/groups/{id}` | 
*MainApi* | [**update_ntp_server**](docs/MainApi#update_ntp_server) | **PUT** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**update_parameters**](docs/MainApi#update_parameters) | **PUT** `/api/2/parameters` | 
*MainApi* | [**update_profile**](docs/MainApi#update_profile) | **PUT** `/api/2/users/me` | 
*MainApi* | [**update_smtp_configuration**](docs/MainApi#update_smtp_configuration) | **PUT** `/api/2/system/smtp` | 
*MainApi* | [**update_user**](docs/MainApi#update_user) | **PUT** `/api/2/users/{id}` | 
*MainApi* | [**update_workstation**](docs/MainApi#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
*MainApi* | [**upload_chunk**](docs/MainApi#upload_chunk) | **POST** `/api/2/uploads/chunk` | 
*MediaLibraryApi* | [**clear_subclip_clipboard**](docs/MediaLibraryApi#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
*MediaLibraryApi* | [**combine_assets_into_set**](docs/MediaLibraryApi#combine_assets_into_set) | **POST** `/api/2/media/assets/combine` | 
*MediaLibraryApi* | [**create_asset**](docs/MediaLibraryApi#create_asset) | **POST** `/api/2/media/assets` | 
*MediaLibraryApi* | [**create_asset_rating**](docs/MediaLibraryApi#create_asset_rating) | **POST** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**create_comment**](docs/MediaLibraryApi#create_comment) | **POST** `/api/2/media/comments` | 
*MediaLibraryApi* | [**create_custom_field**](docs/MediaLibraryApi#create_custom_field) | **POST** `/api/2/media/custom-fields` | 
*MediaLibraryApi* | [**create_external_transcoder**](docs/MediaLibraryApi#create_external_transcoder) | **POST** `/api/2/media/external-transcoders` | 
*MediaLibraryApi* | [**create_marker**](docs/MediaLibraryApi#create_marker) | **POST** `/api/2/media/markers` | 
*MediaLibraryApi* | [**create_media_file_template**](docs/MediaLibraryApi#create_media_file_template) | **POST** `/api/2/media/files/templates` | 
*MediaLibraryApi* | [**create_media_root**](docs/MediaLibraryApi#create_media_root) | **POST** `/api/2/media/roots` | 
*MediaLibraryApi* | [**create_media_root_permission**](docs/MediaLibraryApi#create_media_root_permission) | **POST** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**create_media_tag**](docs/MediaLibraryApi#create_media_tag) | **POST** `/api/2/media/tags` | 
*MediaLibraryApi* | [**create_proxy_profile**](docs/MediaLibraryApi#create_proxy_profile) | **POST** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**create_subclip**](docs/MediaLibraryApi#create_subclip) | **POST** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**create_subclip_clipboard_entry**](docs/MediaLibraryApi#create_subclip_clipboard_entry) | **POST** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**delete_asset**](docs/MediaLibraryApi#delete_asset) | **DELETE** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**delete_asset_rating**](docs/MediaLibraryApi#delete_asset_rating) | **DELETE** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**delete_comment**](docs/MediaLibraryApi#delete_comment) | **DELETE** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**delete_custom_field**](docs/MediaLibraryApi#delete_custom_field) | **DELETE** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**delete_easy_sharing_token_for_bundle**](docs/MediaLibraryApi#delete_easy_sharing_token_for_bundle) | **DELETE** `/api/2/media/bundles/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**delete_easy_sharing_token_for_directory**](docs/MediaLibraryApi#delete_easy_sharing_token_for_directory) | **DELETE** `/api/2/media/files/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**delete_external_transcoder**](docs/MediaLibraryApi#delete_external_transcoder) | **DELETE** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**delete_marker**](docs/MediaLibraryApi#delete_marker) | **DELETE** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**delete_media_file_template**](docs/MediaLibraryApi#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**delete_media_library_objects**](docs/MediaLibraryApi#delete_media_library_objects) | **POST** `/api/2/media/delete` | 
*MediaLibraryApi* | [**delete_media_root**](docs/MediaLibraryApi#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**delete_media_root_permission**](docs/MediaLibraryApi#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**delete_media_tag**](docs/MediaLibraryApi#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**delete_media_update**](docs/MediaLibraryApi#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
*MediaLibraryApi* | [**delete_proxy**](docs/MediaLibraryApi#delete_proxy) | **DELETE** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**delete_proxy_profile**](docs/MediaLibraryApi#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**delete_subclip**](docs/MediaLibraryApi#delete_subclip) | **DELETE** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**delete_subclip_clipboard_entry**](docs/MediaLibraryApi#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
*MediaLibraryApi* | [**discover_media**](docs/MediaLibraryApi#discover_media) | **POST** `/api/2/scanner/discover` | 
*MediaLibraryApi* | [**download_asset_proxy_file**](docs/MediaLibraryApi#download_asset_proxy_file) | **GET** `/api/2/media/assets/{id}/proxy-files/{filename}` | 
*MediaLibraryApi* | [**download_media_file**](docs/MediaLibraryApi#download_media_file) | **GET** `/api/2/media/files/{id}/download` | 
*MediaLibraryApi* | [**download_proxy**](docs/MediaLibraryApi#download_proxy) | **GET** `/api/2/media/proxies/{id}/download` | 
*MediaLibraryApi* | [**forget_deleted_media_files**](docs/MediaLibraryApi#forget_deleted_media_files) | **POST** `/api/2/media/files/{id}/forget-deleted` | 
*MediaLibraryApi* | [**generate_proxies**](docs/MediaLibraryApi#generate_proxies) | **POST** `/api/2/media/proxies` | 
*MediaLibraryApi* | [**get_all_asset_project_links**](docs/MediaLibraryApi#get_all_asset_project_links) | **GET** `/api/2/media/assets/project-links` | 
*MediaLibraryApi* | [**get_all_asset_ratings**](docs/MediaLibraryApi#get_all_asset_ratings) | **GET** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**get_all_asset_tape_backups**](docs/MediaLibraryApi#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
*MediaLibraryApi* | [**get_all_assets**](docs/MediaLibraryApi#get_all_assets) | **GET** `/api/2/media/assets` | 
*MediaLibraryApi* | [**get_all_bundles_for_media_root**](docs/MediaLibraryApi#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
*MediaLibraryApi* | [**get_all_click_links**](docs/MediaLibraryApi#get_all_click_links) | **GET** `/api/2/media/assets/click-links` | 
*MediaLibraryApi* | [**get_all_comments**](docs/MediaLibraryApi#get_all_comments) | **GET** `/api/2/media/comments` | 
*MediaLibraryApi* | [**get_all_custom_fields**](docs/MediaLibraryApi#get_all_custom_fields) | **GET** `/api/2/media/custom-fields` | 
*MediaLibraryApi* | [**get_all_external_transcoders**](docs/MediaLibraryApi#get_all_external_transcoders) | **GET** `/api/2/media/external-transcoders` | 
*MediaLibraryApi* | [**get_all_markers**](docs/MediaLibraryApi#get_all_markers) | **GET** `/api/2/media/markers` | 
*MediaLibraryApi* | [**get_all_media_file_bundles**](docs/MediaLibraryApi#get_all_media_file_bundles) | **GET** `/api/2/media/bundles` | 
*MediaLibraryApi* | [**get_all_media_file_templates**](docs/MediaLibraryApi#get_all_media_file_templates) | **GET** `/api/2/media/files/templates` | 
*MediaLibraryApi* | [**get_all_media_files**](docs/MediaLibraryApi#get_all_media_files) | **GET** `/api/2/media/files` | 
*MediaLibraryApi* | [**get_all_media_files_for_bundles**](docs/MediaLibraryApi#get_all_media_files_for_bundles) | **POST** `/api/2/media/files/for-bundles` | 
*MediaLibraryApi* | [**get_all_media_files_for_media_root**](docs/MediaLibraryApi#get_all_media_files_for_media_root) | **GET** `/api/2/media/files/flat/{root}` | 
*MediaLibraryApi* | [**get_all_media_root_permissions**](docs/MediaLibraryApi#get_all_media_root_permissions) | **GET** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**get_all_media_roots**](docs/MediaLibraryApi#get_all_media_roots) | **GET** `/api/2/media/roots` | 
*MediaLibraryApi* | [**get_all_media_tags**](docs/MediaLibraryApi#get_all_media_tags) | **GET** `/api/2/media/tags` | 
*MediaLibraryApi* | [**get_all_media_updates**](docs/MediaLibraryApi#get_all_media_updates) | **GET** `/api/2/media/updates` | 
*MediaLibraryApi* | [**get_all_proxy_generators**](docs/MediaLibraryApi#get_all_proxy_generators) | **GET** `/api/2/media/proxy-generators` | 
*MediaLibraryApi* | [**get_all_proxy_profiles**](docs/MediaLibraryApi#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**get_all_subclip_clipboard_entries**](docs/MediaLibraryApi#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**get_all_subclips**](docs/MediaLibraryApi#get_all_subclips) | **GET** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**get_all_transcoder_profiles**](docs/MediaLibraryApi#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
*MediaLibraryApi* | [**get_asset**](docs/MediaLibraryApi#get_asset) | **GET** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**get_asset_rating**](docs/MediaLibraryApi#get_asset_rating) | **GET** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**get_comment**](docs/MediaLibraryApi#get_comment) | **GET** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**get_custom_field**](docs/MediaLibraryApi#get_custom_field) | **GET** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**get_easy_sharing_token_for_bundle**](docs/MediaLibraryApi#get_easy_sharing_token_for_bundle) | **GET** `/api/2/media/bundles/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**get_easy_sharing_token_for_directory**](docs/MediaLibraryApi#get_easy_sharing_token_for_directory) | **GET** `/api/2/media/files/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**get_external_transcoder**](docs/MediaLibraryApi#get_external_transcoder) | **GET** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**get_frame**](docs/MediaLibraryApi#get_frame) | **GET** `/api/2/media/assets/{id}/frames/{frame}` | 
*MediaLibraryApi* | [**get_latest_media_update**](docs/MediaLibraryApi#get_latest_media_update) | **GET** `/api/2/media/updates/latest` | 
*MediaLibraryApi* | [**get_marker**](docs/MediaLibraryApi#get_marker) | **GET** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**get_media_file**](docs/MediaLibraryApi#get_media_file) | **GET** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**get_media_file_bundle**](docs/MediaLibraryApi#get_media_file_bundle) | **GET** `/api/2/media/bundles/{id}` | 
*MediaLibraryApi* | [**get_media_file_contents**](docs/MediaLibraryApi#get_media_file_contents) | **GET** `/api/2/media/files/{id}/contents` | 
*MediaLibraryApi* | [**get_media_file_template**](docs/MediaLibraryApi#get_media_file_template) | **GET** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**get_media_root**](docs/MediaLibraryApi#get_media_root) | **GET** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**get_media_root_permission**](docs/MediaLibraryApi#get_media_root_permission) | **GET** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**get_media_tag**](docs/MediaLibraryApi#get_media_tag) | **GET** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**get_multiple_assets**](docs/MediaLibraryApi#get_multiple_assets) | **POST** `/api/2/media/assets/multiple` | 
*MediaLibraryApi* | [**get_multiple_bundles**](docs/MediaLibraryApi#get_multiple_bundles) | **POST** `/api/2/media/bundles/multiple` | 
*MediaLibraryApi* | [**get_multiple_files**](docs/MediaLibraryApi#get_multiple_files) | **POST** `/api/2/media/files/multiple` | 
*MediaLibraryApi* | [**get_my_media_root_permissions**](docs/MediaLibraryApi#get_my_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine` | 
*MediaLibraryApi* | [**get_my_resolved_media_root_permissions**](docs/MediaLibraryApi#get_my_resolved_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine/resolved` | 
*MediaLibraryApi* | [**get_proxy**](docs/MediaLibraryApi#get_proxy) | **GET** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**get_proxy_generator**](docs/MediaLibraryApi#get_proxy_generator) | **GET** `/api/2/media/proxy-generators/{id}` | 
*MediaLibraryApi* | [**get_proxy_profile**](docs/MediaLibraryApi#get_proxy_profile) | **GET** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**get_proxy_profile_proxy_count**](docs/MediaLibraryApi#get_proxy_profile_proxy_count) | **GET** `/api/2/media/proxy-profiles/{id}/proxy-count` | 
*MediaLibraryApi* | [**get_subclip**](docs/MediaLibraryApi#get_subclip) | **GET** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**get_transcoder_profile**](docs/MediaLibraryApi#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
*MediaLibraryApi* | [**get_vantage_workflows**](docs/MediaLibraryApi#get_vantage_workflows) | **GET** `/api/2/media/external-transcoders/{id}/workflows` | 
*MediaLibraryApi* | [**mark_media_directory_as_showroom**](docs/MediaLibraryApi#mark_media_directory_as_showroom) | **POST** `/api/2/media/files/{id}/showroom` | 
*MediaLibraryApi* | [**patch_asset**](docs/MediaLibraryApi#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**patch_asset_rating**](docs/MediaLibraryApi#patch_asset_rating) | **PATCH** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**patch_comment**](docs/MediaLibraryApi#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**patch_custom_field**](docs/MediaLibraryApi#patch_custom_field) | **PATCH** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**patch_external_transcoder**](docs/MediaLibraryApi#patch_external_transcoder) | **PATCH** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**patch_marker**](docs/MediaLibraryApi#patch_marker) | **PATCH** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**patch_media_file**](docs/MediaLibraryApi#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**patch_media_file_template**](docs/MediaLibraryApi#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**patch_media_root**](docs/MediaLibraryApi#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**patch_media_root_permission**](docs/MediaLibraryApi#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**patch_media_tag**](docs/MediaLibraryApi#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**patch_proxy_profile**](docs/MediaLibraryApi#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**patch_subclip**](docs/MediaLibraryApi#patch_subclip) | **PATCH** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**rename_custom_field**](docs/MediaLibraryApi#rename_custom_field) | **POST** `/api/2/media/custom-fields/{id}/rename` | 
*MediaLibraryApi* | [**render_subclip**](docs/MediaLibraryApi#render_subclip) | **POST** `/api/2/media/subclips/{id}/render` | 
*MediaLibraryApi* | [**request_media_scan**](docs/MediaLibraryApi#request_media_scan) | **POST** `/api/2/scanner/scan` | 
*MediaLibraryApi* | [**resolve_comment**](docs/MediaLibraryApi#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
*MediaLibraryApi* | [**share_media_library_objects**](docs/MediaLibraryApi#share_media_library_objects) | **POST** `/api/2/media/share` | 
*MediaLibraryApi* | [**test_external_transcoder_connection**](docs/MediaLibraryApi#test_external_transcoder_connection) | **POST** `/api/2/media/external-transcoders/test-connection` | 
*MediaLibraryApi* | [**transition_workflow**](docs/MediaLibraryApi#transition_workflow) | **POST** `/api/2/media/workflow/transition` | 
*MediaLibraryApi* | [**unmark_media_directory_as_showroom**](docs/MediaLibraryApi#unmark_media_directory_as_showroom) | **DELETE** `/api/2/media/files/{id}/showroom` | 
*MediaLibraryApi* | [**unresolve_comment**](docs/MediaLibraryApi#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
*MediaLibraryApi* | [**update_asset**](docs/MediaLibraryApi#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**update_asset_rating**](docs/MediaLibraryApi#update_asset_rating) | **PUT** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**update_comment**](docs/MediaLibraryApi#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**update_custom_field**](docs/MediaLibraryApi#update_custom_field) | **PUT** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**update_external_transcoder**](docs/MediaLibraryApi#update_external_transcoder) | **PUT** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**update_marker**](docs/MediaLibraryApi#update_marker) | **PUT** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**update_media_file**](docs/MediaLibraryApi#update_media_file) | **PUT** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**update_media_file_template**](docs/MediaLibraryApi#update_media_file_template) | **PUT** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**update_media_root**](docs/MediaLibraryApi#update_media_root) | **PUT** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**update_media_root_permission**](docs/MediaLibraryApi#update_media_root_permission) | **PUT** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**update_media_tag**](docs/MediaLibraryApi#update_media_tag) | **PUT** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**update_proxy_profile**](docs/MediaLibraryApi#update_proxy_profile) | **PUT** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**update_subclip**](docs/MediaLibraryApi#update_subclip) | **PUT** `/api/2/media/subclips/{id}` | 
*StatusApi* | [**get_alert**](docs/StatusApi#get_alert) | **GET** `/api/2/alerts/{id}` | 
*StatusApi* | [**get_all_alerts**](docs/StatusApi#get_all_alerts) | **GET** `/api/2/alerts` | 
*StatusApi* | [**get_telegraf_stats**](docs/StatusApi#get_telegraf_stats) | **GET** `/api/2/telegraf-stats` | 
*StatusApi* | [**patch_alert**](docs/StatusApi#patch_alert) | **PATCH** `/api/2/alerts/{id}` | 
*StatusApi* | [**submit_kapacitor_alert**](docs/StatusApi#submit_kapacitor_alert) | **POST** `/api/2/alerts/submit` | 
*StatusApi* | [**update_alert**](docs/StatusApi#update_alert) | **PUT** `/api/2/alerts/{id}` | 
*StorageApi* | [**apply_workspace_affinity**](docs/StorageApi#apply_workspace_affinity) | **POST** `/api/2/workspaces/{id}/apply-affinity` | 
*StorageApi* | [**bookmark_workspace**](docs/StorageApi#bookmark_workspace) | **POST** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**calculate_directory_size**](docs/StorageApi#calculate_directory_size) | **POST** `/api/2/filesystem/calculate-directory-size` | 
*StorageApi* | [**check_in_into_workspace**](docs/StorageApi#check_in_into_workspace) | **POST** `/api/2/workspaces/{id}/check-in` | 
*StorageApi* | [**check_out_of_workspace**](docs/StorageApi#check_out_of_workspace) | **POST** `/api/2/workspaces/{id}/check-out` | 
*StorageApi* | [**copy_files**](docs/StorageApi#copy_files) | **POST** `/api/2/filesystem/copy` | 
*StorageApi* | [**create_file**](docs/StorageApi#create_file) | **POST** `/api/2/files` | 
*StorageApi* | [**create_path_quota**](docs/StorageApi#create_path_quota) | **POST** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**create_production**](docs/StorageApi#create_production) | **POST** `/api/2/productions` | 
*StorageApi* | [**create_share**](docs/StorageApi#create_share) | **POST** `/api/2/shares` | 
*StorageApi* | [**create_snapshot**](docs/StorageApi#create_snapshot) | **POST** `/api/2/snapshots` | 
*StorageApi* | [**create_workspace**](docs/StorageApi#create_workspace) | **POST** `/api/2/workspaces` | 
*StorageApi* | [**create_workspace_permission**](docs/StorageApi#create_workspace_permission) | **POST** `/api/2/workspace-permissions` | 
*StorageApi* | [**delete_file**](docs/StorageApi#delete_file) | **DELETE** `/api/2/files/{path}` | 
*StorageApi* | [**delete_files**](docs/StorageApi#delete_files) | **POST** `/api/2/filesystem/delete` | 
*StorageApi* | [**delete_path_quota**](docs/StorageApi#delete_path_quota) | **DELETE** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**delete_production**](docs/StorageApi#delete_production) | **DELETE** `/api/2/productions/{id}` | 
*StorageApi* | [**delete_share**](docs/StorageApi#delete_share) | **DELETE** `/api/2/shares/{id}` | 
*StorageApi* | [**delete_snapshot**](docs/StorageApi#delete_snapshot) | **DELETE** `/api/2/snapshots/{id}` | 
*StorageApi* | [**delete_workspace**](docs/StorageApi#delete_workspace) | **DELETE** `/api/2/workspaces/{id}` | 
*StorageApi* | [**delete_workspace_permission**](docs/StorageApi#delete_workspace_permission) | **DELETE** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**get_all_deleted_workspaces**](docs/StorageApi#get_all_deleted_workspaces) | **GET** `/api/2/workspaces/deleted` | 
*StorageApi* | [**get_all_productions**](docs/StorageApi#get_all_productions) | **GET** `/api/2/productions` | 
*StorageApi* | [**get_all_shares**](docs/StorageApi#get_all_shares) | **GET** `/api/2/shares` | 
*StorageApi* | [**get_all_snapshots**](docs/StorageApi#get_all_snapshots) | **GET** `/api/2/snapshots` | 
*StorageApi* | [**get_all_volumes**](docs/StorageApi#get_all_volumes) | **GET** `/api/2/volumes` | 
*StorageApi* | [**get_all_workspace_permissions**](docs/StorageApi#get_all_workspace_permissions) | **GET** `/api/2/workspace-permissions` | 
*StorageApi* | [**get_all_workspaces**](docs/StorageApi#get_all_workspaces) | **GET** `/api/2/workspaces` | 
*StorageApi* | [**get_file**](docs/StorageApi#get_file) | **GET** `/api/2/files/{path}` | 
*StorageApi* | [**get_group_quota**](docs/StorageApi#get_group_quota) | **GET** `/api/2/volumes/{id}/quotas/group/{group_id}` | 
*StorageApi* | [**get_my_workspaces**](docs/StorageApi#get_my_workspaces) | **GET** `/api/2/workspaces/mine` | 
*StorageApi* | [**get_path_quota**](docs/StorageApi#get_path_quota) | **GET** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**get_production**](docs/StorageApi#get_production) | **GET** `/api/2/productions/{id}` | 
*StorageApi* | [**get_root_directory**](docs/StorageApi#get_root_directory) | **GET** `/api/2/files` | 
*StorageApi* | [**get_share**](docs/StorageApi#get_share) | **GET** `/api/2/shares/{id}` | 
*StorageApi* | [**get_snapshot**](docs/StorageApi#get_snapshot) | **GET** `/api/2/snapshots/{id}` | 
*StorageApi* | [**get_user_quota**](docs/StorageApi#get_user_quota) | **GET** `/api/2/volumes/{id}/quotas/user/{user_id}` | 
*StorageApi* | [**get_volume**](docs/StorageApi#get_volume) | **GET** `/api/2/volumes/{id}` | 
*StorageApi* | [**get_volume_active_connections**](docs/StorageApi#get_volume_active_connections) | **GET** `/api/2/volumes/{id}/connections` | 
*StorageApi* | [**get_volume_file_size_distribution**](docs/StorageApi#get_volume_file_size_distribution) | **GET** `/api/2/volumes/{id}/file-size-distribution` | 
*StorageApi* | [**get_volume_stats**](docs/StorageApi#get_volume_stats) | **GET** `/api/2/volumes/{id}/stats` | 
*StorageApi* | [**get_workspace**](docs/StorageApi#get_workspace) | **GET** `/api/2/workspaces/{id}` | 
*StorageApi* | [**get_workspace_permission**](docs/StorageApi#get_workspace_permission) | **GET** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**move_files**](docs/StorageApi#move_files) | **POST** `/api/2/filesystem/move` | 
*StorageApi* | [**move_workspace**](docs/StorageApi#move_workspace) | **POST** `/api/2/workspaces/{id}/move` | 
*StorageApi* | [**move_workspace_to_production**](docs/StorageApi#move_workspace_to_production) | **POST** `/api/2/workspaces/{id}/move-to` | 
*StorageApi* | [**patch_file**](docs/StorageApi#patch_file) | **PATCH** `/api/2/files/{path}` | 
*StorageApi* | [**patch_production**](docs/StorageApi#patch_production) | **PATCH** `/api/2/productions/{id}` | 
*StorageApi* | [**patch_share**](docs/StorageApi#patch_share) | **PATCH** `/api/2/shares/{id}` | 
*StorageApi* | [**patch_snapshot**](docs/StorageApi#patch_snapshot) | **PATCH** `/api/2/snapshots/{id}` | 
*StorageApi* | [**patch_volume**](docs/StorageApi#patch_volume) | **PATCH** `/api/2/volumes/{id}` | 
*StorageApi* | [**patch_workspace**](docs/StorageApi#patch_workspace) | **PATCH** `/api/2/workspaces/{id}` | 
*StorageApi* | [**patch_workspace_permission**](docs/StorageApi#patch_workspace_permission) | **PATCH** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**repair_workspace_permissions**](docs/StorageApi#repair_workspace_permissions) | **POST** `/api/2/workspaces/{id}/repair-permissions` | 
*StorageApi* | [**unbookmark_workspace**](docs/StorageApi#unbookmark_workspace) | **DELETE** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**unzip_file**](docs/StorageApi#unzip_file) | **POST** `/api/2/filesystem/unzip` | 
*StorageApi* | [**update_group_quota**](docs/StorageApi#update_group_quota) | **PUT** `/api/2/volumes/{id}/quotas/group/{group_id}` | 
*StorageApi* | [**update_path_quota**](docs/StorageApi#update_path_quota) | **PUT** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**update_production**](docs/StorageApi#update_production) | **PUT** `/api/2/productions/{id}` | 
*StorageApi* | [**update_share**](docs/StorageApi#update_share) | **PUT** `/api/2/shares/{id}` | 
*StorageApi* | [**update_snapshot**](docs/StorageApi#update_snapshot) | **PUT** `/api/2/snapshots/{id}` | 
*StorageApi* | [**update_user_quota**](docs/StorageApi#update_user_quota) | **PUT** `/api/2/volumes/{id}/quotas/user/{user_id}` | 
*StorageApi* | [**update_volume**](docs/StorageApi#update_volume) | **PUT** `/api/2/volumes/{id}` | 
*StorageApi* | [**update_workspace**](docs/StorageApi#update_workspace) | **PUT** `/api/2/workspaces/{id}` | 
*StorageApi* | [**update_workspace_permission**](docs/StorageApi#update_workspace_permission) | **PUT** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**zip_files**](docs/StorageApi#zip_files) | **POST** `/api/2/filesystem/zip` | 
*TapeArchiveApi* | [**create_tape**](docs/TapeArchiveApi#create_tape) | **POST** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**create_tape_group**](docs/TapeArchiveApi#create_tape_group) | **POST** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**delete_tape**](docs/TapeArchiveApi#delete_tape) | **DELETE** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**delete_tape_group**](docs/TapeArchiveApi#delete_tape_group) | **DELETE** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**get_all_archived_file_entries**](docs/TapeArchiveApi#get_all_archived_file_entries) | **GET** `/api/2/archive/tape/files` | 
*TapeArchiveApi* | [**get_all_tape_groups**](docs/TapeArchiveApi#get_all_tape_groups) | **GET** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**get_all_tapes**](docs/TapeArchiveApi#get_all_tapes) | **GET** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**get_archived_file_entry**](docs/TapeArchiveApi#get_archived_file_entry) | **GET** `/api/2/archive/tape/files/{id}` | 
*TapeArchiveApi* | [**get_tape**](docs/TapeArchiveApi#get_tape) | **GET** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**get_tape_group**](docs/TapeArchiveApi#get_tape_group) | **GET** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**patch_tape**](docs/TapeArchiveApi#patch_tape) | **PATCH** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**patch_tape_group**](docs/TapeArchiveApi#patch_tape_group) | **PATCH** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**update_tape**](docs/TapeArchiveApi#update_tape) | **PUT** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**update_tape_group**](docs/TapeArchiveApi#update_tape_group) | **PUT** `/api/2/archive/tape/groups/{id}` | 


## Models

 - [AWSAccount](docs/AWSAccount)
 - [AWSAccountPartialUpdate](docs/AWSAccountPartialUpdate)
 - [Address](docs/Address)
 - [Alert](docs/Alert)
 - [AlertPartialUpdate](docs/AlertPartialUpdate)
 - [AllMediaFilesForBundlesRequest](docs/AllMediaFilesForBundlesRequest)
 - [ArgumentType](docs/ArgumentType)
 - [Asset](docs/Asset)
 - [AssetBackup](docs/AssetBackup)
 - [AssetCloudLink](docs/AssetCloudLink)
 - [AssetMini](docs/AssetMini)
 - [AssetPartialUpdate](docs/AssetPartialUpdate)
 - [AssetProjectLink](docs/AssetProjectLink)
 - [AssetRating](docs/AssetRating)
 - [AssetRatingPartialUpdate](docs/AssetRatingPartialUpdate)
 - [AuthLoginEndpointRequest](docs/AuthLoginEndpointRequest)
 - [AuthLoginEndpointResponse](docs/AuthLoginEndpointResponse)
 - [Backend](docs/Backend)
 - [BackendProperties](docs/BackendProperties)
 - [BasicFile](docs/BasicFile)
 - [BeeGFSNode](docs/BeeGFSNode)
 - [BeeGFSTarget](docs/BeeGFSTarget)
 - [CPUStat](docs/CPUStat)
 - [ChangeOwnPasswordRequest](docs/ChangeOwnPasswordRequest)
 - [ChangePasswordRequest](docs/ChangePasswordRequest)
 - [CheckConnectivityEndpointResponse](docs/CheckConnectivityEndpointResponse)
 - [ClientSession](docs/ClientSession)
 - [ClientsEndpointResponse](docs/ClientsEndpointResponse)
 - [CloudConnection](docs/CloudConnection)
 - [Comment](docs/Comment)
 - [CommentPartialUpdate](docs/CommentPartialUpdate)
 - [CreateDownloadArchive](docs/CreateDownloadArchive)
 - [CreateHomeWorkspaceRequest](docs/CreateHomeWorkspaceRequest)
 - [CreatePathQuotaRequest](docs/CreatePathQuotaRequest)
 - [CustomField](docs/CustomField)
 - [CustomFieldPartialUpdate](docs/CustomFieldPartialUpdate)
 - [DeletedWorkspace](docs/DeletedWorkspace)
 - [Download](docs/Download)
 - [DownloadArchive](docs/DownloadArchive)
 - [DownloadArchivePartialUpdate](docs/DownloadArchivePartialUpdate)
 - [ElementsGroup](docs/ElementsGroup)
 - [ElementsGroupDetail](docs/ElementsGroupDetail)
 - [ElementsGroupDetailPartialUpdate](docs/ElementsGroupDetailPartialUpdate)
 - [ElementsUser](docs/ElementsUser)
 - [ElementsUserDetail](docs/ElementsUserDetail)
 - [ElementsUserDetailPartialUpdate](docs/ElementsUserDetailPartialUpdate)
 - [ElementsUserMini](docs/ElementsUserMini)
 - [ElementsUserProfile](docs/ElementsUserProfile)
 - [ElementsUserProfilePartialUpdate](docs/ElementsUserProfilePartialUpdate)
 - [ElementsVersion](docs/ElementsVersion)
 - [EmailPreview](docs/EmailPreview)
 - [EnableTOTPRequest](docs/EnableTOTPRequest)
 - [Event](docs/Event)
 - [ExternalTranscoder](docs/ExternalTranscoder)
 - [ExternalTranscoderPartialUpdate](docs/ExternalTranscoderPartialUpdate)
 - [FSProperties](docs/FSProperties)
 - [File](docs/File)
 - [FileCopyEndpointRequest](docs/FileCopyEndpointRequest)
 - [FileDeleteEndpointRequest](docs/FileDeleteEndpointRequest)
 - [FileMoveEndpointRequest](docs/FileMoveEndpointRequest)
 - [FilePartialUpdate](docs/FilePartialUpdate)
 - [FileSizeDistribution](docs/FileSizeDistribution)
 - [FileSizeDistributionItem](docs/FileSizeDistributionItem)
 - [FileSizeEndpointResponse](docs/FileSizeEndpointResponse)
 - [FileUnzipEndpointRequest](docs/FileUnzipEndpointRequest)
 - [FileZipEndpointRequest](docs/FileZipEndpointRequest)
 - [FinishUploadEndpointRequest](docs/FinishUploadEndpointRequest)
 - [GeneratePasswordEndpointResponse](docs/GeneratePasswordEndpointResponse)
 - [GenerateProxiesRequest](docs/GenerateProxiesRequest)
 - [GetMultipleBundlesRequest](docs/GetMultipleBundlesRequest)
 - [GetMultipleFilesRequest](docs/GetMultipleFilesRequest)
 - [GlobalAlert](docs/GlobalAlert)
 - [IOStat](docs/IOStat)
 - [ImpersonationEndpointRequest](docs/ImpersonationEndpointRequest)
 - [InlineResponse200](docs/InlineResponse200)
 - [InlineResponse2001](docs/InlineResponse2001)
 - [InlineResponse2002](docs/InlineResponse2002)
 - [Interface](docs/Interface)
 - [Ipmi](docs/Ipmi)
 - [Job](docs/Job)
 - [JobPartialUpdate](docs/JobPartialUpdate)
 - [KapacitorAlert](docs/KapacitorAlert)
 - [LDAPServer](docs/LDAPServer)
 - [LDAPServerGroup](docs/LDAPServerGroup)
 - [LDAPServerGroups](docs/LDAPServerGroups)
 - [LDAPServerUser](docs/LDAPServerUser)
 - [LDAPServerUsers](docs/LDAPServerUsers)
 - [License](docs/License)
 - [ListBuckets](docs/ListBuckets)
 - [ListTopics](docs/ListTopics)
 - [LizardFSDisk](docs/LizardFSDisk)
 - [LizardFSNode](docs/LizardFSNode)
 - [Marker](docs/Marker)
 - [MarkerPartialUpdate](docs/MarkerPartialUpdate)
 - [MediaFile](docs/MediaFile)
 - [MediaFileBundle](docs/MediaFileBundle)
 - [MediaFileBundleMini](docs/MediaFileBundleMini)
 - [MediaFileContents](docs/MediaFileContents)
 - [MediaFileMini](docs/MediaFileMini)
 - [MediaFilePartialUpdate](docs/MediaFilePartialUpdate)
 - [MediaFileTemplate](docs/MediaFileTemplate)
 - [MediaFileTemplatePartialUpdate](docs/MediaFileTemplatePartialUpdate)
 - [MediaLibraryDeleteRequest](docs/MediaLibraryDeleteRequest)
 - [MediaLibraryShareRequest](docs/MediaLibraryShareRequest)
 - [MediaRoot](docs/MediaRoot)
 - [MediaRootMini](docs/MediaRootMini)
 - [MediaRootPartialUpdate](docs/MediaRootPartialUpdate)
 - [MediaRootPermission](docs/MediaRootPermission)
 - [MediaRootPermissionAccessOptions](docs/MediaRootPermissionAccessOptions)
 - [MediaRootPermissionPartialUpdate](docs/MediaRootPermissionPartialUpdate)
 - [MediaUpdate](docs/MediaUpdate)
 - [MemberPreview](docs/MemberPreview)
 - [MoveWorkspaceRequest](docs/MoveWorkspaceRequest)
 - [MultipleAssetsRequest](docs/MultipleAssetsRequest)
 - [NTPServer](docs/NTPServer)
 - [NTPServerPartialUpdate](docs/NTPServerPartialUpdate)
 - [NetStat](docs/NetStat)
 - [OneTimeAccessToken](docs/OneTimeAccessToken)
 - [OneTimeAccessTokenActivity](docs/OneTimeAccessTokenActivity)
 - [OneTimeAccessTokenSharedObject](docs/OneTimeAccessTokenSharedObject)
 - [Parameters](docs/Parameters)
 - [PasswordResetEndpointRequest](docs/PasswordResetEndpointRequest)
 - [Path](docs/Path)
 - [PathInput](docs/PathInput)
 - [Production](docs/Production)
 - [ProductionPartialUpdate](docs/ProductionPartialUpdate)
 - [Proxy](docs/Proxy)
 - [ProxyCount](docs/ProxyCount)
 - [ProxyGenerator](docs/ProxyGenerator)
 - [ProxyGeneratorProperties](docs/ProxyGeneratorProperties)
 - [ProxyProfile](docs/ProxyProfile)
 - [ProxyProfileMini](docs/ProxyProfileMini)
 - [ProxyProfilePartialUpdate](docs/ProxyProfilePartialUpdate)
 - [PythonEnvironment](docs/PythonEnvironment)
 - [Queue](docs/Queue)
 - [Quota](docs/Quota)
 - [RAMStat](docs/RAMStat)
 - [RegisterUploadEndpointRequest](docs/RegisterUploadEndpointRequest)
 - [ReleaseNotesEndpointResponse](docs/ReleaseNotesEndpointResponse)
 - [RenameCustomFieldRequest](docs/RenameCustomFieldRequest)
 - [RenderRequest](docs/RenderRequest)
 - [SAMLProviderMini](docs/SAMLProviderMini)
 - [SMTPConfiguration](docs/SMTPConfiguration)
 - [SNFSStripeGroup](docs/SNFSStripeGroup)
 - [ScannerDiscoverEndpointRequest](docs/ScannerDiscoverEndpointRequest)
 - [ScannerScanEndpointRequest](docs/ScannerScanEndpointRequest)
 - [Schedule](docs/Schedule)
 - [SchedulePartialUpdate](docs/SchedulePartialUpdate)
 - [SendLinkEmailRequest](docs/SendLinkEmailRequest)
 - [Sensor](docs/Sensor)
 - [Sensors](docs/Sensors)
 - [ServiceStatus](docs/ServiceStatus)
 - [Share](docs/Share)
 - [SharePartialUpdate](docs/SharePartialUpdate)
 - [SlackChannel](docs/SlackChannel)
 - [SlackConnection](docs/SlackConnection)
 - [SlackConnectionPartialUpdate](docs/SlackConnectionPartialUpdate)
 - [SlackConnectionStatus](docs/SlackConnectionStatus)
 - [SlackEmoji](docs/SlackEmoji)
 - [SlackMessage](docs/SlackMessage)
 - [SlackUser](docs/SlackUser)
 - [Snapshot](docs/Snapshot)
 - [SnapshotPartialUpdate](docs/SnapshotPartialUpdate)
 - [SolrReindexEndpointResponse](docs/SolrReindexEndpointResponse)
 - [StartJobRequest](docs/StartJobRequest)
 - [StartTaskRequest](docs/StartTaskRequest)
 - [Stats](docs/Stats)
 - [StorNextConnection](docs/StorNextConnection)
 - [StorNextConnections](docs/StorNextConnections)
 - [StorNextLicenseCheckEndpointResponse](docs/StorNextLicenseCheckEndpointResponse)
 - [StorNextLicenseEndpointResponse](docs/StorNextLicenseEndpointResponse)
 - [StorageNode](docs/StorageNode)
 - [StorageNodeMini](docs/StorageNodeMini)
 - [StorageNodeStatus](docs/StorageNodeStatus)
 - [StornextLicense](docs/StornextLicense)
 - [StornextManagerAttributes](docs/StornextManagerAttributes)
 - [Subclip](docs/Subclip)
 - [SubclipClipboardEntry](docs/SubclipClipboardEntry)
 - [SubclipPartialUpdate](docs/SubclipPartialUpdate)
 - [Subtask](docs/Subtask)
 - [SubtaskPartialUpdate](docs/SubtaskPartialUpdate)
 - [SyncTOTP](docs/SyncTOTP)
 - [SyncTOTPRequest](docs/SyncTOTPRequest)
 - [SystemInfoEndpointResponse](docs/SystemInfoEndpointResponse)
 - [Tag](docs/Tag)
 - [TagPartialUpdate](docs/TagPartialUpdate)
 - [Tape](docs/Tape)
 - [TapeFile](docs/TapeFile)
 - [TapeGroup](docs/TapeGroup)
 - [TapeGroupPartialUpdate](docs/TapeGroupPartialUpdate)
 - [TapePartialUpdate](docs/TapePartialUpdate)
 - [TaskInfo](docs/TaskInfo)
 - [TaskLog](docs/TaskLog)
 - [TaskProgress](docs/TaskProgress)
 - [TaskType](docs/TaskType)
 - [TasksSummary](docs/TasksSummary)
 - [TeamsConnection](docs/TeamsConnection)
 - [TeamsConnectionPartialUpdate](docs/TeamsConnectionPartialUpdate)
 - [TeamsConnectionStatus](docs/TeamsConnectionStatus)
 - [TeamsMessage](docs/TeamsMessage)
 - [TeamsRecipient](docs/TeamsRecipient)
 - [TestAWSCredentialsRequest](docs/TestAWSCredentialsRequest)
 - [TestAWSCredentialsResponse](docs/TestAWSCredentialsResponse)
 - [TestExternalTranscoderConnectionRequest](docs/TestExternalTranscoderConnectionRequest)
 - [TestExternalTranscoderConnectionResponse](docs/TestExternalTranscoderConnectionResponse)
 - [TestSMTP](docs/TestSMTP)
 - [Ticket](docs/Ticket)
 - [TimeEndpointRequest](docs/TimeEndpointRequest)
 - [TimeEndpointResponse](docs/TimeEndpointResponse)
 - [TimeSyncEndpointRequest](docs/TimeSyncEndpointRequest)
 - [TimeSyncEndpointResponse](docs/TimeSyncEndpointResponse)
 - [Timezone](docs/Timezone)
 - [TranscoderProfile](docs/TranscoderProfile)
 - [TypeDocumentation](docs/TypeDocumentation)
 - [UpdateQuotaRequest](docs/UpdateQuotaRequest)
 - [UploadChunkEndpointRequest](docs/UploadChunkEndpointRequest)
 - [UserPreviewRequest](docs/UserPreviewRequest)
 - [UserPreviewResponse](docs/UserPreviewResponse)
 - [VantageWorkflow](docs/VantageWorkflow)
 - [VantageWorkflows](docs/VantageWorkflows)
 - [Volume](docs/Volume)
 - [VolumeBeeGFSStatus](docs/VolumeBeeGFSStatus)
 - [VolumeLizardFSStatus](docs/VolumeLizardFSStatus)
 - [VolumeMini](docs/VolumeMini)
 - [VolumePartialUpdate](docs/VolumePartialUpdate)
 - [VolumeSNFSStatus](docs/VolumeSNFSStatus)
 - [VolumeStat](docs/VolumeStat)
 - [VolumeStats](docs/VolumeStats)
 - [VolumeStatus](docs/VolumeStatus)
 - [WorkflowTransitionRequest](docs/WorkflowTransitionRequest)
 - [WorkflowTransitionResponse](docs/WorkflowTransitionResponse)
 - [Workspace](docs/Workspace)
 - [WorkspaceCheckIn](docs/WorkspaceCheckIn)
 - [WorkspaceEndpoint](docs/WorkspaceEndpoint)
 - [WorkspaceMoveToRequest](docs/WorkspaceMoveToRequest)
 - [WorkspacePartialUpdate](docs/WorkspacePartialUpdate)
 - [WorkspacePermission](docs/WorkspacePermission)
 - [WorkspacePermissionPartialUpdate](docs/WorkspacePermissionPartialUpdate)
 - [WorkspaceResolvedPermission](docs/WorkspaceResolvedPermission)
 - [Workstation](docs/Workstation)
 - [WorkstationPartialUpdate](docs/WorkstationPartialUpdate)


