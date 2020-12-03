# ELEMENTS Python SDK

- API version: 2
- Python 2.7 and 3.4+
- Latest build: 3.0.3

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
*AIApi* | [**abort_ai_dataset_model_creation**](docs/AIApi#abort_ai_dataset_model_creation) | **POST** `/api/2/ai/models/{id}/abort` | 
*AIApi* | [**create_ai_annotation_track**](docs/AIApi#create_ai_annotation_track) | **POST** `/api/2/ai/annotations/tracks/create` | 
*AIApi* | [**create_ai_category**](docs/AIApi#create_ai_category) | **POST** `/api/2/ai/categories` | 
*AIApi* | [**create_ai_dataset**](docs/AIApi#create_ai_dataset) | **POST** `/api/2/ai/datasets` | 
*AIApi* | [**create_ai_dataset_model**](docs/AIApi#create_ai_dataset_model) | **POST** `/api/2/ai/models/create` | 
*AIApi* | [**create_ai_metadata**](docs/AIApi#create_ai_metadata) | **POST** `/api/2/ai/metadata/create` | 
*AIApi* | [**create_ai_model**](docs/AIApi#create_ai_model) | **POST** `/api/2/ai/models` | 
*AIApi* | [**delete_ai_annotation**](docs/AIApi#delete_ai_annotation) | **DELETE** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**delete_ai_annotation_track**](docs/AIApi#delete_ai_annotation_track) | **DELETE** `/api/2/ai/annotations/tracks/{id}` | 
*AIApi* | [**delete_ai_category**](docs/AIApi#delete_ai_category) | **DELETE** `/api/2/ai/categories/{id}` | 
*AIApi* | [**delete_ai_dataset**](docs/AIApi#delete_ai_dataset) | **DELETE** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**delete_ai_model**](docs/AIApi#delete_ai_model) | **DELETE** `/api/2/ai/models/{id}` | 
*AIApi* | [**get_ai_annotation**](docs/AIApi#get_ai_annotation) | **GET** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**get_ai_annotation_image**](docs/AIApi#get_ai_annotation_image) | **GET** `/api/2/ai/annotations/{id}/image` | 
*AIApi* | [**get_ai_category**](docs/AIApi#get_ai_category) | **GET** `/api/2/ai/categories/{id}` | 
*AIApi* | [**get_ai_connection**](docs/AIApi#get_ai_connection) | **GET** `/api/2/ai/connections/{id}` | 
*AIApi* | [**get_ai_dataset**](docs/AIApi#get_ai_dataset) | **GET** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**get_ai_dataset_model_stats**](docs/AIApi#get_ai_dataset_model_stats) | **GET** `/api/2/ai/models/{id}/stats` | 
*AIApi* | [**get_ai_image**](docs/AIApi#get_ai_image) | **GET** `/api/2/ai/images/{id}` | 
*AIApi* | [**get_ai_image_content**](docs/AIApi#get_ai_image_content) | **GET** `/api/2/ai/images/{id}/content` | 
*AIApi* | [**get_ai_metadata**](docs/AIApi#get_ai_metadata) | **GET** `/api/2/ai/metadata/{id}` | 
*AIApi* | [**get_ai_model**](docs/AIApi#get_ai_model) | **GET** `/api/2/ai/models/{id}` | 
*AIApi* | [**get_all_ai_annotation_tracks**](docs/AIApi#get_all_ai_annotation_tracks) | **GET** `/api/2/ai/annotations/tracks` | 
*AIApi* | [**get_all_ai_annotations**](docs/AIApi#get_all_ai_annotations) | **GET** `/api/2/ai/annotations` | 
*AIApi* | [**get_all_ai_categories**](docs/AIApi#get_all_ai_categories) | **GET** `/api/2/ai/categories` | 
*AIApi* | [**get_all_ai_connections**](docs/AIApi#get_all_ai_connections) | **GET** `/api/2/ai/connections` | 
*AIApi* | [**get_all_ai_datasets**](docs/AIApi#get_all_ai_datasets) | **GET** `/api/2/ai/datasets` | 
*AIApi* | [**get_all_ai_images**](docs/AIApi#get_all_ai_images) | **GET** `/api/2/ai/images` | 
*AIApi* | [**get_all_ai_metadata**](docs/AIApi#get_all_ai_metadata) | **GET** `/api/2/ai/metadata` | 
*AIApi* | [**get_all_ai_models**](docs/AIApi#get_all_ai_models) | **GET** `/api/2/ai/models` | 
*AIApi* | [**patch_ai_category**](docs/AIApi#patch_ai_category) | **PATCH** `/api/2/ai/categories/{id}` | 
*AIApi* | [**patch_ai_dataset**](docs/AIApi#patch_ai_dataset) | **PATCH** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**patch_ai_model**](docs/AIApi#patch_ai_model) | **PATCH** `/api/2/ai/models/{id}` | 
*AIApi* | [**update_ai_category**](docs/AIApi#update_ai_category) | **PUT** `/api/2/ai/categories/{id}` | 
*AIApi* | [**update_ai_dataset**](docs/AIApi#update_ai_dataset) | **PUT** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**update_ai_model**](docs/AIApi#update_ai_model) | **PUT** `/api/2/ai/models/{id}` | 
*AuthApi* | [**check_auth_ticket**](docs/AuthApi#check_auth_ticket) | **POST** `/api/2/auth/ticket/check` | 
*AuthApi* | [**create_auth_ticket**](docs/AuthApi#create_auth_ticket) | **POST** `/api/2/auth/ticket` | 
*AuthApi* | [**delete_one_time_access_token**](docs/AuthApi#delete_one_time_access_token) | **DELETE** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**generate_password**](docs/AuthApi#generate_password) | **POST** `/api/2/auth/generate-password` | 
*AuthApi* | [**get_all_one_time_access_tokens**](docs/AuthApi#get_all_one_time_access_tokens) | **GET** `/api/2/auth/access-tokens` | 
*AuthApi* | [**get_one_time_access_token**](docs/AuthApi#get_one_time_access_token) | **GET** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**login**](docs/AuthApi#login) | **POST** `/api/2/auth/login` | 
*AuthApi* | [**logout**](docs/AuthApi#logout) | **POST** `/api/2/auth/logout` | 
*AutomationApi* | [**abort_task**](docs/AutomationApi#abort_task) | **POST** `/api/2/tasks/{id}/abort` | 
*AutomationApi* | [**create_job**](docs/AutomationApi#create_job) | **POST** `/api/2/jobs` | 
*AutomationApi* | [**create_schedule**](docs/AutomationApi#create_schedule) | **POST** `/api/2/schedules` | 
*AutomationApi* | [**create_subtask**](docs/AutomationApi#create_subtask) | **POST** `/api/2/subtasks` | 
*AutomationApi* | [**delete_job**](docs/AutomationApi#delete_job) | **DELETE** `/api/2/jobs/{id}` | 
*AutomationApi* | [**delete_schedule**](docs/AutomationApi#delete_schedule) | **DELETE** `/api/2/schedules/{id}` | 
*AutomationApi* | [**delete_subtask**](docs/AutomationApi#delete_subtask) | **DELETE** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**delete_task**](docs/AutomationApi#delete_task) | **DELETE** `/api/2/tasks/{id}` | 
*AutomationApi* | [**download_all_task_logs**](docs/AutomationApi#download_all_task_logs) | **GET** `/api/2/tasks/logs/download` | 
*AutomationApi* | [**download_task_log**](docs/AutomationApi#download_task_log) | **GET** `/api/2/tasks/{id}/log/download` | 
*AutomationApi* | [**get_all_jobs**](docs/AutomationApi#get_all_jobs) | **GET** `/api/2/jobs` | 
*AutomationApi* | [**get_all_schedules**](docs/AutomationApi#get_all_schedules) | **GET** `/api/2/schedules` | 
*AutomationApi* | [**get_all_subtasks**](docs/AutomationApi#get_all_subtasks) | **GET** `/api/2/subtasks` | 
*AutomationApi* | [**get_all_tasks**](docs/AutomationApi#get_all_tasks) | **GET** `/api/2/tasks` | 
*AutomationApi* | [**get_finished_tasks**](docs/AutomationApi#get_finished_tasks) | **GET** `/api/2/tasks/finished` | 
*AutomationApi* | [**get_job**](docs/AutomationApi#get_job) | **GET** `/api/2/jobs/{id}` | 
*AutomationApi* | [**get_pending_tasks**](docs/AutomationApi#get_pending_tasks) | **GET** `/api/2/tasks/pending` | 
*AutomationApi* | [**get_schedule**](docs/AutomationApi#get_schedule) | **GET** `/api/2/schedules/{id}` | 
*AutomationApi* | [**get_subtask**](docs/AutomationApi#get_subtask) | **GET** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**get_task**](docs/AutomationApi#get_task) | **GET** `/api/2/tasks/{id}` | 
*AutomationApi* | [**get_task_log**](docs/AutomationApi#get_task_log) | **GET** `/api/2/tasks/{id}/log` | 
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
*MainApi* | [**apply_configuration**](docs/MainApi#apply_configuration) | **POST** `/api/2/configuration/apply` | 
*MainApi* | [**check_chunk_uploaded**](docs/MainApi#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
*MainApi* | [**check_stor_next_license**](docs/MainApi#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
*MainApi* | [**create_group**](docs/MainApi#create_group) | **POST** `/api/2/groups` | 
*MainApi* | [**create_home_workspace**](docs/MainApi#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
*MainApi* | [**create_user**](docs/MainApi#create_user) | **POST** `/api/2/users` | 
*MainApi* | [**create_workstation**](docs/MainApi#create_workstation) | **POST** `/api/2/workstations` | 
*MainApi* | [**delete_group**](docs/MainApi#delete_group) | **DELETE** `/api/2/groups/{id}` | 
*MainApi* | [**delete_home_workspace**](docs/MainApi#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
*MainApi* | [**delete_user**](docs/MainApi#delete_user) | **DELETE** `/api/2/users/{id}` | 
*MainApi* | [**delete_workstation**](docs/MainApi#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
*MainApi* | [**disable_user_totp**](docs/MainApi#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
*MainApi* | [**enable_user_totp**](docs/MainApi#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
*MainApi* | [**finish_upload**](docs/MainApi#finish_upload) | **POST** `/api/2/uploads/finish` | 
*MainApi* | [**fix_ldap_group_memberships**](docs/MainApi#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
*MainApi* | [**get_all_downloads**](docs/MainApi#get_all_downloads) | **GET** `/api/2/downloads` | 
*MainApi* | [**get_all_groups**](docs/MainApi#get_all_groups) | **GET** `/api/2/groups` | 
*MainApi* | [**get_all_ldap_servers**](docs/MainApi#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
*MainApi* | [**get_all_storage_nodes**](docs/MainApi#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
*MainApi* | [**get_all_users**](docs/MainApi#get_all_users) | **GET** `/api/2/users` | 
*MainApi* | [**get_all_workstations**](docs/MainApi#get_all_workstations) | **GET** `/api/2/workstations` | 
*MainApi* | [**get_client_download_file**](docs/MainApi#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
*MainApi* | [**get_client_downloads**](docs/MainApi#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
*MainApi* | [**get_current_workstation**](docs/MainApi#get_current_workstation) | **GET** `/api/2/workstations/current` | 
*MainApi* | [**get_download**](docs/MainApi#get_download) | **GET** `/api/2/downloads/{id}` | 
*MainApi* | [**get_download_file**](docs/MainApi#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
*MainApi* | [**get_download_icon**](docs/MainApi#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
*MainApi* | [**get_group**](docs/MainApi#get_group) | **GET** `/api/2/groups/{id}` | 
*MainApi* | [**get_home_workspace**](docs/MainApi#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
*MainApi* | [**get_ldap_server**](docs/MainApi#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
*MainApi* | [**get_ldap_server_groups**](docs/MainApi#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
*MainApi* | [**get_ldap_server_users**](docs/MainApi#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
*MainApi* | [**get_license**](docs/MainApi#get_license) | **GET** `/api/2/license` | 
*MainApi* | [**get_node_ipmi_sensors**](docs/MainApi#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
*MainApi* | [**get_node_stats**](docs/MainApi#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
*MainApi* | [**get_parameters**](docs/MainApi#get_parameters) | **GET** `/api/2/parameters` | 
*MainApi* | [**get_profile**](docs/MainApi#get_profile) | **GET** `/api/2/users/me` | 
*MainApi* | [**get_release_notes**](docs/MainApi#get_release_notes) | **GET** `/api/2/release-notes` | 
*MainApi* | [**get_stor_next_license**](docs/MainApi#get_stor_next_license) | **GET** `/api/2/stornext-license` | 
*MainApi* | [**get_storage_node**](docs/MainApi#get_storage_node) | **GET** `/api/2/nodes/{id}` | 
*MainApi* | [**get_system_info**](docs/MainApi#get_system_info) | **GET** `/api/2/system/info` | 
*MainApi* | [**get_user**](docs/MainApi#get_user) | **GET** `/api/2/users/{id}` | 
*MainApi* | [**get_workstation**](docs/MainApi#get_workstation) | **GET** `/api/2/workstations/{id}` | 
*MainApi* | [**install_stor_next_license**](docs/MainApi#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
*MainApi* | [**patch_current_workstation**](docs/MainApi#patch_current_workstation) | **PATCH** `/api/2/workstations/current` | 
*MainApi* | [**patch_group**](docs/MainApi#patch_group) | **PATCH** `/api/2/groups/{id}` | 
*MainApi* | [**patch_user**](docs/MainApi#patch_user) | **PATCH** `/api/2/users/{id}` | 
*MainApi* | [**patch_workstation**](docs/MainApi#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
*MainApi* | [**preview_user**](docs/MainApi#preview_user) | **POST** `/api/2/users/preview` | 
*MainApi* | [**register_upload**](docs/MainApi#register_upload) | **POST** `/api/2/uploads/register` | 
*MainApi* | [**reset_user_password**](docs/MainApi#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
*MainApi* | [**set_my_password**](docs/MainApi#set_my_password) | **POST** `/api/2/users/me/password` | 
*MainApi* | [**set_user_password**](docs/MainApi#set_user_password) | **POST** `/api/2/users/{id}/password` | 
*MainApi* | [**sync_ldap_group**](docs/MainApi#sync_ldap_group) | **POST** `/api/2/groups/{id}/ldap-sync` | 
*MainApi* | [**sync_ldap_users**](docs/MainApi#sync_ldap_users) | **POST** `/api/2/ldap-servers/{id}/sync-users` | 
*MainApi* | [**sync_user_totp**](docs/MainApi#sync_user_totp) | **PUT** `/api/2/users/{id}/totp` | 
*MainApi* | [**update_current_workstation**](docs/MainApi#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
*MainApi* | [**update_group**](docs/MainApi#update_group) | **PUT** `/api/2/groups/{id}` | 
*MainApi* | [**update_parameters**](docs/MainApi#update_parameters) | **PUT** `/api/2/parameters` | 
*MainApi* | [**update_profile**](docs/MainApi#update_profile) | **PUT** `/api/2/users/me` | 
*MainApi* | [**update_user**](docs/MainApi#update_user) | **PUT** `/api/2/users/{id}` | 
*MainApi* | [**update_workstation**](docs/MainApi#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
*MainApi* | [**upload_chunk**](docs/MainApi#upload_chunk) | **POST** `/api/2/uploads/chunk` | 
*MediaLibraryApi* | [**clear_subclip_clipboard**](docs/MediaLibraryApi#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
*MediaLibraryApi* | [**combine_assets_into_set**](docs/MediaLibraryApi#combine_assets_into_set) | **POST** `/api/2/media/assets/combine` | 
*MediaLibraryApi* | [**create_asset**](docs/MediaLibraryApi#create_asset) | **POST** `/api/2/media/assets` | 
*MediaLibraryApi* | [**create_asset_rating**](docs/MediaLibraryApi#create_asset_rating) | **POST** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**create_comment**](docs/MediaLibraryApi#create_comment) | **POST** `/api/2/media/comments` | 
*MediaLibraryApi* | [**create_custom_field**](docs/MediaLibraryApi#create_custom_field) | **POST** `/api/2/media/custom-fields` | 
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
*MediaLibraryApi* | [**delete_marker**](docs/MediaLibraryApi#delete_marker) | **DELETE** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**delete_media_file_template**](docs/MediaLibraryApi#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**delete_media_root**](docs/MediaLibraryApi#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**delete_media_root_permission**](docs/MediaLibraryApi#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**delete_media_tag**](docs/MediaLibraryApi#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**delete_media_update**](docs/MediaLibraryApi#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
*MediaLibraryApi* | [**delete_proxy**](docs/MediaLibraryApi#delete_proxy) | **DELETE** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**delete_proxy_profile**](docs/MediaLibraryApi#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**delete_subclip**](docs/MediaLibraryApi#delete_subclip) | **DELETE** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**delete_subclip_clipboard_entry**](docs/MediaLibraryApi#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
*MediaLibraryApi* | [**discover_media**](docs/MediaLibraryApi#discover_media) | **POST** `/api/2/scanner/discover` | 
*MediaLibraryApi* | [**get_all_asset_project_links**](docs/MediaLibraryApi#get_all_asset_project_links) | **GET** `/api/2/media/assets/project-links` | 
*MediaLibraryApi* | [**get_all_asset_ratings**](docs/MediaLibraryApi#get_all_asset_ratings) | **GET** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**get_all_asset_tape_backups**](docs/MediaLibraryApi#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
*MediaLibraryApi* | [**get_all_assets**](docs/MediaLibraryApi#get_all_assets) | **GET** `/api/2/media/assets` | 
*MediaLibraryApi* | [**get_all_bundles_for_media_root**](docs/MediaLibraryApi#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
*MediaLibraryApi* | [**get_all_click_links**](docs/MediaLibraryApi#get_all_click_links) | **GET** `/api/2/media/assets/click-links` | 
*MediaLibraryApi* | [**get_all_comments**](docs/MediaLibraryApi#get_all_comments) | **GET** `/api/2/media/comments` | 
*MediaLibraryApi* | [**get_all_custom_fields**](docs/MediaLibraryApi#get_all_custom_fields) | **GET** `/api/2/media/custom-fields` | 
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
*MediaLibraryApi* | [**get_all_proxies**](docs/MediaLibraryApi#get_all_proxies) | **GET** `/api/2/media/proxies` | 
*MediaLibraryApi* | [**get_all_proxy_profiles**](docs/MediaLibraryApi#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**get_all_subclip_clipboard_entries**](docs/MediaLibraryApi#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**get_all_subclips**](docs/MediaLibraryApi#get_all_subclips) | **GET** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**get_all_transcoder_profiles**](docs/MediaLibraryApi#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
*MediaLibraryApi* | [**get_asset**](docs/MediaLibraryApi#get_asset) | **GET** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**get_asset_rating**](docs/MediaLibraryApi#get_asset_rating) | **GET** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**get_comment**](docs/MediaLibraryApi#get_comment) | **GET** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**get_custom_field**](docs/MediaLibraryApi#get_custom_field) | **GET** `/api/2/media/custom-fields/{id}` | 
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
*MediaLibraryApi* | [**get_proxy_profile**](docs/MediaLibraryApi#get_proxy_profile) | **GET** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**get_proxy_profile_proxy_count**](docs/MediaLibraryApi#get_proxy_profile_proxy_count) | **GET** `/api/2/media/proxy-profiles/{id}/proxy-count` | 
*MediaLibraryApi* | [**get_subclip**](docs/MediaLibraryApi#get_subclip) | **GET** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**get_transcoder_profile**](docs/MediaLibraryApi#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
*MediaLibraryApi* | [**patch_asset**](docs/MediaLibraryApi#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**patch_asset_rating**](docs/MediaLibraryApi#patch_asset_rating) | **PATCH** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**patch_comment**](docs/MediaLibraryApi#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**patch_custom_field**](docs/MediaLibraryApi#patch_custom_field) | **PATCH** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**patch_marker**](docs/MediaLibraryApi#patch_marker) | **PATCH** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**patch_media_file**](docs/MediaLibraryApi#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**patch_media_file_template**](docs/MediaLibraryApi#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**patch_media_root**](docs/MediaLibraryApi#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**patch_media_root_permission**](docs/MediaLibraryApi#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**patch_media_tag**](docs/MediaLibraryApi#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**patch_proxy_profile**](docs/MediaLibraryApi#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**patch_subclip**](docs/MediaLibraryApi#patch_subclip) | **PATCH** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**request_media_scan**](docs/MediaLibraryApi#request_media_scan) | **POST** `/api/2/scanner/scan` | 
*MediaLibraryApi* | [**resolve_comment**](docs/MediaLibraryApi#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
*MediaLibraryApi* | [**unresolve_comment**](docs/MediaLibraryApi#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
*MediaLibraryApi* | [**update_asset**](docs/MediaLibraryApi#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**update_asset_rating**](docs/MediaLibraryApi#update_asset_rating) | **PUT** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**update_comment**](docs/MediaLibraryApi#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**update_custom_field**](docs/MediaLibraryApi#update_custom_field) | **PUT** `/api/2/media/custom-fields/{id}` | 
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
*StatusApi* | [**patch_alert**](docs/StatusApi#patch_alert) | **PATCH** `/api/2/alerts/{id}` | 
*StatusApi* | [**update_alert**](docs/StatusApi#update_alert) | **PUT** `/api/2/alerts/{id}` | 
*StorageApi* | [**apply_workspace_affinity**](docs/StorageApi#apply_workspace_affinity) | **POST** `/api/2/workspaces/{id}/apply-affinity` | 
*StorageApi* | [**bookmark_workspace**](docs/StorageApi#bookmark_workspace) | **POST** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**check_in_into_workspace**](docs/StorageApi#check_in_into_workspace) | **POST** `/api/2/workspaces/{id}/check-in` | 
*StorageApi* | [**check_out_of_workspace**](docs/StorageApi#check_out_of_workspace) | **POST** `/api/2/workspaces/{id}/check-out` | 
*StorageApi* | [**create_production**](docs/StorageApi#create_production) | **POST** `/api/2/productions` | 
*StorageApi* | [**create_share**](docs/StorageApi#create_share) | **POST** `/api/2/shares` | 
*StorageApi* | [**create_snapshot**](docs/StorageApi#create_snapshot) | **POST** `/api/2/snapshots` | 
*StorageApi* | [**create_workspace**](docs/StorageApi#create_workspace) | **POST** `/api/2/workspaces` | 
*StorageApi* | [**create_workspace_permission**](docs/StorageApi#create_workspace_permission) | **POST** `/api/2/workspace-permissions` | 
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
*StorageApi* | [**get_my_workspaces**](docs/StorageApi#get_my_workspaces) | **GET** `/api/2/workspaces/mine` | 
*StorageApi* | [**get_production**](docs/StorageApi#get_production) | **GET** `/api/2/productions/{id}` | 
*StorageApi* | [**get_share**](docs/StorageApi#get_share) | **GET** `/api/2/shares/{id}` | 
*StorageApi* | [**get_snapshot**](docs/StorageApi#get_snapshot) | **GET** `/api/2/snapshots/{id}` | 
*StorageApi* | [**get_volume**](docs/StorageApi#get_volume) | **GET** `/api/2/volumes/{id}` | 
*StorageApi* | [**get_volume_active_connections**](docs/StorageApi#get_volume_active_connections) | **GET** `/api/2/volumes/{id}/connections` | 
*StorageApi* | [**get_volume_file_size_distribution**](docs/StorageApi#get_volume_file_size_distribution) | **GET** `/api/2/volumes/{id}/file-size-distribution` | 
*StorageApi* | [**get_volume_stats**](docs/StorageApi#get_volume_stats) | **GET** `/api/2/volumes/{id}/stats` | 
*StorageApi* | [**get_workspace**](docs/StorageApi#get_workspace) | **GET** `/api/2/workspaces/{id}` | 
*StorageApi* | [**get_workspace_permission**](docs/StorageApi#get_workspace_permission) | **GET** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**move_workspace_to_production**](docs/StorageApi#move_workspace_to_production) | **POST** `/api/2/workspaces/{id}/move-to` | 
*StorageApi* | [**patch_production**](docs/StorageApi#patch_production) | **PATCH** `/api/2/productions/{id}` | 
*StorageApi* | [**patch_share**](docs/StorageApi#patch_share) | **PATCH** `/api/2/shares/{id}` | 
*StorageApi* | [**patch_snapshot**](docs/StorageApi#patch_snapshot) | **PATCH** `/api/2/snapshots/{id}` | 
*StorageApi* | [**patch_volume**](docs/StorageApi#patch_volume) | **PATCH** `/api/2/volumes/{id}` | 
*StorageApi* | [**patch_workspace**](docs/StorageApi#patch_workspace) | **PATCH** `/api/2/workspaces/{id}` | 
*StorageApi* | [**patch_workspace_permission**](docs/StorageApi#patch_workspace_permission) | **PATCH** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**repair_workspace_permissions**](docs/StorageApi#repair_workspace_permissions) | **POST** `/api/2/workspaces/{id}/repair-permissions` | 
*StorageApi* | [**unbookmark_workspace**](docs/StorageApi#unbookmark_workspace) | **DELETE** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**update_production**](docs/StorageApi#update_production) | **PUT** `/api/2/productions/{id}` | 
*StorageApi* | [**update_share**](docs/StorageApi#update_share) | **PUT** `/api/2/shares/{id}` | 
*StorageApi* | [**update_snapshot**](docs/StorageApi#update_snapshot) | **PUT** `/api/2/snapshots/{id}` | 
*StorageApi* | [**update_volume**](docs/StorageApi#update_volume) | **PUT** `/api/2/volumes/{id}` | 
*StorageApi* | [**update_workspace**](docs/StorageApi#update_workspace) | **PUT** `/api/2/workspaces/{id}` | 
*StorageApi* | [**update_workspace_permission**](docs/StorageApi#update_workspace_permission) | **PUT** `/api/2/workspace-permissions/{id}` | 
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

 - [AIAnnotation](docs/AIAnnotation)
 - [AIAnnotationCreateRequest](docs/AIAnnotationCreateRequest)
 - [AICategory](docs/AICategory)
 - [AICategoryDetail](docs/AICategoryDetail)
 - [AIConnection](docs/AIConnection)
 - [AIDataset](docs/AIDataset)
 - [AIDatasetSimple](docs/AIDatasetSimple)
 - [AIDatasetWithPreview](docs/AIDatasetWithPreview)
 - [AIImage](docs/AIImage)
 - [AIMetadata](docs/AIMetadata)
 - [AIModel](docs/AIModel)
 - [AIModelProgress](docs/AIModelProgress)
 - [AIModelStat](docs/AIModelStat)
 - [AIModelStats](docs/AIModelStats)
 - [AIProcessingRequest](docs/AIProcessingRequest)
 - [Alert](docs/Alert)
 - [AllMediaFilesForBundlesRequest](docs/AllMediaFilesForBundlesRequest)
 - [Asset](docs/Asset)
 - [AssetBackup](docs/AssetBackup)
 - [AssetCloudLink](docs/AssetCloudLink)
 - [AssetMini](docs/AssetMini)
 - [AssetProjectLink](docs/AssetProjectLink)
 - [AssetRating](docs/AssetRating)
 - [AuthLoginEndpointRequest](docs/AuthLoginEndpointRequest)
 - [AuthLoginEndpointResponse](docs/AuthLoginEndpointResponse)
 - [Backend](docs/Backend)
 - [BackendProperties](docs/BackendProperties)
 - [CPUStat](docs/CPUStat)
 - [ChangeOwnPasswordRequest](docs/ChangeOwnPasswordRequest)
 - [ChangePasswordRequest](docs/ChangePasswordRequest)
 - [ClientSession](docs/ClientSession)
 - [ClientsEndpointResponse](docs/ClientsEndpointResponse)
 - [CloudConnection](docs/CloudConnection)
 - [Comment](docs/Comment)
 - [CreateHomeWorkspaceRequest](docs/CreateHomeWorkspaceRequest)
 - [CustomField](docs/CustomField)
 - [DeletedWorkspace](docs/DeletedWorkspace)
 - [Download](docs/Download)
 - [ElementsGroup](docs/ElementsGroup)
 - [ElementsGroupDetail](docs/ElementsGroupDetail)
 - [ElementsUser](docs/ElementsUser)
 - [ElementsUserDetail](docs/ElementsUserDetail)
 - [ElementsUserMini](docs/ElementsUserMini)
 - [ElementsUserProfile](docs/ElementsUserProfile)
 - [EnableTOTPRequest](docs/EnableTOTPRequest)
 - [FSProperties](docs/FSProperties)
 - [FileSizeDistribution](docs/FileSizeDistribution)
 - [FileSizeDistributionItem](docs/FileSizeDistributionItem)
 - [FinishUploadEndpointRequest](docs/FinishUploadEndpointRequest)
 - [GeneratePasswordEndpointResponse](docs/GeneratePasswordEndpointResponse)
 - [GetMultipleBundlesRequest](docs/GetMultipleBundlesRequest)
 - [GetMultipleFilesRequest](docs/GetMultipleFilesRequest)
 - [IOStat](docs/IOStat)
 - [Interface](docs/Interface)
 - [Job](docs/Job)
 - [LDAPServer](docs/LDAPServer)
 - [LDAPServerGroup](docs/LDAPServerGroup)
 - [LDAPServerGroups](docs/LDAPServerGroups)
 - [LDAPServerUser](docs/LDAPServerUser)
 - [LDAPServerUsers](docs/LDAPServerUsers)
 - [License](docs/License)
 - [Marker](docs/Marker)
 - [MediaFile](docs/MediaFile)
 - [MediaFileBundle](docs/MediaFileBundle)
 - [MediaFileBundleMini](docs/MediaFileBundleMini)
 - [MediaFileContents](docs/MediaFileContents)
 - [MediaFileMini](docs/MediaFileMini)
 - [MediaFileTemplate](docs/MediaFileTemplate)
 - [MediaRoot](docs/MediaRoot)
 - [MediaRootMini](docs/MediaRootMini)
 - [MediaRootPermission](docs/MediaRootPermission)
 - [MediaUpdate](docs/MediaUpdate)
 - [MemberPreview](docs/MemberPreview)
 - [MountedWorkspace](docs/MountedWorkspace)
 - [MultipleAssetsRequest](docs/MultipleAssetsRequest)
 - [NetStat](docs/NetStat)
 - [OneTimeAccessToken](docs/OneTimeAccessToken)
 - [OneTimeAccessTokenActivity](docs/OneTimeAccessTokenActivity)
 - [Parameters](docs/Parameters)
 - [Production](docs/Production)
 - [ProductionMini](docs/ProductionMini)
 - [Proxy](docs/Proxy)
 - [ProxyCount](docs/ProxyCount)
 - [ProxyProfile](docs/ProxyProfile)
 - [ProxyProfileMini](docs/ProxyProfileMini)
 - [Quota](docs/Quota)
 - [RAMStat](docs/RAMStat)
 - [RegisterUploadEndpointRequest](docs/RegisterUploadEndpointRequest)
 - [ReleaseNotesEndpointResponse](docs/ReleaseNotesEndpointResponse)
 - [ScannerDiscoverEndpointRequest](docs/ScannerDiscoverEndpointRequest)
 - [ScannerScanEndpointRequest](docs/ScannerScanEndpointRequest)
 - [Schedule](docs/Schedule)
 - [Sensor](docs/Sensor)
 - [Sensors](docs/Sensors)
 - [Share](docs/Share)
 - [Snapshot](docs/Snapshot)
 - [StartJobRequest](docs/StartJobRequest)
 - [StartTaskRequest](docs/StartTaskRequest)
 - [Stats](docs/Stats)
 - [StorNextConnection](docs/StorNextConnection)
 - [StorNextConnections](docs/StorNextConnections)
 - [StorNextLicenseCheckEndpointResponse](docs/StorNextLicenseCheckEndpointResponse)
 - [StorNextLicenseEndpointResponse](docs/StorNextLicenseEndpointResponse)
 - [StorageNode](docs/StorageNode)
 - [StorageNodeMini](docs/StorageNodeMini)
 - [StornextLicense](docs/StornextLicense)
 - [StornextManagerAttributes](docs/StornextManagerAttributes)
 - [Subclip](docs/Subclip)
 - [SubclipClipboardEntry](docs/SubclipClipboardEntry)
 - [Subtask](docs/Subtask)
 - [SyncTOTP](docs/SyncTOTP)
 - [SyncTOTPRequest](docs/SyncTOTPRequest)
 - [SystemInfoEndpointResponse](docs/SystemInfoEndpointResponse)
 - [Tag](docs/Tag)
 - [Tape](docs/Tape)
 - [TapeFile](docs/TapeFile)
 - [TapeGroup](docs/TapeGroup)
 - [TaskInfo](docs/TaskInfo)
 - [TaskLog](docs/TaskLog)
 - [TaskProgress](docs/TaskProgress)
 - [TasksSummary](docs/TasksSummary)
 - [Ticket](docs/Ticket)
 - [TranscoderProfile](docs/TranscoderProfile)
 - [UploadChunkEndpointRequest](docs/UploadChunkEndpointRequest)
 - [UserPreviewRequest](docs/UserPreviewRequest)
 - [UserPreviewResponse](docs/UserPreviewResponse)
 - [Volume](docs/Volume)
 - [VolumeMini](docs/VolumeMini)
 - [VolumeStat](docs/VolumeStat)
 - [VolumeStats](docs/VolumeStats)
 - [Workspace](docs/Workspace)
 - [WorkspaceCheckIn](docs/WorkspaceCheckIn)
 - [WorkspaceEndpoint](docs/WorkspaceEndpoint)
 - [WorkspaceMini](docs/WorkspaceMini)
 - [WorkspaceMoveToRequest](docs/WorkspaceMoveToRequest)
 - [WorkspacePermission](docs/WorkspacePermission)
 - [WorkspaceResolvedPermission](docs/WorkspaceResolvedPermission)
 - [Workstation](docs/Workstation)


