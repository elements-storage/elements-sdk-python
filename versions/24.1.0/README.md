# ELEMENTS Python SDK

- API version: 2
- Python 2.7 and 3.4+
- Latest build: 24.1.0

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
import elements_sdk
from elements_sdk.api.storage_api import StorageApi
from elements_sdk.model.volume import Volume

config = elements_sdk.Configuration(
    host='http://elements.local',
    discard_unknown_keys=True,
)
config.api_key['Bearer'] = 'Bearer your-api-token-here'
config.client_side_validation = False
config.debug = True


with elements_sdk.ApiClient(config) as api_client:
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
*AIApi* | [**activate_ai_model**](docs/AIApi#activate_ai_model) | **POST** `/api/2/ai/models/{id}/activate` | 
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
*AIApi* | [**export_ai_dataset**](docs/AIApi#export_ai_dataset) | **POST** `/api/2/ai/datasets/{id}/export` | 
*AIApi* | [**export_ai_model**](docs/AIApi#export_ai_model) | **POST** `/api/2/ai/models/{id}/export` | 
*AIApi* | [**get_ai_annotation**](docs/AIApi#get_ai_annotation) | **GET** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**get_ai_annotation_image**](docs/AIApi#get_ai_annotation_image) | **GET** `/api/2/ai/annotations/{id}/image` | 
*AIApi* | [**get_ai_category**](docs/AIApi#get_ai_category) | **GET** `/api/2/ai/categories/{id}` | 
*AIApi* | [**get_ai_connection**](docs/AIApi#get_ai_connection) | **GET** `/api/2/ai/connections/{id}` | 
*AIApi* | [**get_ai_dataset**](docs/AIApi#get_ai_dataset) | **GET** `/api/2/ai/datasets/{id}` | 
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
*AIApi* | [**import_ai_datasets**](docs/AIApi#import_ai_datasets) | **POST** `/api/2/ai/datasets/import` | 
*AIApi* | [**import_ai_models**](docs/AIApi#import_ai_models) | **POST** `/api/2/ai/datasets/{id}/import-models` | 
*AIApi* | [**patch_ai_annotation**](docs/AIApi#patch_ai_annotation) | **PATCH** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**patch_ai_category**](docs/AIApi#patch_ai_category) | **PATCH** `/api/2/ai/categories/{id}` | 
*AIApi* | [**patch_ai_dataset**](docs/AIApi#patch_ai_dataset) | **PATCH** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**patch_ai_model**](docs/AIApi#patch_ai_model) | **PATCH** `/api/2/ai/models/{id}` | 
*AIApi* | [**run_ai_model_inference**](docs/AIApi#run_ai_model_inference) | **POST** `/api/2/ai/models/{id}/inference` | 
*AIApi* | [**update_ai_annotation**](docs/AIApi#update_ai_annotation) | **PUT** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**update_ai_category**](docs/AIApi#update_ai_category) | **PUT** `/api/2/ai/categories/{id}` | 
*AIApi* | [**update_ai_dataset**](docs/AIApi#update_ai_dataset) | **PUT** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**update_ai_model**](docs/AIApi#update_ai_model) | **PUT** `/api/2/ai/models/{id}` | 
*AIApi* | [**upload_ai_image**](docs/AIApi#upload_ai_image) | **POST** `/api/2/ai/images/upload` | 
*AWSApi* | [**create_aws_account**](docs/AWSApi#create_aws_account) | **POST** `/api/2/aws-accounts` | 
*AWSApi* | [**delete_aws_account**](docs/AWSApi#delete_aws_account) | **DELETE** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**get_all_aws_accounts**](docs/AWSApi#get_all_aws_accounts) | **GET** `/api/2/aws-accounts` | 
*AWSApi* | [**get_aws_account**](docs/AWSApi#get_aws_account) | **GET** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**get_aws_account_sns_topics**](docs/AWSApi#get_aws_account_sns_topics) | **GET** `/api/2/aws-accounts/{id}/sns/topics` | 
*AWSApi* | [**patch_aws_account**](docs/AWSApi#patch_aws_account) | **PATCH** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**update_aws_account**](docs/AWSApi#update_aws_account) | **PUT** `/api/2/aws-accounts/{id}` | 
*AuthApi* | [**check_auth_ticket**](docs/AuthApi#check_auth_ticket) | **POST** `/api/2/auth/ticket/check` | 
*AuthApi* | [**create_api_token**](docs/AuthApi#create_api_token) | **POST** `/api/2/api-tokens` | 
*AuthApi* | [**create_auth_ticket**](docs/AuthApi#create_auth_ticket) | **POST** `/api/2/auth/ticket` | 
*AuthApi* | [**create_saml_provider**](docs/AuthApi#create_saml_provider) | **POST** `/api/2/auth/saml` | 
*AuthApi* | [**delete_access_token**](docs/AuthApi#delete_access_token) | **DELETE** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**delete_api_token**](docs/AuthApi#delete_api_token) | **DELETE** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**delete_saml_provider**](docs/AuthApi#delete_saml_provider) | **DELETE** `/api/2/auth/saml/{id}` | 
*AuthApi* | [**generate_password**](docs/AuthApi#generate_password) | **POST** `/api/2/auth/generate-password` | 
*AuthApi* | [**get_access_token**](docs/AuthApi#get_access_token) | **GET** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**get_access_token_by_value**](docs/AuthApi#get_access_token_by_value) | **GET** `/api/2/auth/access-tokens/get/{token}` | 
*AuthApi* | [**get_all_access_tokens**](docs/AuthApi#get_all_access_tokens) | **GET** `/api/2/auth/access-tokens` | 
*AuthApi* | [**get_all_api_tokens**](docs/AuthApi#get_all_api_tokens) | **GET** `/api/2/api-tokens` | 
*AuthApi* | [**get_all_saml_providers**](docs/AuthApi#get_all_saml_providers) | **GET** `/api/2/auth/saml` | 
*AuthApi* | [**get_api_token**](docs/AuthApi#get_api_token) | **GET** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**get_saml_provider**](docs/AuthApi#get_saml_provider) | **GET** `/api/2/auth/saml/{id}` | 
*AuthApi* | [**get_saml_service_provider_metadata**](docs/AuthApi#get_saml_service_provider_metadata) | **GET** `/api/2/auth/saml/{id}/metadata` | 
*AuthApi* | [**login**](docs/AuthApi#login) | **POST** `/api/2/auth/login` | 
*AuthApi* | [**logout**](docs/AuthApi#logout) | **POST** `/api/2/auth/logout` | 
*AuthApi* | [**logout_page**](docs/AuthApi#logout_page) | **GET** `/api/2/auth/logout` | 
*AuthApi* | [**parse_samlidp_metadata**](docs/AuthApi#parse_samlidp_metadata) | **POST** `/api/2/auth/saml/parse-idp-metadata` | 
*AuthApi* | [**patch_api_token**](docs/AuthApi#patch_api_token) | **PATCH** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**patch_saml_provider**](docs/AuthApi#patch_saml_provider) | **PATCH** `/api/2/auth/saml/{id}` | 
*AuthApi* | [**receive_saml_auth_assertion**](docs/AuthApi#receive_saml_auth_assertion) | **POST** `/api/2/auth/saml/{id}/assertion` | 
*AuthApi* | [**refresh_samlidp_metadata**](docs/AuthApi#refresh_samlidp_metadata) | **POST** `/api/2/auth/saml/{id}/refresh-idp-metadata` | 
*AuthApi* | [**reset_password**](docs/AuthApi#reset_password) | **POST** `/api/2/auth/reset-password` | 
*AuthApi* | [**return_from_saml_auth**](docs/AuthApi#return_from_saml_auth) | **GET** `/api/2/auth/saml/{id}/sso/return` | 
*AuthApi* | [**return_from_saml_logout**](docs/AuthApi#return_from_saml_logout) | **GET** `/api/2/auth/saml/{id}/sls/return` | 
*AuthApi* | [**send_access_token_email_notification**](docs/AuthApi#send_access_token_email_notification) | **POST** `/api/2/auth/access-tokens/{id}/email` | 
*AuthApi* | [**start_impersonation**](docs/AuthApi#start_impersonation) | **POST** `/api/2/auth/impersonation` | 
*AuthApi* | [**start_impersonation_via_redirect**](docs/AuthApi#start_impersonation_via_redirect) | **GET** `/api/2/auth/impersonation/redirect/{user_id}` | 
*AuthApi* | [**start_saml_auth**](docs/AuthApi#start_saml_auth) | **GET** `/api/2/auth/saml/{id}/sso` | 
*AuthApi* | [**start_saml_logout**](docs/AuthApi#start_saml_logout) | **GET** `/api/2/auth/saml/{id}/sls` | 
*AuthApi* | [**stop_impersonation**](docs/AuthApi#stop_impersonation) | **POST** `/api/2/auth/impersonation/stop` | 
*AuthApi* | [**update_api_token**](docs/AuthApi#update_api_token) | **PUT** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**update_saml_provider**](docs/AuthApi#update_saml_provider) | **PUT** `/api/2/auth/saml/{id}` | 
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
*AutomationApi* | [**export_job**](docs/AutomationApi#export_job) | **GET** `/api/2/jobs/{id}/export` | 
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
*AutomationApi* | [**get_task_log_v2**](docs/AutomationApi#get_task_log_v2) | **GET** `/api/2/tasks/{id}/log-v2` | 
*AutomationApi* | [**get_task_type**](docs/AutomationApi#get_task_type) | **GET** `/api/2/tasks/types/{type}` | 
*AutomationApi* | [**get_tasks_summary**](docs/AutomationApi#get_tasks_summary) | **GET** `/api/2/tasks/summary` | 
*AutomationApi* | [**import_job**](docs/AutomationApi#import_job) | **POST** `/api/2/jobs/import` | 
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
*ClickApi* | [**abort_click_upload**](docs/ClickApi#abort_click_upload) | **DELETE** `/api/2/click/uploads/{upload_id}` | 
*ClickApi* | [**add_assets_to_click_gallery**](docs/ClickApi#add_assets_to_click_gallery) | **POST** `/api/2/click/connections/{connection_id}/galleries/{id}/add-assets` | 
*ClickApi* | [**continue_click_upload_in_background**](docs/ClickApi#continue_click_upload_in_background) | **POST** `/api/2/click/uploads/{upload_id}/background` | 
*ClickApi* | [**create_click_gallery**](docs/ClickApi#create_click_gallery) | **POST** `/api/2/click/connections/{connection_id}/galleries` | 
*ClickApi* | [**create_click_gallery_link**](docs/ClickApi#create_click_gallery_link) | **POST** `/api/2/click/connections/{connection_id}/gallery-links` | 
*ClickApi* | [**delete_click_gallery_link**](docs/ClickApi#delete_click_gallery_link) | **DELETE** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
*ClickApi* | [**get_all_click_galleries**](docs/ClickApi#get_all_click_galleries) | **GET** `/api/2/click/connections/{connection_id}/galleries` | 
*ClickApi* | [**get_all_click_gallery_links**](docs/ClickApi#get_all_click_gallery_links) | **GET** `/api/2/click/connections/{connection_id}/gallery-links` | 
*ClickApi* | [**get_click_gallery**](docs/ClickApi#get_click_gallery) | **GET** `/api/2/click/connections/{connection_id}/galleries/{id}` | 
*ClickApi* | [**get_click_gallery_link**](docs/ClickApi#get_click_gallery_link) | **GET** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
*ClickApi* | [**send_click_gallery_link_email**](docs/ClickApi#send_click_gallery_link_email) | **POST** `/api/2/click/connections/{connection_id}/gallery-links/{link_id}/send` | 
*ClickApi* | [**start_click_upload**](docs/ClickApi#start_click_upload) | **POST** `/api/2/click/uploads` | 
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
*MainApi* | [**acknowledge_all_notifications**](docs/MainApi#acknowledge_all_notifications) | **POST** `/api/2/notifications/acknowledge-all` | 
*MainApi* | [**apply_configuration**](docs/MainApi#apply_configuration) | **POST** `/api/2/configuration/apply` | 
*MainApi* | [**beep**](docs/MainApi#beep) | **POST** `/api/2/system/beep` | 
*MainApi* | [**check_certificate**](docs/MainApi#check_certificate) | **POST** `/api/2/system/certificate/check` | 
*MainApi* | [**check_chunk_uploaded**](docs/MainApi#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
*MainApi* | [**check_internet_connectivity**](docs/MainApi#check_internet_connectivity) | **POST** `/api/2/system/check-connectivity` | 
*MainApi* | [**check_stor_next_license**](docs/MainApi#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
*MainApi* | [**collect_diagnostics**](docs/MainApi#collect_diagnostics) | **POST** `/api/2/system/collect-diagnostics` | 
*MainApi* | [**count_unread_notifications**](docs/MainApi#count_unread_notifications) | **GET** `/api/2/notifications/count-unread` | 
*MainApi* | [**create_archive**](docs/MainApi#create_archive) | **POST** `/api/2/download-archive/create` | 
*MainApi* | [**create_cloud_account**](docs/MainApi#create_cloud_account) | **POST** `/api/2/cloud/accounts` | 
*MainApi* | [**create_filesystem_permission**](docs/MainApi#create_filesystem_permission) | **POST** `/api/2/filesystem-permissions` | 
*MainApi* | [**create_group**](docs/MainApi#create_group) | **POST** `/api/2/groups` | 
*MainApi* | [**create_home_workspace**](docs/MainApi#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
*MainApi* | [**create_notification_setting**](docs/MainApi#create_notification_setting) | **POST** `/api/2/notification-settings` | 
*MainApi* | [**create_ntp_server**](docs/MainApi#create_ntp_server) | **POST** `/api/2/system/time/servers` | 
*MainApi* | [**create_storage_node**](docs/MainApi#create_storage_node) | **POST** `/api/2/nodes` | 
*MainApi* | [**create_user**](docs/MainApi#create_user) | **POST** `/api/2/users` | 
*MainApi* | [**create_workstation**](docs/MainApi#create_workstation) | **POST** `/api/2/workstations` | 
*MainApi* | [**delete_all_notifications**](docs/MainApi#delete_all_notifications) | **DELETE** `/api/2/notifications/all` | 
*MainApi* | [**delete_cloud_account**](docs/MainApi#delete_cloud_account) | **DELETE** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**delete_download_archive**](docs/MainApi#delete_download_archive) | **DELETE** `/api/2/download-archive/{id}` | 
*MainApi* | [**delete_filesystem_permission**](docs/MainApi#delete_filesystem_permission) | **DELETE** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**delete_group**](docs/MainApi#delete_group) | **DELETE** `/api/2/groups/{id}` | 
*MainApi* | [**delete_home_workspace**](docs/MainApi#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
*MainApi* | [**delete_my_avatar**](docs/MainApi#delete_my_avatar) | **DELETE** `/api/2/users/me/avatar` | 
*MainApi* | [**delete_notification**](docs/MainApi#delete_notification) | **DELETE** `/api/2/notifications/{id}` | 
*MainApi* | [**delete_notification_setting**](docs/MainApi#delete_notification_setting) | **DELETE** `/api/2/notification-settings/{id}` | 
*MainApi* | [**delete_ntp_server**](docs/MainApi#delete_ntp_server) | **DELETE** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**delete_storage_node**](docs/MainApi#delete_storage_node) | **DELETE** `/api/2/nodes/{id}` | 
*MainApi* | [**delete_user**](docs/MainApi#delete_user) | **DELETE** `/api/2/users/{id}` | 
*MainApi* | [**delete_user_avatar**](docs/MainApi#delete_user_avatar) | **DELETE** `/api/2/users/{id}/avatar` | 
*MainApi* | [**delete_workstation**](docs/MainApi#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
*MainApi* | [**disable_user_totp**](docs/MainApi#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
*MainApi* | [**enable_user_totp**](docs/MainApi#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
*MainApi* | [**finish_upload**](docs/MainApi#finish_upload) | **POST** `/api/2/uploads/finish` | 
*MainApi* | [**fix_ldap_group_memberships**](docs/MainApi#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
*MainApi* | [**get_all_client_sessions**](docs/MainApi#get_all_client_sessions) | **GET** `/api/2/client-sessions` | 
*MainApi* | [**get_all_cloud_accounts**](docs/MainApi#get_all_cloud_accounts) | **GET** `/api/2/cloud/accounts` | 
*MainApi* | [**get_all_download_archives**](docs/MainApi#get_all_download_archives) | **GET** `/api/2/download-archive` | 
*MainApi* | [**get_all_downloads**](docs/MainApi#get_all_downloads) | **GET** `/api/2/downloads` | 
*MainApi* | [**get_all_filesystem_permissions**](docs/MainApi#get_all_filesystem_permissions) | **GET** `/api/2/filesystem-permissions` | 
*MainApi* | [**get_all_groups**](docs/MainApi#get_all_groups) | **GET** `/api/2/groups` | 
*MainApi* | [**get_all_ldap_servers**](docs/MainApi#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
*MainApi* | [**get_all_notification_receipts**](docs/MainApi#get_all_notification_receipts) | **GET** `/api/2/notification-receipts` | 
*MainApi* | [**get_all_notification_settings**](docs/MainApi#get_all_notification_settings) | **GET** `/api/2/notification-settings` | 
*MainApi* | [**get_all_notifications**](docs/MainApi#get_all_notifications) | **GET** `/api/2/notifications` | 
*MainApi* | [**get_all_ntp_servers**](docs/MainApi#get_all_ntp_servers) | **GET** `/api/2/system/time/servers` | 
*MainApi* | [**get_all_storage_nodes**](docs/MainApi#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
*MainApi* | [**get_all_users**](docs/MainApi#get_all_users) | **GET** `/api/2/users` | 
*MainApi* | [**get_all_workstations**](docs/MainApi#get_all_workstations) | **GET** `/api/2/workstations` | 
*MainApi* | [**get_certificate_configuration**](docs/MainApi#get_certificate_configuration) | **GET** `/api/2/system/certificate` | 
*MainApi* | [**get_client_download_file**](docs/MainApi#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
*MainApi* | [**get_client_downloads**](docs/MainApi#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
*MainApi* | [**get_client_session**](docs/MainApi#get_client_session) | **GET** `/api/2/client-sessions/{id}` | 
*MainApi* | [**get_cloud_account**](docs/MainApi#get_cloud_account) | **GET** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**get_cloud_account_costs**](docs/MainApi#get_cloud_account_costs) | **GET** `/api/2/cloud/accounts/{id}/costs` | 
*MainApi* | [**get_cloud_account_storage_roots**](docs/MainApi#get_cloud_account_storage_roots) | **GET** `/api/2/cloud/accounts/{id}/storage-roots` | 
*MainApi* | [**get_cloud_account_volume_sizes**](docs/MainApi#get_cloud_account_volume_sizes) | **GET** `/api/2/cloud/accounts/{id}/volume-sizes` | 
*MainApi* | [**get_current_workstation**](docs/MainApi#get_current_workstation) | **GET** `/api/2/workstations/current` | 
*MainApi* | [**get_download**](docs/MainApi#get_download) | **GET** `/api/2/downloads/{id}` | 
*MainApi* | [**get_download_archive**](docs/MainApi#get_download_archive) | **GET** `/api/2/download-archive/{id}` | 
*MainApi* | [**get_download_archive_file**](docs/MainApi#get_download_archive_file) | **GET** `/api/2/download-archive/{id}/download` | 
*MainApi* | [**get_download_file**](docs/MainApi#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
*MainApi* | [**get_download_icon**](docs/MainApi#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
*MainApi* | [**get_filesystem_permission**](docs/MainApi#get_filesystem_permission) | **GET** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**get_group**](docs/MainApi#get_group) | **GET** `/api/2/groups/{id}` | 
*MainApi* | [**get_home_workspace**](docs/MainApi#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
*MainApi* | [**get_ipmi_configuration**](docs/MainApi#get_ipmi_configuration) | **GET** `/api/2/nodes/{id}/ipmi` | 
*MainApi* | [**get_ldap_server**](docs/MainApi#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
*MainApi* | [**get_ldap_server_groups**](docs/MainApi#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
*MainApi* | [**get_ldap_server_users**](docs/MainApi#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
*MainApi* | [**get_license**](docs/MainApi#get_license) | **GET** `/api/2/license` | 
*MainApi* | [**get_local_time**](docs/MainApi#get_local_time) | **GET** `/api/2/system/time` | 
*MainApi* | [**get_log**](docs/MainApi#get_log) | **GET** `/api/2/system/log/{path}` | 
*MainApi* | [**get_my_avatar**](docs/MainApi#get_my_avatar) | **GET** `/api/2/users/me/avatar` | 
*MainApi* | [**get_node_ipmi_sensors**](docs/MainApi#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
*MainApi* | [**get_node_stats**](docs/MainApi#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
*MainApi* | [**get_notification**](docs/MainApi#get_notification) | **GET** `/api/2/notifications/{id}` | 
*MainApi* | [**get_notification_receipt**](docs/MainApi#get_notification_receipt) | **GET** `/api/2/notification-receipts/{id}` | 
*MainApi* | [**get_notification_setting**](docs/MainApi#get_notification_setting) | **GET** `/api/2/notification-settings/{id}` | 
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
*MainApi* | [**get_user_avatar**](docs/MainApi#get_user_avatar) | **GET** `/api/2/users/{id}/avatar` | 
*MainApi* | [**get_workstation**](docs/MainApi#get_workstation) | **GET** `/api/2/workstations/{id}` | 
*MainApi* | [**install_stor_next_license**](docs/MainApi#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
*MainApi* | [**patch_cloud_account**](docs/MainApi#patch_cloud_account) | **PATCH** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**patch_current_workstation**](docs/MainApi#patch_current_workstation) | **PATCH** `/api/2/workstations/current` | 
*MainApi* | [**patch_download_archive**](docs/MainApi#patch_download_archive) | **PATCH** `/api/2/download-archive/{id}` | 
*MainApi* | [**patch_filesystem_permission**](docs/MainApi#patch_filesystem_permission) | **PATCH** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**patch_group**](docs/MainApi#patch_group) | **PATCH** `/api/2/groups/{id}` | 
*MainApi* | [**patch_notification**](docs/MainApi#patch_notification) | **PATCH** `/api/2/notifications/{id}` | 
*MainApi* | [**patch_notification_receipt**](docs/MainApi#patch_notification_receipt) | **PATCH** `/api/2/notification-receipts/{id}` | 
*MainApi* | [**patch_notification_setting**](docs/MainApi#patch_notification_setting) | **PATCH** `/api/2/notification-settings/{id}` | 
*MainApi* | [**patch_ntp_server**](docs/MainApi#patch_ntp_server) | **PATCH** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**patch_profile**](docs/MainApi#patch_profile) | **PATCH** `/api/2/users/me` | 
*MainApi* | [**patch_storage_node**](docs/MainApi#patch_storage_node) | **PATCH** `/api/2/nodes/{id}` | 
*MainApi* | [**patch_user**](docs/MainApi#patch_user) | **PATCH** `/api/2/users/{id}` | 
*MainApi* | [**patch_workstation**](docs/MainApi#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
*MainApi* | [**reboot**](docs/MainApi#reboot) | **POST** `/api/2/system/reboot` | 
*MainApi* | [**register_upload**](docs/MainApi#register_upload) | **POST** `/api/2/uploads/register` | 
*MainApi* | [**register_upload_metadata**](docs/MainApi#register_upload_metadata) | **POST** `/api/2/uploads/metadata` | 
*MainApi* | [**render_email_template_preview**](docs/MainApi#render_email_template_preview) | **POST** `/api/2/system/smtp/preview` | 
*MainApi* | [**reset_user_password**](docs/MainApi#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
*MainApi* | [**restart_web_ui**](docs/MainApi#restart_web_ui) | **POST** `/api/2/system/restart-webui` | 
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
*MainApi* | [**test_cloud_account_credentials**](docs/MainApi#test_cloud_account_credentials) | **POST** `/api/2/cloud/accounts/test-credentials` | 
*MainApi* | [**test_smtp_configuration**](docs/MainApi#test_smtp_configuration) | **POST** `/api/2/system/smtp/test` | 
*MainApi* | [**update_certificate_configuration**](docs/MainApi#update_certificate_configuration) | **PUT** `/api/2/system/certificate` | 
*MainApi* | [**update_cloud_account**](docs/MainApi#update_cloud_account) | **PUT** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**update_current_workstation**](docs/MainApi#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
*MainApi* | [**update_download_archive**](docs/MainApi#update_download_archive) | **PUT** `/api/2/download-archive/{id}` | 
*MainApi* | [**update_filesystem_permission**](docs/MainApi#update_filesystem_permission) | **PUT** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**update_group**](docs/MainApi#update_group) | **PUT** `/api/2/groups/{id}` | 
*MainApi* | [**update_my_avatar**](docs/MainApi#update_my_avatar) | **POST** `/api/2/users/me/avatar` | 
*MainApi* | [**update_notification**](docs/MainApi#update_notification) | **PUT** `/api/2/notifications/{id}` | 
*MainApi* | [**update_notification_receipt**](docs/MainApi#update_notification_receipt) | **PUT** `/api/2/notification-receipts/{id}` | 
*MainApi* | [**update_notification_setting**](docs/MainApi#update_notification_setting) | **PUT** `/api/2/notification-settings/{id}` | 
*MainApi* | [**update_ntp_server**](docs/MainApi#update_ntp_server) | **PUT** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**update_parameters**](docs/MainApi#update_parameters) | **PUT** `/api/2/parameters` | 
*MainApi* | [**update_profile**](docs/MainApi#update_profile) | **PUT** `/api/2/users/me` | 
*MainApi* | [**update_smtp_configuration**](docs/MainApi#update_smtp_configuration) | **PUT** `/api/2/system/smtp` | 
*MainApi* | [**update_storage_node**](docs/MainApi#update_storage_node) | **PUT** `/api/2/nodes/{id}` | 
*MainApi* | [**update_user**](docs/MainApi#update_user) | **PUT** `/api/2/users/{id}` | 
*MainApi* | [**update_user_avatar**](docs/MainApi#update_user_avatar) | **POST** `/api/2/users/{id}/avatar` | 
*MainApi* | [**update_workstation**](docs/MainApi#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
*MainApi* | [**upload_chunk**](docs/MainApi#upload_chunk) | **POST** `/api/2/uploads/chunk` | 
*MediaLibraryApi* | [**bookmark_media_directory**](docs/MediaLibraryApi#bookmark_media_directory) | **POST** `/api/2/media/files/{id}/bookmark` | 
*MediaLibraryApi* | [**clear_subclip_clipboard**](docs/MediaLibraryApi#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
*MediaLibraryApi* | [**clear_subtitle_clipboard**](docs/MediaLibraryApi#clear_subtitle_clipboard) | **DELETE** `/api/2/media/subtitles/clipboard/clear` | 
*MediaLibraryApi* | [**combine_assets_into_set**](docs/MediaLibraryApi#combine_assets_into_set) | **POST** `/api/2/media/assets/combine` | 
*MediaLibraryApi* | [**count_unresolved_comments**](docs/MediaLibraryApi#count_unresolved_comments) | **GET** `/api/2/media/comments/count-unresolved` | 
*MediaLibraryApi* | [**create_asset**](docs/MediaLibraryApi#create_asset) | **POST** `/api/2/media/assets` | 
*MediaLibraryApi* | [**create_asset_rating**](docs/MediaLibraryApi#create_asset_rating) | **POST** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**create_asset_subtitle_link**](docs/MediaLibraryApi#create_asset_subtitle_link) | **POST** `/api/2/media/assets/subtitle-links` | 
*MediaLibraryApi* | [**create_comment**](docs/MediaLibraryApi#create_comment) | **POST** `/api/2/media/comments` | 
*MediaLibraryApi* | [**create_custom_field**](docs/MediaLibraryApi#create_custom_field) | **POST** `/api/2/media/custom-fields` | 
*MediaLibraryApi* | [**create_editor_project**](docs/MediaLibraryApi#create_editor_project) | **POST** `/api/2/media/editor` | 
*MediaLibraryApi* | [**create_editor_subtitle**](docs/MediaLibraryApi#create_editor_subtitle) | **POST** `/api/2/media/subtitles` | 
*MediaLibraryApi* | [**create_external_transcoder**](docs/MediaLibraryApi#create_external_transcoder) | **POST** `/api/2/media/external-transcoders` | 
*MediaLibraryApi* | [**create_marker**](docs/MediaLibraryApi#create_marker) | **POST** `/api/2/media/markers` | 
*MediaLibraryApi* | [**create_media_file_template**](docs/MediaLibraryApi#create_media_file_template) | **POST** `/api/2/media/files/templates` | 
*MediaLibraryApi* | [**create_media_root**](docs/MediaLibraryApi#create_media_root) | **POST** `/api/2/media/roots` | 
*MediaLibraryApi* | [**create_media_root_permission**](docs/MediaLibraryApi#create_media_root_permission) | **POST** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**create_media_tag**](docs/MediaLibraryApi#create_media_tag) | **POST** `/api/2/media/tags` | 
*MediaLibraryApi* | [**create_proxy_profile**](docs/MediaLibraryApi#create_proxy_profile) | **POST** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**create_saved_search**](docs/MediaLibraryApi#create_saved_search) | **POST** `/api/2/media/saved-searches` | 
*MediaLibraryApi* | [**create_sharing_permission_preset**](docs/MediaLibraryApi#create_sharing_permission_preset) | **POST** `/api/2/media/sharing-permission-presets` | 
*MediaLibraryApi* | [**create_subclip**](docs/MediaLibraryApi#create_subclip) | **POST** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**create_subclip_clipboard_entry**](docs/MediaLibraryApi#create_subclip_clipboard_entry) | **POST** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**create_subtitle_clipboard_entry**](docs/MediaLibraryApi#create_subtitle_clipboard_entry) | **POST** `/api/2/media/subtitles/clipboard` | 
*MediaLibraryApi* | [**delete_asset**](docs/MediaLibraryApi#delete_asset) | **DELETE** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**delete_asset_rating**](docs/MediaLibraryApi#delete_asset_rating) | **DELETE** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**delete_asset_subtitle_link**](docs/MediaLibraryApi#delete_asset_subtitle_link) | **DELETE** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**delete_comment**](docs/MediaLibraryApi#delete_comment) | **DELETE** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**delete_custom_field**](docs/MediaLibraryApi#delete_custom_field) | **DELETE** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**delete_easy_sharing_token_for_bundle**](docs/MediaLibraryApi#delete_easy_sharing_token_for_bundle) | **DELETE** `/api/2/media/bundles/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**delete_easy_sharing_token_for_directory**](docs/MediaLibraryApi#delete_easy_sharing_token_for_directory) | **DELETE** `/api/2/media/files/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**delete_external_transcoder**](docs/MediaLibraryApi#delete_external_transcoder) | **DELETE** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**delete_marker**](docs/MediaLibraryApi#delete_marker) | **DELETE** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**delete_media_file_template**](docs/MediaLibraryApi#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**delete_media_library_objects**](docs/MediaLibraryApi#delete_media_library_objects) | **POST** `/api/2/media/delete` | 
*MediaLibraryApi* | [**delete_media_root**](docs/MediaLibraryApi#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**delete_media_root_cover_image**](docs/MediaLibraryApi#delete_media_root_cover_image) | **DELETE** `/api/2/media/roots/{id}/cover` | 
*MediaLibraryApi* | [**delete_media_root_permission**](docs/MediaLibraryApi#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**delete_media_tag**](docs/MediaLibraryApi#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**delete_media_update**](docs/MediaLibraryApi#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
*MediaLibraryApi* | [**delete_proxy**](docs/MediaLibraryApi#delete_proxy) | **DELETE** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**delete_proxy_profile**](docs/MediaLibraryApi#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**delete_proxy_profile_watermark_image**](docs/MediaLibraryApi#delete_proxy_profile_watermark_image) | **DELETE** `/api/2/media/proxy-profiles/{id}/watermark` | 
*MediaLibraryApi* | [**delete_saved_search**](docs/MediaLibraryApi#delete_saved_search) | **DELETE** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**delete_sharing_permission_preset**](docs/MediaLibraryApi#delete_sharing_permission_preset) | **DELETE** `/api/2/media/sharing-permission-presets/{id}` | 
*MediaLibraryApi* | [**delete_subclip**](docs/MediaLibraryApi#delete_subclip) | **DELETE** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**delete_subclip_clipboard_entry**](docs/MediaLibraryApi#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
*MediaLibraryApi* | [**delete_subtitle_clipboard_entry**](docs/MediaLibraryApi#delete_subtitle_clipboard_entry) | **DELETE** `/api/2/media/subtitles/clipboard/{id}` | 
*MediaLibraryApi* | [**discover_media**](docs/MediaLibraryApi#discover_media) | **POST** `/api/2/scanner/discover` | 
*MediaLibraryApi* | [**download_asset_proxy_file**](docs/MediaLibraryApi#download_asset_proxy_file) | **GET** `/api/2/media/assets/{id}/proxy-files/{filename}` | 
*MediaLibraryApi* | [**download_media_file**](docs/MediaLibraryApi#download_media_file) | **GET** `/api/2/media/files/{id}/download` | 
*MediaLibraryApi* | [**download_proxy**](docs/MediaLibraryApi#download_proxy) | **GET** `/api/2/media/proxies/{id}/download` | 
*MediaLibraryApi* | [**editor_export_xml_for_assset**](docs/MediaLibraryApi#editor_export_xml_for_assset) | **GET** `/api/2/media/editor/asset/{asset_ids}/xml-export` | 
*MediaLibraryApi* | [**editor_export_xml_for_bundle**](docs/MediaLibraryApi#editor_export_xml_for_bundle) | **GET** `/api/2/media/editor/bundle/{bundle_ids}/xml-export` | 
*MediaLibraryApi* | [**editor_export_xml_for_project**](docs/MediaLibraryApi#editor_export_xml_for_project) | **GET** `/api/2/media/editor/{id}/xml-export` | 
*MediaLibraryApi* | [**export_comments_for_avid**](docs/MediaLibraryApi#export_comments_for_avid) | **GET** `/api/2/media/editor/asset/{asset_id}/{export_format}-export/avid-comments` | 
*MediaLibraryApi* | [**export_editor_timeline**](docs/MediaLibraryApi#export_editor_timeline) | **POST** `/api/2/media/editor/timeline-export` | 
*MediaLibraryApi* | [**extract_stream**](docs/MediaLibraryApi#extract_stream) | **POST** `/api/2/media/assets/{id}/extract-stream` | 
*MediaLibraryApi* | [**forget_deleted_media_files**](docs/MediaLibraryApi#forget_deleted_media_files) | **POST** `/api/2/media/files/{id}/forget-deleted` | 
*MediaLibraryApi* | [**generate_proxies**](docs/MediaLibraryApi#generate_proxies) | **POST** `/api/2/media/proxies` | 
*MediaLibraryApi* | [**get_all_asset_project_links**](docs/MediaLibraryApi#get_all_asset_project_links) | **GET** `/api/2/media/assets/project-links` | 
*MediaLibraryApi* | [**get_all_asset_ratings**](docs/MediaLibraryApi#get_all_asset_ratings) | **GET** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**get_all_asset_subtitle_links**](docs/MediaLibraryApi#get_all_asset_subtitle_links) | **GET** `/api/2/media/assets/subtitle-links` | 
*MediaLibraryApi* | [**get_all_asset_tape_backups**](docs/MediaLibraryApi#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
*MediaLibraryApi* | [**get_all_assets**](docs/MediaLibraryApi#get_all_assets) | **GET** `/api/2/media/assets` | 
*MediaLibraryApi* | [**get_all_bundles_for_media_root**](docs/MediaLibraryApi#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
*MediaLibraryApi* | [**get_all_bundles_in_subtree**](docs/MediaLibraryApi#get_all_bundles_in_subtree) | **GET** `/api/2/media/bundles/flat/subtree/{file}` | 
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
*MediaLibraryApi* | [**get_all_media_files_in_subtree**](docs/MediaLibraryApi#get_all_media_files_in_subtree) | **GET** `/api/2/media/files/flat/subtree/{file}` | 
*MediaLibraryApi* | [**get_all_media_root_permissions**](docs/MediaLibraryApi#get_all_media_root_permissions) | **GET** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**get_all_media_roots**](docs/MediaLibraryApi#get_all_media_roots) | **GET** `/api/2/media/roots` | 
*MediaLibraryApi* | [**get_all_media_tags**](docs/MediaLibraryApi#get_all_media_tags) | **GET** `/api/2/media/tags` | 
*MediaLibraryApi* | [**get_all_media_updates**](docs/MediaLibraryApi#get_all_media_updates) | **GET** `/api/2/media/updates` | 
*MediaLibraryApi* | [**get_all_proxy_generators**](docs/MediaLibraryApi#get_all_proxy_generators) | **GET** `/api/2/media/proxy-generators` | 
*MediaLibraryApi* | [**get_all_proxy_profiles**](docs/MediaLibraryApi#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**get_all_saved_searches**](docs/MediaLibraryApi#get_all_saved_searches) | **GET** `/api/2/media/saved-searches` | 
*MediaLibraryApi* | [**get_all_sharing_permission_presets**](docs/MediaLibraryApi#get_all_sharing_permission_presets) | **GET** `/api/2/media/sharing-permission-presets` | 
*MediaLibraryApi* | [**get_all_subclip_clipboard_entries**](docs/MediaLibraryApi#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**get_all_subclips**](docs/MediaLibraryApi#get_all_subclips) | **GET** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**get_all_subtitle_clipboard_entries**](docs/MediaLibraryApi#get_all_subtitle_clipboard_entries) | **GET** `/api/2/media/subtitles/clipboard` | 
*MediaLibraryApi* | [**get_all_transcoder_profiles**](docs/MediaLibraryApi#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
*MediaLibraryApi* | [**get_asset**](docs/MediaLibraryApi#get_asset) | **GET** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**get_asset_rating**](docs/MediaLibraryApi#get_asset_rating) | **GET** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**get_asset_subtitle_link**](docs/MediaLibraryApi#get_asset_subtitle_link) | **GET** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**get_bookmarked_media_files_directories**](docs/MediaLibraryApi#get_bookmarked_media_files_directories) | **GET** `/api/2/media/files/bookmarks` | 
*MediaLibraryApi* | [**get_comment**](docs/MediaLibraryApi#get_comment) | **GET** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**get_custom_field**](docs/MediaLibraryApi#get_custom_field) | **GET** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**get_easy_sharing_token_for_bundle**](docs/MediaLibraryApi#get_easy_sharing_token_for_bundle) | **GET** `/api/2/media/bundles/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**get_easy_sharing_token_for_directory**](docs/MediaLibraryApi#get_easy_sharing_token_for_directory) | **GET** `/api/2/media/files/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**get_editor_project**](docs/MediaLibraryApi#get_editor_project) | **GET** `/api/2/media/editor/{id}` | 
*MediaLibraryApi* | [**get_editor_subtitle**](docs/MediaLibraryApi#get_editor_subtitle) | **GET** `/api/2/media/subtitles/{id}` | 
*MediaLibraryApi* | [**get_external_transcoder**](docs/MediaLibraryApi#get_external_transcoder) | **GET** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**get_frame**](docs/MediaLibraryApi#get_frame) | **GET** `/api/2/media/assets/{id}/frames/{frame}` | 
*MediaLibraryApi* | [**get_marker**](docs/MediaLibraryApi#get_marker) | **GET** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**get_media_file**](docs/MediaLibraryApi#get_media_file) | **GET** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**get_media_file_bundle**](docs/MediaLibraryApi#get_media_file_bundle) | **GET** `/api/2/media/bundles/{id}` | 
*MediaLibraryApi* | [**get_media_file_contents**](docs/MediaLibraryApi#get_media_file_contents) | **GET** `/api/2/media/files/{id}/contents` | 
*MediaLibraryApi* | [**get_media_file_template**](docs/MediaLibraryApi#get_media_file_template) | **GET** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**get_media_root**](docs/MediaLibraryApi#get_media_root) | **GET** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**get_media_root_cover_image**](docs/MediaLibraryApi#get_media_root_cover_image) | **GET** `/api/2/media/roots/{id}/cover` | 
*MediaLibraryApi* | [**get_media_root_permission**](docs/MediaLibraryApi#get_media_root_permission) | **GET** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**get_media_root_users**](docs/MediaLibraryApi#get_media_root_users) | **GET** `/api/2/media/roots/{id}/users` | 
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
*MediaLibraryApi* | [**get_proxy_profile_watermark_image**](docs/MediaLibraryApi#get_proxy_profile_watermark_image) | **GET** `/api/2/media/proxy-profiles/{id}/watermark` | 
*MediaLibraryApi* | [**get_saved_search**](docs/MediaLibraryApi#get_saved_search) | **GET** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**get_sharing_permission_preset**](docs/MediaLibraryApi#get_sharing_permission_preset) | **GET** `/api/2/media/sharing-permission-presets/{id}` | 
*MediaLibraryApi* | [**get_subclip**](docs/MediaLibraryApi#get_subclip) | **GET** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**get_subtitles**](docs/MediaLibraryApi#get_subtitles) | **GET** `/api/2/media/assets/{id}/subtitle/{title}` | 
*MediaLibraryApi* | [**get_transcoder_profile**](docs/MediaLibraryApi#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
*MediaLibraryApi* | [**get_vantage_workflows**](docs/MediaLibraryApi#get_vantage_workflows) | **GET** `/api/2/media/external-transcoders/{id}/workflows` | 
*MediaLibraryApi* | [**instantiate_media_file_template**](docs/MediaLibraryApi#instantiate_media_file_template) | **POST** `/api/2/media/files/templates/{id}/instantiate` | 
*MediaLibraryApi* | [**locate_editor_project_paths**](docs/MediaLibraryApi#locate_editor_project_paths) | **GET** `/api/2/media/editor/{id}/locate-paths` | 
*MediaLibraryApi* | [**lookup_media_files**](docs/MediaLibraryApi#lookup_media_files) | **POST** `/api/2/media/files/lookup` | 
*MediaLibraryApi* | [**mark_media_directory_as_showroom**](docs/MediaLibraryApi#mark_media_directory_as_showroom) | **POST** `/api/2/media/files/{id}/showroom` | 
*MediaLibraryApi* | [**patch_asset**](docs/MediaLibraryApi#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**patch_asset_rating**](docs/MediaLibraryApi#patch_asset_rating) | **PATCH** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**patch_asset_subtitle_link**](docs/MediaLibraryApi#patch_asset_subtitle_link) | **PATCH** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**patch_comment**](docs/MediaLibraryApi#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**patch_custom_field**](docs/MediaLibraryApi#patch_custom_field) | **PATCH** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**patch_editor_project**](docs/MediaLibraryApi#patch_editor_project) | **PATCH** `/api/2/media/editor/{id}` | 
*MediaLibraryApi* | [**patch_editor_subtitle**](docs/MediaLibraryApi#patch_editor_subtitle) | **PATCH** `/api/2/media/subtitles/{id}` | 
*MediaLibraryApi* | [**patch_external_transcoder**](docs/MediaLibraryApi#patch_external_transcoder) | **PATCH** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**patch_marker**](docs/MediaLibraryApi#patch_marker) | **PATCH** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**patch_media_file**](docs/MediaLibraryApi#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**patch_media_file_template**](docs/MediaLibraryApi#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**patch_media_root**](docs/MediaLibraryApi#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**patch_media_root_permission**](docs/MediaLibraryApi#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**patch_media_tag**](docs/MediaLibraryApi#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**patch_proxy_profile**](docs/MediaLibraryApi#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**patch_saved_search**](docs/MediaLibraryApi#patch_saved_search) | **PATCH** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**patch_sharing_permission_preset**](docs/MediaLibraryApi#patch_sharing_permission_preset) | **PATCH** `/api/2/media/sharing-permission-presets/{id}` | 
*MediaLibraryApi* | [**patch_subclip**](docs/MediaLibraryApi#patch_subclip) | **PATCH** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**recursively_tag_media_directory**](docs/MediaLibraryApi#recursively_tag_media_directory) | **POST** `/api/2/media/files/{id}/tag` | 
*MediaLibraryApi* | [**reindex_media_directory**](docs/MediaLibraryApi#reindex_media_directory) | **POST** `/api/2/media/files/{id}/search-reindex` | 
*MediaLibraryApi* | [**rename_custom_field**](docs/MediaLibraryApi#rename_custom_field) | **POST** `/api/2/media/custom-fields/{id}/rename` | 
*MediaLibraryApi* | [**render_sequence**](docs/MediaLibraryApi#render_sequence) | **POST** `/api/2/media/editor/render` | 
*MediaLibraryApi* | [**render_subclip**](docs/MediaLibraryApi#render_subclip) | **POST** `/api/2/media/subclips/{id}/render` | 
*MediaLibraryApi* | [**request_media_scan**](docs/MediaLibraryApi#request_media_scan) | **POST** `/api/2/scanner/scan` | 
*MediaLibraryApi* | [**resolve_comment**](docs/MediaLibraryApi#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
*MediaLibraryApi* | [**share_media_library_objects**](docs/MediaLibraryApi#share_media_library_objects) | **POST** `/api/2/media/share` | 
*MediaLibraryApi* | [**test_external_transcoder_connection**](docs/MediaLibraryApi#test_external_transcoder_connection) | **POST** `/api/2/media/external-transcoders/test-connection` | 
*MediaLibraryApi* | [**transition_workflow**](docs/MediaLibraryApi#transition_workflow) | **POST** `/api/2/media/workflow/transition` | 
*MediaLibraryApi* | [**unbookmark_media_directory**](docs/MediaLibraryApi#unbookmark_media_directory) | **DELETE** `/api/2/media/files/{id}/bookmark` | 
*MediaLibraryApi* | [**unmark_media_directory_as_showroom**](docs/MediaLibraryApi#unmark_media_directory_as_showroom) | **DELETE** `/api/2/media/files/{id}/showroom` | 
*MediaLibraryApi* | [**unresolve_comment**](docs/MediaLibraryApi#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
*MediaLibraryApi* | [**update_asset**](docs/MediaLibraryApi#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**update_asset_rating**](docs/MediaLibraryApi#update_asset_rating) | **PUT** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**update_asset_subtitle_link**](docs/MediaLibraryApi#update_asset_subtitle_link) | **PUT** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**update_comment**](docs/MediaLibraryApi#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**update_custom_field**](docs/MediaLibraryApi#update_custom_field) | **PUT** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**update_editor_project**](docs/MediaLibraryApi#update_editor_project) | **PUT** `/api/2/media/editor/{id}` | 
*MediaLibraryApi* | [**update_editor_subtitle**](docs/MediaLibraryApi#update_editor_subtitle) | **PUT** `/api/2/media/subtitles/{id}` | 
*MediaLibraryApi* | [**update_external_transcoder**](docs/MediaLibraryApi#update_external_transcoder) | **PUT** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**update_marker**](docs/MediaLibraryApi#update_marker) | **PUT** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**update_media_file**](docs/MediaLibraryApi#update_media_file) | **PUT** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**update_media_file_template**](docs/MediaLibraryApi#update_media_file_template) | **PUT** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**update_media_root**](docs/MediaLibraryApi#update_media_root) | **PUT** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**update_media_root_cover_image**](docs/MediaLibraryApi#update_media_root_cover_image) | **POST** `/api/2/media/roots/{id}/cover` | 
*MediaLibraryApi* | [**update_media_root_permission**](docs/MediaLibraryApi#update_media_root_permission) | **PUT** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**update_media_tag**](docs/MediaLibraryApi#update_media_tag) | **PUT** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**update_proxy_profile**](docs/MediaLibraryApi#update_proxy_profile) | **PUT** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**update_proxy_profile_watermark_image**](docs/MediaLibraryApi#update_proxy_profile_watermark_image) | **POST** `/api/2/media/proxy-profiles/{id}/watermark` | 
*MediaLibraryApi* | [**update_saved_search**](docs/MediaLibraryApi#update_saved_search) | **PUT** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**update_sharing_permission_preset**](docs/MediaLibraryApi#update_sharing_permission_preset) | **PUT** `/api/2/media/sharing-permission-presets/{id}` | 
*MediaLibraryApi* | [**update_subclip**](docs/MediaLibraryApi#update_subclip) | **PUT** `/api/2/media/subclips/{id}` | 
*PrivateApi* | [**export_non_proxied_assets**](docs/PrivateApi#export_non_proxied_assets) | **GET** `/api/2/private/export/non-proxied/{root_id}` | 
*PrivateApi* | [**export_non_proxied_assets_for_path**](docs/PrivateApi#export_non_proxied_assets_for_path) | **GET** `/api/2/private/export/non-proxied/{root_id}/{path}` | 
*PrivateApi* | [**export_updates**](docs/PrivateApi#export_updates) | **GET** `/api/2/private/export/updates/{root_id}` | 
*PrivateApi* | [**fast_lane_login_page**](docs/PrivateApi#fast_lane_login_page) | **GET** `/auth/fast-lane/{token}` | 
*PrivateApi* | [**fast_lane_login_with_password**](docs/PrivateApi#fast_lane_login_with_password) | **POST** `/auth/fast-lane/{token}` | 
*PrivateApi* | [**get**](docs/PrivateApi#get) | **GET** `/api/2/private/bootstrap` | 
*PrivateApi* | [**get_client_side_url**](docs/PrivateApi#get_client_side_url) | **POST** `/api/2/private/client-side-url` | 
*PrivateApi* | [**get_help_page**](docs/PrivateApi#get_help_page) | **GET** `/api/2/help/{id}` | 
*PrivateApi* | [**get_locale**](docs/PrivateApi#get_locale) | **GET** `/api/2/private/locale/{lang}` | 
*PrivateApi* | [**get_proxy_fs_size**](docs/PrivateApi#get_proxy_fs_size) | **GET** `/api/2/private/media/proxyfs-size` | 
*PrivateApi* | [**get_stored_image**](docs/PrivateApi#get_stored_image) | **GET** `/api/2/image/{name}` | 
*PrivateApi* | [**install_license**](docs/PrivateApi#install_license) | **POST** `/api/2/license/install` | 
*PrivateApi* | [**language_server_request**](docs/PrivateApi#language_server_request) | **POST** `/api/2/language-server/{language}` | 
*PrivateApi* | [**locate_file**](docs/PrivateApi#locate_file) | **POST** `/api/2/private/locate` | 
*PrivateApi* | [**locate_markers**](docs/PrivateApi#locate_markers) | **POST** `/api/2/panel/locate-markers` | 
*PrivateApi* | [**locate_proxies**](docs/PrivateApi#locate_proxies) | **POST** `/api/2/panel/locate-proxies` | 
*PrivateApi* | [**start_benchmark_session**](docs/PrivateApi#start_benchmark_session) | **POST** `/api/2/private/benchmark` | 
*PrivateApi* | [**submit_node_status**](docs/PrivateApi#submit_node_status) | **POST** `/api/2/private/node-stats` | 
*SharedstorageApi* | [**get_shared_storage_value**](docs/SharedstorageApi#get_shared_storage_value) | **GET** `/api/2/private/shared-storage/{name}` | 
*SharedstorageApi* | [**get_user_storage_value**](docs/SharedstorageApi#get_user_storage_value) | **GET** `/api/2/private/user-storage/{name}` | 
*SharedstorageApi* | [**set_shared_storage_value**](docs/SharedstorageApi#set_shared_storage_value) | **POST** `/api/2/private/shared-storage/{name}` | 
*SharedstorageApi* | [**set_user_storage_value**](docs/SharedstorageApi#set_user_storage_value) | **POST** `/api/2/private/user-storage/{name}` | 
*StatusApi* | [**get_alert**](docs/StatusApi#get_alert) | **GET** `/api/2/alerts/{id}` | 
*StatusApi* | [**get_all_alerts**](docs/StatusApi#get_all_alerts) | **GET** `/api/2/alerts` | 
*StatusApi* | [**get_telegraf_stats**](docs/StatusApi#get_telegraf_stats) | **GET** `/api/2/telegraf-stats` | 
*StatusApi* | [**patch_alert**](docs/StatusApi#patch_alert) | **PATCH** `/api/2/alerts/{id}` | 
*StatusApi* | [**submit_kapacitor_alert**](docs/StatusApi#submit_kapacitor_alert) | **POST** `/api/2/alerts/submit` | 
*StatusApi* | [**update_alert**](docs/StatusApi#update_alert) | **PUT** `/api/2/alerts/{id}` | 
*StorageApi* | [**apply_workspace_affinity**](docs/StorageApi#apply_workspace_affinity) | **POST** `/api/2/workspaces/{id}/apply-affinity` | 
*StorageApi* | [**authorize_cloud_workspace**](docs/StorageApi#authorize_cloud_workspace) | **POST** `/api/2/workspaces/{id}/authorize-cloud-mount` | 
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
*StorageApi* | [**create_volume**](docs/StorageApi#create_volume) | **POST** `/api/2/volumes` | 
*StorageApi* | [**create_workspace**](docs/StorageApi#create_workspace) | **POST** `/api/2/workspaces` | 
*StorageApi* | [**create_workspace_permission**](docs/StorageApi#create_workspace_permission) | **POST** `/api/2/workspace-permissions` | 
*StorageApi* | [**delete_file**](docs/StorageApi#delete_file) | **DELETE** `/api/2/files/{path}` | 
*StorageApi* | [**delete_files**](docs/StorageApi#delete_files) | **POST** `/api/2/filesystem/delete` | 
*StorageApi* | [**delete_path_quota**](docs/StorageApi#delete_path_quota) | **DELETE** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**delete_production**](docs/StorageApi#delete_production) | **DELETE** `/api/2/productions/{id}` | 
*StorageApi* | [**delete_share**](docs/StorageApi#delete_share) | **DELETE** `/api/2/shares/{id}` | 
*StorageApi* | [**delete_snapshot**](docs/StorageApi#delete_snapshot) | **DELETE** `/api/2/snapshots/{id}` | 
*StorageApi* | [**delete_volume**](docs/StorageApi#delete_volume) | **DELETE** `/api/2/volumes/{id}` | 
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
*StorageApi* | [**get_samba_dfree_string**](docs/StorageApi#get_samba_dfree_string) | **POST** `/api/2/private/dfree` | 
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
*StorageApi* | [**record_storage_trace**](docs/StorageApi#record_storage_trace) | **POST** `/api/2/filesystem/trace` | 
*StorageApi* | [**repair_workspace_permissions**](docs/StorageApi#repair_workspace_permissions) | **POST** `/api/2/workspaces/{id}/repair-permissions` | 
*StorageApi* | [**share_to_home_workspace**](docs/StorageApi#share_to_home_workspace) | **POST** `/api/2/share-to-home-workspace` | 
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
*TapeArchiveApi* | [**archive_to_tape**](docs/TapeArchiveApi#archive_to_tape) | **POST** `/api/2/archive/tape/archive` | 
*TapeArchiveApi* | [**cancel_all_tape_archive_jobs**](docs/TapeArchiveApi#cancel_all_tape_archive_jobs) | **POST** `/api/2/archive/tape/jobs/cancel-all` | 
*TapeArchiveApi* | [**cancel_tape_archive_job**](docs/TapeArchiveApi#cancel_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/cancel` | 
*TapeArchiveApi* | [**check_tape**](docs/TapeArchiveApi#check_tape) | **POST** `/api/2/archive/tape/library/check` | 
*TapeArchiveApi* | [**create_tape**](docs/TapeArchiveApi#create_tape) | **POST** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**create_tape_group**](docs/TapeArchiveApi#create_tape_group) | **POST** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**delete_tape**](docs/TapeArchiveApi#delete_tape) | **DELETE** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**delete_tape_archive_job**](docs/TapeArchiveApi#delete_tape_archive_job) | **DELETE** `/api/2/archive/tape/jobs/{id}` | 
*TapeArchiveApi* | [**delete_tape_group**](docs/TapeArchiveApi#delete_tape_group) | **DELETE** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**format_tape**](docs/TapeArchiveApi#format_tape) | **POST** `/api/2/archive/tape/library/format` | 
*TapeArchiveApi* | [**get_all_archived_file_entries**](docs/TapeArchiveApi#get_all_archived_file_entries) | **GET** `/api/2/archive/tape/files` | 
*TapeArchiveApi* | [**get_all_tape_archive_jobs**](docs/TapeArchiveApi#get_all_tape_archive_jobs) | **GET** `/api/2/archive/tape/jobs` | 
*TapeArchiveApi* | [**get_all_tape_groups**](docs/TapeArchiveApi#get_all_tape_groups) | **GET** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**get_all_tapes**](docs/TapeArchiveApi#get_all_tapes) | **GET** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**get_archived_file_entry**](docs/TapeArchiveApi#get_archived_file_entry) | **GET** `/api/2/archive/tape/files/{id}` | 
*TapeArchiveApi* | [**get_tape**](docs/TapeArchiveApi#get_tape) | **GET** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**get_tape_archive_job**](docs/TapeArchiveApi#get_tape_archive_job) | **GET** `/api/2/archive/tape/jobs/{id}` | 
*TapeArchiveApi* | [**get_tape_archive_job_sources**](docs/TapeArchiveApi#get_tape_archive_job_sources) | **GET** `/api/2/archive/tape/jobs/{id}/sources` | 
*TapeArchiveApi* | [**get_tape_group**](docs/TapeArchiveApi#get_tape_group) | **GET** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**get_tape_library_state**](docs/TapeArchiveApi#get_tape_library_state) | **GET** `/api/2/archive/tape/library` | 
*TapeArchiveApi* | [**load_tape**](docs/TapeArchiveApi#load_tape) | **POST** `/api/2/archive/tape/library/load` | 
*TapeArchiveApi* | [**move_tape**](docs/TapeArchiveApi#move_tape) | **POST** `/api/2/archive/tape/library/move` | 
*TapeArchiveApi* | [**patch_tape**](docs/TapeArchiveApi#patch_tape) | **PATCH** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**patch_tape_group**](docs/TapeArchiveApi#patch_tape_group) | **PATCH** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**pause_tape_archive_job**](docs/TapeArchiveApi#pause_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/pause` | 
*TapeArchiveApi* | [**refresh_tape_library_state**](docs/TapeArchiveApi#refresh_tape_library_state) | **POST** `/api/2/archive/tape/library/refresh` | 
*TapeArchiveApi* | [**reindex_tape**](docs/TapeArchiveApi#reindex_tape) | **POST** `/api/2/archive/tape/library/reindex` | 
*TapeArchiveApi* | [**remove_finished_tape_archive_jobs**](docs/TapeArchiveApi#remove_finished_tape_archive_jobs) | **POST** `/api/2/archive/tape/jobs/remove-finished` | 
*TapeArchiveApi* | [**restart_tape_archive_job**](docs/TapeArchiveApi#restart_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/restart` | 
*TapeArchiveApi* | [**restore_from_tape**](docs/TapeArchiveApi#restore_from_tape) | **POST** `/api/2/archive/tape/restore` | 
*TapeArchiveApi* | [**resume_tape_archive_job**](docs/TapeArchiveApi#resume_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/resume` | 
*TapeArchiveApi* | [**search_tape_archive**](docs/TapeArchiveApi#search_tape_archive) | **POST** `/api/2/archive/tape/search` | 
*TapeArchiveApi* | [**unload_tape**](docs/TapeArchiveApi#unload_tape) | **POST** `/api/2/archive/tape/library/unload` | 
*TapeArchiveApi* | [**update_tape**](docs/TapeArchiveApi#update_tape) | **PUT** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**update_tape_group**](docs/TapeArchiveApi#update_tape_group) | **PUT** `/api/2/archive/tape/groups/{id}` | 


## Models

 - [AIAnnotation](docs/AIAnnotation)
 - [AIAnnotationCreateRequest](docs/AIAnnotationCreateRequest)
 - [AIAnnotationPartialUpdate](docs/AIAnnotationPartialUpdate)
 - [AIAnnotationUpdate](docs/AIAnnotationUpdate)
 - [AICategory](docs/AICategory)
 - [AICategoryDetail](docs/AICategoryDetail)
 - [AICategoryDetailPartialUpdate](docs/AICategoryDetailPartialUpdate)
 - [AICategoryDetailUpdate](docs/AICategoryDetailUpdate)
 - [AICategoryMini](docs/AICategoryMini)
 - [AICategoryMiniReference](docs/AICategoryMiniReference)
 - [AICombinedInferenceResult](docs/AICombinedInferenceResult)
 - [AIConnection](docs/AIConnection)
 - [AIDataset](docs/AIDataset)
 - [AIDatasetDetailReference](docs/AIDatasetDetailReference)
 - [AIDatasetExportRequest](docs/AIDatasetExportRequest)
 - [AIDatasetExportResponse](docs/AIDatasetExportResponse)
 - [AIDatasetReference](docs/AIDatasetReference)
 - [AIDatasetWithPreview](docs/AIDatasetWithPreview)
 - [AIDatasetWithPreviewPartialUpdate](docs/AIDatasetWithPreviewPartialUpdate)
 - [AIDatasetWithPreviewUpdate](docs/AIDatasetWithPreviewUpdate)
 - [AIImage](docs/AIImage)
 - [AIImageReference](docs/AIImageReference)
 - [AIInferencePosition](docs/AIInferencePosition)
 - [AIMetadata](docs/AIMetadata)
 - [AIModel](docs/AIModel)
 - [AIModelExportRequest](docs/AIModelExportRequest)
 - [AIModelExportResponse](docs/AIModelExportResponse)
 - [AIModelInferenceRequest](docs/AIModelInferenceRequest)
 - [AIModelInferenceResponse](docs/AIModelInferenceResponse)
 - [AIModelPartialUpdate](docs/AIModelPartialUpdate)
 - [AIModelProgress](docs/AIModelProgress)
 - [AIModelTrainingRequest](docs/AIModelTrainingRequest)
 - [AIModelUpdate](docs/AIModelUpdate)
 - [AIProcessingRequest](docs/AIProcessingRequest)
 - [APIToken](docs/APIToken)
 - [APITokenPartialUpdate](docs/APITokenPartialUpdate)
 - [APITokenUpdate](docs/APITokenUpdate)
 - [APITokenWithSecret](docs/APITokenWithSecret)
 - [APITokenWithSecretUpdate](docs/APITokenWithSecretUpdate)
 - [AddAssetsToClickGallery](docs/AddAssetsToClickGallery)
 - [Address](docs/Address)
 - [Alert](docs/Alert)
 - [AlertPartialUpdate](docs/AlertPartialUpdate)
 - [AlertUpdate](docs/AlertUpdate)
 - [AllMediaFilesForBundlesRequest](docs/AllMediaFilesForBundlesRequest)
 - [ArchiveEndpointRequest](docs/ArchiveEndpointRequest)
 - [ArgumentType](docs/ArgumentType)
 - [Asset](docs/Asset)
 - [AssetBackup](docs/AssetBackup)
 - [AssetCloudLink](docs/AssetCloudLink)
 - [AssetMini](docs/AssetMini)
 - [AssetMiniReference](docs/AssetMiniReference)
 - [AssetPartialUpdate](docs/AssetPartialUpdate)
 - [AssetProjectLink](docs/AssetProjectLink)
 - [AssetRating](docs/AssetRating)
 - [AssetRatingPartialUpdate](docs/AssetRatingPartialUpdate)
 - [AssetRatingUpdate](docs/AssetRatingUpdate)
 - [AssetSubtitleLink](docs/AssetSubtitleLink)
 - [AssetSubtitleLinkPartialUpdate](docs/AssetSubtitleLinkPartialUpdate)
 - [AssetSubtitleLinkUpdate](docs/AssetSubtitleLinkUpdate)
 - [AssetUpdate](docs/AssetUpdate)
 - [AuthFastLaneEndpointRequest](docs/AuthFastLaneEndpointRequest)
 - [AuthFastLaneEndpointResponse](docs/AuthFastLaneEndpointResponse)
 - [AuthLoginEndpointRequest](docs/AuthLoginEndpointRequest)
 - [AuthLoginEndpointResponse](docs/AuthLoginEndpointResponse)
 - [Backend](docs/Backend)
 - [BackendProperties](docs/BackendProperties)
 - [BasicFile](docs/BasicFile)
 - [BeeGFSNode](docs/BeeGFSNode)
 - [BeeGFSTarget](docs/BeeGFSTarget)
 - [BenchmarkEndpointRequest](docs/BenchmarkEndpointRequest)
 - [BootstrapData](docs/BootstrapData)
 - [CPUStat](docs/CPUStat)
 - [Certificate](docs/Certificate)
 - [CertificateUpdate](docs/CertificateUpdate)
 - [ChangeOwnPasswordRequest](docs/ChangeOwnPasswordRequest)
 - [ChangePasswordRequest](docs/ChangePasswordRequest)
 - [CheckConnectivityEndpointResponse](docs/CheckConnectivityEndpointResponse)
 - [ClickBackgroundUploadEndpointRequest](docs/ClickBackgroundUploadEndpointRequest)
 - [ClickGallery](docs/ClickGallery)
 - [ClickGalleryLink](docs/ClickGalleryLink)
 - [ClickGalleryUpdate](docs/ClickGalleryUpdate)
 - [ClickLinkUser](docs/ClickLinkUser)
 - [ClickStartUploadEndpointRequest](docs/ClickStartUploadEndpointRequest)
 - [ClientSession](docs/ClientSession)
 - [ClientSidePathEndpointRequest](docs/ClientSidePathEndpointRequest)
 - [ClientSidePathEndpointResponse](docs/ClientSidePathEndpointResponse)
 - [ClientsEndpointResponse](docs/ClientsEndpointResponse)
 - [CloudAccount](docs/CloudAccount)
 - [CloudAccountMini](docs/CloudAccountMini)
 - [CloudAccountMiniPartialUpdate](docs/CloudAccountMiniPartialUpdate)
 - [CloudAccountMiniUpdate](docs/CloudAccountMiniUpdate)
 - [CloudAccountPartialUpdate](docs/CloudAccountPartialUpdate)
 - [CloudAccountUpdate](docs/CloudAccountUpdate)
 - [CloudBucketCosts](docs/CloudBucketCosts)
 - [CloudConnection](docs/CloudConnection)
 - [CloudMountAuthorization](docs/CloudMountAuthorization)
 - [CloudStorageCosts](docs/CloudStorageCosts)
 - [Comment](docs/Comment)
 - [CommentPartialUpdate](docs/CommentPartialUpdate)
 - [CommentUpdate](docs/CommentUpdate)
 - [Cost](docs/Cost)
 - [CreateDownloadArchive](docs/CreateDownloadArchive)
 - [CreateHomeWorkspaceRequest](docs/CreateHomeWorkspaceRequest)
 - [CreatePathQuotaRequest](docs/CreatePathQuotaRequest)
 - [CustomField](docs/CustomField)
 - [CustomFieldPartialUpdate](docs/CustomFieldPartialUpdate)
 - [CustomFieldReference](docs/CustomFieldReference)
 - [CustomFieldUpdate](docs/CustomFieldUpdate)
 - [DeletedWorkspace](docs/DeletedWorkspace)
 - [Download](docs/Download)
 - [DownloadArchive](docs/DownloadArchive)
 - [DownloadArchivePartialUpdate](docs/DownloadArchivePartialUpdate)
 - [DownloadArchiveUpdate](docs/DownloadArchiveUpdate)
 - [EditorMarker](docs/EditorMarker)
 - [EditorProject](docs/EditorProject)
 - [EditorProjectPartialUpdate](docs/EditorProjectPartialUpdate)
 - [EditorProjectUpdate](docs/EditorProjectUpdate)
 - [EditorSubtitle](docs/EditorSubtitle)
 - [EditorSubtitlePartialUpdate](docs/EditorSubtitlePartialUpdate)
 - [EditorSubtitleUpdate](docs/EditorSubtitleUpdate)
 - [ElementsGroup](docs/ElementsGroup)
 - [ElementsGroupDetail](docs/ElementsGroupDetail)
 - [ElementsGroupDetailPartialUpdate](docs/ElementsGroupDetailPartialUpdate)
 - [ElementsGroupDetailUpdate](docs/ElementsGroupDetailUpdate)
 - [ElementsGroupReference](docs/ElementsGroupReference)
 - [ElementsUser](docs/ElementsUser)
 - [ElementsUserDetail](docs/ElementsUserDetail)
 - [ElementsUserDetailPartialUpdate](docs/ElementsUserDetailPartialUpdate)
 - [ElementsUserDetailUpdate](docs/ElementsUserDetailUpdate)
 - [ElementsUserMini](docs/ElementsUserMini)
 - [ElementsUserMiniReference](docs/ElementsUserMiniReference)
 - [ElementsUserProfile](docs/ElementsUserProfile)
 - [ElementsUserProfilePartialUpdate](docs/ElementsUserProfilePartialUpdate)
 - [ElementsUserProfileUpdate](docs/ElementsUserProfileUpdate)
 - [ElementsUserReference](docs/ElementsUserReference)
 - [ElementsVersion](docs/ElementsVersion)
 - [EmailPreviewRequest](docs/EmailPreviewRequest)
 - [EmailPreviewResponse](docs/EmailPreviewResponse)
 - [EnableTOTPRequest](docs/EnableTOTPRequest)
 - [Event](docs/Event)
 - [ExternalTranscoder](docs/ExternalTranscoder)
 - [ExternalTranscoderPartialUpdate](docs/ExternalTranscoderPartialUpdate)
 - [ExternalTranscoderUpdate](docs/ExternalTranscoderUpdate)
 - [ExtractRequest](docs/ExtractRequest)
 - [FSProperties](docs/FSProperties)
 - [FileCopyEndpointRequest](docs/FileCopyEndpointRequest)
 - [FileDeleteEndpointRequest](docs/FileDeleteEndpointRequest)
 - [FileMoveEndpointRequest](docs/FileMoveEndpointRequest)
 - [FilePartialUpdate](docs/FilePartialUpdate)
 - [FileSizeDistribution](docs/FileSizeDistribution)
 - [FileSizeDistributionItem](docs/FileSizeDistributionItem)
 - [FileSizeEndpointResponse](docs/FileSizeEndpointResponse)
 - [FileUnzipEndpointRequest](docs/FileUnzipEndpointRequest)
 - [FileUpdate](docs/FileUpdate)
 - [FileZipEndpointRequest](docs/FileZipEndpointRequest)
 - [FilesystemFile](docs/FilesystemFile)
 - [FilesystemPermission](docs/FilesystemPermission)
 - [FilesystemPermissionPartialUpdate](docs/FilesystemPermissionPartialUpdate)
 - [FilesystemPermissionUpdate](docs/FilesystemPermissionUpdate)
 - [FilesystemTraceEndpointRequest](docs/FilesystemTraceEndpointRequest)
 - [FilesystemTraceEndpointResponse](docs/FilesystemTraceEndpointResponse)
 - [FinishUploadEndpointRequest](docs/FinishUploadEndpointRequest)
 - [FormatMetadata](docs/FormatMetadata)
 - [GeneratePasswordEndpointResponse](docs/GeneratePasswordEndpointResponse)
 - [GenerateProxiesRequest](docs/GenerateProxiesRequest)
 - [GetCloudAccountCostsResponse](docs/GetCloudAccountCostsResponse)
 - [GetCloudAccountVolumeSizesResponse](docs/GetCloudAccountVolumeSizesResponse)
 - [GetMultipleBundlesRequest](docs/GetMultipleBundlesRequest)
 - [GetMultipleFilesRequest](docs/GetMultipleFilesRequest)
 - [GlobalAlert](docs/GlobalAlert)
 - [HelpEndpointResponse](docs/HelpEndpointResponse)
 - [IOStat](docs/IOStat)
 - [ImageUploadRequest](docs/ImageUploadRequest)
 - [ImpersonationEndpointRequest](docs/ImpersonationEndpointRequest)
 - [ImportAIDatasetRequest](docs/ImportAIDatasetRequest)
 - [ImportAIDatasetResponse](docs/ImportAIDatasetResponse)
 - [ImportAIModelRequest](docs/ImportAIModelRequest)
 - [ImportAIModelResponse](docs/ImportAIModelResponse)
 - [ImportJobRequest](docs/ImportJobRequest)
 - [ImportJobResponse](docs/ImportJobResponse)
 - [InlineResponse200](docs/InlineResponse200)
 - [InstallLicenseEndpointRequest](docs/InstallLicenseEndpointRequest)
 - [InstantiateFileTemplateRequest](docs/InstantiateFileTemplateRequest)
 - [Interface](docs/Interface)
 - [Ipmi](docs/Ipmi)
 - [Job](docs/Job)
 - [JobDetail](docs/JobDetail)
 - [JobDetailPartialUpdate](docs/JobDetailPartialUpdate)
 - [JobDetailUpdate](docs/JobDetailUpdate)
 - [JobReference](docs/JobReference)
 - [KapacitorAlert](docs/KapacitorAlert)
 - [LDAPServer](docs/LDAPServer)
 - [LDAPServerGroup](docs/LDAPServerGroup)
 - [LDAPServerGroups](docs/LDAPServerGroups)
 - [LDAPServerReference](docs/LDAPServerReference)
 - [LDAPServerUser](docs/LDAPServerUser)
 - [LDAPServerUsers](docs/LDAPServerUsers)
 - [License](docs/License)
 - [ListTopics](docs/ListTopics)
 - [LizardFSDisk](docs/LizardFSDisk)
 - [LizardFSNode](docs/LizardFSNode)
 - [LocaleEndpointResponse](docs/LocaleEndpointResponse)
 - [LocateEndpointRequest](docs/LocateEndpointRequest)
 - [LocateMarkersEndpointRequest](docs/LocateMarkersEndpointRequest)
 - [LocateMarkersEndpointResponse](docs/LocateMarkersEndpointResponse)
 - [LocateProxiesEndpointRequest](docs/LocateProxiesEndpointRequest)
 - [LocateProxiesEndpointResponse](docs/LocateProxiesEndpointResponse)
 - [LocateResult](docs/LocateResult)
 - [Marker](docs/Marker)
 - [MarkerPartialUpdate](docs/MarkerPartialUpdate)
 - [MarkerUpdate](docs/MarkerUpdate)
 - [MediaFile](docs/MediaFile)
 - [MediaFileBundle](docs/MediaFileBundle)
 - [MediaFileBundleMini](docs/MediaFileBundleMini)
 - [MediaFileBundleMiniReference](docs/MediaFileBundleMiniReference)
 - [MediaFileContents](docs/MediaFileContents)
 - [MediaFileMini](docs/MediaFileMini)
 - [MediaFilePartialUpdate](docs/MediaFilePartialUpdate)
 - [MediaFileReference](docs/MediaFileReference)
 - [MediaFileTemplate](docs/MediaFileTemplate)
 - [MediaFileTemplatePartialUpdate](docs/MediaFileTemplatePartialUpdate)
 - [MediaFileTemplateUpdate](docs/MediaFileTemplateUpdate)
 - [MediaFileUpdate](docs/MediaFileUpdate)
 - [MediaFilesLookupRequest](docs/MediaFilesLookupRequest)
 - [MediaLibraryDeleteRequest](docs/MediaLibraryDeleteRequest)
 - [MediaLibraryShareRequest](docs/MediaLibraryShareRequest)
 - [MediaRoot](docs/MediaRoot)
 - [MediaRootDetail](docs/MediaRootDetail)
 - [MediaRootDetailPartialUpdate](docs/MediaRootDetailPartialUpdate)
 - [MediaRootDetailUpdate](docs/MediaRootDetailUpdate)
 - [MediaRootMini](docs/MediaRootMini)
 - [MediaRootMiniReference](docs/MediaRootMiniReference)
 - [MediaRootPermission](docs/MediaRootPermission)
 - [MediaRootPermissionAccessOptions](docs/MediaRootPermissionAccessOptions)
 - [MediaRootPermissionPartialUpdate](docs/MediaRootPermissionPartialUpdate)
 - [MediaRootPermissionUpdate](docs/MediaRootPermissionUpdate)
 - [MediaRootUpdate](docs/MediaRootUpdate)
 - [MediaUpdate](docs/MediaUpdate)
 - [MemberPreview](docs/MemberPreview)
 - [MetadataItem](docs/MetadataItem)
 - [MoveWorkspaceRequest](docs/MoveWorkspaceRequest)
 - [MultipleAssetsRequest](docs/MultipleAssetsRequest)
 - [NFSPermission](docs/NFSPermission)
 - [NTPServer](docs/NTPServer)
 - [NTPServerPartialUpdate](docs/NTPServerPartialUpdate)
 - [NTPServerUpdate](docs/NTPServerUpdate)
 - [NetStat](docs/NetStat)
 - [Notification](docs/Notification)
 - [NotificationPartialUpdate](docs/NotificationPartialUpdate)
 - [NotificationReceipt](docs/NotificationReceipt)
 - [NotificationReceiptPartialUpdate](docs/NotificationReceiptPartialUpdate)
 - [NotificationReceiptReference](docs/NotificationReceiptReference)
 - [NotificationReceiptUpdate](docs/NotificationReceiptUpdate)
 - [NotificationSetting](docs/NotificationSetting)
 - [NotificationSettingPartialUpdate](docs/NotificationSettingPartialUpdate)
 - [NotificationSettingUpdate](docs/NotificationSettingUpdate)
 - [NotificationUpdate](docs/NotificationUpdate)
 - [OneTimeAccessToken](docs/OneTimeAccessToken)
 - [OneTimeAccessTokenActivity](docs/OneTimeAccessTokenActivity)
 - [OneTimeAccessTokenSharedObject](docs/OneTimeAccessTokenSharedObject)
 - [Parameters](docs/Parameters)
 - [ParametersUpdate](docs/ParametersUpdate)
 - [ParseSAMLIDPMetadataRequest](docs/ParseSAMLIDPMetadataRequest)
 - [ParsedSAMLIDPMetadata](docs/ParsedSAMLIDPMetadata)
 - [PasswordResetEndpointRequest](docs/PasswordResetEndpointRequest)
 - [Path](docs/Path)
 - [PathInput](docs/PathInput)
 - [Production](docs/Production)
 - [ProductionMiniReference](docs/ProductionMiniReference)
 - [ProductionPartialUpdate](docs/ProductionPartialUpdate)
 - [ProductionReference](docs/ProductionReference)
 - [ProductionUpdate](docs/ProductionUpdate)
 - [Proxy](docs/Proxy)
 - [ProxyCount](docs/ProxyCount)
 - [ProxyFSSizeEndpointResponse](docs/ProxyFSSizeEndpointResponse)
 - [ProxyGenerator](docs/ProxyGenerator)
 - [ProxyGeneratorProperties](docs/ProxyGeneratorProperties)
 - [ProxyProfile](docs/ProxyProfile)
 - [ProxyProfileMini](docs/ProxyProfileMini)
 - [ProxyProfilePartialUpdate](docs/ProxyProfilePartialUpdate)
 - [ProxyProfileUpdate](docs/ProxyProfileUpdate)
 - [PublicParameters](docs/PublicParameters)
 - [PythonEnvironment](docs/PythonEnvironment)
 - [Queue](docs/Queue)
 - [Quota](docs/Quota)
 - [RAMStat](docs/RAMStat)
 - [RegisterUploadEndpointRequest](docs/RegisterUploadEndpointRequest)
 - [RegisterUploadMetadataEndpointRequest](docs/RegisterUploadMetadataEndpointRequest)
 - [ReleaseNotesEndpointResponse](docs/ReleaseNotesEndpointResponse)
 - [RenameCustomFieldRequest](docs/RenameCustomFieldRequest)
 - [RenderEndpointRequest](docs/RenderEndpointRequest)
 - [RenderRequest](docs/RenderRequest)
 - [RestoreEndpointRequest](docs/RestoreEndpointRequest)
 - [RestrictedOneTimeAccessToken](docs/RestrictedOneTimeAccessToken)
 - [SAMLProvider](docs/SAMLProvider)
 - [SAMLProviderMini](docs/SAMLProviderMini)
 - [SAMLProviderPartialUpdate](docs/SAMLProviderPartialUpdate)
 - [SAMLProviderUpdate](docs/SAMLProviderUpdate)
 - [SMTPConfiguration](docs/SMTPConfiguration)
 - [SMTPConfigurationUpdate](docs/SMTPConfigurationUpdate)
 - [SNFSStripeGroup](docs/SNFSStripeGroup)
 - [SavedSearch](docs/SavedSearch)
 - [SavedSearchPartialUpdate](docs/SavedSearchPartialUpdate)
 - [SavedSearchUpdate](docs/SavedSearchUpdate)
 - [ScannerDiscoverEndpointRequest](docs/ScannerDiscoverEndpointRequest)
 - [ScannerScanEndpointRequest](docs/ScannerScanEndpointRequest)
 - [Schedule](docs/Schedule)
 - [SchedulePartialUpdate](docs/SchedulePartialUpdate)
 - [ScheduleReference](docs/ScheduleReference)
 - [ScheduleUpdate](docs/ScheduleUpdate)
 - [SearchEndpointRequest](docs/SearchEndpointRequest)
 - [SearchEndpointResponse](docs/SearchEndpointResponse)
 - [SendLinkEmailRequest](docs/SendLinkEmailRequest)
 - [Sensor](docs/Sensor)
 - [Sensors](docs/Sensors)
 - [ServiceStatus](docs/ServiceStatus)
 - [Share](docs/Share)
 - [SharePartialUpdate](docs/SharePartialUpdate)
 - [ShareToHomeWorkspaceEndpointRequest](docs/ShareToHomeWorkspaceEndpointRequest)
 - [ShareUpdate](docs/ShareUpdate)
 - [SharingPermissionPreset](docs/SharingPermissionPreset)
 - [SharingPermissionPresetPartialUpdate](docs/SharingPermissionPresetPartialUpdate)
 - [SharingPermissionPresetUpdate](docs/SharingPermissionPresetUpdate)
 - [SlackChannel](docs/SlackChannel)
 - [SlackConnection](docs/SlackConnection)
 - [SlackConnectionPartialUpdate](docs/SlackConnectionPartialUpdate)
 - [SlackConnectionStatus](docs/SlackConnectionStatus)
 - [SlackConnectionUpdate](docs/SlackConnectionUpdate)
 - [SlackEmoji](docs/SlackEmoji)
 - [SlackMessage](docs/SlackMessage)
 - [SlackUser](docs/SlackUser)
 - [Snapshot](docs/Snapshot)
 - [SnapshotPartialUpdate](docs/SnapshotPartialUpdate)
 - [SnapshotUpdate](docs/SnapshotUpdate)
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
 - [StorageNodePartialUpdate](docs/StorageNodePartialUpdate)
 - [StorageNodeReference](docs/StorageNodeReference)
 - [StorageNodeStatus](docs/StorageNodeStatus)
 - [StorageNodeUpdate](docs/StorageNodeUpdate)
 - [StorageRequest](docs/StorageRequest)
 - [StorageResponse](docs/StorageResponse)
 - [StorageRoot](docs/StorageRoot)
 - [StornextLicense](docs/StornextLicense)
 - [StornextManagerAttributes](docs/StornextManagerAttributes)
 - [Subclip](docs/Subclip)
 - [SubclipClipboardEntry](docs/SubclipClipboardEntry)
 - [SubclipClipboardEntryUpdate](docs/SubclipClipboardEntryUpdate)
 - [SubclipPartialUpdate](docs/SubclipPartialUpdate)
 - [SubclipReference](docs/SubclipReference)
 - [SubclipUpdate](docs/SubclipUpdate)
 - [Subscription](docs/Subscription)
 - [Subtask](docs/Subtask)
 - [SubtaskPartialUpdate](docs/SubtaskPartialUpdate)
 - [SubtaskReference](docs/SubtaskReference)
 - [SubtaskUpdate](docs/SubtaskUpdate)
 - [Subtitle](docs/Subtitle)
 - [SubtitleClipboardEntry](docs/SubtitleClipboardEntry)
 - [SubtitleClipboardEntryUpdate](docs/SubtitleClipboardEntryUpdate)
 - [SubtitleEvent](docs/SubtitleEvent)
 - [SyncTOTP](docs/SyncTOTP)
 - [SyncTOTPRequest](docs/SyncTOTPRequest)
 - [SystemInfoEndpointResponse](docs/SystemInfoEndpointResponse)
 - [TagMediaDirectoryRequest](docs/TagMediaDirectoryRequest)
 - [TagReference](docs/TagReference)
 - [Tape](docs/Tape)
 - [TapeFile](docs/TapeFile)
 - [TapeGroup](docs/TapeGroup)
 - [TapeGroupPartialUpdate](docs/TapeGroupPartialUpdate)
 - [TapeGroupUpdate](docs/TapeGroupUpdate)
 - [TapeJob](docs/TapeJob)
 - [TapeJobSource](docs/TapeJobSource)
 - [TapeLibraryEndpointResponse](docs/TapeLibraryEndpointResponse)
 - [TapeLibraryFormatEndpointRequest](docs/TapeLibraryFormatEndpointRequest)
 - [TapeLibraryFsckEndpointRequest](docs/TapeLibraryFsckEndpointRequest)
 - [TapeLibraryLoadEndpointRequest](docs/TapeLibraryLoadEndpointRequest)
 - [TapeLibraryMoveEndpointRequest](docs/TapeLibraryMoveEndpointRequest)
 - [TapeLibraryReindexEndpointRequest](docs/TapeLibraryReindexEndpointRequest)
 - [TapeLibrarySlot](docs/TapeLibrarySlot)
 - [TapeLibraryUnloadEndpointRequest](docs/TapeLibraryUnloadEndpointRequest)
 - [TapeMiniReference](docs/TapeMiniReference)
 - [TapePartialUpdate](docs/TapePartialUpdate)
 - [TapeUpdate](docs/TapeUpdate)
 - [TaskInfo](docs/TaskInfo)
 - [TaskLog](docs/TaskLog)
 - [TaskLogEntry](docs/TaskLogEntry)
 - [TaskLogEntryData](docs/TaskLogEntryData)
 - [TaskLogV2](docs/TaskLogV2)
 - [TaskProgress](docs/TaskProgress)
 - [TaskType](docs/TaskType)
 - [TasksSummary](docs/TasksSummary)
 - [TeamsConnection](docs/TeamsConnection)
 - [TeamsConnectionPartialUpdate](docs/TeamsConnectionPartialUpdate)
 - [TeamsConnectionStatus](docs/TeamsConnectionStatus)
 - [TeamsConnectionUpdate](docs/TeamsConnectionUpdate)
 - [TeamsMessage](docs/TeamsMessage)
 - [TeamsRecipient](docs/TeamsRecipient)
 - [TestCloudAccountCredentialsRequest](docs/TestCloudAccountCredentialsRequest)
 - [TestCloudAccountCredentialsResponse](docs/TestCloudAccountCredentialsResponse)
 - [TestExternalTranscoderConnectionRequest](docs/TestExternalTranscoderConnectionRequest)
 - [TestExternalTranscoderConnectionResponse](docs/TestExternalTranscoderConnectionResponse)
 - [TestSMTP](docs/TestSMTP)
 - [Ticket](docs/Ticket)
 - [TimeEndpointRequest](docs/TimeEndpointRequest)
 - [TimeEndpointResponse](docs/TimeEndpointResponse)
 - [TimeSyncEndpointRequest](docs/TimeSyncEndpointRequest)
 - [TimeSyncEndpointResponse](docs/TimeSyncEndpointResponse)
 - [TimelineExportRequest](docs/TimelineExportRequest)
 - [Timezone](docs/Timezone)
 - [TraceNode](docs/TraceNode)
 - [TranscoderProfile](docs/TranscoderProfile)
 - [Transforms](docs/Transforms)
 - [TypeDocumentation](docs/TypeDocumentation)
 - [UnfilteredTag](docs/UnfilteredTag)
 - [UnfilteredTagPartialUpdate](docs/UnfilteredTagPartialUpdate)
 - [UnfilteredTagUpdate](docs/UnfilteredTagUpdate)
 - [UnreadCount](docs/UnreadCount)
 - [UnresolvedCount](docs/UnresolvedCount)
 - [UpdateQuotaRequest](docs/UpdateQuotaRequest)
 - [UpdatedFile](docs/UpdatedFile)
 - [UploadAIImageRequest](docs/UploadAIImageRequest)
 - [UploadChunkEndpointRequest](docs/UploadChunkEndpointRequest)
 - [VantageWorkflow](docs/VantageWorkflow)
 - [VantageWorkflows](docs/VantageWorkflows)
 - [Volume](docs/Volume)
 - [VolumeBeeGFSStatus](docs/VolumeBeeGFSStatus)
 - [VolumeLizardFSStatus](docs/VolumeLizardFSStatus)
 - [VolumeMini](docs/VolumeMini)
 - [VolumeMiniReference](docs/VolumeMiniReference)
 - [VolumePartialUpdate](docs/VolumePartialUpdate)
 - [VolumeReference](docs/VolumeReference)
 - [VolumeSNFSStatus](docs/VolumeSNFSStatus)
 - [VolumeStat](docs/VolumeStat)
 - [VolumeStats](docs/VolumeStats)
 - [VolumeStatus](docs/VolumeStatus)
 - [VolumeUpdate](docs/VolumeUpdate)
 - [WorkflowTransitionRequest](docs/WorkflowTransitionRequest)
 - [WorkflowTransitionResponse](docs/WorkflowTransitionResponse)
 - [Workspace](docs/Workspace)
 - [WorkspaceCheckIn](docs/WorkspaceCheckIn)
 - [WorkspaceDetail](docs/WorkspaceDetail)
 - [WorkspaceDetailPartialUpdate](docs/WorkspaceDetailPartialUpdate)
 - [WorkspaceDetailUpdate](docs/WorkspaceDetailUpdate)
 - [WorkspaceEndpoint](docs/WorkspaceEndpoint)
 - [WorkspaceMoveToRequest](docs/WorkspaceMoveToRequest)
 - [WorkspacePermission](docs/WorkspacePermission)
 - [WorkspacePermissionPartialUpdate](docs/WorkspacePermissionPartialUpdate)
 - [WorkspacePermissionUpdate](docs/WorkspacePermissionUpdate)
 - [WorkspaceResolvedPermission](docs/WorkspaceResolvedPermission)
 - [Workstation](docs/Workstation)
 - [WorkstationMini](docs/WorkstationMini)
 - [WorkstationPartialUpdate](docs/WorkstationPartialUpdate)
 - [WorkstationUpdate](docs/WorkstationUpdate)
 - [XMLExport](docs/XMLExport)


