# ELEMENTS Python SDK

- API version: 2
- Python 2.7 and 3.4+
- Latest build: 3.0b1

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
*AIApi* | [**abort_ai_dataset_model_creation**](AIApi#abort_ai_dataset_model_creation) | **POST** `/api/2/ai/models/{id}/abort` | 
*AIApi* | [**create_ai_annotation_track**](AIApi#create_ai_annotation_track) | **POST** `/api/2/ai/annotations/tracks/create` | 
*AIApi* | [**create_ai_category**](AIApi#create_ai_category) | **POST** `/api/2/ai/categories` | 
*AIApi* | [**create_ai_dataset**](AIApi#create_ai_dataset) | **POST** `/api/2/ai/datasets` | 
*AIApi* | [**create_ai_dataset_model**](AIApi#create_ai_dataset_model) | **POST** `/api/2/ai/models/create` | 
*AIApi* | [**create_ai_metadata**](AIApi#create_ai_metadata) | **POST** `/api/2/ai/metadata/create` | 
*AIApi* | [**create_ai_model**](AIApi#create_ai_model) | **POST** `/api/2/ai/models` | 
*AIApi* | [**delete_ai_annotation**](AIApi#delete_ai_annotation) | **DELETE** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**delete_ai_annotation_track**](AIApi#delete_ai_annotation_track) | **DELETE** `/api/2/ai/annotations/tracks/{id}` | 
*AIApi* | [**delete_ai_category**](AIApi#delete_ai_category) | **DELETE** `/api/2/ai/categories/{id}` | 
*AIApi* | [**delete_ai_dataset**](AIApi#delete_ai_dataset) | **DELETE** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**delete_ai_model**](AIApi#delete_ai_model) | **DELETE** `/api/2/ai/models/{id}` | 
*AIApi* | [**get_ai_annotation**](AIApi#get_ai_annotation) | **GET** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**get_ai_annotation_image**](AIApi#get_ai_annotation_image) | **GET** `/api/2/ai/annotations/{id}/image` | 
*AIApi* | [**get_ai_category**](AIApi#get_ai_category) | **GET** `/api/2/ai/categories/{id}` | 
*AIApi* | [**get_ai_connection**](AIApi#get_ai_connection) | **GET** `/api/2/ai/connections/{id}` | 
*AIApi* | [**get_ai_dataset**](AIApi#get_ai_dataset) | **GET** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**get_ai_dataset_model_stats**](AIApi#get_ai_dataset_model_stats) | **GET** `/api/2/ai/models/{id}/stats` | 
*AIApi* | [**get_ai_image**](AIApi#get_ai_image) | **GET** `/api/2/ai/images/{id}` | 
*AIApi* | [**get_ai_image_content**](AIApi#get_ai_image_content) | **GET** `/api/2/ai/images/{id}/content` | 
*AIApi* | [**get_ai_metadata**](AIApi#get_ai_metadata) | **GET** `/api/2/ai/metadata/{id}` | 
*AIApi* | [**get_ai_model**](AIApi#get_ai_model) | **GET** `/api/2/ai/models/{id}` | 
*AIApi* | [**get_all_ai_annotation_tracks**](AIApi#get_all_ai_annotation_tracks) | **GET** `/api/2/ai/annotations/tracks` | 
*AIApi* | [**get_all_ai_annotations**](AIApi#get_all_ai_annotations) | **GET** `/api/2/ai/annotations` | 
*AIApi* | [**get_all_ai_categories**](AIApi#get_all_ai_categories) | **GET** `/api/2/ai/categories` | 
*AIApi* | [**get_all_ai_connections**](AIApi#get_all_ai_connections) | **GET** `/api/2/ai/connections` | 
*AIApi* | [**get_all_ai_datasets**](AIApi#get_all_ai_datasets) | **GET** `/api/2/ai/datasets` | 
*AIApi* | [**get_all_ai_images**](AIApi#get_all_ai_images) | **GET** `/api/2/ai/images` | 
*AIApi* | [**get_all_ai_metadata**](AIApi#get_all_ai_metadata) | **GET** `/api/2/ai/metadata` | 
*AIApi* | [**get_all_ai_models**](AIApi#get_all_ai_models) | **GET** `/api/2/ai/models` | 
*AIApi* | [**patch_ai_category**](AIApi#patch_ai_category) | **PATCH** `/api/2/ai/categories/{id}` | 
*AIApi* | [**patch_ai_dataset**](AIApi#patch_ai_dataset) | **PATCH** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**patch_ai_model**](AIApi#patch_ai_model) | **PATCH** `/api/2/ai/models/{id}` | 
*AIApi* | [**update_ai_category**](AIApi#update_ai_category) | **PUT** `/api/2/ai/categories/{id}` | 
*AIApi* | [**update_ai_dataset**](AIApi#update_ai_dataset) | **PUT** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**update_ai_model**](AIApi#update_ai_model) | **PUT** `/api/2/ai/models/{id}` | 
*AuthApi* | [**check_auth_ticket**](AuthApi#check_auth_ticket) | **POST** `/api/2/auth/ticket/check` | 
*AuthApi* | [**create_auth_ticket**](AuthApi#create_auth_ticket) | **POST** `/api/2/auth/ticket` | 
*AuthApi* | [**delete_onetimeaccesstoken**](AuthApi#delete_onetimeaccesstoken) | **DELETE** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**generate_password**](AuthApi#generate_password) | **POST** `/api/2/auth/generate-password` | 
*AuthApi* | [**get_all_onetimeaccesstokens**](AuthApi#get_all_onetimeaccesstokens) | **GET** `/api/2/auth/access-tokens` | 
*AuthApi* | [**get_onetimeaccesstoken**](AuthApi#get_onetimeaccesstoken) | **GET** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**login**](AuthApi#login) | **POST** `/api/2/auth/login` | 
*AuthApi* | [**logout**](AuthApi#logout) | **POST** `/api/2/auth/logout` | 
*AutomationApi* | [**abort_task**](AutomationApi#abort_task) | **POST** `/api/2/tasks/{id}/abort` | 
*AutomationApi* | [**create_job**](AutomationApi#create_job) | **POST** `/api/2/jobs` | 
*AutomationApi* | [**create_schedule**](AutomationApi#create_schedule) | **POST** `/api/2/schedules` | 
*AutomationApi* | [**create_subtask**](AutomationApi#create_subtask) | **POST** `/api/2/subtasks` | 
*AutomationApi* | [**delete_job**](AutomationApi#delete_job) | **DELETE** `/api/2/jobs/{id}` | 
*AutomationApi* | [**delete_schedule**](AutomationApi#delete_schedule) | **DELETE** `/api/2/schedules/{id}` | 
*AutomationApi* | [**delete_subtask**](AutomationApi#delete_subtask) | **DELETE** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**delete_taskinfo**](AutomationApi#delete_taskinfo) | **DELETE** `/api/2/tasks/{id}` | 
*AutomationApi* | [**download_all_task_logs**](AutomationApi#download_all_task_logs) | **GET** `/api/2/tasks/logs/download` | 
*AutomationApi* | [**download_task_log**](AutomationApi#download_task_log) | **GET** `/api/2/tasks/{id}/log/download` | 
*AutomationApi* | [**get_all_jobs**](AutomationApi#get_all_jobs) | **GET** `/api/2/jobs` | 
*AutomationApi* | [**get_all_schedules**](AutomationApi#get_all_schedules) | **GET** `/api/2/schedules` | 
*AutomationApi* | [**get_all_subtasks**](AutomationApi#get_all_subtasks) | **GET** `/api/2/subtasks` | 
*AutomationApi* | [**get_all_taskinfos**](AutomationApi#get_all_taskinfos) | **GET** `/api/2/tasks` | 
*AutomationApi* | [**get_finished_tasks**](AutomationApi#get_finished_tasks) | **GET** `/api/2/tasks/finished` | 
*AutomationApi* | [**get_job**](AutomationApi#get_job) | **GET** `/api/2/jobs/{id}` | 
*AutomationApi* | [**get_pending_tasks**](AutomationApi#get_pending_tasks) | **GET** `/api/2/tasks/pending` | 
*AutomationApi* | [**get_schedule**](AutomationApi#get_schedule) | **GET** `/api/2/schedules/{id}` | 
*AutomationApi* | [**get_subtask**](AutomationApi#get_subtask) | **GET** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**get_task_log**](AutomationApi#get_task_log) | **GET** `/api/2/tasks/{id}/log` | 
*AutomationApi* | [**get_taskinfo**](AutomationApi#get_taskinfo) | **GET** `/api/2/tasks/{id}` | 
*AutomationApi* | [**get_tasks_summary**](AutomationApi#get_tasks_summary) | **GET** `/api/2/tasks/summary` | 
*AutomationApi* | [**kill_all_pending_tasks**](AutomationApi#kill_all_pending_tasks) | **DELETE** `/api/2/tasks/pending` | 
*AutomationApi* | [**kill_task**](AutomationApi#kill_task) | **POST** `/api/2/tasks/{id}/kill` | 
*AutomationApi* | [**patch_job**](AutomationApi#patch_job) | **PATCH** `/api/2/jobs/{id}` | 
*AutomationApi* | [**patch_schedule**](AutomationApi#patch_schedule) | **PATCH** `/api/2/schedules/{id}` | 
*AutomationApi* | [**patch_subtask**](AutomationApi#patch_subtask) | **PATCH** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**restart_task**](AutomationApi#restart_task) | **POST** `/api/2/tasks/{id}/restart` | 
*AutomationApi* | [**start_job**](AutomationApi#start_job) | **POST** `/api/2/jobs/{id}/start` | 
*AutomationApi* | [**start_task**](AutomationApi#start_task) | **POST** `/api/2/tasks/start` | 
*AutomationApi* | [**update_job**](AutomationApi#update_job) | **PUT** `/api/2/jobs/{id}` | 
*AutomationApi* | [**update_schedule**](AutomationApi#update_schedule) | **PUT** `/api/2/schedules/{id}` | 
*AutomationApi* | [**update_subtask**](AutomationApi#update_subtask) | **PUT** `/api/2/subtasks/{id}` | 
*MainApi* | [**apply_configuration**](MainApi#apply_configuration) | **POST** `/api/2/configuration/apply` | 
*MainApi* | [**check_chunk_uploaded**](MainApi#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
*MainApi* | [**check_stor_next_license**](MainApi#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
*MainApi* | [**create_group**](MainApi#create_group) | **POST** `/api/2/groups` | 
*MainApi* | [**create_home_workspace**](MainApi#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
*MainApi* | [**create_user**](MainApi#create_user) | **POST** `/api/2/users` | 
*MainApi* | [**create_workstation**](MainApi#create_workstation) | **POST** `/api/2/workstations` | 
*MainApi* | [**delete_group**](MainApi#delete_group) | **DELETE** `/api/2/groups/{id}` | 
*MainApi* | [**delete_home_workspace**](MainApi#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
*MainApi* | [**delete_user**](MainApi#delete_user) | **DELETE** `/api/2/users/{id}` | 
*MainApi* | [**delete_workstation**](MainApi#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
*MainApi* | [**disable_user_totp**](MainApi#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
*MainApi* | [**enable_user_totp**](MainApi#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
*MainApi* | [**finish_upload**](MainApi#finish_upload) | **POST** `/api/2/uploads/finish` | 
*MainApi* | [**fix_ldap_group_memberships**](MainApi#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
*MainApi* | [**get_all_downloads**](MainApi#get_all_downloads) | **GET** `/api/2/downloads` | 
*MainApi* | [**get_all_groups**](MainApi#get_all_groups) | **GET** `/api/2/groups` | 
*MainApi* | [**get_all_ldap_servers**](MainApi#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
*MainApi* | [**get_all_storage_nodes**](MainApi#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
*MainApi* | [**get_all_users**](MainApi#get_all_users) | **GET** `/api/2/users` | 
*MainApi* | [**get_all_workstations**](MainApi#get_all_workstations) | **GET** `/api/2/workstations` | 
*MainApi* | [**get_client_download_file**](MainApi#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
*MainApi* | [**get_client_downloads**](MainApi#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
*MainApi* | [**get_current_workstation**](MainApi#get_current_workstation) | **GET** `/api/2/workstations/current` | 
*MainApi* | [**get_download**](MainApi#get_download) | **GET** `/api/2/downloads/{id}` | 
*MainApi* | [**get_download_file**](MainApi#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
*MainApi* | [**get_download_icon**](MainApi#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
*MainApi* | [**get_group**](MainApi#get_group) | **GET** `/api/2/groups/{id}` | 
*MainApi* | [**get_home_workspace**](MainApi#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
*MainApi* | [**get_ldap_server**](MainApi#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
*MainApi* | [**get_ldap_server_groups**](MainApi#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
*MainApi* | [**get_ldap_server_users**](MainApi#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
*MainApi* | [**get_node_ipmi_sensors**](MainApi#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
*MainApi* | [**get_node_stats**](MainApi#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
*MainApi* | [**get_parameters**](MainApi#get_parameters) | **GET** `/api/2/parameters` | 
*MainApi* | [**get_profile**](MainApi#get_profile) | **GET** `/api/2/users/me` | 
*MainApi* | [**get_release_notes**](MainApi#get_release_notes) | **GET** `/api/2/release-notes` | 
*MainApi* | [**get_stor_next_license**](MainApi#get_stor_next_license) | **GET** `/api/2/stornext-license` | 
*MainApi* | [**get_storage_node**](MainApi#get_storage_node) | **GET** `/api/2/nodes/{id}` | 
*MainApi* | [**get_system_info**](MainApi#get_system_info) | **GET** `/api/2/system/info` | 
*MainApi* | [**get_user**](MainApi#get_user) | **GET** `/api/2/users/{id}` | 
*MainApi* | [**get_workstation**](MainApi#get_workstation) | **GET** `/api/2/workstations/{id}` | 
*MainApi* | [**install_stor_next_license**](MainApi#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
*MainApi* | [**patch_group**](MainApi#patch_group) | **PATCH** `/api/2/groups/{id}` | 
*MainApi* | [**patch_user**](MainApi#patch_user) | **PATCH** `/api/2/users/{id}` | 
*MainApi* | [**patch_workstation**](MainApi#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
*MainApi* | [**preview_user**](MainApi#preview_user) | **POST** `/api/2/users/preview` | 
*MainApi* | [**register_upload**](MainApi#register_upload) | **POST** `/api/2/uploads/register` | 
*MainApi* | [**reset_user_password**](MainApi#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
*MainApi* | [**set_my_password**](MainApi#set_my_password) | **POST** `/api/2/users/me/password` | 
*MainApi* | [**set_user_password**](MainApi#set_user_password) | **POST** `/api/2/users/{id}/password` | 
*MainApi* | [**sync_ldap_group**](MainApi#sync_ldap_group) | **POST** `/api/2/groups/{id}/ldap-sync` | 
*MainApi* | [**sync_ldap_users**](MainApi#sync_ldap_users) | **POST** `/api/2/ldap-servers/{id}/sync-users` | 
*MainApi* | [**sync_user_totp**](MainApi#sync_user_totp) | **PUT** `/api/2/users/{id}/totp` | 
*MainApi* | [**update_current_workstation**](MainApi#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
*MainApi* | [**update_group**](MainApi#update_group) | **PUT** `/api/2/groups/{id}` | 
*MainApi* | [**update_parameters**](MainApi#update_parameters) | **PUT** `/api/2/parameters` | 
*MainApi* | [**update_profile**](MainApi#update_profile) | **PUT** `/api/2/users/me` | 
*MainApi* | [**update_user**](MainApi#update_user) | **PUT** `/api/2/users/{id}` | 
*MainApi* | [**update_workstation**](MainApi#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
*MainApi* | [**upload_chunk**](MainApi#upload_chunk) | **POST** `/api/2/uploads/chunk` | 
*MediaLibraryApi* | [**clear_subclip_clipboard**](MediaLibraryApi#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
*MediaLibraryApi* | [**combine_assets_into_set**](MediaLibraryApi#combine_assets_into_set) | **POST** `/api/2/media/assets/combine` | 
*MediaLibraryApi* | [**create_asset**](MediaLibraryApi#create_asset) | **POST** `/api/2/media/assets` | 
*MediaLibraryApi* | [**create_asset_rating**](MediaLibraryApi#create_asset_rating) | **POST** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**create_comment**](MediaLibraryApi#create_comment) | **POST** `/api/2/media/comments` | 
*MediaLibraryApi* | [**create_marker**](MediaLibraryApi#create_marker) | **POST** `/api/2/media/markers` | 
*MediaLibraryApi* | [**create_media_file_template**](MediaLibraryApi#create_media_file_template) | **POST** `/api/2/media/files/templates` | 
*MediaLibraryApi* | [**create_media_root**](MediaLibraryApi#create_media_root) | **POST** `/api/2/media/roots` | 
*MediaLibraryApi* | [**create_media_root_permission**](MediaLibraryApi#create_media_root_permission) | **POST** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**create_media_tag**](MediaLibraryApi#create_media_tag) | **POST** `/api/2/media/tags` | 
*MediaLibraryApi* | [**create_proxy_profile**](MediaLibraryApi#create_proxy_profile) | **POST** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**create_subclip**](MediaLibraryApi#create_subclip) | **POST** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**create_subclip_clipboard_entry**](MediaLibraryApi#create_subclip_clipboard_entry) | **POST** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**delete_asset**](MediaLibraryApi#delete_asset) | **DELETE** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**delete_asset_rating**](MediaLibraryApi#delete_asset_rating) | **DELETE** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**delete_comment**](MediaLibraryApi#delete_comment) | **DELETE** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**delete_marker**](MediaLibraryApi#delete_marker) | **DELETE** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**delete_media_file_template**](MediaLibraryApi#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**delete_media_root**](MediaLibraryApi#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**delete_media_root_permission**](MediaLibraryApi#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**delete_media_tag**](MediaLibraryApi#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**delete_media_update**](MediaLibraryApi#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
*MediaLibraryApi* | [**delete_proxy**](MediaLibraryApi#delete_proxy) | **DELETE** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**delete_proxy_profile**](MediaLibraryApi#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**delete_subclip**](MediaLibraryApi#delete_subclip) | **DELETE** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**delete_subclip_clipboard_entry**](MediaLibraryApi#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
*MediaLibraryApi* | [**discover_media**](MediaLibraryApi#discover_media) | **POST** `/api/2/scanner/discover` | 
*MediaLibraryApi* | [**get_all_asset_project_links**](MediaLibraryApi#get_all_asset_project_links) | **GET** `/api/2/media/assets/project-links` | 
*MediaLibraryApi* | [**get_all_asset_ratings**](MediaLibraryApi#get_all_asset_ratings) | **GET** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**get_all_asset_tape_backups**](MediaLibraryApi#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
*MediaLibraryApi* | [**get_all_assets**](MediaLibraryApi#get_all_assets) | **GET** `/api/2/media/assets` | 
*MediaLibraryApi* | [**get_all_bundles_for_media_root**](MediaLibraryApi#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
*MediaLibraryApi* | [**get_all_click_links**](MediaLibraryApi#get_all_click_links) | **GET** `/api/2/media/assets/click-links` | 
*MediaLibraryApi* | [**get_all_comments**](MediaLibraryApi#get_all_comments) | **GET** `/api/2/media/comments` | 
*MediaLibraryApi* | [**get_all_markers**](MediaLibraryApi#get_all_markers) | **GET** `/api/2/media/markers` | 
*MediaLibraryApi* | [**get_all_media_file_bundles**](MediaLibraryApi#get_all_media_file_bundles) | **GET** `/api/2/media/bundles` | 
*MediaLibraryApi* | [**get_all_media_file_templates**](MediaLibraryApi#get_all_media_file_templates) | **GET** `/api/2/media/files/templates` | 
*MediaLibraryApi* | [**get_all_media_files**](MediaLibraryApi#get_all_media_files) | **GET** `/api/2/media/files` | 
*MediaLibraryApi* | [**get_all_media_files_for_bundles**](MediaLibraryApi#get_all_media_files_for_bundles) | **POST** `/api/2/media/files/for-bundles` | 
*MediaLibraryApi* | [**get_all_media_files_for_media_root**](MediaLibraryApi#get_all_media_files_for_media_root) | **GET** `/api/2/media/files/flat/{root}` | 
*MediaLibraryApi* | [**get_all_media_root_permissions**](MediaLibraryApi#get_all_media_root_permissions) | **GET** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**get_all_media_roots**](MediaLibraryApi#get_all_media_roots) | **GET** `/api/2/media/roots` | 
*MediaLibraryApi* | [**get_all_media_tags**](MediaLibraryApi#get_all_media_tags) | **GET** `/api/2/media/tags` | 
*MediaLibraryApi* | [**get_all_media_updates**](MediaLibraryApi#get_all_media_updates) | **GET** `/api/2/media/updates` | 
*MediaLibraryApi* | [**get_all_proxies**](MediaLibraryApi#get_all_proxies) | **GET** `/api/2/media/proxies` | 
*MediaLibraryApi* | [**get_all_proxy_profiles**](MediaLibraryApi#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**get_all_subclip_clipboard_entries**](MediaLibraryApi#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**get_all_subclips**](MediaLibraryApi#get_all_subclips) | **GET** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**get_all_transcoder_profiles**](MediaLibraryApi#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
*MediaLibraryApi* | [**get_asset**](MediaLibraryApi#get_asset) | **GET** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**get_asset_rating**](MediaLibraryApi#get_asset_rating) | **GET** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**get_comment**](MediaLibraryApi#get_comment) | **GET** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**get_latest_media_update**](MediaLibraryApi#get_latest_media_update) | **GET** `/api/2/media/updates/latest` | 
*MediaLibraryApi* | [**get_marker**](MediaLibraryApi#get_marker) | **GET** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**get_media_file**](MediaLibraryApi#get_media_file) | **GET** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**get_media_file_bundle**](MediaLibraryApi#get_media_file_bundle) | **GET** `/api/2/media/bundles/{id}` | 
*MediaLibraryApi* | [**get_media_file_contents**](MediaLibraryApi#get_media_file_contents) | **GET** `/api/2/media/files/{id}/contents` | 
*MediaLibraryApi* | [**get_media_file_template**](MediaLibraryApi#get_media_file_template) | **GET** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**get_media_root**](MediaLibraryApi#get_media_root) | **GET** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**get_media_root_permission**](MediaLibraryApi#get_media_root_permission) | **GET** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**get_media_tag**](MediaLibraryApi#get_media_tag) | **GET** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**get_multiple_assets**](MediaLibraryApi#get_multiple_assets) | **POST** `/api/2/media/assets/multiple` | 
*MediaLibraryApi* | [**get_multiple_bundles**](MediaLibraryApi#get_multiple_bundles) | **POST** `/api/2/media/bundles/multiple` | 
*MediaLibraryApi* | [**get_multiple_files**](MediaLibraryApi#get_multiple_files) | **POST** `/api/2/media/files/multiple` | 
*MediaLibraryApi* | [**get_my_media_root_permissions**](MediaLibraryApi#get_my_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine` | 
*MediaLibraryApi* | [**get_my_resolved_media_root_permissions**](MediaLibraryApi#get_my_resolved_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine/resolved` | 
*MediaLibraryApi* | [**get_proxy**](MediaLibraryApi#get_proxy) | **GET** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**get_proxy_profile**](MediaLibraryApi#get_proxy_profile) | **GET** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**get_proxy_profile_proxy_count**](MediaLibraryApi#get_proxy_profile_proxy_count) | **GET** `/api/2/media/proxy-profiles/{id}/proxy-count` | 
*MediaLibraryApi* | [**get_subclip**](MediaLibraryApi#get_subclip) | **GET** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**get_transcoder_profile**](MediaLibraryApi#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
*MediaLibraryApi* | [**patch_asset**](MediaLibraryApi#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**patch_asset_rating**](MediaLibraryApi#patch_asset_rating) | **PATCH** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**patch_comment**](MediaLibraryApi#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**patch_marker**](MediaLibraryApi#patch_marker) | **PATCH** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**patch_media_file**](MediaLibraryApi#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**patch_media_file_template**](MediaLibraryApi#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**patch_media_root**](MediaLibraryApi#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**patch_media_root_permission**](MediaLibraryApi#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**patch_media_tag**](MediaLibraryApi#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**patch_proxy_profile**](MediaLibraryApi#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**patch_subclip**](MediaLibraryApi#patch_subclip) | **PATCH** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**request_media_scan**](MediaLibraryApi#request_media_scan) | **POST** `/api/2/scanner/scan` | 
*MediaLibraryApi* | [**resolve_comment**](MediaLibraryApi#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
*MediaLibraryApi* | [**unresolve_comment**](MediaLibraryApi#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
*MediaLibraryApi* | [**update_asset**](MediaLibraryApi#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**update_asset_rating**](MediaLibraryApi#update_asset_rating) | **PUT** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**update_comment**](MediaLibraryApi#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**update_marker**](MediaLibraryApi#update_marker) | **PUT** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**update_media_file**](MediaLibraryApi#update_media_file) | **PUT** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**update_media_file_template**](MediaLibraryApi#update_media_file_template) | **PUT** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**update_media_root**](MediaLibraryApi#update_media_root) | **PUT** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**update_media_root_permission**](MediaLibraryApi#update_media_root_permission) | **PUT** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**update_media_tag**](MediaLibraryApi#update_media_tag) | **PUT** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**update_proxy_profile**](MediaLibraryApi#update_proxy_profile) | **PUT** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**update_subclip**](MediaLibraryApi#update_subclip) | **PUT** `/api/2/media/subclips/{id}` | 
*StatusApi* | [**get_alert**](StatusApi#get_alert) | **GET** `/api/2/alerts/{id}` | 
*StatusApi* | [**get_all_alerts**](StatusApi#get_all_alerts) | **GET** `/api/2/alerts` | 
*StatusApi* | [**patch_alert**](StatusApi#patch_alert) | **PATCH** `/api/2/alerts/{id}` | 
*StatusApi* | [**update_alert**](StatusApi#update_alert) | **PUT** `/api/2/alerts/{id}` | 
*StorageApi* | [**apply_workspace_affinity**](StorageApi#apply_workspace_affinity) | **POST** `/api/2/workspaces/{id}/apply-affinity` | 
*StorageApi* | [**bookmark_workspace**](StorageApi#bookmark_workspace) | **POST** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**check_in_into_workspace**](StorageApi#check_in_into_workspace) | **POST** `/api/2/workspaces/{id}/check-in` | 
*StorageApi* | [**check_out_of_workspace**](StorageApi#check_out_of_workspace) | **POST** `/api/2/workspaces/{id}/check-out` | 
*StorageApi* | [**create_production**](StorageApi#create_production) | **POST** `/api/2/productions` | 
*StorageApi* | [**create_share**](StorageApi#create_share) | **POST** `/api/2/shares` | 
*StorageApi* | [**create_snapshot**](StorageApi#create_snapshot) | **POST** `/api/2/snapshots` | 
*StorageApi* | [**create_workspace**](StorageApi#create_workspace) | **POST** `/api/2/workspaces` | 
*StorageApi* | [**create_workspace_permission**](StorageApi#create_workspace_permission) | **POST** `/api/2/workspace-permissions` | 
*StorageApi* | [**delete_production**](StorageApi#delete_production) | **DELETE** `/api/2/productions/{id}` | 
*StorageApi* | [**delete_share**](StorageApi#delete_share) | **DELETE** `/api/2/shares/{id}` | 
*StorageApi* | [**delete_snapshot**](StorageApi#delete_snapshot) | **DELETE** `/api/2/snapshots/{id}` | 
*StorageApi* | [**delete_workspace**](StorageApi#delete_workspace) | **DELETE** `/api/2/workspaces/{id}` | 
*StorageApi* | [**delete_workspace_permission**](StorageApi#delete_workspace_permission) | **DELETE** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**get_all_deleted_workspaces**](StorageApi#get_all_deleted_workspaces) | **GET** `/api/2/workspaces/deleted` | 
*StorageApi* | [**get_all_productions**](StorageApi#get_all_productions) | **GET** `/api/2/productions` | 
*StorageApi* | [**get_all_shares**](StorageApi#get_all_shares) | **GET** `/api/2/shares` | 
*StorageApi* | [**get_all_snapshots**](StorageApi#get_all_snapshots) | **GET** `/api/2/snapshots` | 
*StorageApi* | [**get_all_volumes**](StorageApi#get_all_volumes) | **GET** `/api/2/volumes` | 
*StorageApi* | [**get_all_workspace_permissions**](StorageApi#get_all_workspace_permissions) | **GET** `/api/2/workspace-permissions` | 
*StorageApi* | [**get_all_workspaces**](StorageApi#get_all_workspaces) | **GET** `/api/2/workspaces` | 
*StorageApi* | [**get_my_workspaces**](StorageApi#get_my_workspaces) | **GET** `/api/2/workspaces/mine` | 
*StorageApi* | [**get_production**](StorageApi#get_production) | **GET** `/api/2/productions/{id}` | 
*StorageApi* | [**get_share**](StorageApi#get_share) | **GET** `/api/2/shares/{id}` | 
*StorageApi* | [**get_snapshot**](StorageApi#get_snapshot) | **GET** `/api/2/snapshots/{id}` | 
*StorageApi* | [**get_volume**](StorageApi#get_volume) | **GET** `/api/2/volumes/{id}` | 
*StorageApi* | [**get_volume_active_connections**](StorageApi#get_volume_active_connections) | **GET** `/api/2/volumes/{id}/connections` | 
*StorageApi* | [**get_volume_file_size_distribution**](StorageApi#get_volume_file_size_distribution) | **GET** `/api/2/volumes/{id}/file-size-distribution` | 
*StorageApi* | [**get_volume_stats**](StorageApi#get_volume_stats) | **GET** `/api/2/volumes/{id}/stats` | 
*StorageApi* | [**get_workspace**](StorageApi#get_workspace) | **GET** `/api/2/workspaces/{id}` | 
*StorageApi* | [**get_workspace_permission**](StorageApi#get_workspace_permission) | **GET** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**move_workspace_to_production**](StorageApi#move_workspace_to_production) | **POST** `/api/2/workspaces/{id}/move-to` | 
*StorageApi* | [**patch_production**](StorageApi#patch_production) | **PATCH** `/api/2/productions/{id}` | 
*StorageApi* | [**patch_share**](StorageApi#patch_share) | **PATCH** `/api/2/shares/{id}` | 
*StorageApi* | [**patch_snapshot**](StorageApi#patch_snapshot) | **PATCH** `/api/2/snapshots/{id}` | 
*StorageApi* | [**patch_workspace**](StorageApi#patch_workspace) | **PATCH** `/api/2/workspaces/{id}` | 
*StorageApi* | [**patch_workspace_permission**](StorageApi#patch_workspace_permission) | **PATCH** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**repair_workspace_permissions**](StorageApi#repair_workspace_permissions) | **POST** `/api/2/workspaces/{id}/repair-permissions` | 
*StorageApi* | [**unbookmark_workspace**](StorageApi#unbookmark_workspace) | **DELETE** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**update_production**](StorageApi#update_production) | **PUT** `/api/2/productions/{id}` | 
*StorageApi* | [**update_share**](StorageApi#update_share) | **PUT** `/api/2/shares/{id}` | 
*StorageApi* | [**update_snapshot**](StorageApi#update_snapshot) | **PUT** `/api/2/snapshots/{id}` | 
*StorageApi* | [**update_workspace**](StorageApi#update_workspace) | **PUT** `/api/2/workspaces/{id}` | 
*StorageApi* | [**update_workspace_permission**](StorageApi#update_workspace_permission) | **PUT** `/api/2/workspace-permissions/{id}` | 
*TapeArchiveApi* | [**create_tape**](TapeArchiveApi#create_tape) | **POST** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**create_tapegroup**](TapeArchiveApi#create_tapegroup) | **POST** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**delete_tape**](TapeArchiveApi#delete_tape) | **DELETE** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**delete_tapegroup**](TapeArchiveApi#delete_tapegroup) | **DELETE** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**get_all_archivedfileentries**](TapeArchiveApi#get_all_archivedfileentries) | **GET** `/api/2/archive/tape/files` | 
*TapeArchiveApi* | [**get_all_tapegroups**](TapeArchiveApi#get_all_tapegroups) | **GET** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**get_all_tapes**](TapeArchiveApi#get_all_tapes) | **GET** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**get_archivedfileentry**](TapeArchiveApi#get_archivedfileentry) | **GET** `/api/2/archive/tape/files/{id}` | 
*TapeArchiveApi* | [**get_tape**](TapeArchiveApi#get_tape) | **GET** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**get_tapegroup**](TapeArchiveApi#get_tapegroup) | **GET** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**patch_tape**](TapeArchiveApi#patch_tape) | **PATCH** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**patch_tapegroup**](TapeArchiveApi#patch_tapegroup) | **PATCH** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**update_tape**](TapeArchiveApi#update_tape) | **PUT** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**update_tapegroup**](TapeArchiveApi#update_tapegroup) | **PUT** `/api/2/archive/tape/groups/{id}` | 


## Models

 - [AIAnnotation](AIAnnotation)
 - [AIAnnotationCreateRequest](AIAnnotationCreateRequest)
 - [AICategory](AICategory)
 - [AICategoryDetail](AICategoryDetail)
 - [AIConnection](AIConnection)
 - [AIDataset](AIDataset)
 - [AIDatasetSimple](AIDatasetSimple)
 - [AIDatasetWithPreview](AIDatasetWithPreview)
 - [AIImage](AIImage)
 - [AIMetadata](AIMetadata)
 - [AIModel](AIModel)
 - [AIModelProgress](AIModelProgress)
 - [AIModelStat](AIModelStat)
 - [AIModelStats](AIModelStats)
 - [AIProcessingRequest](AIProcessingRequest)
 - [Alert](Alert)
 - [AllMediaFilesForBundlesRequest](AllMediaFilesForBundlesRequest)
 - [Asset](Asset)
 - [AssetBackup](AssetBackup)
 - [AssetCloudLink](AssetCloudLink)
 - [AssetMini](AssetMini)
 - [AssetProjectLink](AssetProjectLink)
 - [AssetRating](AssetRating)
 - [AuthLoginEndpointRequest](AuthLoginEndpointRequest)
 - [AuthLoginEndpointResponse](AuthLoginEndpointResponse)
 - [Backend](Backend)
 - [BackendProperties](BackendProperties)
 - [CPUStat](CPUStat)
 - [ChangeOwnPasswordRequest](ChangeOwnPasswordRequest)
 - [ChangePasswordRequest](ChangePasswordRequest)
 - [ClientSession](ClientSession)
 - [ClientsEndpointResponse](ClientsEndpointResponse)
 - [CloudConnection](CloudConnection)
 - [Comment](Comment)
 - [CreateHomeWorkspaceRequest](CreateHomeWorkspaceRequest)
 - [DeletedWorkspace](DeletedWorkspace)
 - [Download](Download)
 - [ElementsGroup](ElementsGroup)
 - [ElementsGroupDetail](ElementsGroupDetail)
 - [ElementsUser](ElementsUser)
 - [ElementsUserDetail](ElementsUserDetail)
 - [ElementsUserMini](ElementsUserMini)
 - [ElementsUserProfile](ElementsUserProfile)
 - [EnableTOTPRequest](EnableTOTPRequest)
 - [FSProperties](FSProperties)
 - [FileSizeDistribution](FileSizeDistribution)
 - [FileSizeDistributionItem](FileSizeDistributionItem)
 - [FinishUploadEndpointRequest](FinishUploadEndpointRequest)
 - [GeneratePasswordEndpointResponse](GeneratePasswordEndpointResponse)
 - [GetMultipleBundlesRequest](GetMultipleBundlesRequest)
 - [GetMultipleFilesRequest](GetMultipleFilesRequest)
 - [IOStat](IOStat)
 - [Interface](Interface)
 - [Job](Job)
 - [LDAPServer](LDAPServer)
 - [LDAPServerGroup](LDAPServerGroup)
 - [LDAPServerGroups](LDAPServerGroups)
 - [LDAPServerUser](LDAPServerUser)
 - [LDAPServerUsers](LDAPServerUsers)
 - [License](License)
 - [Marker](Marker)
 - [MediaFile](MediaFile)
 - [MediaFileBundle](MediaFileBundle)
 - [MediaFileBundleMini](MediaFileBundleMini)
 - [MediaFileContents](MediaFileContents)
 - [MediaFileMini](MediaFileMini)
 - [MediaFileTemplate](MediaFileTemplate)
 - [MediaRoot](MediaRoot)
 - [MediaRootMini](MediaRootMini)
 - [MediaRootPermission](MediaRootPermission)
 - [MediaUpdate](MediaUpdate)
 - [MemberPreview](MemberPreview)
 - [MountedWorkspace](MountedWorkspace)
 - [MultipleAssetsRequest](MultipleAssetsRequest)
 - [NetStat](NetStat)
 - [Network](Network)
 - [OneTimeAccessToken](OneTimeAccessToken)
 - [OneTimeAccessTokenActivity](OneTimeAccessTokenActivity)
 - [Parameters](Parameters)
 - [Production](Production)
 - [ProductionMini](ProductionMini)
 - [Proxy](Proxy)
 - [ProxyCount](ProxyCount)
 - [ProxyProfile](ProxyProfile)
 - [ProxyProfileMini](ProxyProfileMini)
 - [Quota](Quota)
 - [RAMStat](RAMStat)
 - [RegisterUploadEndpointRequest](RegisterUploadEndpointRequest)
 - [ReleaseNotesEndpointResponse](ReleaseNotesEndpointResponse)
 - [ScannerDiscoverEndpointRequest](ScannerDiscoverEndpointRequest)
 - [ScannerScanEndpointRequest](ScannerScanEndpointRequest)
 - [Schedule](Schedule)
 - [Sensor](Sensor)
 - [Sensors](Sensors)
 - [Share](Share)
 - [Snapshot](Snapshot)
 - [StartJobRequest](StartJobRequest)
 - [StartTaskRequest](StartTaskRequest)
 - [Stats](Stats)
 - [StorNextConnection](StorNextConnection)
 - [StorNextConnections](StorNextConnections)
 - [StorNextLicenseCheckEndpointResponse](StorNextLicenseCheckEndpointResponse)
 - [StorNextLicenseEndpointResponse](StorNextLicenseEndpointResponse)
 - [StorageNode](StorageNode)
 - [StornextLicense](StornextLicense)
 - [StornextManagerAttributes](StornextManagerAttributes)
 - [Subclip](Subclip)
 - [SubclipClipboardEntry](SubclipClipboardEntry)
 - [Subtask](Subtask)
 - [SyncTOTP](SyncTOTP)
 - [SyncTOTPRequest](SyncTOTPRequest)
 - [SystemInfoEndpointResponse](SystemInfoEndpointResponse)
 - [Tag](Tag)
 - [Tape](Tape)
 - [TapeFile](TapeFile)
 - [TapeGroup](TapeGroup)
 - [TaskInfo](TaskInfo)
 - [TaskLog](TaskLog)
 - [TaskProgress](TaskProgress)
 - [TasksSummary](TasksSummary)
 - [Ticket](Ticket)
 - [TranscoderProfile](TranscoderProfile)
 - [UploadChunkEndpointRequest](UploadChunkEndpointRequest)
 - [UserPreviewRequest](UserPreviewRequest)
 - [UserPreviewResponse](UserPreviewResponse)
 - [Volume](Volume)
 - [VolumeMini](VolumeMini)
 - [VolumeStat](VolumeStat)
 - [VolumeStats](VolumeStats)
 - [Workspace](Workspace)
 - [WorkspaceCheckIn](WorkspaceCheckIn)
 - [WorkspaceEndpoint](WorkspaceEndpoint)
 - [WorkspaceMini](WorkspaceMini)
 - [WorkspaceMoveToRequest](WorkspaceMoveToRequest)
 - [WorkspacePermission](WorkspacePermission)
 - [WorkspaceResolvedPermission](WorkspaceResolvedPermission)
 - [Workstation](Workstation)


