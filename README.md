# ELEMENTS Python SDK

- API version: 2
- Python 2.7 and 3.4+
- Latest build: 3.5.4

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
*AIApi* | [**abort_ai_dataset_model_creation**](docs/AIApi.md#abort_ai_dataset_model_creation) | **POST** `/api/2/ai/models/{id}/abort` | 
*AIApi* | [**activate_ai_model**](docs/AIApi.md#activate_ai_model) | **POST** `/api/2/ai/models/{id}/activate` | 
*AIApi* | [**create_ai_annotation_track**](docs/AIApi.md#create_ai_annotation_track) | **POST** `/api/2/ai/annotations/tracks/create` | 
*AIApi* | [**create_ai_category**](docs/AIApi.md#create_ai_category) | **POST** `/api/2/ai/categories` | 
*AIApi* | [**create_ai_dataset**](docs/AIApi.md#create_ai_dataset) | **POST** `/api/2/ai/datasets` | 
*AIApi* | [**create_ai_dataset_model**](docs/AIApi.md#create_ai_dataset_model) | **POST** `/api/2/ai/models/create` | 
*AIApi* | [**create_ai_metadata**](docs/AIApi.md#create_ai_metadata) | **POST** `/api/2/ai/metadata/create` | 
*AIApi* | [**create_ai_model**](docs/AIApi.md#create_ai_model) | **POST** `/api/2/ai/models` | 
*AIApi* | [**delete_ai_annotation**](docs/AIApi.md#delete_ai_annotation) | **DELETE** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**delete_ai_annotation_track**](docs/AIApi.md#delete_ai_annotation_track) | **DELETE** `/api/2/ai/annotations/tracks/{id}` | 
*AIApi* | [**delete_ai_category**](docs/AIApi.md#delete_ai_category) | **DELETE** `/api/2/ai/categories/{id}` | 
*AIApi* | [**delete_ai_dataset**](docs/AIApi.md#delete_ai_dataset) | **DELETE** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**delete_ai_model**](docs/AIApi.md#delete_ai_model) | **DELETE** `/api/2/ai/models/{id}` | 
*AIApi* | [**export_ai_dataset**](docs/AIApi.md#export_ai_dataset) | **POST** `/api/2/ai/datasets/{id}/export` | 
*AIApi* | [**export_ai_model**](docs/AIApi.md#export_ai_model) | **POST** `/api/2/ai/models/{id}/export` | 
*AIApi* | [**get_ai_annotation**](docs/AIApi.md#get_ai_annotation) | **GET** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**get_ai_annotation_image**](docs/AIApi.md#get_ai_annotation_image) | **GET** `/api/2/ai/annotations/{id}/image` | 
*AIApi* | [**get_ai_category**](docs/AIApi.md#get_ai_category) | **GET** `/api/2/ai/categories/{id}` | 
*AIApi* | [**get_ai_connection**](docs/AIApi.md#get_ai_connection) | **GET** `/api/2/ai/connections/{id}` | 
*AIApi* | [**get_ai_dataset**](docs/AIApi.md#get_ai_dataset) | **GET** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**get_ai_image**](docs/AIApi.md#get_ai_image) | **GET** `/api/2/ai/images/{id}` | 
*AIApi* | [**get_ai_image_content**](docs/AIApi.md#get_ai_image_content) | **GET** `/api/2/ai/images/{id}/content` | 
*AIApi* | [**get_ai_metadata**](docs/AIApi.md#get_ai_metadata) | **GET** `/api/2/ai/metadata/{id}` | 
*AIApi* | [**get_ai_model**](docs/AIApi.md#get_ai_model) | **GET** `/api/2/ai/models/{id}` | 
*AIApi* | [**get_all_ai_annotation_tracks**](docs/AIApi.md#get_all_ai_annotation_tracks) | **GET** `/api/2/ai/annotations/tracks` | 
*AIApi* | [**get_all_ai_annotations**](docs/AIApi.md#get_all_ai_annotations) | **GET** `/api/2/ai/annotations` | 
*AIApi* | [**get_all_ai_categories**](docs/AIApi.md#get_all_ai_categories) | **GET** `/api/2/ai/categories` | 
*AIApi* | [**get_all_ai_connections**](docs/AIApi.md#get_all_ai_connections) | **GET** `/api/2/ai/connections` | 
*AIApi* | [**get_all_ai_datasets**](docs/AIApi.md#get_all_ai_datasets) | **GET** `/api/2/ai/datasets` | 
*AIApi* | [**get_all_ai_images**](docs/AIApi.md#get_all_ai_images) | **GET** `/api/2/ai/images` | 
*AIApi* | [**get_all_ai_metadata**](docs/AIApi.md#get_all_ai_metadata) | **GET** `/api/2/ai/metadata` | 
*AIApi* | [**get_all_ai_models**](docs/AIApi.md#get_all_ai_models) | **GET** `/api/2/ai/models` | 
*AIApi* | [**import_ai_datasets**](docs/AIApi.md#import_ai_datasets) | **POST** `/api/2/ai/datasets/import` | 
*AIApi* | [**import_ai_models**](docs/AIApi.md#import_ai_models) | **POST** `/api/2/ai/datasets/{id}/import-models` | 
*AIApi* | [**patch_ai_annotation**](docs/AIApi.md#patch_ai_annotation) | **PATCH** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**patch_ai_category**](docs/AIApi.md#patch_ai_category) | **PATCH** `/api/2/ai/categories/{id}` | 
*AIApi* | [**patch_ai_dataset**](docs/AIApi.md#patch_ai_dataset) | **PATCH** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**patch_ai_model**](docs/AIApi.md#patch_ai_model) | **PATCH** `/api/2/ai/models/{id}` | 
*AIApi* | [**run_ai_model_inference**](docs/AIApi.md#run_ai_model_inference) | **POST** `/api/2/ai/models/{id}/inference` | 
*AIApi* | [**update_ai_annotation**](docs/AIApi.md#update_ai_annotation) | **PUT** `/api/2/ai/annotations/{id}` | 
*AIApi* | [**update_ai_category**](docs/AIApi.md#update_ai_category) | **PUT** `/api/2/ai/categories/{id}` | 
*AIApi* | [**update_ai_dataset**](docs/AIApi.md#update_ai_dataset) | **PUT** `/api/2/ai/datasets/{id}` | 
*AIApi* | [**update_ai_model**](docs/AIApi.md#update_ai_model) | **PUT** `/api/2/ai/models/{id}` | 
*AIApi* | [**upload_ai_image**](docs/AIApi.md#upload_ai_image) | **POST** `/api/2/ai/images/upload` | 
*AWSApi* | [**create_aws_account**](docs/AWSApi.md#create_aws_account) | **POST** `/api/2/aws-accounts` | 
*AWSApi* | [**delete_aws_account**](docs/AWSApi.md#delete_aws_account) | **DELETE** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**get_all_aws_accounts**](docs/AWSApi.md#get_all_aws_accounts) | **GET** `/api/2/aws-accounts` | 
*AWSApi* | [**get_aws_account**](docs/AWSApi.md#get_aws_account) | **GET** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**get_aws_account_sns_topics**](docs/AWSApi.md#get_aws_account_sns_topics) | **GET** `/api/2/aws-accounts/{id}/sns/topics` | 
*AWSApi* | [**patch_aws_account**](docs/AWSApi.md#patch_aws_account) | **PATCH** `/api/2/aws-accounts/{id}` | 
*AWSApi* | [**test_aws_account_credentials**](docs/AWSApi.md#test_aws_account_credentials) | **POST** `/api/2/aws-accounts/test-credentials` | 
*AWSApi* | [**update_aws_account**](docs/AWSApi.md#update_aws_account) | **PUT** `/api/2/aws-accounts/{id}` | 
*AuthApi* | [**check_auth_ticket**](docs/AuthApi.md#check_auth_ticket) | **POST** `/api/2/auth/ticket/check` | 
*AuthApi* | [**create_api_token**](docs/AuthApi.md#create_api_token) | **POST** `/api/2/api-tokens` | 
*AuthApi* | [**create_auth_ticket**](docs/AuthApi.md#create_auth_ticket) | **POST** `/api/2/auth/ticket` | 
*AuthApi* | [**create_saml_provider**](docs/AuthApi.md#create_saml_provider) | **POST** `/api/2/auth/saml` | 
*AuthApi* | [**delete_access_token**](docs/AuthApi.md#delete_access_token) | **DELETE** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**delete_api_token**](docs/AuthApi.md#delete_api_token) | **DELETE** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**delete_saml_provider**](docs/AuthApi.md#delete_saml_provider) | **DELETE** `/api/2/auth/saml/{id}` | 
*AuthApi* | [**generate_password**](docs/AuthApi.md#generate_password) | **POST** `/api/2/auth/generate-password` | 
*AuthApi* | [**get_access_token**](docs/AuthApi.md#get_access_token) | **GET** `/api/2/auth/access-tokens/{id}` | 
*AuthApi* | [**get_all_access_tokens**](docs/AuthApi.md#get_all_access_tokens) | **GET** `/api/2/auth/access-tokens` | 
*AuthApi* | [**get_all_api_tokens**](docs/AuthApi.md#get_all_api_tokens) | **GET** `/api/2/api-tokens` | 
*AuthApi* | [**get_all_saml_providers**](docs/AuthApi.md#get_all_saml_providers) | **GET** `/api/2/auth/saml` | 
*AuthApi* | [**get_api_token**](docs/AuthApi.md#get_api_token) | **GET** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**get_saml_provider**](docs/AuthApi.md#get_saml_provider) | **GET** `/api/2/auth/saml/{id}` | 
*AuthApi* | [**get_saml_service_provider_metadata**](docs/AuthApi.md#get_saml_service_provider_metadata) | **GET** `/api/2/auth/saml/{id}/metadata` | 
*AuthApi* | [**login**](docs/AuthApi.md#login) | **POST** `/api/2/auth/login` | 
*AuthApi* | [**logout**](docs/AuthApi.md#logout) | **POST** `/api/2/auth/logout` | 
*AuthApi* | [**logout_page**](docs/AuthApi.md#logout_page) | **GET** `/api/2/auth/logout` | 
*AuthApi* | [**parse_samlidp_metadata**](docs/AuthApi.md#parse_samlidp_metadata) | **POST** `/api/2/auth/saml/parse-idp-metadata` | 
*AuthApi* | [**patch_api_token**](docs/AuthApi.md#patch_api_token) | **PATCH** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**patch_saml_provider**](docs/AuthApi.md#patch_saml_provider) | **PATCH** `/api/2/auth/saml/{id}` | 
*AuthApi* | [**receive_saml_auth_assertion**](docs/AuthApi.md#receive_saml_auth_assertion) | **POST** `/api/2/auth/saml/{id}/assertion` | 
*AuthApi* | [**refresh_samlidp_metadata**](docs/AuthApi.md#refresh_samlidp_metadata) | **POST** `/api/2/auth/saml/{id}/refresh-idp-metadata` | 
*AuthApi* | [**reset_password**](docs/AuthApi.md#reset_password) | **POST** `/api/2/auth/reset-password` | 
*AuthApi* | [**return_from_saml_auth**](docs/AuthApi.md#return_from_saml_auth) | **GET** `/api/2/auth/saml/{id}/sso/return` | 
*AuthApi* | [**return_from_saml_logout**](docs/AuthApi.md#return_from_saml_logout) | **GET** `/api/2/auth/saml/{id}/sls/return` | 
*AuthApi* | [**send_access_token_email_notification**](docs/AuthApi.md#send_access_token_email_notification) | **POST** `/api/2/auth/access-tokens/{id}/email` | 
*AuthApi* | [**start_impersonation**](docs/AuthApi.md#start_impersonation) | **POST** `/api/2/auth/impersonation` | 
*AuthApi* | [**start_saml_auth**](docs/AuthApi.md#start_saml_auth) | **GET** `/api/2/auth/saml/{id}/sso` | 
*AuthApi* | [**start_saml_logout**](docs/AuthApi.md#start_saml_logout) | **GET** `/api/2/auth/saml/{id}/sls` | 
*AuthApi* | [**stop_impersonation**](docs/AuthApi.md#stop_impersonation) | **POST** `/api/2/auth/impersonation/stop` | 
*AuthApi* | [**update_api_token**](docs/AuthApi.md#update_api_token) | **PUT** `/api/2/api-tokens/{id}` | 
*AuthApi* | [**update_saml_provider**](docs/AuthApi.md#update_saml_provider) | **PUT** `/api/2/auth/saml/{id}` | 
*AutomationApi* | [**abort_task**](docs/AutomationApi.md#abort_task) | **POST** `/api/2/tasks/{id}/abort` | 
*AutomationApi* | [**create_job**](docs/AutomationApi.md#create_job) | **POST** `/api/2/jobs` | 
*AutomationApi* | [**create_schedule**](docs/AutomationApi.md#create_schedule) | **POST** `/api/2/schedules` | 
*AutomationApi* | [**create_subtask**](docs/AutomationApi.md#create_subtask) | **POST** `/api/2/subtasks` | 
*AutomationApi* | [**delete_finished_tasks**](docs/AutomationApi.md#delete_finished_tasks) | **DELETE** `/api/2/tasks/finished` | 
*AutomationApi* | [**delete_job**](docs/AutomationApi.md#delete_job) | **DELETE** `/api/2/jobs/{id}` | 
*AutomationApi* | [**delete_schedule**](docs/AutomationApi.md#delete_schedule) | **DELETE** `/api/2/schedules/{id}` | 
*AutomationApi* | [**delete_subtask**](docs/AutomationApi.md#delete_subtask) | **DELETE** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**delete_task**](docs/AutomationApi.md#delete_task) | **DELETE** `/api/2/tasks/{id}` | 
*AutomationApi* | [**download_all_task_logs**](docs/AutomationApi.md#download_all_task_logs) | **GET** `/api/2/tasks/logs/download` | 
*AutomationApi* | [**download_task_log**](docs/AutomationApi.md#download_task_log) | **GET** `/api/2/tasks/{id}/log/download` | 
*AutomationApi* | [**export_job**](docs/AutomationApi.md#export_job) | **GET** `/api/2/jobs/{id}/export` | 
*AutomationApi* | [**get_all_events**](docs/AutomationApi.md#get_all_events) | **GET** `/api/2/events` | 
*AutomationApi* | [**get_all_jobs**](docs/AutomationApi.md#get_all_jobs) | **GET** `/api/2/jobs` | 
*AutomationApi* | [**get_all_schedules**](docs/AutomationApi.md#get_all_schedules) | **GET** `/api/2/schedules` | 
*AutomationApi* | [**get_all_subtasks**](docs/AutomationApi.md#get_all_subtasks) | **GET** `/api/2/subtasks` | 
*AutomationApi* | [**get_all_task_queues**](docs/AutomationApi.md#get_all_task_queues) | **GET** `/api/2/tasks/queues` | 
*AutomationApi* | [**get_all_task_types**](docs/AutomationApi.md#get_all_task_types) | **GET** `/api/2/tasks/types` | 
*AutomationApi* | [**get_all_tasks**](docs/AutomationApi.md#get_all_tasks) | **GET** `/api/2/tasks` | 
*AutomationApi* | [**get_event**](docs/AutomationApi.md#get_event) | **GET** `/api/2/events/{id}` | 
*AutomationApi* | [**get_finished_tasks**](docs/AutomationApi.md#get_finished_tasks) | **GET** `/api/2/tasks/finished` | 
*AutomationApi* | [**get_job**](docs/AutomationApi.md#get_job) | **GET** `/api/2/jobs/{id}` | 
*AutomationApi* | [**get_pending_tasks**](docs/AutomationApi.md#get_pending_tasks) | **GET** `/api/2/tasks/pending` | 
*AutomationApi* | [**get_python_environments**](docs/AutomationApi.md#get_python_environments) | **GET** `/api/2/python/environments` | 
*AutomationApi* | [**get_schedule**](docs/AutomationApi.md#get_schedule) | **GET** `/api/2/schedules/{id}` | 
*AutomationApi* | [**get_subtask**](docs/AutomationApi.md#get_subtask) | **GET** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**get_task**](docs/AutomationApi.md#get_task) | **GET** `/api/2/tasks/{id}` | 
*AutomationApi* | [**get_task_log**](docs/AutomationApi.md#get_task_log) | **GET** `/api/2/tasks/{id}/log` | 
*AutomationApi* | [**get_task_type**](docs/AutomationApi.md#get_task_type) | **GET** `/api/2/tasks/types/{type}` | 
*AutomationApi* | [**get_tasks_summary**](docs/AutomationApi.md#get_tasks_summary) | **GET** `/api/2/tasks/summary` | 
*AutomationApi* | [**import_job**](docs/AutomationApi.md#import_job) | **POST** `/api/2/jobs/import` | 
*AutomationApi* | [**kill_all_pending_tasks**](docs/AutomationApi.md#kill_all_pending_tasks) | **DELETE** `/api/2/tasks/pending` | 
*AutomationApi* | [**kill_task**](docs/AutomationApi.md#kill_task) | **POST** `/api/2/tasks/{id}/kill` | 
*AutomationApi* | [**patch_job**](docs/AutomationApi.md#patch_job) | **PATCH** `/api/2/jobs/{id}` | 
*AutomationApi* | [**patch_schedule**](docs/AutomationApi.md#patch_schedule) | **PATCH** `/api/2/schedules/{id}` | 
*AutomationApi* | [**patch_subtask**](docs/AutomationApi.md#patch_subtask) | **PATCH** `/api/2/subtasks/{id}` | 
*AutomationApi* | [**restart_task**](docs/AutomationApi.md#restart_task) | **POST** `/api/2/tasks/{id}/restart` | 
*AutomationApi* | [**start_job**](docs/AutomationApi.md#start_job) | **POST** `/api/2/jobs/{id}/start` | 
*AutomationApi* | [**start_task**](docs/AutomationApi.md#start_task) | **POST** `/api/2/tasks/start` | 
*AutomationApi* | [**update_job**](docs/AutomationApi.md#update_job) | **PUT** `/api/2/jobs/{id}` | 
*AutomationApi* | [**update_schedule**](docs/AutomationApi.md#update_schedule) | **PUT** `/api/2/schedules/{id}` | 
*AutomationApi* | [**update_subtask**](docs/AutomationApi.md#update_subtask) | **PUT** `/api/2/subtasks/{id}` | 
*ClickApi* | [**abort_click_upload**](docs/ClickApi.md#abort_click_upload) | **DELETE** `/api/2/click/uploads/{upload_id}` | 
*ClickApi* | [**add_assets_to_click_gallery**](docs/ClickApi.md#add_assets_to_click_gallery) | **POST** `/api/2/click/connections/{connection_id}/galleries/{id}/add-assets` | 
*ClickApi* | [**continue_click_upload_in_background**](docs/ClickApi.md#continue_click_upload_in_background) | **POST** `/api/2/click/uploads/{upload_id}/background` | 
*ClickApi* | [**create_click_gallery**](docs/ClickApi.md#create_click_gallery) | **POST** `/api/2/click/connections/{connection_id}/galleries` | 
*ClickApi* | [**create_click_gallery_link**](docs/ClickApi.md#create_click_gallery_link) | **POST** `/api/2/click/connections/{connection_id}/gallery-links` | 
*ClickApi* | [**delete_click_gallery_link**](docs/ClickApi.md#delete_click_gallery_link) | **DELETE** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
*ClickApi* | [**get_all_click_galleries**](docs/ClickApi.md#get_all_click_galleries) | **GET** `/api/2/click/connections/{connection_id}/galleries` | 
*ClickApi* | [**get_all_click_gallery_links**](docs/ClickApi.md#get_all_click_gallery_links) | **GET** `/api/2/click/connections/{connection_id}/gallery-links` | 
*ClickApi* | [**get_click_gallery**](docs/ClickApi.md#get_click_gallery) | **GET** `/api/2/click/connections/{connection_id}/galleries/{id}` | 
*ClickApi* | [**get_click_gallery_link**](docs/ClickApi.md#get_click_gallery_link) | **GET** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
*ClickApi* | [**send_click_gallery_link_email**](docs/ClickApi.md#send_click_gallery_link_email) | **POST** `/api/2/click/connections/{connection_id}/gallery-links/{link_id}/send` | 
*ClickApi* | [**start_click_upload**](docs/ClickApi.md#start_click_upload) | **POST** `/api/2/click/uploads` | 
*IntegrationsApi* | [**delete_slack_connection**](docs/IntegrationsApi.md#delete_slack_connection) | **DELETE** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**delete_teams_connection**](docs/IntegrationsApi.md#delete_teams_connection) | **DELETE** `/api/2/integrations/teams/{id}` | 
*IntegrationsApi* | [**get_all_slack_connections**](docs/IntegrationsApi.md#get_all_slack_connections) | **GET** `/api/2/integrations/slack` | 
*IntegrationsApi* | [**get_all_teams_connections**](docs/IntegrationsApi.md#get_all_teams_connections) | **GET** `/api/2/integrations/teams` | 
*IntegrationsApi* | [**get_slack_channels**](docs/IntegrationsApi.md#get_slack_channels) | **GET** `/api/2/integrations/slack/{id}/channels` | 
*IntegrationsApi* | [**get_slack_connection**](docs/IntegrationsApi.md#get_slack_connection) | **GET** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**get_slack_emoji**](docs/IntegrationsApi.md#get_slack_emoji) | **GET** `/api/2/integrations/slack/{id}/emoji` | 
*IntegrationsApi* | [**get_slack_users**](docs/IntegrationsApi.md#get_slack_users) | **GET** `/api/2/integrations/slack/{id}/users` | 
*IntegrationsApi* | [**get_teams_channels**](docs/IntegrationsApi.md#get_teams_channels) | **GET** `/api/2/integrations/teams/{id}/channels` | 
*IntegrationsApi* | [**get_teams_connection**](docs/IntegrationsApi.md#get_teams_connection) | **GET** `/api/2/integrations/teams/{id}` | 
*IntegrationsApi* | [**get_teams_users**](docs/IntegrationsApi.md#get_teams_users) | **GET** `/api/2/integrations/teams/{id}/users` | 
*IntegrationsApi* | [**patch_slack_connection**](docs/IntegrationsApi.md#patch_slack_connection) | **PATCH** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**patch_teams_connection**](docs/IntegrationsApi.md#patch_teams_connection) | **PATCH** `/api/2/integrations/teams/{id}` | 
*IntegrationsApi* | [**send_slack_message**](docs/IntegrationsApi.md#send_slack_message) | **POST** `/api/2/integrations/slack/{id}/message` | 
*IntegrationsApi* | [**send_teams_message**](docs/IntegrationsApi.md#send_teams_message) | **POST** `/api/2/integrations/teams/{id}/send-message` | 
*IntegrationsApi* | [**start_slack_connection_flow**](docs/IntegrationsApi.md#start_slack_connection_flow) | **GET** `/api/2/integrations/slack/connect` | 
*IntegrationsApi* | [**start_slack_connection_token_refresh_flow**](docs/IntegrationsApi.md#start_slack_connection_token_refresh_flow) | **GET** `/api/2/integrations/slack/{id}/refresh-token` | 
*IntegrationsApi* | [**start_teams_connection_flow**](docs/IntegrationsApi.md#start_teams_connection_flow) | **GET** `/api/2/integrations/teams/connect` | 
*IntegrationsApi* | [**start_teams_connection_token_refresh_flow**](docs/IntegrationsApi.md#start_teams_connection_token_refresh_flow) | **GET** `/api/2/integrations/teams/{id}/refresh-token` | 
*IntegrationsApi* | [**update_slack_connection**](docs/IntegrationsApi.md#update_slack_connection) | **PUT** `/api/2/integrations/slack/{id}` | 
*IntegrationsApi* | [**update_teams_connection**](docs/IntegrationsApi.md#update_teams_connection) | **PUT** `/api/2/integrations/teams/{id}` | 
*MainApi* | [**apply_configuration**](docs/MainApi.md#apply_configuration) | **POST** `/api/2/configuration/apply` | 
*MainApi* | [**beep**](docs/MainApi.md#beep) | **POST** `/api/2/system/beep` | 
*MainApi* | [**check_certificate**](docs/MainApi.md#check_certificate) | **POST** `/api/2/system/certificate/check` | 
*MainApi* | [**check_chunk_uploaded**](docs/MainApi.md#check_chunk_uploaded) | **GET** `/api/2/uploads/chunk` | 
*MainApi* | [**check_internet_connectivity**](docs/MainApi.md#check_internet_connectivity) | **POST** `/api/2/system/check-connectivity` | 
*MainApi* | [**check_stor_next_license**](docs/MainApi.md#check_stor_next_license) | **POST** `/api/2/stornext-license/check` | 
*MainApi* | [**collect_diagnostics**](docs/MainApi.md#collect_diagnostics) | **POST** `/api/2/system/collect-diagnostics` | 
*MainApi* | [**create_archive**](docs/MainApi.md#create_archive) | **POST** `/api/2/download-archive/create` | 
*MainApi* | [**create_cloud_account**](docs/MainApi.md#create_cloud_account) | **POST** `/api/2/cloud/accounts` | 
*MainApi* | [**create_filesystem_permission**](docs/MainApi.md#create_filesystem_permission) | **POST** `/api/2/filesystem-permissions` | 
*MainApi* | [**create_group**](docs/MainApi.md#create_group) | **POST** `/api/2/groups` | 
*MainApi* | [**create_home_workspace**](docs/MainApi.md#create_home_workspace) | **POST** `/api/2/users/{id}/home` | 
*MainApi* | [**create_ntp_server**](docs/MainApi.md#create_ntp_server) | **POST** `/api/2/system/time/servers` | 
*MainApi* | [**create_user**](docs/MainApi.md#create_user) | **POST** `/api/2/users` | 
*MainApi* | [**create_workstation**](docs/MainApi.md#create_workstation) | **POST** `/api/2/workstations` | 
*MainApi* | [**delete_cloud_account**](docs/MainApi.md#delete_cloud_account) | **DELETE** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**delete_download_archive**](docs/MainApi.md#delete_download_archive) | **DELETE** `/api/2/download-archive/{id}` | 
*MainApi* | [**delete_filesystem_permission**](docs/MainApi.md#delete_filesystem_permission) | **DELETE** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**delete_group**](docs/MainApi.md#delete_group) | **DELETE** `/api/2/groups/{id}` | 
*MainApi* | [**delete_home_workspace**](docs/MainApi.md#delete_home_workspace) | **DELETE** `/api/2/users/{id}/home` | 
*MainApi* | [**delete_ntp_server**](docs/MainApi.md#delete_ntp_server) | **DELETE** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**delete_user**](docs/MainApi.md#delete_user) | **DELETE** `/api/2/users/{id}` | 
*MainApi* | [**delete_workstation**](docs/MainApi.md#delete_workstation) | **DELETE** `/api/2/workstations/{id}` | 
*MainApi* | [**disable_user_totp**](docs/MainApi.md#disable_user_totp) | **DELETE** `/api/2/users/{id}/totp` | 
*MainApi* | [**enable_user_totp**](docs/MainApi.md#enable_user_totp) | **POST** `/api/2/users/{id}/totp` | 
*MainApi* | [**finish_upload**](docs/MainApi.md#finish_upload) | **POST** `/api/2/uploads/finish` | 
*MainApi* | [**fix_ldap_group_memberships**](docs/MainApi.md#fix_ldap_group_memberships) | **POST** `/api/2/ldap-servers/{id}/fix-memberships` | 
*MainApi* | [**get_all_client_sessions**](docs/MainApi.md#get_all_client_sessions) | **GET** `/api/2/client-sessions` | 
*MainApi* | [**get_all_cloud_accounts**](docs/MainApi.md#get_all_cloud_accounts) | **GET** `/api/2/cloud/accounts` | 
*MainApi* | [**get_all_download_archives**](docs/MainApi.md#get_all_download_archives) | **GET** `/api/2/download-archive` | 
*MainApi* | [**get_all_downloads**](docs/MainApi.md#get_all_downloads) | **GET** `/api/2/downloads` | 
*MainApi* | [**get_all_filesystem_permissions**](docs/MainApi.md#get_all_filesystem_permissions) | **GET** `/api/2/filesystem-permissions` | 
*MainApi* | [**get_all_groups**](docs/MainApi.md#get_all_groups) | **GET** `/api/2/groups` | 
*MainApi* | [**get_all_ldap_servers**](docs/MainApi.md#get_all_ldap_servers) | **GET** `/api/2/ldap-servers` | 
*MainApi* | [**get_all_ntp_servers**](docs/MainApi.md#get_all_ntp_servers) | **GET** `/api/2/system/time/servers` | 
*MainApi* | [**get_all_storage_nodes**](docs/MainApi.md#get_all_storage_nodes) | **GET** `/api/2/nodes` | 
*MainApi* | [**get_all_users**](docs/MainApi.md#get_all_users) | **GET** `/api/2/users` | 
*MainApi* | [**get_all_workstations**](docs/MainApi.md#get_all_workstations) | **GET** `/api/2/workstations` | 
*MainApi* | [**get_certificate_configuration**](docs/MainApi.md#get_certificate_configuration) | **GET** `/api/2/system/certificate` | 
*MainApi* | [**get_client_download_file**](docs/MainApi.md#get_client_download_file) | **GET** `/api/2/downloads/clients/{file}` | 
*MainApi* | [**get_client_downloads**](docs/MainApi.md#get_client_downloads) | **GET** `/api/2/downloads/clients` | 
*MainApi* | [**get_client_session**](docs/MainApi.md#get_client_session) | **GET** `/api/2/client-sessions/{id}` | 
*MainApi* | [**get_cloud_account**](docs/MainApi.md#get_cloud_account) | **GET** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**get_cloud_account_storage_roots**](docs/MainApi.md#get_cloud_account_storage_roots) | **GET** `/api/2/cloud/accounts/{id}/storage-roots` | 
*MainApi* | [**get_current_workstation**](docs/MainApi.md#get_current_workstation) | **GET** `/api/2/workstations/current` | 
*MainApi* | [**get_download**](docs/MainApi.md#get_download) | **GET** `/api/2/downloads/{id}` | 
*MainApi* | [**get_download_archive**](docs/MainApi.md#get_download_archive) | **GET** `/api/2/download-archive/{id}` | 
*MainApi* | [**get_download_archive_file**](docs/MainApi.md#get_download_archive_file) | **GET** `/api/2/download-archive/{id}/download` | 
*MainApi* | [**get_download_file**](docs/MainApi.md#get_download_file) | **GET** `/api/2/downloads/{id}/download` | 
*MainApi* | [**get_download_icon**](docs/MainApi.md#get_download_icon) | **GET** `/api/2/downloads/{id}/icon` | 
*MainApi* | [**get_filesystem_permission**](docs/MainApi.md#get_filesystem_permission) | **GET** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**get_group**](docs/MainApi.md#get_group) | **GET** `/api/2/groups/{id}` | 
*MainApi* | [**get_home_workspace**](docs/MainApi.md#get_home_workspace) | **GET** `/api/2/users/{id}/home` | 
*MainApi* | [**get_ipmi_configuration**](docs/MainApi.md#get_ipmi_configuration) | **GET** `/api/2/nodes/{id}/ipmi` | 
*MainApi* | [**get_ldap_server**](docs/MainApi.md#get_ldap_server) | **GET** `/api/2/ldap-servers/{id}` | 
*MainApi* | [**get_ldap_server_groups**](docs/MainApi.md#get_ldap_server_groups) | **GET** `/api/2/ldap-servers/{id}/groups` | 
*MainApi* | [**get_ldap_server_users**](docs/MainApi.md#get_ldap_server_users) | **GET** `/api/2/ldap-servers/{id}/users` | 
*MainApi* | [**get_license**](docs/MainApi.md#get_license) | **GET** `/api/2/license` | 
*MainApi* | [**get_local_time**](docs/MainApi.md#get_local_time) | **GET** `/api/2/system/time` | 
*MainApi* | [**get_log**](docs/MainApi.md#get_log) | **GET** `/api/2/system/log/{path}` | 
*MainApi* | [**get_node_ipmi_sensors**](docs/MainApi.md#get_node_ipmi_sensors) | **GET** `/api/2/nodes/{id}/sensors` | 
*MainApi* | [**get_node_stats**](docs/MainApi.md#get_node_stats) | **GET** `/api/2/nodes/{id}/stats` | 
*MainApi* | [**get_ntp_server**](docs/MainApi.md#get_ntp_server) | **GET** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**get_parameters**](docs/MainApi.md#get_parameters) | **GET** `/api/2/parameters` | 
*MainApi* | [**get_profile**](docs/MainApi.md#get_profile) | **GET** `/api/2/users/me` | 
*MainApi* | [**get_release_notes**](docs/MainApi.md#get_release_notes) | **GET** `/api/2/release-notes` | 
*MainApi* | [**get_service_status**](docs/MainApi.md#get_service_status) | **GET** `/api/2/nodes/{id}/services/{service}` | 
*MainApi* | [**get_smtp_configuration**](docs/MainApi.md#get_smtp_configuration) | **GET** `/api/2/system/smtp` | 
*MainApi* | [**get_stor_next_license**](docs/MainApi.md#get_stor_next_license) | **GET** `/api/2/stornext-license` | 
*MainApi* | [**get_storage_node**](docs/MainApi.md#get_storage_node) | **GET** `/api/2/nodes/{id}` | 
*MainApi* | [**get_system_info**](docs/MainApi.md#get_system_info) | **GET** `/api/2/system/info` | 
*MainApi* | [**get_user**](docs/MainApi.md#get_user) | **GET** `/api/2/users/{id}` | 
*MainApi* | [**get_workstation**](docs/MainApi.md#get_workstation) | **GET** `/api/2/workstations/{id}` | 
*MainApi* | [**install_stor_next_license**](docs/MainApi.md#install_stor_next_license) | **POST** `/api/2/stornext-license` | 
*MainApi* | [**patch_cloud_account**](docs/MainApi.md#patch_cloud_account) | **PATCH** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**patch_current_workstation**](docs/MainApi.md#patch_current_workstation) | **PATCH** `/api/2/workstations/current` | 
*MainApi* | [**patch_download_archive**](docs/MainApi.md#patch_download_archive) | **PATCH** `/api/2/download-archive/{id}` | 
*MainApi* | [**patch_filesystem_permission**](docs/MainApi.md#patch_filesystem_permission) | **PATCH** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**patch_group**](docs/MainApi.md#patch_group) | **PATCH** `/api/2/groups/{id}` | 
*MainApi* | [**patch_ntp_server**](docs/MainApi.md#patch_ntp_server) | **PATCH** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**patch_profile**](docs/MainApi.md#patch_profile) | **PATCH** `/api/2/users/me` | 
*MainApi* | [**patch_user**](docs/MainApi.md#patch_user) | **PATCH** `/api/2/users/{id}` | 
*MainApi* | [**patch_workstation**](docs/MainApi.md#patch_workstation) | **PATCH** `/api/2/workstations/{id}` | 
*MainApi* | [**preview_user**](docs/MainApi.md#preview_user) | **POST** `/api/2/users/preview` | 
*MainApi* | [**reboot**](docs/MainApi.md#reboot) | **POST** `/api/2/system/reboot` | 
*MainApi* | [**register_upload**](docs/MainApi.md#register_upload) | **POST** `/api/2/uploads/register` | 
*MainApi* | [**register_upload_metadata**](docs/MainApi.md#register_upload_metadata) | **POST** `/api/2/uploads/metadata` | 
*MainApi* | [**render_email_template_preview**](docs/MainApi.md#render_email_template_preview) | **POST** `/api/2/system/smtp/preview` | 
*MainApi* | [**reset_user_password**](docs/MainApi.md#reset_user_password) | **POST** `/api/2/users/{id}/password/reset` | 
*MainApi* | [**restart_web_ui**](docs/MainApi.md#restart_web_ui) | **POST** `/api/2/system/restart-webui` | 
*MainApi* | [**run_service_operation**](docs/MainApi.md#run_service_operation) | **POST** `/api/2/nodes/{id}/services/{service}/{operation}` | 
*MainApi* | [**set_ipmi_configuration**](docs/MainApi.md#set_ipmi_configuration) | **PUT** `/api/2/nodes/{id}/ipmi` | 
*MainApi* | [**set_local_time**](docs/MainApi.md#set_local_time) | **POST** `/api/2/system/time` | 
*MainApi* | [**set_my_password**](docs/MainApi.md#set_my_password) | **POST** `/api/2/users/me/password` | 
*MainApi* | [**set_user_password**](docs/MainApi.md#set_user_password) | **POST** `/api/2/users/{id}/password` | 
*MainApi* | [**shutdown**](docs/MainApi.md#shutdown) | **POST** `/api/2/system/shutdown` | 
*MainApi* | [**start_solr_reindex**](docs/MainApi.md#start_solr_reindex) | **POST** `/api/2/system/solr/reindex` | 
*MainApi* | [**start_support_session**](docs/MainApi.md#start_support_session) | **POST** `/api/2/system/support-session/start` | 
*MainApi* | [**start_system_backup**](docs/MainApi.md#start_system_backup) | **POST** `/api/2/system/backup/start` | 
*MainApi* | [**sync_ldap_group**](docs/MainApi.md#sync_ldap_group) | **POST** `/api/2/groups/{id}/ldap-sync` | 
*MainApi* | [**sync_ldap_users**](docs/MainApi.md#sync_ldap_users) | **POST** `/api/2/ldap-servers/{id}/sync-users` | 
*MainApi* | [**sync_time**](docs/MainApi.md#sync_time) | **POST** `/api/2/system/time/sync` | 
*MainApi* | [**sync_user_totp**](docs/MainApi.md#sync_user_totp) | **PUT** `/api/2/users/{id}/totp` | 
*MainApi* | [**test_cloud_account_credentials**](docs/MainApi.md#test_cloud_account_credentials) | **POST** `/api/2/cloud/accounts/test-credentials` | 
*MainApi* | [**test_smtp_configuration**](docs/MainApi.md#test_smtp_configuration) | **POST** `/api/2/system/smtp/test` | 
*MainApi* | [**update_certificate_configuration**](docs/MainApi.md#update_certificate_configuration) | **PUT** `/api/2/system/certificate` | 
*MainApi* | [**update_cloud_account**](docs/MainApi.md#update_cloud_account) | **PUT** `/api/2/cloud/accounts/{id}` | 
*MainApi* | [**update_current_workstation**](docs/MainApi.md#update_current_workstation) | **PUT** `/api/2/workstations/current` | 
*MainApi* | [**update_download_archive**](docs/MainApi.md#update_download_archive) | **PUT** `/api/2/download-archive/{id}` | 
*MainApi* | [**update_filesystem_permission**](docs/MainApi.md#update_filesystem_permission) | **PUT** `/api/2/filesystem-permissions/{id}` | 
*MainApi* | [**update_group**](docs/MainApi.md#update_group) | **PUT** `/api/2/groups/{id}` | 
*MainApi* | [**update_ntp_server**](docs/MainApi.md#update_ntp_server) | **PUT** `/api/2/system/time/servers/{id}` | 
*MainApi* | [**update_parameters**](docs/MainApi.md#update_parameters) | **PUT** `/api/2/parameters` | 
*MainApi* | [**update_profile**](docs/MainApi.md#update_profile) | **PUT** `/api/2/users/me` | 
*MainApi* | [**update_smtp_configuration**](docs/MainApi.md#update_smtp_configuration) | **PUT** `/api/2/system/smtp` | 
*MainApi* | [**update_user**](docs/MainApi.md#update_user) | **PUT** `/api/2/users/{id}` | 
*MainApi* | [**update_workstation**](docs/MainApi.md#update_workstation) | **PUT** `/api/2/workstations/{id}` | 
*MainApi* | [**upload_chunk**](docs/MainApi.md#upload_chunk) | **POST** `/api/2/uploads/chunk` | 
*MediaLibraryApi* | [**bookmark_media_directory**](docs/MediaLibraryApi.md#bookmark_media_directory) | **POST** `/api/2/media/files/{id}/bookmark` | 
*MediaLibraryApi* | [**clear_subclip_clipboard**](docs/MediaLibraryApi.md#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
*MediaLibraryApi* | [**clear_subtitle_clipboard**](docs/MediaLibraryApi.md#clear_subtitle_clipboard) | **DELETE** `/api/2/media/subtitles/clipboard/clear` | 
*MediaLibraryApi* | [**combine_assets_into_set**](docs/MediaLibraryApi.md#combine_assets_into_set) | **POST** `/api/2/media/assets/combine` | 
*MediaLibraryApi* | [**create_asset**](docs/MediaLibraryApi.md#create_asset) | **POST** `/api/2/media/assets` | 
*MediaLibraryApi* | [**create_asset_rating**](docs/MediaLibraryApi.md#create_asset_rating) | **POST** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**create_asset_subtitle_link**](docs/MediaLibraryApi.md#create_asset_subtitle_link) | **POST** `/api/2/media/assets/subtitle-links` | 
*MediaLibraryApi* | [**create_comment**](docs/MediaLibraryApi.md#create_comment) | **POST** `/api/2/media/comments` | 
*MediaLibraryApi* | [**create_custom_field**](docs/MediaLibraryApi.md#create_custom_field) | **POST** `/api/2/media/custom-fields` | 
*MediaLibraryApi* | [**create_editor_project**](docs/MediaLibraryApi.md#create_editor_project) | **POST** `/api/2/media/editor` | 
*MediaLibraryApi* | [**create_editor_subtitle**](docs/MediaLibraryApi.md#create_editor_subtitle) | **POST** `/api/2/media/subtitles` | 
*MediaLibraryApi* | [**create_external_transcoder**](docs/MediaLibraryApi.md#create_external_transcoder) | **POST** `/api/2/media/external-transcoders` | 
*MediaLibraryApi* | [**create_marker**](docs/MediaLibraryApi.md#create_marker) | **POST** `/api/2/media/markers` | 
*MediaLibraryApi* | [**create_media_file_template**](docs/MediaLibraryApi.md#create_media_file_template) | **POST** `/api/2/media/files/templates` | 
*MediaLibraryApi* | [**create_media_root**](docs/MediaLibraryApi.md#create_media_root) | **POST** `/api/2/media/roots` | 
*MediaLibraryApi* | [**create_media_root_permission**](docs/MediaLibraryApi.md#create_media_root_permission) | **POST** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**create_media_tag**](docs/MediaLibraryApi.md#create_media_tag) | **POST** `/api/2/media/tags` | 
*MediaLibraryApi* | [**create_proxy_profile**](docs/MediaLibraryApi.md#create_proxy_profile) | **POST** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**create_saved_search**](docs/MediaLibraryApi.md#create_saved_search) | **POST** `/api/2/media/saved-searches` | 
*MediaLibraryApi* | [**create_subclip**](docs/MediaLibraryApi.md#create_subclip) | **POST** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**create_subclip_clipboard_entry**](docs/MediaLibraryApi.md#create_subclip_clipboard_entry) | **POST** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**create_subtitle_clipboard_entry**](docs/MediaLibraryApi.md#create_subtitle_clipboard_entry) | **POST** `/api/2/media/subtitles/clipboard` | 
*MediaLibraryApi* | [**delete_asset**](docs/MediaLibraryApi.md#delete_asset) | **DELETE** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**delete_asset_rating**](docs/MediaLibraryApi.md#delete_asset_rating) | **DELETE** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**delete_asset_subtitle_link**](docs/MediaLibraryApi.md#delete_asset_subtitle_link) | **DELETE** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**delete_comment**](docs/MediaLibraryApi.md#delete_comment) | **DELETE** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**delete_custom_field**](docs/MediaLibraryApi.md#delete_custom_field) | **DELETE** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**delete_easy_sharing_token_for_bundle**](docs/MediaLibraryApi.md#delete_easy_sharing_token_for_bundle) | **DELETE** `/api/2/media/bundles/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**delete_easy_sharing_token_for_directory**](docs/MediaLibraryApi.md#delete_easy_sharing_token_for_directory) | **DELETE** `/api/2/media/files/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**delete_external_transcoder**](docs/MediaLibraryApi.md#delete_external_transcoder) | **DELETE** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**delete_marker**](docs/MediaLibraryApi.md#delete_marker) | **DELETE** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**delete_media_file_template**](docs/MediaLibraryApi.md#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**delete_media_library_objects**](docs/MediaLibraryApi.md#delete_media_library_objects) | **POST** `/api/2/media/delete` | 
*MediaLibraryApi* | [**delete_media_root**](docs/MediaLibraryApi.md#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**delete_media_root_permission**](docs/MediaLibraryApi.md#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**delete_media_tag**](docs/MediaLibraryApi.md#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**delete_media_update**](docs/MediaLibraryApi.md#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
*MediaLibraryApi* | [**delete_proxy**](docs/MediaLibraryApi.md#delete_proxy) | **DELETE** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**delete_proxy_profile**](docs/MediaLibraryApi.md#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**delete_saved_search**](docs/MediaLibraryApi.md#delete_saved_search) | **DELETE** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**delete_subclip**](docs/MediaLibraryApi.md#delete_subclip) | **DELETE** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**delete_subclip_clipboard_entry**](docs/MediaLibraryApi.md#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
*MediaLibraryApi* | [**delete_subtitle_clipboard_entry**](docs/MediaLibraryApi.md#delete_subtitle_clipboard_entry) | **DELETE** `/api/2/media/subtitles/clipboard/{id}` | 
*MediaLibraryApi* | [**discover_media**](docs/MediaLibraryApi.md#discover_media) | **POST** `/api/2/scanner/discover` | 
*MediaLibraryApi* | [**download_asset_proxy_file**](docs/MediaLibraryApi.md#download_asset_proxy_file) | **GET** `/api/2/media/assets/{id}/proxy-files/{filename}` | 
*MediaLibraryApi* | [**download_media_file**](docs/MediaLibraryApi.md#download_media_file) | **GET** `/api/2/media/files/{id}/download` | 
*MediaLibraryApi* | [**download_proxy**](docs/MediaLibraryApi.md#download_proxy) | **GET** `/api/2/media/proxies/{id}/download` | 
*MediaLibraryApi* | [**editor_export_xml_for_assset**](docs/MediaLibraryApi.md#editor_export_xml_for_assset) | **GET** `/api/2/media/editor/asset/{asset_ids}/xml-export` | 
*MediaLibraryApi* | [**editor_export_xml_for_bundle**](docs/MediaLibraryApi.md#editor_export_xml_for_bundle) | **GET** `/api/2/media/editor/bundle/{bundle_ids}/xml-export` | 
*MediaLibraryApi* | [**editor_export_xml_for_project**](docs/MediaLibraryApi.md#editor_export_xml_for_project) | **GET** `/api/2/media/editor/{id}/xml-export` | 
*MediaLibraryApi* | [**export_comments_for_avid**](docs/MediaLibraryApi.md#export_comments_for_avid) | **GET** `/api/2/media/editor/asset/{asset_id}/{export_format}-export/avid-comments` | 
*MediaLibraryApi* | [**export_editor_timeline**](docs/MediaLibraryApi.md#export_editor_timeline) | **POST** `/api/2/media/editor/timeline-export` | 
*MediaLibraryApi* | [**extract_stream**](docs/MediaLibraryApi.md#extract_stream) | **POST** `/api/2/media/assets/{id}/extract-stream` | 
*MediaLibraryApi* | [**forget_deleted_media_files**](docs/MediaLibraryApi.md#forget_deleted_media_files) | **POST** `/api/2/media/files/{id}/forget-deleted` | 
*MediaLibraryApi* | [**generate_proxies**](docs/MediaLibraryApi.md#generate_proxies) | **POST** `/api/2/media/proxies` | 
*MediaLibraryApi* | [**get_all_asset_project_links**](docs/MediaLibraryApi.md#get_all_asset_project_links) | **GET** `/api/2/media/assets/project-links` | 
*MediaLibraryApi* | [**get_all_asset_ratings**](docs/MediaLibraryApi.md#get_all_asset_ratings) | **GET** `/api/2/media/ratings` | 
*MediaLibraryApi* | [**get_all_asset_subtitle_links**](docs/MediaLibraryApi.md#get_all_asset_subtitle_links) | **GET** `/api/2/media/assets/subtitle-links` | 
*MediaLibraryApi* | [**get_all_asset_tape_backups**](docs/MediaLibraryApi.md#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
*MediaLibraryApi* | [**get_all_assets**](docs/MediaLibraryApi.md#get_all_assets) | **GET** `/api/2/media/assets` | 
*MediaLibraryApi* | [**get_all_bundles_for_media_root**](docs/MediaLibraryApi.md#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
*MediaLibraryApi* | [**get_all_bundles_in_subtree**](docs/MediaLibraryApi.md#get_all_bundles_in_subtree) | **GET** `/api/2/media/bundles/flat/subtree/{file}` | 
*MediaLibraryApi* | [**get_all_click_links**](docs/MediaLibraryApi.md#get_all_click_links) | **GET** `/api/2/media/assets/click-links` | 
*MediaLibraryApi* | [**get_all_comments**](docs/MediaLibraryApi.md#get_all_comments) | **GET** `/api/2/media/comments` | 
*MediaLibraryApi* | [**get_all_custom_fields**](docs/MediaLibraryApi.md#get_all_custom_fields) | **GET** `/api/2/media/custom-fields` | 
*MediaLibraryApi* | [**get_all_external_transcoders**](docs/MediaLibraryApi.md#get_all_external_transcoders) | **GET** `/api/2/media/external-transcoders` | 
*MediaLibraryApi* | [**get_all_markers**](docs/MediaLibraryApi.md#get_all_markers) | **GET** `/api/2/media/markers` | 
*MediaLibraryApi* | [**get_all_media_file_bundles**](docs/MediaLibraryApi.md#get_all_media_file_bundles) | **GET** `/api/2/media/bundles` | 
*MediaLibraryApi* | [**get_all_media_file_templates**](docs/MediaLibraryApi.md#get_all_media_file_templates) | **GET** `/api/2/media/files/templates` | 
*MediaLibraryApi* | [**get_all_media_files**](docs/MediaLibraryApi.md#get_all_media_files) | **GET** `/api/2/media/files` | 
*MediaLibraryApi* | [**get_all_media_files_for_bundles**](docs/MediaLibraryApi.md#get_all_media_files_for_bundles) | **POST** `/api/2/media/files/for-bundles` | 
*MediaLibraryApi* | [**get_all_media_files_for_media_root**](docs/MediaLibraryApi.md#get_all_media_files_for_media_root) | **GET** `/api/2/media/files/flat/{root}` | 
*MediaLibraryApi* | [**get_all_media_files_in_subtree**](docs/MediaLibraryApi.md#get_all_media_files_in_subtree) | **GET** `/api/2/media/files/flat/subtree/{file}` | 
*MediaLibraryApi* | [**get_all_media_root_permissions**](docs/MediaLibraryApi.md#get_all_media_root_permissions) | **GET** `/api/2/media/root-permissions` | 
*MediaLibraryApi* | [**get_all_media_roots**](docs/MediaLibraryApi.md#get_all_media_roots) | **GET** `/api/2/media/roots` | 
*MediaLibraryApi* | [**get_all_media_tags**](docs/MediaLibraryApi.md#get_all_media_tags) | **GET** `/api/2/media/tags` | 
*MediaLibraryApi* | [**get_all_media_updates**](docs/MediaLibraryApi.md#get_all_media_updates) | **GET** `/api/2/media/updates` | 
*MediaLibraryApi* | [**get_all_proxy_generators**](docs/MediaLibraryApi.md#get_all_proxy_generators) | **GET** `/api/2/media/proxy-generators` | 
*MediaLibraryApi* | [**get_all_proxy_profiles**](docs/MediaLibraryApi.md#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
*MediaLibraryApi* | [**get_all_saved_searches**](docs/MediaLibraryApi.md#get_all_saved_searches) | **GET** `/api/2/media/saved-searches` | 
*MediaLibraryApi* | [**get_all_subclip_clipboard_entries**](docs/MediaLibraryApi.md#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
*MediaLibraryApi* | [**get_all_subclips**](docs/MediaLibraryApi.md#get_all_subclips) | **GET** `/api/2/media/subclips` | 
*MediaLibraryApi* | [**get_all_subtitle_clipboard_entries**](docs/MediaLibraryApi.md#get_all_subtitle_clipboard_entries) | **GET** `/api/2/media/subtitles/clipboard` | 
*MediaLibraryApi* | [**get_all_transcoder_profiles**](docs/MediaLibraryApi.md#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
*MediaLibraryApi* | [**get_asset**](docs/MediaLibraryApi.md#get_asset) | **GET** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**get_asset_rating**](docs/MediaLibraryApi.md#get_asset_rating) | **GET** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**get_asset_subtitle_link**](docs/MediaLibraryApi.md#get_asset_subtitle_link) | **GET** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**get_bookmarked_media_files_directories**](docs/MediaLibraryApi.md#get_bookmarked_media_files_directories) | **GET** `/api/2/media/files/bookmarks` | 
*MediaLibraryApi* | [**get_comment**](docs/MediaLibraryApi.md#get_comment) | **GET** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**get_custom_field**](docs/MediaLibraryApi.md#get_custom_field) | **GET** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**get_easy_sharing_token_for_bundle**](docs/MediaLibraryApi.md#get_easy_sharing_token_for_bundle) | **GET** `/api/2/media/bundles/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**get_easy_sharing_token_for_directory**](docs/MediaLibraryApi.md#get_easy_sharing_token_for_directory) | **GET** `/api/2/media/files/{id}/easy-sharing-token` | 
*MediaLibraryApi* | [**get_editor_project**](docs/MediaLibraryApi.md#get_editor_project) | **GET** `/api/2/media/editor/{id}` | 
*MediaLibraryApi* | [**get_editor_subtitle**](docs/MediaLibraryApi.md#get_editor_subtitle) | **GET** `/api/2/media/subtitles/{id}` | 
*MediaLibraryApi* | [**get_external_transcoder**](docs/MediaLibraryApi.md#get_external_transcoder) | **GET** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**get_frame**](docs/MediaLibraryApi.md#get_frame) | **GET** `/api/2/media/assets/{id}/frames/{frame}` | 
*MediaLibraryApi* | [**get_latest_media_update**](docs/MediaLibraryApi.md#get_latest_media_update) | **GET** `/api/2/media/updates/latest` | 
*MediaLibraryApi* | [**get_marker**](docs/MediaLibraryApi.md#get_marker) | **GET** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**get_media_file**](docs/MediaLibraryApi.md#get_media_file) | **GET** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**get_media_file_bundle**](docs/MediaLibraryApi.md#get_media_file_bundle) | **GET** `/api/2/media/bundles/{id}` | 
*MediaLibraryApi* | [**get_media_file_contents**](docs/MediaLibraryApi.md#get_media_file_contents) | **GET** `/api/2/media/files/{id}/contents` | 
*MediaLibraryApi* | [**get_media_file_template**](docs/MediaLibraryApi.md#get_media_file_template) | **GET** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**get_media_root**](docs/MediaLibraryApi.md#get_media_root) | **GET** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**get_media_root_permission**](docs/MediaLibraryApi.md#get_media_root_permission) | **GET** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**get_media_tag**](docs/MediaLibraryApi.md#get_media_tag) | **GET** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**get_multiple_assets**](docs/MediaLibraryApi.md#get_multiple_assets) | **POST** `/api/2/media/assets/multiple` | 
*MediaLibraryApi* | [**get_multiple_bundles**](docs/MediaLibraryApi.md#get_multiple_bundles) | **POST** `/api/2/media/bundles/multiple` | 
*MediaLibraryApi* | [**get_multiple_files**](docs/MediaLibraryApi.md#get_multiple_files) | **POST** `/api/2/media/files/multiple` | 
*MediaLibraryApi* | [**get_my_media_root_permissions**](docs/MediaLibraryApi.md#get_my_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine` | 
*MediaLibraryApi* | [**get_my_resolved_media_root_permissions**](docs/MediaLibraryApi.md#get_my_resolved_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine/resolved` | 
*MediaLibraryApi* | [**get_proxy**](docs/MediaLibraryApi.md#get_proxy) | **GET** `/api/2/media/proxies/{id}` | 
*MediaLibraryApi* | [**get_proxy_generator**](docs/MediaLibraryApi.md#get_proxy_generator) | **GET** `/api/2/media/proxy-generators/{id}` | 
*MediaLibraryApi* | [**get_proxy_profile**](docs/MediaLibraryApi.md#get_proxy_profile) | **GET** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**get_proxy_profile_proxy_count**](docs/MediaLibraryApi.md#get_proxy_profile_proxy_count) | **GET** `/api/2/media/proxy-profiles/{id}/proxy-count` | 
*MediaLibraryApi* | [**get_saved_search**](docs/MediaLibraryApi.md#get_saved_search) | **GET** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**get_subclip**](docs/MediaLibraryApi.md#get_subclip) | **GET** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**get_subtitles**](docs/MediaLibraryApi.md#get_subtitles) | **GET** `/api/2/media/assets/{id}/subtitle/{title}` | 
*MediaLibraryApi* | [**get_transcoder_profile**](docs/MediaLibraryApi.md#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
*MediaLibraryApi* | [**get_vantage_workflows**](docs/MediaLibraryApi.md#get_vantage_workflows) | **GET** `/api/2/media/external-transcoders/{id}/workflows` | 
*MediaLibraryApi* | [**instantiate_media_file_template**](docs/MediaLibraryApi.md#instantiate_media_file_template) | **POST** `/api/2/media/files/templates/{id}/instantiate` | 
*MediaLibraryApi* | [**locate_editor_project_paths**](docs/MediaLibraryApi.md#locate_editor_project_paths) | **GET** `/api/2/media/editor/{id}/locate-paths` | 
*MediaLibraryApi* | [**lookup_media_files**](docs/MediaLibraryApi.md#lookup_media_files) | **POST** `/api/2/media/files/lookup` | 
*MediaLibraryApi* | [**mark_media_directory_as_showroom**](docs/MediaLibraryApi.md#mark_media_directory_as_showroom) | **POST** `/api/2/media/files/{id}/showroom` | 
*MediaLibraryApi* | [**patch_asset**](docs/MediaLibraryApi.md#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**patch_asset_rating**](docs/MediaLibraryApi.md#patch_asset_rating) | **PATCH** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**patch_asset_subtitle_link**](docs/MediaLibraryApi.md#patch_asset_subtitle_link) | **PATCH** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**patch_comment**](docs/MediaLibraryApi.md#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**patch_custom_field**](docs/MediaLibraryApi.md#patch_custom_field) | **PATCH** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**patch_editor_project**](docs/MediaLibraryApi.md#patch_editor_project) | **PATCH** `/api/2/media/editor/{id}` | 
*MediaLibraryApi* | [**patch_editor_subtitle**](docs/MediaLibraryApi.md#patch_editor_subtitle) | **PATCH** `/api/2/media/subtitles/{id}` | 
*MediaLibraryApi* | [**patch_external_transcoder**](docs/MediaLibraryApi.md#patch_external_transcoder) | **PATCH** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**patch_marker**](docs/MediaLibraryApi.md#patch_marker) | **PATCH** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**patch_media_file**](docs/MediaLibraryApi.md#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**patch_media_file_template**](docs/MediaLibraryApi.md#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**patch_media_root**](docs/MediaLibraryApi.md#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**patch_media_root_permission**](docs/MediaLibraryApi.md#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**patch_media_tag**](docs/MediaLibraryApi.md#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**patch_proxy_profile**](docs/MediaLibraryApi.md#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**patch_saved_search**](docs/MediaLibraryApi.md#patch_saved_search) | **PATCH** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**patch_subclip**](docs/MediaLibraryApi.md#patch_subclip) | **PATCH** `/api/2/media/subclips/{id}` | 
*MediaLibraryApi* | [**recursively_tag_media_directory**](docs/MediaLibraryApi.md#recursively_tag_media_directory) | **POST** `/api/2/media/files/{id}/tag` | 
*MediaLibraryApi* | [**reindex_media_directory**](docs/MediaLibraryApi.md#reindex_media_directory) | **POST** `/api/2/media/files/{id}/search-reindex` | 
*MediaLibraryApi* | [**rename_custom_field**](docs/MediaLibraryApi.md#rename_custom_field) | **POST** `/api/2/media/custom-fields/{id}/rename` | 
*MediaLibraryApi* | [**render_sequence**](docs/MediaLibraryApi.md#render_sequence) | **POST** `/api/2/media/editor/render` | 
*MediaLibraryApi* | [**render_subclip**](docs/MediaLibraryApi.md#render_subclip) | **POST** `/api/2/media/subclips/{id}/render` | 
*MediaLibraryApi* | [**request_media_scan**](docs/MediaLibraryApi.md#request_media_scan) | **POST** `/api/2/scanner/scan` | 
*MediaLibraryApi* | [**resolve_comment**](docs/MediaLibraryApi.md#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
*MediaLibraryApi* | [**share_media_library_objects**](docs/MediaLibraryApi.md#share_media_library_objects) | **POST** `/api/2/media/share` | 
*MediaLibraryApi* | [**test_external_transcoder_connection**](docs/MediaLibraryApi.md#test_external_transcoder_connection) | **POST** `/api/2/media/external-transcoders/test-connection` | 
*MediaLibraryApi* | [**transition_workflow**](docs/MediaLibraryApi.md#transition_workflow) | **POST** `/api/2/media/workflow/transition` | 
*MediaLibraryApi* | [**unbookmark_media_directory**](docs/MediaLibraryApi.md#unbookmark_media_directory) | **DELETE** `/api/2/media/files/{id}/bookmark` | 
*MediaLibraryApi* | [**unmark_media_directory_as_showroom**](docs/MediaLibraryApi.md#unmark_media_directory_as_showroom) | **DELETE** `/api/2/media/files/{id}/showroom` | 
*MediaLibraryApi* | [**unresolve_comment**](docs/MediaLibraryApi.md#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
*MediaLibraryApi* | [**update_asset**](docs/MediaLibraryApi.md#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
*MediaLibraryApi* | [**update_asset_rating**](docs/MediaLibraryApi.md#update_asset_rating) | **PUT** `/api/2/media/ratings/{id}` | 
*MediaLibraryApi* | [**update_asset_subtitle_link**](docs/MediaLibraryApi.md#update_asset_subtitle_link) | **PUT** `/api/2/media/assets/subtitle-links/{id}` | 
*MediaLibraryApi* | [**update_comment**](docs/MediaLibraryApi.md#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
*MediaLibraryApi* | [**update_custom_field**](docs/MediaLibraryApi.md#update_custom_field) | **PUT** `/api/2/media/custom-fields/{id}` | 
*MediaLibraryApi* | [**update_editor_project**](docs/MediaLibraryApi.md#update_editor_project) | **PUT** `/api/2/media/editor/{id}` | 
*MediaLibraryApi* | [**update_editor_subtitle**](docs/MediaLibraryApi.md#update_editor_subtitle) | **PUT** `/api/2/media/subtitles/{id}` | 
*MediaLibraryApi* | [**update_external_transcoder**](docs/MediaLibraryApi.md#update_external_transcoder) | **PUT** `/api/2/media/external-transcoders/{id}` | 
*MediaLibraryApi* | [**update_marker**](docs/MediaLibraryApi.md#update_marker) | **PUT** `/api/2/media/markers/{id}` | 
*MediaLibraryApi* | [**update_media_file**](docs/MediaLibraryApi.md#update_media_file) | **PUT** `/api/2/media/files/{id}` | 
*MediaLibraryApi* | [**update_media_file_template**](docs/MediaLibraryApi.md#update_media_file_template) | **PUT** `/api/2/media/files/templates/{id}` | 
*MediaLibraryApi* | [**update_media_root**](docs/MediaLibraryApi.md#update_media_root) | **PUT** `/api/2/media/roots/{id}` | 
*MediaLibraryApi* | [**update_media_root_permission**](docs/MediaLibraryApi.md#update_media_root_permission) | **PUT** `/api/2/media/root-permissions/{id}` | 
*MediaLibraryApi* | [**update_media_tag**](docs/MediaLibraryApi.md#update_media_tag) | **PUT** `/api/2/media/tags/{id}` | 
*MediaLibraryApi* | [**update_proxy_profile**](docs/MediaLibraryApi.md#update_proxy_profile) | **PUT** `/api/2/media/proxy-profiles/{id}` | 
*MediaLibraryApi* | [**update_saved_search**](docs/MediaLibraryApi.md#update_saved_search) | **PUT** `/api/2/media/saved-searches/{id}` | 
*MediaLibraryApi* | [**update_subclip**](docs/MediaLibraryApi.md#update_subclip) | **PUT** `/api/2/media/subclips/{id}` | 
*PrivateApi* | [**delete_stored_image**](docs/PrivateApi.md#delete_stored_image) | **DELETE** `/api/2/image/{name}` | 
*PrivateApi* | [**delete_veritone_tdo**](docs/PrivateApi.md#delete_veritone_tdo) | **DELETE** `/api/2/veritone/connections/{id}/tdo/{tdo_id}` | 
*PrivateApi* | [**export_non_proxied_assets**](docs/PrivateApi.md#export_non_proxied_assets) | **GET** `/api/2/private/export/non-proxied/{root_id}` | 
*PrivateApi* | [**export_non_proxied_assets_for_path**](docs/PrivateApi.md#export_non_proxied_assets_for_path) | **GET** `/api/2/private/export/non-proxied/{root_id}/{path}` | 
*PrivateApi* | [**export_updates**](docs/PrivateApi.md#export_updates) | **GET** `/api/2/private/export/updates/{root_id}` | 
*PrivateApi* | [**get**](docs/PrivateApi.md#get) | **GET** `/api/2/private/bootstrap` | 
*PrivateApi* | [**get_all_veritone_connections**](docs/PrivateApi.md#get_all_veritone_connections) | **GET** `/api/2/veritone/connections` | 
*PrivateApi* | [**get_all_veritone_metadata**](docs/PrivateApi.md#get_all_veritone_metadata) | **GET** `/api/2/veritone/metadata` | 
*PrivateApi* | [**get_client_side_url**](docs/PrivateApi.md#get_client_side_url) | **POST** `/api/2/private/client-side-url` | 
*PrivateApi* | [**get_help_page**](docs/PrivateApi.md#get_help_page) | **GET** `/api/2/help/{id}` | 
*PrivateApi* | [**get_locale**](docs/PrivateApi.md#get_locale) | **GET** `/api/2/private/locale/{lang}` | 
*PrivateApi* | [**get_proxy_fs_size**](docs/PrivateApi.md#get_proxy_fs_size) | **GET** `/api/2/private/media/proxyfs-size` | 
*PrivateApi* | [**get_stored_image**](docs/PrivateApi.md#get_stored_image) | **GET** `/api/2/image/{name}` | 
*PrivateApi* | [**get_veritone_connection**](docs/PrivateApi.md#get_veritone_connection) | **GET** `/api/2/veritone/connections/{id}` | 
*PrivateApi* | [**get_veritone_engines**](docs/PrivateApi.md#get_veritone_engines) | **GET** `/api/2/veritone/connections/{id}/engines` | 
*PrivateApi* | [**get_veritone_jobs**](docs/PrivateApi.md#get_veritone_jobs) | **GET** `/api/2/veritone/connections/{id}/jobs` | 
*PrivateApi* | [**get_veritone_metadata**](docs/PrivateApi.md#get_veritone_metadata) | **GET** `/api/2/veritone/metadata/{id}` | 
*PrivateApi* | [**install_license**](docs/PrivateApi.md#install_license) | **POST** `/api/2/license/install` | 
*PrivateApi* | [**language_server_request**](docs/PrivateApi.md#language_server_request) | **POST** `/api/2/language-server/{language}` | 
*PrivateApi* | [**locate_file**](docs/PrivateApi.md#locate_file) | **POST** `/api/2/private/locate` | 
*PrivateApi* | [**locate_proxies**](docs/PrivateApi.md#locate_proxies) | **POST** `/api/2/panel/locate-proxies` | 
*PrivateApi* | [**upload_stored_image**](docs/PrivateApi.md#upload_stored_image) | **POST** `/api/2/private/images/upload` | 
*PrivateApi* | [**upload_to_veritone**](docs/PrivateApi.md#upload_to_veritone) | **POST** `/api/2/veritone/connections/{id}/upload` | 
*SatelliteApi* | [**activate_satellite_host**](docs/SatelliteApi.md#activate_satellite_host) | **POST** `/api/2/rdc/hosts/{id}/activate` | 
*SatelliteApi* | [**announce_satellite_host**](docs/SatelliteApi.md#announce_satellite_host) | **POST** `/api/2/rdc/hosts/announce` | 
*SatelliteApi* | [**create_satellite_session**](docs/SatelliteApi.md#create_satellite_session) | **POST** `/api/2/rdc/sessions` | 
*SatelliteApi* | [**delete_satellite_session**](docs/SatelliteApi.md#delete_satellite_session) | **DELETE** `/api/2/rdc/sessions/{id}` | 
*SatelliteApi* | [**get_all_satellite_hosts**](docs/SatelliteApi.md#get_all_satellite_hosts) | **GET** `/api/2/rdc/hosts` | 
*SatelliteApi* | [**get_all_satellite_sessions**](docs/SatelliteApi.md#get_all_satellite_sessions) | **GET** `/api/2/rdc/sessions` | 
*SatelliteApi* | [**get_satellite_host**](docs/SatelliteApi.md#get_satellite_host) | **GET** `/api/2/rdc/hosts/{id}` | 
*SatelliteApi* | [**get_satellite_session**](docs/SatelliteApi.md#get_satellite_session) | **GET** `/api/2/rdc/sessions/{id}` | 
*SharedstorageApi* | [**get_shared_storage_value**](docs/SharedstorageApi.md#get_shared_storage_value) | **GET** `/api/2/private/shared-storage/{name}` | 
*SharedstorageApi* | [**get_user_storage_value**](docs/SharedstorageApi.md#get_user_storage_value) | **GET** `/api/2/private/user-storage/{name}` | 
*SharedstorageApi* | [**set_shared_storage_value**](docs/SharedstorageApi.md#set_shared_storage_value) | **POST** `/api/2/private/shared-storage/{name}` | 
*SharedstorageApi* | [**set_user_storage_value**](docs/SharedstorageApi.md#set_user_storage_value) | **POST** `/api/2/private/user-storage/{name}` | 
*StatusApi* | [**get_alert**](docs/StatusApi.md#get_alert) | **GET** `/api/2/alerts/{id}` | 
*StatusApi* | [**get_all_alerts**](docs/StatusApi.md#get_all_alerts) | **GET** `/api/2/alerts` | 
*StatusApi* | [**get_telegraf_stats**](docs/StatusApi.md#get_telegraf_stats) | **GET** `/api/2/telegraf-stats` | 
*StatusApi* | [**patch_alert**](docs/StatusApi.md#patch_alert) | **PATCH** `/api/2/alerts/{id}` | 
*StatusApi* | [**submit_kapacitor_alert**](docs/StatusApi.md#submit_kapacitor_alert) | **POST** `/api/2/alerts/submit` | 
*StatusApi* | [**update_alert**](docs/StatusApi.md#update_alert) | **PUT** `/api/2/alerts/{id}` | 
*StorageApi* | [**apply_workspace_affinity**](docs/StorageApi.md#apply_workspace_affinity) | **POST** `/api/2/workspaces/{id}/apply-affinity` | 
*StorageApi* | [**bookmark_workspace**](docs/StorageApi.md#bookmark_workspace) | **POST** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**calculate_directory_size**](docs/StorageApi.md#calculate_directory_size) | **POST** `/api/2/filesystem/calculate-directory-size` | 
*StorageApi* | [**check_in_into_workspace**](docs/StorageApi.md#check_in_into_workspace) | **POST** `/api/2/workspaces/{id}/check-in` | 
*StorageApi* | [**check_out_of_workspace**](docs/StorageApi.md#check_out_of_workspace) | **POST** `/api/2/workspaces/{id}/check-out` | 
*StorageApi* | [**copy_files**](docs/StorageApi.md#copy_files) | **POST** `/api/2/filesystem/copy` | 
*StorageApi* | [**create_file**](docs/StorageApi.md#create_file) | **POST** `/api/2/files` | 
*StorageApi* | [**create_path_quota**](docs/StorageApi.md#create_path_quota) | **POST** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**create_production**](docs/StorageApi.md#create_production) | **POST** `/api/2/productions` | 
*StorageApi* | [**create_share**](docs/StorageApi.md#create_share) | **POST** `/api/2/shares` | 
*StorageApi* | [**create_snapshot**](docs/StorageApi.md#create_snapshot) | **POST** `/api/2/snapshots` | 
*StorageApi* | [**create_template_folder**](docs/StorageApi.md#create_template_folder) | **POST** `/api/2/private/create-template-folder` | 
*StorageApi* | [**create_volume**](docs/StorageApi.md#create_volume) | **POST** `/api/2/volumes` | 
*StorageApi* | [**create_workspace**](docs/StorageApi.md#create_workspace) | **POST** `/api/2/workspaces` | 
*StorageApi* | [**create_workspace_permission**](docs/StorageApi.md#create_workspace_permission) | **POST** `/api/2/workspace-permissions` | 
*StorageApi* | [**delete_file**](docs/StorageApi.md#delete_file) | **DELETE** `/api/2/files/{path}` | 
*StorageApi* | [**delete_files**](docs/StorageApi.md#delete_files) | **POST** `/api/2/filesystem/delete` | 
*StorageApi* | [**delete_path_quota**](docs/StorageApi.md#delete_path_quota) | **DELETE** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**delete_production**](docs/StorageApi.md#delete_production) | **DELETE** `/api/2/productions/{id}` | 
*StorageApi* | [**delete_share**](docs/StorageApi.md#delete_share) | **DELETE** `/api/2/shares/{id}` | 
*StorageApi* | [**delete_snapshot**](docs/StorageApi.md#delete_snapshot) | **DELETE** `/api/2/snapshots/{id}` | 
*StorageApi* | [**delete_workspace**](docs/StorageApi.md#delete_workspace) | **DELETE** `/api/2/workspaces/{id}` | 
*StorageApi* | [**delete_workspace_permission**](docs/StorageApi.md#delete_workspace_permission) | **DELETE** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**get_all_deleted_workspaces**](docs/StorageApi.md#get_all_deleted_workspaces) | **GET** `/api/2/workspaces/deleted` | 
*StorageApi* | [**get_all_productions**](docs/StorageApi.md#get_all_productions) | **GET** `/api/2/productions` | 
*StorageApi* | [**get_all_shares**](docs/StorageApi.md#get_all_shares) | **GET** `/api/2/shares` | 
*StorageApi* | [**get_all_snapshots**](docs/StorageApi.md#get_all_snapshots) | **GET** `/api/2/snapshots` | 
*StorageApi* | [**get_all_volumes**](docs/StorageApi.md#get_all_volumes) | **GET** `/api/2/volumes` | 
*StorageApi* | [**get_all_workspace_permissions**](docs/StorageApi.md#get_all_workspace_permissions) | **GET** `/api/2/workspace-permissions` | 
*StorageApi* | [**get_all_workspaces**](docs/StorageApi.md#get_all_workspaces) | **GET** `/api/2/workspaces` | 
*StorageApi* | [**get_file**](docs/StorageApi.md#get_file) | **GET** `/api/2/files/{path}` | 
*StorageApi* | [**get_group_quota**](docs/StorageApi.md#get_group_quota) | **GET** `/api/2/volumes/{id}/quotas/group/{group_id}` | 
*StorageApi* | [**get_my_workspaces**](docs/StorageApi.md#get_my_workspaces) | **GET** `/api/2/workspaces/mine` | 
*StorageApi* | [**get_path_quota**](docs/StorageApi.md#get_path_quota) | **GET** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**get_production**](docs/StorageApi.md#get_production) | **GET** `/api/2/productions/{id}` | 
*StorageApi* | [**get_root_directory**](docs/StorageApi.md#get_root_directory) | **GET** `/api/2/files` | 
*StorageApi* | [**get_samba_dfree_string**](docs/StorageApi.md#get_samba_dfree_string) | **POST** `/api/2/private/dfree` | 
*StorageApi* | [**get_share**](docs/StorageApi.md#get_share) | **GET** `/api/2/shares/{id}` | 
*StorageApi* | [**get_snapshot**](docs/StorageApi.md#get_snapshot) | **GET** `/api/2/snapshots/{id}` | 
*StorageApi* | [**get_user_quota**](docs/StorageApi.md#get_user_quota) | **GET** `/api/2/volumes/{id}/quotas/user/{user_id}` | 
*StorageApi* | [**get_volume**](docs/StorageApi.md#get_volume) | **GET** `/api/2/volumes/{id}` | 
*StorageApi* | [**get_volume_active_connections**](docs/StorageApi.md#get_volume_active_connections) | **GET** `/api/2/volumes/{id}/connections` | 
*StorageApi* | [**get_volume_file_size_distribution**](docs/StorageApi.md#get_volume_file_size_distribution) | **GET** `/api/2/volumes/{id}/file-size-distribution` | 
*StorageApi* | [**get_volume_stats**](docs/StorageApi.md#get_volume_stats) | **GET** `/api/2/volumes/{id}/stats` | 
*StorageApi* | [**get_workspace**](docs/StorageApi.md#get_workspace) | **GET** `/api/2/workspaces/{id}` | 
*StorageApi* | [**get_workspace_permission**](docs/StorageApi.md#get_workspace_permission) | **GET** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**move_files**](docs/StorageApi.md#move_files) | **POST** `/api/2/filesystem/move` | 
*StorageApi* | [**move_workspace**](docs/StorageApi.md#move_workspace) | **POST** `/api/2/workspaces/{id}/move` | 
*StorageApi* | [**move_workspace_to_production**](docs/StorageApi.md#move_workspace_to_production) | **POST** `/api/2/workspaces/{id}/move-to` | 
*StorageApi* | [**patch_file**](docs/StorageApi.md#patch_file) | **PATCH** `/api/2/files/{path}` | 
*StorageApi* | [**patch_production**](docs/StorageApi.md#patch_production) | **PATCH** `/api/2/productions/{id}` | 
*StorageApi* | [**patch_share**](docs/StorageApi.md#patch_share) | **PATCH** `/api/2/shares/{id}` | 
*StorageApi* | [**patch_snapshot**](docs/StorageApi.md#patch_snapshot) | **PATCH** `/api/2/snapshots/{id}` | 
*StorageApi* | [**patch_volume**](docs/StorageApi.md#patch_volume) | **PATCH** `/api/2/volumes/{id}` | 
*StorageApi* | [**patch_workspace**](docs/StorageApi.md#patch_workspace) | **PATCH** `/api/2/workspaces/{id}` | 
*StorageApi* | [**patch_workspace_permission**](docs/StorageApi.md#patch_workspace_permission) | **PATCH** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**record_storage_trace**](docs/StorageApi.md#record_storage_trace) | **POST** `/api/2/filesystem/trace` | 
*StorageApi* | [**repair_workspace_permissions**](docs/StorageApi.md#repair_workspace_permissions) | **POST** `/api/2/workspaces/{id}/repair-permissions` | 
*StorageApi* | [**share_to_home_workspace**](docs/StorageApi.md#share_to_home_workspace) | **POST** `/api/2/share-to-home-workspace` | 
*StorageApi* | [**unbookmark_workspace**](docs/StorageApi.md#unbookmark_workspace) | **DELETE** `/api/2/workspaces/{id}/bookmark` | 
*StorageApi* | [**unzip_file**](docs/StorageApi.md#unzip_file) | **POST** `/api/2/filesystem/unzip` | 
*StorageApi* | [**update_group_quota**](docs/StorageApi.md#update_group_quota) | **PUT** `/api/2/volumes/{id}/quotas/group/{group_id}` | 
*StorageApi* | [**update_path_quota**](docs/StorageApi.md#update_path_quota) | **PUT** `/api/2/volumes/{id}/quotas/path/{relative_path}` | 
*StorageApi* | [**update_production**](docs/StorageApi.md#update_production) | **PUT** `/api/2/productions/{id}` | 
*StorageApi* | [**update_share**](docs/StorageApi.md#update_share) | **PUT** `/api/2/shares/{id}` | 
*StorageApi* | [**update_snapshot**](docs/StorageApi.md#update_snapshot) | **PUT** `/api/2/snapshots/{id}` | 
*StorageApi* | [**update_user_quota**](docs/StorageApi.md#update_user_quota) | **PUT** `/api/2/volumes/{id}/quotas/user/{user_id}` | 
*StorageApi* | [**update_volume**](docs/StorageApi.md#update_volume) | **PUT** `/api/2/volumes/{id}` | 
*StorageApi* | [**update_workspace**](docs/StorageApi.md#update_workspace) | **PUT** `/api/2/workspaces/{id}` | 
*StorageApi* | [**update_workspace_permission**](docs/StorageApi.md#update_workspace_permission) | **PUT** `/api/2/workspace-permissions/{id}` | 
*StorageApi* | [**zip_files**](docs/StorageApi.md#zip_files) | **POST** `/api/2/filesystem/zip` | 
*TapeArchiveApi* | [**archive_to_tape**](docs/TapeArchiveApi.md#archive_to_tape) | **POST** `/api/2/archive/tape/archive` | 
*TapeArchiveApi* | [**cancel_all_tape_archive_jobs**](docs/TapeArchiveApi.md#cancel_all_tape_archive_jobs) | **POST** `/api/2/archive/tape/jobs/cancel-all` | 
*TapeArchiveApi* | [**check_tape**](docs/TapeArchiveApi.md#check_tape) | **POST** `/api/2/archive/tape/library/check` | 
*TapeArchiveApi* | [**create_tape**](docs/TapeArchiveApi.md#create_tape) | **POST** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**create_tape_group**](docs/TapeArchiveApi.md#create_tape_group) | **POST** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**delete_tape**](docs/TapeArchiveApi.md#delete_tape) | **DELETE** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**delete_tape_archive_job**](docs/TapeArchiveApi.md#delete_tape_archive_job) | **DELETE** `/api/2/archive/tape/jobs/{id}` | 
*TapeArchiveApi* | [**delete_tape_group**](docs/TapeArchiveApi.md#delete_tape_group) | **DELETE** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**format_tape**](docs/TapeArchiveApi.md#format_tape) | **POST** `/api/2/archive/tape/library/format` | 
*TapeArchiveApi* | [**get_all_archived_file_entries**](docs/TapeArchiveApi.md#get_all_archived_file_entries) | **GET** `/api/2/archive/tape/files` | 
*TapeArchiveApi* | [**get_all_tape_archive_jobs**](docs/TapeArchiveApi.md#get_all_tape_archive_jobs) | **GET** `/api/2/archive/tape/jobs` | 
*TapeArchiveApi* | [**get_all_tape_groups**](docs/TapeArchiveApi.md#get_all_tape_groups) | **GET** `/api/2/archive/tape/groups` | 
*TapeArchiveApi* | [**get_all_tapes**](docs/TapeArchiveApi.md#get_all_tapes) | **GET** `/api/2/archive/tape/tapes` | 
*TapeArchiveApi* | [**get_archived_file_entry**](docs/TapeArchiveApi.md#get_archived_file_entry) | **GET** `/api/2/archive/tape/files/{id}` | 
*TapeArchiveApi* | [**get_tape**](docs/TapeArchiveApi.md#get_tape) | **GET** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**get_tape_archive_job**](docs/TapeArchiveApi.md#get_tape_archive_job) | **GET** `/api/2/archive/tape/jobs/{id}` | 
*TapeArchiveApi* | [**get_tape_archive_job_sources**](docs/TapeArchiveApi.md#get_tape_archive_job_sources) | **GET** `/api/2/archive/tape/jobs/{id}/sources` | 
*TapeArchiveApi* | [**get_tape_group**](docs/TapeArchiveApi.md#get_tape_group) | **GET** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**get_tape_library_state**](docs/TapeArchiveApi.md#get_tape_library_state) | **GET** `/api/2/archive/tape/library` | 
*TapeArchiveApi* | [**load_tape**](docs/TapeArchiveApi.md#load_tape) | **POST** `/api/2/archive/tape/library/load` | 
*TapeArchiveApi* | [**move_tape**](docs/TapeArchiveApi.md#move_tape) | **POST** `/api/2/archive/tape/library/move` | 
*TapeArchiveApi* | [**patch_tape**](docs/TapeArchiveApi.md#patch_tape) | **PATCH** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**patch_tape_group**](docs/TapeArchiveApi.md#patch_tape_group) | **PATCH** `/api/2/archive/tape/groups/{id}` | 
*TapeArchiveApi* | [**pause_tape_archive_job**](docs/TapeArchiveApi.md#pause_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/pause` | 
*TapeArchiveApi* | [**refresh_tape_library_state**](docs/TapeArchiveApi.md#refresh_tape_library_state) | **POST** `/api/2/archive/tape/library/refresh` | 
*TapeArchiveApi* | [**reindex_tape**](docs/TapeArchiveApi.md#reindex_tape) | **POST** `/api/2/archive/tape/library/reindex` | 
*TapeArchiveApi* | [**remove_finished_tape_archive_jobs**](docs/TapeArchiveApi.md#remove_finished_tape_archive_jobs) | **POST** `/api/2/archive/tape/jobs/remove-finished` | 
*TapeArchiveApi* | [**restart_tape_archive_job**](docs/TapeArchiveApi.md#restart_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/restart` | 
*TapeArchiveApi* | [**restore_from_tape**](docs/TapeArchiveApi.md#restore_from_tape) | **POST** `/api/2/archive/tape/restore` | 
*TapeArchiveApi* | [**resume_tape_archive_job**](docs/TapeArchiveApi.md#resume_tape_archive_job) | **POST** `/api/2/archive/tape/jobs/{id}/resume` | 
*TapeArchiveApi* | [**search_tape_archive**](docs/TapeArchiveApi.md#search_tape_archive) | **POST** `/api/2/archive/tape/search` | 
*TapeArchiveApi* | [**unload_tape**](docs/TapeArchiveApi.md#unload_tape) | **POST** `/api/2/archive/tape/library/unload` | 
*TapeArchiveApi* | [**update_tape**](docs/TapeArchiveApi.md#update_tape) | **PUT** `/api/2/archive/tape/tapes/{id}` | 
*TapeArchiveApi* | [**update_tape_group**](docs/TapeArchiveApi.md#update_tape_group) | **PUT** `/api/2/archive/tape/groups/{id}` | 


## Models

 - [AIAnnotation](docs/AIAnnotation.md)
 - [AIAnnotationCreateRequest](docs/AIAnnotationCreateRequest.md)
 - [AIAnnotationPartialUpdate](docs/AIAnnotationPartialUpdate.md)
 - [AIAnnotationUpdate](docs/AIAnnotationUpdate.md)
 - [AICategory](docs/AICategory.md)
 - [AICategoryDetail](docs/AICategoryDetail.md)
 - [AICategoryDetailPartialUpdate](docs/AICategoryDetailPartialUpdate.md)
 - [AICategoryDetailUpdate](docs/AICategoryDetailUpdate.md)
 - [AICategoryMiniReference](docs/AICategoryMiniReference.md)
 - [AIConnection](docs/AIConnection.md)
 - [AIDataset](docs/AIDataset.md)
 - [AIDatasetDetailReference](docs/AIDatasetDetailReference.md)
 - [AIDatasetExportRequest](docs/AIDatasetExportRequest.md)
 - [AIDatasetExportResponse](docs/AIDatasetExportResponse.md)
 - [AIDatasetReference](docs/AIDatasetReference.md)
 - [AIDatasetWithPreview](docs/AIDatasetWithPreview.md)
 - [AIDatasetWithPreviewPartialUpdate](docs/AIDatasetWithPreviewPartialUpdate.md)
 - [AIDatasetWithPreviewUpdate](docs/AIDatasetWithPreviewUpdate.md)
 - [AIImage](docs/AIImage.md)
 - [AIImageReference](docs/AIImageReference.md)
 - [AIMetadata](docs/AIMetadata.md)
 - [AIModel](docs/AIModel.md)
 - [AIModelExportRequest](docs/AIModelExportRequest.md)
 - [AIModelExportResponse](docs/AIModelExportResponse.md)
 - [AIModelInferenceRequest](docs/AIModelInferenceRequest.md)
 - [AIModelInferenceResponse](docs/AIModelInferenceResponse.md)
 - [AIModelPartialUpdate](docs/AIModelPartialUpdate.md)
 - [AIModelProgress](docs/AIModelProgress.md)
 - [AIModelTrainingRequest](docs/AIModelTrainingRequest.md)
 - [AIModelUpdate](docs/AIModelUpdate.md)
 - [AIProcessingRequest](docs/AIProcessingRequest.md)
 - [APIToken](docs/APIToken.md)
 - [APITokenPartialUpdate](docs/APITokenPartialUpdate.md)
 - [APITokenUpdate](docs/APITokenUpdate.md)
 - [APITokenWithSecret](docs/APITokenWithSecret.md)
 - [APITokenWithSecretUpdate](docs/APITokenWithSecretUpdate.md)
 - [AddAssetsToClickGallery](docs/AddAssetsToClickGallery.md)
 - [Address](docs/Address.md)
 - [Alert](docs/Alert.md)
 - [AlertPartialUpdate](docs/AlertPartialUpdate.md)
 - [AlertUpdate](docs/AlertUpdate.md)
 - [AllMediaFilesForBundlesRequest](docs/AllMediaFilesForBundlesRequest.md)
 - [ArchiveEndpointRequest](docs/ArchiveEndpointRequest.md)
 - [ArgumentType](docs/ArgumentType.md)
 - [Asset](docs/Asset.md)
 - [AssetBackup](docs/AssetBackup.md)
 - [AssetCloudLink](docs/AssetCloudLink.md)
 - [AssetMini](docs/AssetMini.md)
 - [AssetMiniReference](docs/AssetMiniReference.md)
 - [AssetPartialUpdate](docs/AssetPartialUpdate.md)
 - [AssetProjectLink](docs/AssetProjectLink.md)
 - [AssetRating](docs/AssetRating.md)
 - [AssetRatingPartialUpdate](docs/AssetRatingPartialUpdate.md)
 - [AssetRatingUpdate](docs/AssetRatingUpdate.md)
 - [AssetSubtitleLink](docs/AssetSubtitleLink.md)
 - [AssetSubtitleLinkPartialUpdate](docs/AssetSubtitleLinkPartialUpdate.md)
 - [AssetSubtitleLinkUpdate](docs/AssetSubtitleLinkUpdate.md)
 - [AssetUpdate](docs/AssetUpdate.md)
 - [AuthLoginEndpointRequest](docs/AuthLoginEndpointRequest.md)
 - [AuthLoginEndpointResponse](docs/AuthLoginEndpointResponse.md)
 - [Backend](docs/Backend.md)
 - [BackendProperties](docs/BackendProperties.md)
 - [BasicFile](docs/BasicFile.md)
 - [BeeGFSNode](docs/BeeGFSNode.md)
 - [BeeGFSTarget](docs/BeeGFSTarget.md)
 - [BootstrapData](docs/BootstrapData.md)
 - [CPUStat](docs/CPUStat.md)
 - [Certificate](docs/Certificate.md)
 - [CertificateUpdate](docs/CertificateUpdate.md)
 - [ChangeOwnPasswordRequest](docs/ChangeOwnPasswordRequest.md)
 - [ChangePasswordRequest](docs/ChangePasswordRequest.md)
 - [CheckConnectivityEndpointResponse](docs/CheckConnectivityEndpointResponse.md)
 - [ClickBackgroundUploadEndpointRequest](docs/ClickBackgroundUploadEndpointRequest.md)
 - [ClickGallery](docs/ClickGallery.md)
 - [ClickGalleryLink](docs/ClickGalleryLink.md)
 - [ClickGalleryUpdate](docs/ClickGalleryUpdate.md)
 - [ClickLinkUser](docs/ClickLinkUser.md)
 - [ClickStartUploadEndpointRequest](docs/ClickStartUploadEndpointRequest.md)
 - [ClientSession](docs/ClientSession.md)
 - [ClientSidePathEndpointRequest](docs/ClientSidePathEndpointRequest.md)
 - [ClientSidePathEndpointResponse](docs/ClientSidePathEndpointResponse.md)
 - [ClientsEndpointResponse](docs/ClientsEndpointResponse.md)
 - [CloudAccount](docs/CloudAccount.md)
 - [CloudAccountMini](docs/CloudAccountMini.md)
 - [CloudAccountMiniPartialUpdate](docs/CloudAccountMiniPartialUpdate.md)
 - [CloudAccountMiniUpdate](docs/CloudAccountMiniUpdate.md)
 - [CloudAccountPartialUpdate](docs/CloudAccountPartialUpdate.md)
 - [CloudAccountUpdate](docs/CloudAccountUpdate.md)
 - [CloudConnection](docs/CloudConnection.md)
 - [Comment](docs/Comment.md)
 - [CommentPartialUpdate](docs/CommentPartialUpdate.md)
 - [CommentUpdate](docs/CommentUpdate.md)
 - [CreateDownloadArchive](docs/CreateDownloadArchive.md)
 - [CreateHomeWorkspaceRequest](docs/CreateHomeWorkspaceRequest.md)
 - [CreatePathQuotaRequest](docs/CreatePathQuotaRequest.md)
 - [CreateTemplateFolderEndpointRequest](docs/CreateTemplateFolderEndpointRequest.md)
 - [CustomField](docs/CustomField.md)
 - [CustomFieldPartialUpdate](docs/CustomFieldPartialUpdate.md)
 - [CustomFieldReference](docs/CustomFieldReference.md)
 - [CustomFieldUpdate](docs/CustomFieldUpdate.md)
 - [DeletedWorkspace](docs/DeletedWorkspace.md)
 - [Download](docs/Download.md)
 - [DownloadArchive](docs/DownloadArchive.md)
 - [DownloadArchivePartialUpdate](docs/DownloadArchivePartialUpdate.md)
 - [DownloadArchiveUpdate](docs/DownloadArchiveUpdate.md)
 - [EditorProject](docs/EditorProject.md)
 - [EditorProjectPartialUpdate](docs/EditorProjectPartialUpdate.md)
 - [EditorProjectUpdate](docs/EditorProjectUpdate.md)
 - [EditorSubtitle](docs/EditorSubtitle.md)
 - [EditorSubtitlePartialUpdate](docs/EditorSubtitlePartialUpdate.md)
 - [EditorSubtitleUpdate](docs/EditorSubtitleUpdate.md)
 - [ElementsGroup](docs/ElementsGroup.md)
 - [ElementsGroupDetail](docs/ElementsGroupDetail.md)
 - [ElementsGroupDetailPartialUpdate](docs/ElementsGroupDetailPartialUpdate.md)
 - [ElementsGroupDetailUpdate](docs/ElementsGroupDetailUpdate.md)
 - [ElementsGroupReference](docs/ElementsGroupReference.md)
 - [ElementsUser](docs/ElementsUser.md)
 - [ElementsUserDetail](docs/ElementsUserDetail.md)
 - [ElementsUserDetailPartialUpdate](docs/ElementsUserDetailPartialUpdate.md)
 - [ElementsUserDetailUpdate](docs/ElementsUserDetailUpdate.md)
 - [ElementsUserMini](docs/ElementsUserMini.md)
 - [ElementsUserMiniReference](docs/ElementsUserMiniReference.md)
 - [ElementsUserProfile](docs/ElementsUserProfile.md)
 - [ElementsUserProfilePartialUpdate](docs/ElementsUserProfilePartialUpdate.md)
 - [ElementsUserProfileUpdate](docs/ElementsUserProfileUpdate.md)
 - [ElementsUserReference](docs/ElementsUserReference.md)
 - [ElementsVersion](docs/ElementsVersion.md)
 - [EmailPreview](docs/EmailPreview.md)
 - [EnableTOTPRequest](docs/EnableTOTPRequest.md)
 - [Event](docs/Event.md)
 - [ExternalTranscoder](docs/ExternalTranscoder.md)
 - [ExternalTranscoderPartialUpdate](docs/ExternalTranscoderPartialUpdate.md)
 - [ExternalTranscoderUpdate](docs/ExternalTranscoderUpdate.md)
 - [ExtractRequest](docs/ExtractRequest.md)
 - [FSProperties](docs/FSProperties.md)
 - [FileCopyEndpointRequest](docs/FileCopyEndpointRequest.md)
 - [FileDeleteEndpointRequest](docs/FileDeleteEndpointRequest.md)
 - [FileMoveEndpointRequest](docs/FileMoveEndpointRequest.md)
 - [FilePartialUpdate](docs/FilePartialUpdate.md)
 - [FileSizeDistribution](docs/FileSizeDistribution.md)
 - [FileSizeDistributionItem](docs/FileSizeDistributionItem.md)
 - [FileSizeEndpointResponse](docs/FileSizeEndpointResponse.md)
 - [FileUnzipEndpointRequest](docs/FileUnzipEndpointRequest.md)
 - [FileUpdate](docs/FileUpdate.md)
 - [FileZipEndpointRequest](docs/FileZipEndpointRequest.md)
 - [FilesystemFile](docs/FilesystemFile.md)
 - [FilesystemPermission](docs/FilesystemPermission.md)
 - [FilesystemPermissionPartialUpdate](docs/FilesystemPermissionPartialUpdate.md)
 - [FilesystemPermissionUpdate](docs/FilesystemPermissionUpdate.md)
 - [FilesystemTraceEndpointRequest](docs/FilesystemTraceEndpointRequest.md)
 - [FilesystemTraceEndpointResponse](docs/FilesystemTraceEndpointResponse.md)
 - [FinishUploadEndpointRequest](docs/FinishUploadEndpointRequest.md)
 - [FormatMetadata](docs/FormatMetadata.md)
 - [GeneratePasswordEndpointResponse](docs/GeneratePasswordEndpointResponse.md)
 - [GenerateProxiesRequest](docs/GenerateProxiesRequest.md)
 - [GetMultipleBundlesRequest](docs/GetMultipleBundlesRequest.md)
 - [GetMultipleFilesRequest](docs/GetMultipleFilesRequest.md)
 - [GlobalAlert](docs/GlobalAlert.md)
 - [HelpEndpointResponse](docs/HelpEndpointResponse.md)
 - [IOStat](docs/IOStat.md)
 - [ImpersonationEndpointRequest](docs/ImpersonationEndpointRequest.md)
 - [ImportAIDatasetRequest](docs/ImportAIDatasetRequest.md)
 - [ImportAIDatasetResponse](docs/ImportAIDatasetResponse.md)
 - [ImportAIModelRequest](docs/ImportAIModelRequest.md)
 - [ImportAIModelResponse](docs/ImportAIModelResponse.md)
 - [ImportJobRequest](docs/ImportJobRequest.md)
 - [ImportJobResponse](docs/ImportJobResponse.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InstallLicenseEndpointRequest](docs/InstallLicenseEndpointRequest.md)
 - [InstantiateFileTemplateRequest](docs/InstantiateFileTemplateRequest.md)
 - [Interface](docs/Interface.md)
 - [Ipmi](docs/Ipmi.md)
 - [Job](docs/Job.md)
 - [JobPartialUpdate](docs/JobPartialUpdate.md)
 - [JobReference](docs/JobReference.md)
 - [JobUpdate](docs/JobUpdate.md)
 - [KapacitorAlert](docs/KapacitorAlert.md)
 - [LDAPServer](docs/LDAPServer.md)
 - [LDAPServerGroup](docs/LDAPServerGroup.md)
 - [LDAPServerGroups](docs/LDAPServerGroups.md)
 - [LDAPServerReference](docs/LDAPServerReference.md)
 - [LDAPServerUser](docs/LDAPServerUser.md)
 - [LDAPServerUsers](docs/LDAPServerUsers.md)
 - [License](docs/License.md)
 - [ListTopics](docs/ListTopics.md)
 - [LizardFSDisk](docs/LizardFSDisk.md)
 - [LizardFSNode](docs/LizardFSNode.md)
 - [LocaleEndpointResponse](docs/LocaleEndpointResponse.md)
 - [LocateEndpointRequest](docs/LocateEndpointRequest.md)
 - [LocateProxiesEndpointRequest](docs/LocateProxiesEndpointRequest.md)
 - [LocateProxiesEndpointResponse](docs/LocateProxiesEndpointResponse.md)
 - [LocateResult](docs/LocateResult.md)
 - [Marker](docs/Marker.md)
 - [MarkerPartialUpdate](docs/MarkerPartialUpdate.md)
 - [MarkerUpdate](docs/MarkerUpdate.md)
 - [MediaFile](docs/MediaFile.md)
 - [MediaFileBundle](docs/MediaFileBundle.md)
 - [MediaFileBundleMini](docs/MediaFileBundleMini.md)
 - [MediaFileBundleMiniReference](docs/MediaFileBundleMiniReference.md)
 - [MediaFileContents](docs/MediaFileContents.md)
 - [MediaFileMini](docs/MediaFileMini.md)
 - [MediaFilePartialUpdate](docs/MediaFilePartialUpdate.md)
 - [MediaFileReference](docs/MediaFileReference.md)
 - [MediaFileTemplate](docs/MediaFileTemplate.md)
 - [MediaFileTemplatePartialUpdate](docs/MediaFileTemplatePartialUpdate.md)
 - [MediaFileTemplateUpdate](docs/MediaFileTemplateUpdate.md)
 - [MediaFileUpdate](docs/MediaFileUpdate.md)
 - [MediaFilesLookupRequest](docs/MediaFilesLookupRequest.md)
 - [MediaLibraryDeleteRequest](docs/MediaLibraryDeleteRequest.md)
 - [MediaLibraryShareRequest](docs/MediaLibraryShareRequest.md)
 - [MediaRoot](docs/MediaRoot.md)
 - [MediaRootDetail](docs/MediaRootDetail.md)
 - [MediaRootDetailPartialUpdate](docs/MediaRootDetailPartialUpdate.md)
 - [MediaRootDetailUpdate](docs/MediaRootDetailUpdate.md)
 - [MediaRootMini](docs/MediaRootMini.md)
 - [MediaRootMiniReference](docs/MediaRootMiniReference.md)
 - [MediaRootPermission](docs/MediaRootPermission.md)
 - [MediaRootPermissionAccessOptions](docs/MediaRootPermissionAccessOptions.md)
 - [MediaRootPermissionPartialUpdate](docs/MediaRootPermissionPartialUpdate.md)
 - [MediaRootPermissionUpdate](docs/MediaRootPermissionUpdate.md)
 - [MediaUpdate](docs/MediaUpdate.md)
 - [MemberPreview](docs/MemberPreview.md)
 - [MetadataItem](docs/MetadataItem.md)
 - [MoveWorkspaceRequest](docs/MoveWorkspaceRequest.md)
 - [MultipleAssetsRequest](docs/MultipleAssetsRequest.md)
 - [NFSPermission](docs/NFSPermission.md)
 - [NTPServer](docs/NTPServer.md)
 - [NTPServerPartialUpdate](docs/NTPServerPartialUpdate.md)
 - [NTPServerUpdate](docs/NTPServerUpdate.md)
 - [NetStat](docs/NetStat.md)
 - [OneTimeAccessToken](docs/OneTimeAccessToken.md)
 - [OneTimeAccessTokenActivity](docs/OneTimeAccessTokenActivity.md)
 - [OneTimeAccessTokenSharedObject](docs/OneTimeAccessTokenSharedObject.md)
 - [Parameters](docs/Parameters.md)
 - [ParametersUpdate](docs/ParametersUpdate.md)
 - [ParseSAMLIDPMetadataRequest](docs/ParseSAMLIDPMetadataRequest.md)
 - [ParsedSAMLIDPMetadata](docs/ParsedSAMLIDPMetadata.md)
 - [PasswordResetEndpointRequest](docs/PasswordResetEndpointRequest.md)
 - [Path](docs/Path.md)
 - [PathInput](docs/PathInput.md)
 - [Production](docs/Production.md)
 - [ProductionMiniReference](docs/ProductionMiniReference.md)
 - [ProductionPartialUpdate](docs/ProductionPartialUpdate.md)
 - [ProductionReference](docs/ProductionReference.md)
 - [ProductionUpdate](docs/ProductionUpdate.md)
 - [Proxy](docs/Proxy.md)
 - [ProxyCount](docs/ProxyCount.md)
 - [ProxyFSSizeEndpointResponse](docs/ProxyFSSizeEndpointResponse.md)
 - [ProxyGenerator](docs/ProxyGenerator.md)
 - [ProxyGeneratorProperties](docs/ProxyGeneratorProperties.md)
 - [ProxyProfile](docs/ProxyProfile.md)
 - [ProxyProfileMini](docs/ProxyProfileMini.md)
 - [ProxyProfilePartialUpdate](docs/ProxyProfilePartialUpdate.md)
 - [ProxyProfileUpdate](docs/ProxyProfileUpdate.md)
 - [PythonEnvironment](docs/PythonEnvironment.md)
 - [Queue](docs/Queue.md)
 - [Quota](docs/Quota.md)
 - [RAMStat](docs/RAMStat.md)
 - [RDCActivation](docs/RDCActivation.md)
 - [RDCHost](docs/RDCHost.md)
 - [RDCSession](docs/RDCSession.md)
 - [RDCSessionCreate](docs/RDCSessionCreate.md)
 - [RegisterUploadEndpointRequest](docs/RegisterUploadEndpointRequest.md)
 - [RegisterUploadMetadataEndpointRequest](docs/RegisterUploadMetadataEndpointRequest.md)
 - [ReleaseNotesEndpointResponse](docs/ReleaseNotesEndpointResponse.md)
 - [RenameCustomFieldRequest](docs/RenameCustomFieldRequest.md)
 - [RenderEndpointRequest](docs/RenderEndpointRequest.md)
 - [RenderRequest](docs/RenderRequest.md)
 - [RestoreEndpointRequest](docs/RestoreEndpointRequest.md)
 - [SAMLProvider](docs/SAMLProvider.md)
 - [SAMLProviderMini](docs/SAMLProviderMini.md)
 - [SAMLProviderPartialUpdate](docs/SAMLProviderPartialUpdate.md)
 - [SAMLProviderUpdate](docs/SAMLProviderUpdate.md)
 - [SMTPConfiguration](docs/SMTPConfiguration.md)
 - [SMTPConfigurationUpdate](docs/SMTPConfigurationUpdate.md)
 - [SNFSStripeGroup](docs/SNFSStripeGroup.md)
 - [SavedSearch](docs/SavedSearch.md)
 - [SavedSearchPartialUpdate](docs/SavedSearchPartialUpdate.md)
 - [SavedSearchUpdate](docs/SavedSearchUpdate.md)
 - [ScannerDiscoverEndpointRequest](docs/ScannerDiscoverEndpointRequest.md)
 - [ScannerScanEndpointRequest](docs/ScannerScanEndpointRequest.md)
 - [Schedule](docs/Schedule.md)
 - [SchedulePartialUpdate](docs/SchedulePartialUpdate.md)
 - [ScheduleReference](docs/ScheduleReference.md)
 - [ScheduleUpdate](docs/ScheduleUpdate.md)
 - [SearchEndpointRequest](docs/SearchEndpointRequest.md)
 - [SearchEndpointResponse](docs/SearchEndpointResponse.md)
 - [SendLinkEmailRequest](docs/SendLinkEmailRequest.md)
 - [Sensor](docs/Sensor.md)
 - [Sensors](docs/Sensors.md)
 - [ServiceStatus](docs/ServiceStatus.md)
 - [Share](docs/Share.md)
 - [SharePartialUpdate](docs/SharePartialUpdate.md)
 - [ShareToHomeWorkspaceEndpointRequest](docs/ShareToHomeWorkspaceEndpointRequest.md)
 - [ShareUpdate](docs/ShareUpdate.md)
 - [SlackChannel](docs/SlackChannel.md)
 - [SlackConnection](docs/SlackConnection.md)
 - [SlackConnectionPartialUpdate](docs/SlackConnectionPartialUpdate.md)
 - [SlackConnectionStatus](docs/SlackConnectionStatus.md)
 - [SlackConnectionUpdate](docs/SlackConnectionUpdate.md)
 - [SlackEmoji](docs/SlackEmoji.md)
 - [SlackMessage](docs/SlackMessage.md)
 - [SlackUser](docs/SlackUser.md)
 - [Snapshot](docs/Snapshot.md)
 - [SnapshotPartialUpdate](docs/SnapshotPartialUpdate.md)
 - [SnapshotUpdate](docs/SnapshotUpdate.md)
 - [SolrReindexEndpointResponse](docs/SolrReindexEndpointResponse.md)
 - [StartJobRequest](docs/StartJobRequest.md)
 - [StartTaskRequest](docs/StartTaskRequest.md)
 - [Stats](docs/Stats.md)
 - [StorNextConnection](docs/StorNextConnection.md)
 - [StorNextConnections](docs/StorNextConnections.md)
 - [StorNextLicenseCheckEndpointResponse](docs/StorNextLicenseCheckEndpointResponse.md)
 - [StorNextLicenseEndpointResponse](docs/StorNextLicenseEndpointResponse.md)
 - [StorageNode](docs/StorageNode.md)
 - [StorageNodeMini](docs/StorageNodeMini.md)
 - [StorageNodeStatus](docs/StorageNodeStatus.md)
 - [StorageRequest](docs/StorageRequest.md)
 - [StorageResponse](docs/StorageResponse.md)
 - [StorageRoot](docs/StorageRoot.md)
 - [StornextLicense](docs/StornextLicense.md)
 - [StornextManagerAttributes](docs/StornextManagerAttributes.md)
 - [Subclip](docs/Subclip.md)
 - [SubclipClipboardEntry](docs/SubclipClipboardEntry.md)
 - [SubclipClipboardEntryUpdate](docs/SubclipClipboardEntryUpdate.md)
 - [SubclipPartialUpdate](docs/SubclipPartialUpdate.md)
 - [SubclipReference](docs/SubclipReference.md)
 - [SubclipUpdate](docs/SubclipUpdate.md)
 - [Subscription](docs/Subscription.md)
 - [Subtask](docs/Subtask.md)
 - [SubtaskPartialUpdate](docs/SubtaskPartialUpdate.md)
 - [SubtaskReference](docs/SubtaskReference.md)
 - [SubtaskUpdate](docs/SubtaskUpdate.md)
 - [Subtitle](docs/Subtitle.md)
 - [SubtitleClipboardEntry](docs/SubtitleClipboardEntry.md)
 - [SubtitleClipboardEntryUpdate](docs/SubtitleClipboardEntryUpdate.md)
 - [SubtitleEvent](docs/SubtitleEvent.md)
 - [SyncTOTP](docs/SyncTOTP.md)
 - [SyncTOTPRequest](docs/SyncTOTPRequest.md)
 - [SystemInfoEndpointResponse](docs/SystemInfoEndpointResponse.md)
 - [TagMediaDirectoryRequest](docs/TagMediaDirectoryRequest.md)
 - [TagReference](docs/TagReference.md)
 - [Tape](docs/Tape.md)
 - [TapeFile](docs/TapeFile.md)
 - [TapeGroup](docs/TapeGroup.md)
 - [TapeGroupPartialUpdate](docs/TapeGroupPartialUpdate.md)
 - [TapeGroupUpdate](docs/TapeGroupUpdate.md)
 - [TapeJob](docs/TapeJob.md)
 - [TapeJobSource](docs/TapeJobSource.md)
 - [TapeLibraryEndpointResponse](docs/TapeLibraryEndpointResponse.md)
 - [TapeLibraryFormatEndpointRequest](docs/TapeLibraryFormatEndpointRequest.md)
 - [TapeLibraryFsckEndpointRequest](docs/TapeLibraryFsckEndpointRequest.md)
 - [TapeLibraryLoadEndpointRequest](docs/TapeLibraryLoadEndpointRequest.md)
 - [TapeLibraryMoveEndpointRequest](docs/TapeLibraryMoveEndpointRequest.md)
 - [TapeLibraryReindexEndpointRequest](docs/TapeLibraryReindexEndpointRequest.md)
 - [TapeLibrarySlot](docs/TapeLibrarySlot.md)
 - [TapeLibraryUnloadEndpointRequest](docs/TapeLibraryUnloadEndpointRequest.md)
 - [TapePartialUpdate](docs/TapePartialUpdate.md)
 - [TapeReference](docs/TapeReference.md)
 - [TapeUpdate](docs/TapeUpdate.md)
 - [TaskInfo](docs/TaskInfo.md)
 - [TaskLog](docs/TaskLog.md)
 - [TaskProgress](docs/TaskProgress.md)
 - [TaskType](docs/TaskType.md)
 - [TasksSummary](docs/TasksSummary.md)
 - [TeamsConnection](docs/TeamsConnection.md)
 - [TeamsConnectionPartialUpdate](docs/TeamsConnectionPartialUpdate.md)
 - [TeamsConnectionStatus](docs/TeamsConnectionStatus.md)
 - [TeamsConnectionUpdate](docs/TeamsConnectionUpdate.md)
 - [TeamsMessage](docs/TeamsMessage.md)
 - [TeamsRecipient](docs/TeamsRecipient.md)
 - [TestAWSCredentialsRequest](docs/TestAWSCredentialsRequest.md)
 - [TestAWSCredentialsResponse](docs/TestAWSCredentialsResponse.md)
 - [TestCloudAccountCredentialsRequest](docs/TestCloudAccountCredentialsRequest.md)
 - [TestCloudAccountCredentialsResponse](docs/TestCloudAccountCredentialsResponse.md)
 - [TestExternalTranscoderConnectionRequest](docs/TestExternalTranscoderConnectionRequest.md)
 - [TestExternalTranscoderConnectionResponse](docs/TestExternalTranscoderConnectionResponse.md)
 - [TestSMTP](docs/TestSMTP.md)
 - [Ticket](docs/Ticket.md)
 - [TimeEndpointRequest](docs/TimeEndpointRequest.md)
 - [TimeEndpointResponse](docs/TimeEndpointResponse.md)
 - [TimeSyncEndpointRequest](docs/TimeSyncEndpointRequest.md)
 - [TimeSyncEndpointResponse](docs/TimeSyncEndpointResponse.md)
 - [TimelineExportRequest](docs/TimelineExportRequest.md)
 - [Timezone](docs/Timezone.md)
 - [TraceNode](docs/TraceNode.md)
 - [TranscoderProfile](docs/TranscoderProfile.md)
 - [TypeDocumentation](docs/TypeDocumentation.md)
 - [UnfilteredTag](docs/UnfilteredTag.md)
 - [UnfilteredTagPartialUpdate](docs/UnfilteredTagPartialUpdate.md)
 - [UnfilteredTagUpdate](docs/UnfilteredTagUpdate.md)
 - [UpdateQuotaRequest](docs/UpdateQuotaRequest.md)
 - [UploadAIImageRequest](docs/UploadAIImageRequest.md)
 - [UploadChunkEndpointRequest](docs/UploadChunkEndpointRequest.md)
 - [UploadImageEndpointRequest](docs/UploadImageEndpointRequest.md)
 - [UserPreviewRequest](docs/UserPreviewRequest.md)
 - [UserPreviewResponse](docs/UserPreviewResponse.md)
 - [VantageWorkflow](docs/VantageWorkflow.md)
 - [VantageWorkflows](docs/VantageWorkflows.md)
 - [VeritoneConnection](docs/VeritoneConnection.md)
 - [VeritoneEngineList](docs/VeritoneEngineList.md)
 - [VeritoneJobList](docs/VeritoneJobList.md)
 - [VeritoneMetadata](docs/VeritoneMetadata.md)
 - [VeritoneUploadRequest](docs/VeritoneUploadRequest.md)
 - [Volume](docs/Volume.md)
 - [VolumeBeeGFSStatus](docs/VolumeBeeGFSStatus.md)
 - [VolumeLizardFSStatus](docs/VolumeLizardFSStatus.md)
 - [VolumeMini](docs/VolumeMini.md)
 - [VolumeMiniReference](docs/VolumeMiniReference.md)
 - [VolumePartialUpdate](docs/VolumePartialUpdate.md)
 - [VolumeReference](docs/VolumeReference.md)
 - [VolumeSNFSStatus](docs/VolumeSNFSStatus.md)
 - [VolumeStat](docs/VolumeStat.md)
 - [VolumeStats](docs/VolumeStats.md)
 - [VolumeStatus](docs/VolumeStatus.md)
 - [VolumeUpdate](docs/VolumeUpdate.md)
 - [WorkflowTransitionRequest](docs/WorkflowTransitionRequest.md)
 - [WorkflowTransitionResponse](docs/WorkflowTransitionResponse.md)
 - [Workspace](docs/Workspace.md)
 - [WorkspaceCheckIn](docs/WorkspaceCheckIn.md)
 - [WorkspaceDetail](docs/WorkspaceDetail.md)
 - [WorkspaceDetailPartialUpdate](docs/WorkspaceDetailPartialUpdate.md)
 - [WorkspaceDetailUpdate](docs/WorkspaceDetailUpdate.md)
 - [WorkspaceEndpoint](docs/WorkspaceEndpoint.md)
 - [WorkspaceMoveToRequest](docs/WorkspaceMoveToRequest.md)
 - [WorkspacePermission](docs/WorkspacePermission.md)
 - [WorkspacePermissionPartialUpdate](docs/WorkspacePermissionPartialUpdate.md)
 - [WorkspacePermissionUpdate](docs/WorkspacePermissionUpdate.md)
 - [WorkspaceResolvedPermission](docs/WorkspaceResolvedPermission.md)
 - [Workstation](docs/Workstation.md)
 - [WorkstationMini](docs/WorkstationMini.md)
 - [WorkstationPartialUpdate](docs/WorkstationPartialUpdate.md)
 - [WorkstationUpdate](docs/WorkstationUpdate.md)


