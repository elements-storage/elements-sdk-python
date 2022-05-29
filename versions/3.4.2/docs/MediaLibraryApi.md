# elements_sdk.MediaLibraryApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmark_media_directory**](MediaLibraryApi.md#bookmark_media_directory) | **POST** `/api/2/media/files/{id}/bookmark` | 
[**clear_subclip_clipboard**](MediaLibraryApi.md#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
[**combine_assets_into_set**](MediaLibraryApi.md#combine_assets_into_set) | **POST** `/api/2/media/assets/combine` | 
[**create_asset**](MediaLibraryApi.md#create_asset) | **POST** `/api/2/media/assets` | 
[**create_asset_rating**](MediaLibraryApi.md#create_asset_rating) | **POST** `/api/2/media/ratings` | 
[**create_comment**](MediaLibraryApi.md#create_comment) | **POST** `/api/2/media/comments` | 
[**create_custom_field**](MediaLibraryApi.md#create_custom_field) | **POST** `/api/2/media/custom-fields` | 
[**create_editor_project**](MediaLibraryApi.md#create_editor_project) | **POST** `/api/2/media/editor` | 
[**create_external_transcoder**](MediaLibraryApi.md#create_external_transcoder) | **POST** `/api/2/media/external-transcoders` | 
[**create_marker**](MediaLibraryApi.md#create_marker) | **POST** `/api/2/media/markers` | 
[**create_media_file_template**](MediaLibraryApi.md#create_media_file_template) | **POST** `/api/2/media/files/templates` | 
[**create_media_root**](MediaLibraryApi.md#create_media_root) | **POST** `/api/2/media/roots` | 
[**create_media_root_permission**](MediaLibraryApi.md#create_media_root_permission) | **POST** `/api/2/media/root-permissions` | 
[**create_media_tag**](MediaLibraryApi.md#create_media_tag) | **POST** `/api/2/media/tags` | 
[**create_proxy_profile**](MediaLibraryApi.md#create_proxy_profile) | **POST** `/api/2/media/proxy-profiles` | 
[**create_subclip**](MediaLibraryApi.md#create_subclip) | **POST** `/api/2/media/subclips` | 
[**create_subclip_clipboard_entry**](MediaLibraryApi.md#create_subclip_clipboard_entry) | **POST** `/api/2/media/subclips/clipboard` | 
[**delete_asset**](MediaLibraryApi.md#delete_asset) | **DELETE** `/api/2/media/assets/{id}` | 
[**delete_asset_rating**](MediaLibraryApi.md#delete_asset_rating) | **DELETE** `/api/2/media/ratings/{id}` | 
[**delete_comment**](MediaLibraryApi.md#delete_comment) | **DELETE** `/api/2/media/comments/{id}` | 
[**delete_custom_field**](MediaLibraryApi.md#delete_custom_field) | **DELETE** `/api/2/media/custom-fields/{id}` | 
[**delete_easy_sharing_token_for_bundle**](MediaLibraryApi.md#delete_easy_sharing_token_for_bundle) | **DELETE** `/api/2/media/bundles/{id}/easy-sharing-token` | 
[**delete_easy_sharing_token_for_directory**](MediaLibraryApi.md#delete_easy_sharing_token_for_directory) | **DELETE** `/api/2/media/files/{id}/easy-sharing-token` | 
[**delete_external_transcoder**](MediaLibraryApi.md#delete_external_transcoder) | **DELETE** `/api/2/media/external-transcoders/{id}` | 
[**delete_marker**](MediaLibraryApi.md#delete_marker) | **DELETE** `/api/2/media/markers/{id}` | 
[**delete_media_file_template**](MediaLibraryApi.md#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
[**delete_media_library_objects**](MediaLibraryApi.md#delete_media_library_objects) | **POST** `/api/2/media/delete` | 
[**delete_media_root**](MediaLibraryApi.md#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
[**delete_media_root_permission**](MediaLibraryApi.md#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
[**delete_media_tag**](MediaLibraryApi.md#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
[**delete_media_update**](MediaLibraryApi.md#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
[**delete_proxy**](MediaLibraryApi.md#delete_proxy) | **DELETE** `/api/2/media/proxies/{id}` | 
[**delete_proxy_profile**](MediaLibraryApi.md#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
[**delete_subclip**](MediaLibraryApi.md#delete_subclip) | **DELETE** `/api/2/media/subclips/{id}` | 
[**delete_subclip_clipboard_entry**](MediaLibraryApi.md#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
[**discover_media**](MediaLibraryApi.md#discover_media) | **POST** `/api/2/scanner/discover` | 
[**download_asset_proxy_file**](MediaLibraryApi.md#download_asset_proxy_file) | **GET** `/api/2/media/assets/{id}/proxy-files/{filename}` | 
[**download_media_file**](MediaLibraryApi.md#download_media_file) | **GET** `/api/2/media/files/{id}/download` | 
[**download_proxy**](MediaLibraryApi.md#download_proxy) | **GET** `/api/2/media/proxies/{id}/download` | 
[**editor_export_xml_for_assset**](MediaLibraryApi.md#editor_export_xml_for_assset) | **GET** `/api/2/media/editor/asset/{asset_ids}/xml-export` | 
[**editor_export_xml_for_bundle**](MediaLibraryApi.md#editor_export_xml_for_bundle) | **GET** `/api/2/media/editor/bundle/{bundle_ids}/xml-export` | 
[**editor_export_xml_for_project**](MediaLibraryApi.md#editor_export_xml_for_project) | **GET** `/api/2/media/editor/{id}/xml-export` | 
[**export_comments_for_avid**](MediaLibraryApi.md#export_comments_for_avid) | **GET** `/api/2/media/editor/asset/{asset_id}/{export_format}-export/avid-comments` | 
[**export_editor_timeline**](MediaLibraryApi.md#export_editor_timeline) | **POST** `/api/2/media/editor/timeline-export` | 
[**forget_deleted_media_files**](MediaLibraryApi.md#forget_deleted_media_files) | **POST** `/api/2/media/files/{id}/forget-deleted` | 
[**generate_proxies**](MediaLibraryApi.md#generate_proxies) | **POST** `/api/2/media/proxies` | 
[**get_all_asset_project_links**](MediaLibraryApi.md#get_all_asset_project_links) | **GET** `/api/2/media/assets/project-links` | 
[**get_all_asset_ratings**](MediaLibraryApi.md#get_all_asset_ratings) | **GET** `/api/2/media/ratings` | 
[**get_all_asset_tape_backups**](MediaLibraryApi.md#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
[**get_all_assets**](MediaLibraryApi.md#get_all_assets) | **GET** `/api/2/media/assets` | 
[**get_all_bundles_for_media_root**](MediaLibraryApi.md#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
[**get_all_click_links**](MediaLibraryApi.md#get_all_click_links) | **GET** `/api/2/media/assets/click-links` | 
[**get_all_comments**](MediaLibraryApi.md#get_all_comments) | **GET** `/api/2/media/comments` | 
[**get_all_custom_fields**](MediaLibraryApi.md#get_all_custom_fields) | **GET** `/api/2/media/custom-fields` | 
[**get_all_external_transcoders**](MediaLibraryApi.md#get_all_external_transcoders) | **GET** `/api/2/media/external-transcoders` | 
[**get_all_markers**](MediaLibraryApi.md#get_all_markers) | **GET** `/api/2/media/markers` | 
[**get_all_media_file_bundles**](MediaLibraryApi.md#get_all_media_file_bundles) | **GET** `/api/2/media/bundles` | 
[**get_all_media_file_templates**](MediaLibraryApi.md#get_all_media_file_templates) | **GET** `/api/2/media/files/templates` | 
[**get_all_media_files**](MediaLibraryApi.md#get_all_media_files) | **GET** `/api/2/media/files` | 
[**get_all_media_files_for_bundles**](MediaLibraryApi.md#get_all_media_files_for_bundles) | **POST** `/api/2/media/files/for-bundles` | 
[**get_all_media_files_for_media_root**](MediaLibraryApi.md#get_all_media_files_for_media_root) | **GET** `/api/2/media/files/flat/{root}` | 
[**get_all_media_root_permissions**](MediaLibraryApi.md#get_all_media_root_permissions) | **GET** `/api/2/media/root-permissions` | 
[**get_all_media_roots**](MediaLibraryApi.md#get_all_media_roots) | **GET** `/api/2/media/roots` | 
[**get_all_media_tags**](MediaLibraryApi.md#get_all_media_tags) | **GET** `/api/2/media/tags` | 
[**get_all_media_updates**](MediaLibraryApi.md#get_all_media_updates) | **GET** `/api/2/media/updates` | 
[**get_all_proxy_generators**](MediaLibraryApi.md#get_all_proxy_generators) | **GET** `/api/2/media/proxy-generators` | 
[**get_all_proxy_profiles**](MediaLibraryApi.md#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
[**get_all_subclip_clipboard_entries**](MediaLibraryApi.md#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
[**get_all_subclips**](MediaLibraryApi.md#get_all_subclips) | **GET** `/api/2/media/subclips` | 
[**get_all_transcoder_profiles**](MediaLibraryApi.md#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
[**get_asset**](MediaLibraryApi.md#get_asset) | **GET** `/api/2/media/assets/{id}` | 
[**get_asset_rating**](MediaLibraryApi.md#get_asset_rating) | **GET** `/api/2/media/ratings/{id}` | 
[**get_bookmarked_media_files_directories**](MediaLibraryApi.md#get_bookmarked_media_files_directories) | **GET** `/api/2/media/files/bookmarks` | 
[**get_comment**](MediaLibraryApi.md#get_comment) | **GET** `/api/2/media/comments/{id}` | 
[**get_custom_field**](MediaLibraryApi.md#get_custom_field) | **GET** `/api/2/media/custom-fields/{id}` | 
[**get_easy_sharing_token_for_bundle**](MediaLibraryApi.md#get_easy_sharing_token_for_bundle) | **GET** `/api/2/media/bundles/{id}/easy-sharing-token` | 
[**get_easy_sharing_token_for_directory**](MediaLibraryApi.md#get_easy_sharing_token_for_directory) | **GET** `/api/2/media/files/{id}/easy-sharing-token` | 
[**get_editor_project**](MediaLibraryApi.md#get_editor_project) | **GET** `/api/2/media/editor/{id}` | 
[**get_external_transcoder**](MediaLibraryApi.md#get_external_transcoder) | **GET** `/api/2/media/external-transcoders/{id}` | 
[**get_frame**](MediaLibraryApi.md#get_frame) | **GET** `/api/2/media/assets/{id}/frames/{frame}` | 
[**get_latest_media_update**](MediaLibraryApi.md#get_latest_media_update) | **GET** `/api/2/media/updates/latest` | 
[**get_marker**](MediaLibraryApi.md#get_marker) | **GET** `/api/2/media/markers/{id}` | 
[**get_media_file**](MediaLibraryApi.md#get_media_file) | **GET** `/api/2/media/files/{id}` | 
[**get_media_file_bundle**](MediaLibraryApi.md#get_media_file_bundle) | **GET** `/api/2/media/bundles/{id}` | 
[**get_media_file_contents**](MediaLibraryApi.md#get_media_file_contents) | **GET** `/api/2/media/files/{id}/contents` | 
[**get_media_file_template**](MediaLibraryApi.md#get_media_file_template) | **GET** `/api/2/media/files/templates/{id}` | 
[**get_media_root**](MediaLibraryApi.md#get_media_root) | **GET** `/api/2/media/roots/{id}` | 
[**get_media_root_permission**](MediaLibraryApi.md#get_media_root_permission) | **GET** `/api/2/media/root-permissions/{id}` | 
[**get_media_tag**](MediaLibraryApi.md#get_media_tag) | **GET** `/api/2/media/tags/{id}` | 
[**get_multiple_assets**](MediaLibraryApi.md#get_multiple_assets) | **POST** `/api/2/media/assets/multiple` | 
[**get_multiple_bundles**](MediaLibraryApi.md#get_multiple_bundles) | **POST** `/api/2/media/bundles/multiple` | 
[**get_multiple_files**](MediaLibraryApi.md#get_multiple_files) | **POST** `/api/2/media/files/multiple` | 
[**get_my_media_root_permissions**](MediaLibraryApi.md#get_my_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine` | 
[**get_my_resolved_media_root_permissions**](MediaLibraryApi.md#get_my_resolved_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine/resolved` | 
[**get_proxy**](MediaLibraryApi.md#get_proxy) | **GET** `/api/2/media/proxies/{id}` | 
[**get_proxy_generator**](MediaLibraryApi.md#get_proxy_generator) | **GET** `/api/2/media/proxy-generators/{id}` | 
[**get_proxy_profile**](MediaLibraryApi.md#get_proxy_profile) | **GET** `/api/2/media/proxy-profiles/{id}` | 
[**get_proxy_profile_proxy_count**](MediaLibraryApi.md#get_proxy_profile_proxy_count) | **GET** `/api/2/media/proxy-profiles/{id}/proxy-count` | 
[**get_subclip**](MediaLibraryApi.md#get_subclip) | **GET** `/api/2/media/subclips/{id}` | 
[**get_transcoder_profile**](MediaLibraryApi.md#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
[**get_vantage_workflows**](MediaLibraryApi.md#get_vantage_workflows) | **GET** `/api/2/media/external-transcoders/{id}/workflows` | 
[**instantiate_media_file_template**](MediaLibraryApi.md#instantiate_media_file_template) | **POST** `/api/2/media/files/templates/{id}/instantiate` | 
[**locate_editor_project_paths**](MediaLibraryApi.md#locate_editor_project_paths) | **GET** `/api/2/media/editor/{id}/locate-paths` | 
[**mark_media_directory_as_showroom**](MediaLibraryApi.md#mark_media_directory_as_showroom) | **POST** `/api/2/media/files/{id}/showroom` | 
[**patch_asset**](MediaLibraryApi.md#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
[**patch_asset_rating**](MediaLibraryApi.md#patch_asset_rating) | **PATCH** `/api/2/media/ratings/{id}` | 
[**patch_comment**](MediaLibraryApi.md#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
[**patch_custom_field**](MediaLibraryApi.md#patch_custom_field) | **PATCH** `/api/2/media/custom-fields/{id}` | 
[**patch_editor_project**](MediaLibraryApi.md#patch_editor_project) | **PATCH** `/api/2/media/editor/{id}` | 
[**patch_external_transcoder**](MediaLibraryApi.md#patch_external_transcoder) | **PATCH** `/api/2/media/external-transcoders/{id}` | 
[**patch_marker**](MediaLibraryApi.md#patch_marker) | **PATCH** `/api/2/media/markers/{id}` | 
[**patch_media_file**](MediaLibraryApi.md#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
[**patch_media_file_template**](MediaLibraryApi.md#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
[**patch_media_root**](MediaLibraryApi.md#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
[**patch_media_root_permission**](MediaLibraryApi.md#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
[**patch_media_tag**](MediaLibraryApi.md#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
[**patch_proxy_profile**](MediaLibraryApi.md#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
[**patch_subclip**](MediaLibraryApi.md#patch_subclip) | **PATCH** `/api/2/media/subclips/{id}` | 
[**recursively_tag_media_directory**](MediaLibraryApi.md#recursively_tag_media_directory) | **POST** `/api/2/media/files/{id}/tag` | 
[**reindex_media_directory**](MediaLibraryApi.md#reindex_media_directory) | **POST** `/api/2/media/files/{id}/search-reindex` | 
[**rename_custom_field**](MediaLibraryApi.md#rename_custom_field) | **POST** `/api/2/media/custom-fields/{id}/rename` | 
[**render_sequence**](MediaLibraryApi.md#render_sequence) | **POST** `/api/2/media/editor/render` | 
[**render_subclip**](MediaLibraryApi.md#render_subclip) | **POST** `/api/2/media/subclips/{id}/render` | 
[**request_media_scan**](MediaLibraryApi.md#request_media_scan) | **POST** `/api/2/scanner/scan` | 
[**resolve_comment**](MediaLibraryApi.md#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
[**share_media_library_objects**](MediaLibraryApi.md#share_media_library_objects) | **POST** `/api/2/media/share` | 
[**test_external_transcoder_connection**](MediaLibraryApi.md#test_external_transcoder_connection) | **POST** `/api/2/media/external-transcoders/test-connection` | 
[**transition_workflow**](MediaLibraryApi.md#transition_workflow) | **POST** `/api/2/media/workflow/transition` | 
[**unbookmark_media_directory**](MediaLibraryApi.md#unbookmark_media_directory) | **DELETE** `/api/2/media/files/{id}/bookmark` | 
[**unmark_media_directory_as_showroom**](MediaLibraryApi.md#unmark_media_directory_as_showroom) | **DELETE** `/api/2/media/files/{id}/showroom` | 
[**unresolve_comment**](MediaLibraryApi.md#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
[**update_asset**](MediaLibraryApi.md#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
[**update_asset_rating**](MediaLibraryApi.md#update_asset_rating) | **PUT** `/api/2/media/ratings/{id}` | 
[**update_comment**](MediaLibraryApi.md#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
[**update_custom_field**](MediaLibraryApi.md#update_custom_field) | **PUT** `/api/2/media/custom-fields/{id}` | 
[**update_editor_project**](MediaLibraryApi.md#update_editor_project) | **PUT** `/api/2/media/editor/{id}` | 
[**update_external_transcoder**](MediaLibraryApi.md#update_external_transcoder) | **PUT** `/api/2/media/external-transcoders/{id}` | 
[**update_marker**](MediaLibraryApi.md#update_marker) | **PUT** `/api/2/media/markers/{id}` | 
[**update_media_file**](MediaLibraryApi.md#update_media_file) | **PUT** `/api/2/media/files/{id}` | 
[**update_media_file_template**](MediaLibraryApi.md#update_media_file_template) | **PUT** `/api/2/media/files/templates/{id}` | 
[**update_media_root**](MediaLibraryApi.md#update_media_root) | **PUT** `/api/2/media/roots/{id}` | 
[**update_media_root_permission**](MediaLibraryApi.md#update_media_root_permission) | **PUT** `/api/2/media/root-permissions/{id}` | 
[**update_media_tag**](MediaLibraryApi.md#update_media_tag) | **PUT** `/api/2/media/tags/{id}` | 
[**update_proxy_profile**](MediaLibraryApi.md#update_proxy_profile) | **PUT** `/api/2/media/proxy-profiles/{id}` | 
[**update_subclip**](MediaLibraryApi.md#update_subclip) | **PUT** `/api/2/media/subclips/{id}` | 



***

# **bookmark_media_directory**

    def bookmark_media_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.bookmark_media_directory(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->bookmark_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **clear_subclip_clipboard**

    def clear_subclip_clipboard()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    
    try:
        api_instance.clear_subclip_clipboard()
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->clear_subclip_clipboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **combine_assets_into_set**

    def combine_assets_into_set(multiple_assets_request)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    multiple_assets_request = elements_sdk.MultipleAssetsRequest() # MultipleAssetsRequest | 

    try:
        api_instance.combine_assets_into_set(multiple_assets_request)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->combine_assets_into_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_assets_request** | [**MultipleAssetsRequest**](MultipleAssetsRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_asset**

    def create_asset(asset) -> Asset 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = elements_sdk.Asset() # Asset | 

    try:
        api_response = api_instance.create_asset(asset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_asset_rating**

    def create_asset_rating(asset_rating) -> AssetRating 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset_rating = elements_sdk.AssetRating() # AssetRating | 

    try:
        api_response = api_instance.create_asset_rating(asset_rating)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_rating** | [**AssetRating**](AssetRating.md)|  | 

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_comment**

    def create_comment(comment) -> Comment 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    comment = elements_sdk.Comment() # Comment | 

    try:
        api_response = api_instance.create_comment(comment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_custom_field**

    def create_custom_field(custom_field) -> CustomField 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    custom_field = elements_sdk.CustomField() # CustomField | 

    try:
        api_response = api_instance.create_custom_field(custom_field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field** | [**CustomField**](CustomField.md)|  | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_editor_project**

    def create_editor_project(editor_project) -> EditorProject 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    editor_project = elements_sdk.EditorProject() # EditorProject | 

    try:
        api_response = api_instance.create_editor_project(editor_project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editor_project** | [**EditorProject**](EditorProject.md)|  | 

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_external_transcoder**

    def create_external_transcoder(external_transcoder) -> ExternalTranscoder 



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    external_transcoder = elements_sdk.ExternalTranscoder() # ExternalTranscoder | 

    try:
        api_response = api_instance.create_external_transcoder(external_transcoder)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_transcoder** | [**ExternalTranscoder**](ExternalTranscoder.md)|  | 

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_marker**

    def create_marker(marker) -> Marker 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    marker = elements_sdk.Marker() # Marker | 

    try:
        api_response = api_instance.create_marker(marker)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marker** | [**Marker**](Marker.md)|  | 

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_file_template**

    def create_media_file_template(media_file_template) -> MediaFileTemplate 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    media_file_template = elements_sdk.MediaFileTemplate() # MediaFileTemplate | 

    try:
        api_response = api_instance.create_media_file_template(media_file_template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_file_template** | [**MediaFileTemplate**](MediaFileTemplate.md)|  | 

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_root**

    def create_media_root(media_root) -> MediaRoot 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    media_root = elements_sdk.MediaRoot() # MediaRoot | 

    try:
        api_response = api_instance.create_media_root(media_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_root** | [**MediaRoot**](MediaRoot.md)|  | 

### Return type

[**MediaRoot**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_root_permission**

    def create_media_root_permission(media_root_permission) -> MediaRootPermission 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    media_root_permission = elements_sdk.MediaRootPermission() # MediaRootPermission | 

    try:
        api_response = api_instance.create_media_root_permission(media_root_permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_root_permission** | [**MediaRootPermission**](MediaRootPermission.md)|  | 

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_tag**

    def create_media_tag(unfiltered_tag) -> UnfilteredTag 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    unfiltered_tag = elements_sdk.UnfilteredTag() # UnfilteredTag | 

    try:
        api_response = api_instance.create_media_tag(unfiltered_tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unfiltered_tag** | [**UnfilteredTag**](UnfilteredTag.md)|  | 

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_proxy_profile**

    def create_proxy_profile(proxy_profile) -> ProxyProfile 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    proxy_profile = elements_sdk.ProxyProfile() # ProxyProfile | 

    try:
        api_response = api_instance.create_proxy_profile(proxy_profile)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_profile** | [**ProxyProfile**](ProxyProfile.md)|  | 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_subclip**

    def create_subclip(subclip) -> Subclip 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    subclip = elements_sdk.Subclip() # Subclip | 

    try:
        api_response = api_instance.create_subclip(subclip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subclip** | [**Subclip**](Subclip.md)|  | 

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_subclip_clipboard_entry**

    def create_subclip_clipboard_entry(subclip_clipboard_entry) -> SubclipClipboardEntry 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    subclip_clipboard_entry = elements_sdk.SubclipClipboardEntry() # SubclipClipboardEntry | 

    try:
        api_response = api_instance.create_subclip_clipboard_entry(subclip_clipboard_entry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_subclip_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subclip_clipboard_entry** | [**SubclipClipboardEntry**](SubclipClipboardEntry.md)|  | 

### Return type

[**SubclipClipboardEntry**](SubclipClipboardEntry.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_asset**

    def delete_asset(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Asset.

    try:
        api_instance.delete_asset(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_asset_rating**

    def delete_asset_rating(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Rating.

    try:
        api_instance.delete_asset_rating(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Rating. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_comment**

    def delete_comment(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Comment.

    try:
        api_instance.delete_comment(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_custom_field**

    def delete_custom_field(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Custom field.

    try:
        api_instance.delete_custom_field(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_easy_sharing_token_for_bundle**

    def delete_easy_sharing_token_for_bundle(id)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Bundle.

    try:
        api_instance.delete_easy_sharing_token_for_bundle(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_easy_sharing_token_for_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_easy_sharing_token_for_directory**

    def delete_easy_sharing_token_for_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.delete_easy_sharing_token_for_directory(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_easy_sharing_token_for_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_external_transcoder**

    def delete_external_transcoder(id)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this external transcoder.

    try:
        api_instance.delete_external_transcoder(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_marker**

    def delete_marker(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this marker.

    try:
        api_instance.delete_marker(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this marker. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_file_template**

    def delete_media_file_template(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Template.

    try:
        api_instance.delete_media_file_template(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_library_objects**

    def delete_media_library_objects(media_library_delete_request) -> list[TaskInfo] 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    media_library_delete_request = elements_sdk.MediaLibraryDeleteRequest() # MediaLibraryDeleteRequest | 

    try:
        api_response = api_instance.delete_media_library_objects(media_library_delete_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_library_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_library_delete_request** | [**MediaLibraryDeleteRequest**](MediaLibraryDeleteRequest.md)|  | 

### Return type

[**list[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_root**

    def delete_media_root(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this media root.

    try:
        api_instance.delete_media_root(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_root_permission**

    def delete_media_root_permission(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Media Root Permission.

    try:
        api_instance.delete_media_root_permission(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_tag**

    def delete_media_tag(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Tag.

    try:
        api_instance.delete_media_tag(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_update**

    def delete_media_update(id)



### Required permissions    * User account permission: `media:access` (read) / `media:updates:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Update.

    try:
        api_instance.delete_media_update(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Update. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_proxy**

    def delete_proxy(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy.

    try:
        api_instance.delete_proxy(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_proxy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_proxy_profile**

    def delete_proxy_profile(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy profile.

    try:
        api_instance.delete_proxy_profile(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_subclip**

    def delete_subclip(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this subclip.

    try:
        api_instance.delete_subclip(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_subclip_clipboard_entry**

    def delete_subclip_clipboard_entry(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this subclip clipboard entry.

    try:
        api_instance.delete_subclip_clipboard_entry(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_subclip_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip clipboard entry. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **discover_media**

    def discover_media(scanner_discover_endpoint_request) -> MediaFile 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    scanner_discover_endpoint_request = elements_sdk.ScannerDiscoverEndpointRequest() # ScannerDiscoverEndpointRequest | 

    try:
        api_response = api_instance.discover_media(scanner_discover_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->discover_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_discover_endpoint_request** | [**ScannerDiscoverEndpointRequest**](ScannerDiscoverEndpointRequest.md)|  | 

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **download_asset_proxy_file**

    def download_asset_proxy_file(filename, id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    filename = 'filename_example' # str | 
id = 56 # int | A unique integer value identifying this Asset.

    try:
        api_instance.download_asset_proxy_file(filename, id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->download_asset_proxy_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 
 **id** | **int**| A unique integer value identifying this Asset. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **download_media_file**

    def download_media_file(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.download_media_file(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->download_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **download_proxy**

    def download_proxy(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy.

    try:
        api_instance.download_proxy(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->download_proxy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **editor_export_xml_for_assset**

    def editor_export_xml_for_assset(asset_ids, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset_ids = 'asset_ids_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_instance.editor_export_xml_for_assset(asset_ids, ordering=ordering, limit=limit, offset=offset)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_assset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **editor_export_xml_for_bundle**

    def editor_export_xml_for_bundle(bundle_ids, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    bundle_ids = 'bundle_ids_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_instance.editor_export_xml_for_bundle(bundle_ids, ordering=ordering, limit=limit, offset=offset)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_ids** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **editor_export_xml_for_project**

    def editor_export_xml_for_project(id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.editor_export_xml_for_project(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **export_comments_for_avid**

    def export_comments_for_avid(asset_id, export_format, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset_id = 'asset_id_example' # str | 
export_format = 'export_format_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_instance.export_comments_for_avid(asset_id, export_format, ordering=ordering, limit=limit, offset=offset)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->export_comments_for_avid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **export_format** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **export_editor_timeline**

    def export_editor_timeline(timeline_export_request)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    timeline_export_request = elements_sdk.TimelineExportRequest() # TimelineExportRequest | 

    try:
        api_instance.export_editor_timeline(timeline_export_request)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->export_editor_timeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeline_export_request** | [**TimelineExportRequest**](TimelineExportRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **forget_deleted_media_files**

    def forget_deleted_media_files(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.forget_deleted_media_files(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->forget_deleted_media_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **generate_proxies**

    def generate_proxies(generate_proxies_request) -> list[TaskInfo] 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    generate_proxies_request = elements_sdk.GenerateProxiesRequest() # GenerateProxiesRequest | 

    try:
        api_response = api_instance.generate_proxies(generate_proxies_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->generate_proxies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_proxies_request** | [**GenerateProxiesRequest**](GenerateProxiesRequest.md)|  | 

### Return type

[**list[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_asset_project_links**

    def get_all_asset_project_links(asset=asset, project=project, ordering=ordering, limit=limit, offset=offset) -> list[AssetProjectLink] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
project = 'project_example' # str | Filter the returned list by `project`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_asset_project_links(asset=asset, project=project, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_project_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **project** | **str**| Filter the returned list by &#x60;project&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[AssetProjectLink]**](AssetProjectLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_asset_ratings**

    def get_all_asset_ratings(user=user, asset=asset, ordering=ordering, limit=limit, offset=offset) -> list[AssetRating] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    user = 'user_example' # str | Filter the returned list by `user`. (optional)
asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_asset_ratings(user=user, asset=asset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_ratings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Filter the returned list by &#x60;user&#x60;. | [optional] 
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[AssetRating]**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_asset_tape_backups**

    def get_all_asset_tape_backups(asset=asset, ordering=ordering, limit=limit, offset=offset, include_asset=include_asset, advanced_search=advanced_search) -> list[AssetBackup] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
include_asset = True # bool |  (optional)
advanced_search = 'advanced_search_example' # str |  (optional)

    try:
        api_response = api_instance.get_all_asset_tape_backups(asset=asset, ordering=ordering, limit=limit, offset=offset, include_asset=include_asset, advanced_search=advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_tape_backups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **include_asset** | **bool**|  | [optional] 
 **advanced_search** | **str**|  | [optional] 

### Return type

[**list[AssetBackup]**](AssetBackup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_assets**

    def get_all_assets(sync_id=sync_id, display_name=display_name, set=set, ordering=ordering, limit=limit, offset=offset, include_proxies=include_proxies, include_modified_by=include_modified_by, resolve_asset_permission=resolve_asset_permission, for_root=for_root) -> list[Asset] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    sync_id = 'sync_id_example' # str | Filter the returned list by `sync_id`. (optional)
display_name = 'display_name_example' # str | Filter the returned list by `display_name`. (optional)
set = 'set_example' # str | Filter the returned list by `set`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
include_proxies = True # bool |  (optional)
include_modified_by = True # bool |  (optional)
resolve_asset_permission = True # bool |  (optional)
for_root = 56 # int |  (optional)

    try:
        api_response = api_instance.get_all_assets(sync_id=sync_id, display_name=display_name, set=set, ordering=ordering, limit=limit, offset=offset, include_proxies=include_proxies, include_modified_by=include_modified_by, resolve_asset_permission=resolve_asset_permission, for_root=for_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_id** | **str**| Filter the returned list by &#x60;sync_id&#x60;. | [optional] 
 **display_name** | **str**| Filter the returned list by &#x60;display_name&#x60;. | [optional] 
 **set** | **str**| Filter the returned list by &#x60;set&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **include_proxies** | **bool**|  | [optional] 
 **include_modified_by** | **bool**|  | [optional] 
 **resolve_asset_permission** | **bool**|  | [optional] 
 **for_root** | **int**|  | [optional] 

### Return type

[**list[Asset]**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_bundles_for_media_root**

    def get_all_bundles_for_media_root(root, asset=asset, location=location, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, name=name, ordering=ordering, limit=limit, offset=offset) -> list[MediaFileBundle] 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    root = 'root_example' # str | 
asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
location = 'location_example' # str | Filter the returned list by `location`. (optional)
shared_via_tokens = 'shared_via_tokens_example' # str | Filter the returned list by `shared_via_tokens`. (optional)
shared_via_tokens__token = 'shared_via_tokens__token_example' # str | Filter the returned list by `shared_via_tokens__token`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_bundles_for_media_root(root, asset=asset, location=location, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_bundles_for_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**|  | 
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **location** | **str**| Filter the returned list by &#x60;location&#x60;. | [optional] 
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional] 
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_click_links**

    def get_all_click_links(asset=asset, connection=connection, ordering=ordering, limit=limit, offset=offset) -> list[AssetCloudLink] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
connection = 'connection_example' # str | Filter the returned list by `connection`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_click_links(asset=asset, connection=connection, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_click_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **connection** | **str**| Filter the returned list by &#x60;connection&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[AssetCloudLink]**](AssetCloudLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_comments**

    def get_all_comments(asset=asset, root=root, user=user, ordering=ordering, limit=limit, offset=offset, for_root=for_root, tasks_for_user=tasks_for_user, include_full_asset=include_full_asset, advanced_search=advanced_search) -> list[Comment] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
root = 'root_example' # str | Filter the returned list by `root`. (optional)
user = 'user_example' # str | Filter the returned list by `user`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
for_root = 56 # int |  (optional)
tasks_for_user = 56 # int |  (optional)
include_full_asset = True # bool |  (optional)
advanced_search = 'advanced_search_example' # str |  (optional)

    try:
        api_response = api_instance.get_all_comments(asset=asset, root=root, user=user, ordering=ordering, limit=limit, offset=offset, for_root=for_root, tasks_for_user=tasks_for_user, include_full_asset=include_full_asset, advanced_search=advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **user** | **str**| Filter the returned list by &#x60;user&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **for_root** | **int**|  | [optional] 
 **tasks_for_user** | **int**|  | [optional] 
 **include_full_asset** | **bool**|  | [optional] 
 **advanced_search** | **str**|  | [optional] 

### Return type

[**list[Comment]**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_custom_fields**

    def get_all_custom_fields(ordering=ordering, limit=limit, offset=offset) -> list[CustomField] 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_custom_fields(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_custom_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[CustomField]**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_external_transcoders**

    def get_all_external_transcoders(name=name, id=id, ordering=ordering, limit=limit, offset=offset) -> list[ExternalTranscoder] 



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    name = 'name_example' # str | Filter the returned list by `name`. (optional)
id = 3.4 # float | Filter the returned list by `id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_external_transcoders(name=name, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_external_transcoders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[ExternalTranscoder]**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_markers**

    def get_all_markers(asset=asset, user=user, ordering=ordering, limit=limit, offset=offset) -> list[Marker] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
user = 'user_example' # str | Filter the returned list by `user`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_markers(asset=asset, user=user, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_markers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **user** | **str**| Filter the returned list by &#x60;user&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Marker]**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_file_bundles**

    def get_all_media_file_bundles(asset=asset, location=location, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, name=name, ordering=ordering, limit=limit, offset=offset, exclude_deleted=exclude_deleted, exclude_unrecognized=exclude_unrecognized, include_proxies=include_proxies, include_parents=include_parents, advanced_search=advanced_search) -> list[MediaFileBundle] 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
location = 'location_example' # str | Filter the returned list by `location`. (optional)
shared_via_tokens = 'shared_via_tokens_example' # str | Filter the returned list by `shared_via_tokens`. (optional)
shared_via_tokens__token = 'shared_via_tokens__token_example' # str | Filter the returned list by `shared_via_tokens__token`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
exclude_deleted = True # bool |  (optional)
exclude_unrecognized = True # bool |  (optional)
include_proxies = True # bool |  (optional)
include_parents = True # bool |  (optional)
advanced_search = 'advanced_search_example' # str |  (optional)

    try:
        api_response = api_instance.get_all_media_file_bundles(asset=asset, location=location, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, name=name, ordering=ordering, limit=limit, offset=offset, exclude_deleted=exclude_deleted, exclude_unrecognized=exclude_unrecognized, include_proxies=include_proxies, include_parents=include_parents, advanced_search=advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_file_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **location** | **str**| Filter the returned list by &#x60;location&#x60;. | [optional] 
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional] 
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **exclude_deleted** | **bool**|  | [optional] 
 **exclude_unrecognized** | **bool**|  | [optional] 
 **include_proxies** | **bool**|  | [optional] 
 **include_parents** | **bool**|  | [optional] 
 **advanced_search** | **str**|  | [optional] 

### Return type

[**list[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_file_templates**

    def get_all_media_file_templates(ordering=ordering, limit=limit, offset=offset) -> list[MediaFileTemplate] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_file_templates(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_file_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFileTemplate]**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_files**

    def get_all_media_files(bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset, resolve_file_permission=resolve_file_permission, include_modified_by=include_modified_by, include_effective_custom_fields=include_effective_custom_fields, include_root=include_root, include_parents=include_parents, advanced_search=advanced_search) -> list[MediaFile] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    bundle = 'bundle_example' # str | Filter the returned list by `bundle`. (optional)
bundle__in = 'bundle__in_example' # str | Multiple values may be separated by commas. (optional)
parent = 'parent_example' # str | Filter the returned list by `parent`. (optional)
path = 'path_example' # str | Filter the returned list by `path`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_dir = 'is_dir_example' # str | Filter the returned list by `is_dir`. (optional)
is_showroom = 'is_showroom_example' # str | Filter the returned list by `is_showroom`. (optional)
present = 'present_example' # str | Filter the returned list by `present`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
shared_via_tokens = 'shared_via_tokens_example' # str | Filter the returned list by `shared_via_tokens`. (optional)
shared_via_tokens__token = 'shared_via_tokens__token_example' # str | Filter the returned list by `shared_via_tokens__token`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
resolve_file_permission = True # bool |  (optional)
include_modified_by = True # bool |  (optional)
include_effective_custom_fields = True # bool |  (optional)
include_root = True # bool |  (optional)
include_parents = True # bool |  (optional)
advanced_search = 'advanced_search_example' # str |  (optional)

    try:
        api_response = api_instance.get_all_media_files(bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset, resolve_file_permission=resolve_file_permission, include_modified_by=include_modified_by, include_effective_custom_fields=include_effective_custom_fields, include_root=include_root, include_parents=include_parents, advanced_search=advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**| Filter the returned list by &#x60;bundle&#x60;. | [optional] 
 **bundle__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **parent** | **str**| Filter the returned list by &#x60;parent&#x60;. | [optional] 
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional] 
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional] 
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional] 
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **resolve_file_permission** | **bool**|  | [optional] 
 **include_modified_by** | **bool**|  | [optional] 
 **include_effective_custom_fields** | **bool**|  | [optional] 
 **include_root** | **bool**|  | [optional] 
 **include_parents** | **bool**|  | [optional] 
 **advanced_search** | **str**|  | [optional] 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_files_for_bundles**

    def get_all_media_files_for_bundles(all_media_files_for_bundles_request) -> list[MediaFile] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    all_media_files_for_bundles_request = elements_sdk.AllMediaFilesForBundlesRequest() # AllMediaFilesForBundlesRequest | 

    try:
        api_response = api_instance.get_all_media_files_for_bundles(all_media_files_for_bundles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_for_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_media_files_for_bundles_request** | [**AllMediaFilesForBundlesRequest**](AllMediaFilesForBundlesRequest.md)|  | 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_files_for_media_root**

    def get_all_media_files_for_media_root(root, bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset) -> list[MediaFile] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    root = 'root_example' # str | 
bundle = 'bundle_example' # str | Filter the returned list by `bundle`. (optional)
bundle__in = 'bundle__in_example' # str | Multiple values may be separated by commas. (optional)
parent = 'parent_example' # str | Filter the returned list by `parent`. (optional)
path = 'path_example' # str | Filter the returned list by `path`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_dir = 'is_dir_example' # str | Filter the returned list by `is_dir`. (optional)
is_showroom = 'is_showroom_example' # str | Filter the returned list by `is_showroom`. (optional)
present = 'present_example' # str | Filter the returned list by `present`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
shared_via_tokens = 'shared_via_tokens_example' # str | Filter the returned list by `shared_via_tokens`. (optional)
shared_via_tokens__token = 'shared_via_tokens__token_example' # str | Filter the returned list by `shared_via_tokens__token`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_files_for_media_root(root, bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_for_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**|  | 
 **bundle** | **str**| Filter the returned list by &#x60;bundle&#x60;. | [optional] 
 **bundle__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **parent** | **str**| Filter the returned list by &#x60;parent&#x60;. | [optional] 
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional] 
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional] 
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional] 
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_root_permissions**

    def get_all_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset) -> list[MediaRootPermission] 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    root = 'root_example' # str | Filter the returned list by `root`. (optional)
id = 3.4 # float | Filter the returned list by `id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_root_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaRootPermission]**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_roots**

    def get_all_media_roots(path=path, volume=volume, name=name, ordering=ordering, limit=limit, offset=offset) -> list[MediaRoot] 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    path = 'path_example' # str | Filter the returned list by `path`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_roots(path=path, volume=volume, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_roots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaRoot]**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_tags**

    def get_all_media_tags(name=name, name__icontains=name__icontains, roots=roots, roots__isnull=roots__isnull, shared=shared, ordering=ordering, limit=limit, offset=offset, for_root=for_root) -> list[UnfilteredTag] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    name = 'name_example' # str | Filter the returned list by `name`. (optional)
name__icontains = 'name__icontains_example' # str | Filter the returned list by `name__icontains`. (optional)
roots = 'roots_example' # str | Filter the returned list by `roots`. (optional)
roots__isnull = 'roots__isnull_example' # str | Filter the returned list by `roots__isnull`. (optional)
shared = 'shared_example' # str | Filter the returned list by `shared`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
for_root = 56 # int |  (optional)

    try:
        api_response = api_instance.get_all_media_tags(name=name, name__icontains=name__icontains, roots=roots, roots__isnull=roots__isnull, shared=shared, ordering=ordering, limit=limit, offset=offset, for_root=for_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **name__icontains** | **str**| Filter the returned list by &#x60;name__icontains&#x60;. | [optional] 
 **roots** | **str**| Filter the returned list by &#x60;roots&#x60;. | [optional] 
 **roots__isnull** | **str**| Filter the returned list by &#x60;roots__isnull&#x60;. | [optional] 
 **shared** | **str**| Filter the returned list by &#x60;shared&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **for_root** | **int**|  | [optional] 

### Return type

[**list[UnfilteredTag]**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_updates**

    def get_all_media_updates(asset=asset, user=user, root=root, ordering=ordering, limit=limit, offset=offset) -> list[MediaUpdate] 



### Required permissions    * User account permission: `media:access` (read) / `media:updates:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
user = 'user_example' # str | Filter the returned list by `user`. (optional)
root = 'root_example' # str | Filter the returned list by `root`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_updates(asset=asset, user=user, root=root, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_updates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **user** | **str**| Filter the returned list by &#x60;user&#x60;. | [optional] 
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaUpdate]**](MediaUpdate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_proxy_generators**

    def get_all_proxy_generators(ordering=ordering, limit=limit, offset=offset) -> list[ProxyGenerator] 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_proxy_generators(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_proxy_generators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[ProxyGenerator]**](ProxyGenerator.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_proxy_profiles**

    def get_all_proxy_profiles(name=name, ordering=ordering, limit=limit, offset=offset, for_root=for_root) -> list[ProxyProfile] 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
for_root = 56 # int |  (optional)

    try:
        api_response = api_instance.get_all_proxy_profiles(name=name, ordering=ordering, limit=limit, offset=offset, for_root=for_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_proxy_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **for_root** | **int**|  | [optional] 

### Return type

[**list[ProxyProfile]**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_subclip_clipboard_entries**

    def get_all_subclip_clipboard_entries(cut=cut, ordering=ordering, limit=limit, offset=offset) -> list[SubclipClipboardEntry] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    cut = 'cut_example' # str | Filter the returned list by `cut`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_subclip_clipboard_entries(cut=cut, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_subclip_clipboard_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cut** | **str**| Filter the returned list by &#x60;cut&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[SubclipClipboardEntry]**](SubclipClipboardEntry.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_subclips**

    def get_all_subclips(asset=asset, asset__in=asset__in, root=root, name=name, ordering=ordering, limit=limit, offset=offset) -> list[Subclip] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
asset__in = 'asset__in_example' # str | Multiple values may be separated by commas. (optional)
root = 'root_example' # str | Filter the returned list by `root`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_subclips(asset=asset, asset__in=asset__in, root=root, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_subclips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **asset__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Subclip]**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_transcoder_profiles**

    def get_all_transcoder_profiles(ordering=ordering, limit=limit, offset=offset) -> list[TranscoderProfile] 



### Required permissions    * User account permission: `tasks:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_transcoder_profiles(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_transcoder_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[TranscoderProfile]**](TranscoderProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_asset**

    def get_asset(id, include_proxies=include_proxies, include_modified_by=include_modified_by, resolve_asset_permission=resolve_asset_permission, for_root=for_root) -> Asset 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Asset.
include_proxies = True # bool |  (optional)
include_modified_by = True # bool |  (optional)
resolve_asset_permission = True # bool |  (optional)
for_root = 56 # int |  (optional)

    try:
        api_response = api_instance.get_asset(id, include_proxies=include_proxies, include_modified_by=include_modified_by, resolve_asset_permission=resolve_asset_permission, for_root=for_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 
 **include_proxies** | **bool**|  | [optional] 
 **include_modified_by** | **bool**|  | [optional] 
 **resolve_asset_permission** | **bool**|  | [optional] 
 **for_root** | **int**|  | [optional] 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_asset_rating**

    def get_asset_rating(id) -> AssetRating 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Rating.

    try:
        api_response = api_instance.get_asset_rating(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Rating. | 

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_bookmarked_media_files_directories**

    def get_bookmarked_media_files_directories(bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset) -> list[MediaFile] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    bundle = 'bundle_example' # str | Filter the returned list by `bundle`. (optional)
bundle__in = 'bundle__in_example' # str | Multiple values may be separated by commas. (optional)
parent = 'parent_example' # str | Filter the returned list by `parent`. (optional)
path = 'path_example' # str | Filter the returned list by `path`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_dir = 'is_dir_example' # str | Filter the returned list by `is_dir`. (optional)
is_showroom = 'is_showroom_example' # str | Filter the returned list by `is_showroom`. (optional)
present = 'present_example' # str | Filter the returned list by `present`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
shared_via_tokens = 'shared_via_tokens_example' # str | Filter the returned list by `shared_via_tokens`. (optional)
shared_via_tokens__token = 'shared_via_tokens__token_example' # str | Filter the returned list by `shared_via_tokens__token`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_bookmarked_media_files_directories(bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_bookmarked_media_files_directories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**| Filter the returned list by &#x60;bundle&#x60;. | [optional] 
 **bundle__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **parent** | **str**| Filter the returned list by &#x60;parent&#x60;. | [optional] 
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional] 
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional] 
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional] 
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_comment**

    def get_comment(id, for_root=for_root, tasks_for_user=tasks_for_user, include_full_asset=include_full_asset, advanced_search=advanced_search) -> Comment 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Comment.
for_root = 56 # int |  (optional)
tasks_for_user = 56 # int |  (optional)
include_full_asset = True # bool |  (optional)
advanced_search = 'advanced_search_example' # str |  (optional)

    try:
        api_response = api_instance.get_comment(id, for_root=for_root, tasks_for_user=tasks_for_user, include_full_asset=include_full_asset, advanced_search=advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 
 **for_root** | **int**|  | [optional] 
 **tasks_for_user** | **int**|  | [optional] 
 **include_full_asset** | **bool**|  | [optional] 
 **advanced_search** | **str**|  | [optional] 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_custom_field**

    def get_custom_field(id) -> CustomField 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Custom field.

    try:
        api_response = api_instance.get_custom_field(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_easy_sharing_token_for_bundle**

    def get_easy_sharing_token_for_bundle(id) -> OneTimeAccessToken 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Bundle.

    try:
        api_response = api_instance.get_easy_sharing_token_for_bundle(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_easy_sharing_token_for_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. | 

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_easy_sharing_token_for_directory**

    def get_easy_sharing_token_for_directory(id) -> OneTimeAccessToken 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_response = api_instance.get_easy_sharing_token_for_directory(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_easy_sharing_token_for_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_editor_project**

    def get_editor_project(id) -> EditorProject 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_response = api_instance.get_editor_project(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_external_transcoder**

    def get_external_transcoder(id) -> ExternalTranscoder 



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this external transcoder.

    try:
        api_response = api_instance.get_external_transcoder(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. | 

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_frame**

    def get_frame(frame, id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    frame = 'frame_example' # str | 
id = 56 # int | A unique integer value identifying this Asset.

    try:
        api_instance.get_frame(frame, id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_frame: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **frame** | **str**|  | 
 **id** | **int**| A unique integer value identifying this Asset. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_latest_media_update**

    def get_latest_media_update(asset=asset, user=user, root=root, ordering=ordering, limit=limit, offset=offset) -> MediaUpdate 



### Required permissions    * User account permission: `media:access` (read) / `media:updates:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
user = 'user_example' # str | Filter the returned list by `user`. (optional)
root = 'root_example' # str | Filter the returned list by `root`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_latest_media_update(asset=asset, user=user, root=root, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_latest_media_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **user** | **str**| Filter the returned list by &#x60;user&#x60;. | [optional] 
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**MediaUpdate**](MediaUpdate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_marker**

    def get_marker(id) -> Marker 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this marker.

    try:
        api_response = api_instance.get_marker(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this marker. | 

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_file**

    def get_media_file(id, resolve_file_permission=resolve_file_permission, include_modified_by=include_modified_by, include_effective_custom_fields=include_effective_custom_fields, include_root=include_root, include_parents=include_parents, advanced_search=advanced_search) -> MediaFile 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.
resolve_file_permission = True # bool |  (optional)
include_modified_by = True # bool |  (optional)
include_effective_custom_fields = True # bool |  (optional)
include_root = True # bool |  (optional)
include_parents = True # bool |  (optional)
advanced_search = 'advanced_search_example' # str |  (optional)

    try:
        api_response = api_instance.get_media_file(id, resolve_file_permission=resolve_file_permission, include_modified_by=include_modified_by, include_effective_custom_fields=include_effective_custom_fields, include_root=include_root, include_parents=include_parents, advanced_search=advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **resolve_file_permission** | **bool**|  | [optional] 
 **include_modified_by** | **bool**|  | [optional] 
 **include_effective_custom_fields** | **bool**|  | [optional] 
 **include_root** | **bool**|  | [optional] 
 **include_parents** | **bool**|  | [optional] 
 **advanced_search** | **str**|  | [optional] 

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_file_bundle**

    def get_media_file_bundle(id, exclude_deleted=exclude_deleted, exclude_unrecognized=exclude_unrecognized, include_proxies=include_proxies, include_parents=include_parents, offset=offset, limit=limit, advanced_search=advanced_search) -> MediaFileBundle 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Bundle.
exclude_deleted = True # bool |  (optional)
exclude_unrecognized = True # bool |  (optional)
include_proxies = True # bool |  (optional)
include_parents = True # bool |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
advanced_search = 'advanced_search_example' # str |  (optional)

    try:
        api_response = api_instance.get_media_file_bundle(id, exclude_deleted=exclude_deleted, exclude_unrecognized=exclude_unrecognized, include_proxies=include_proxies, include_parents=include_parents, offset=offset, limit=limit, advanced_search=advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. | 
 **exclude_deleted** | **bool**|  | [optional] 
 **exclude_unrecognized** | **bool**|  | [optional] 
 **include_proxies** | **bool**|  | [optional] 
 **include_parents** | **bool**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **advanced_search** | **str**|  | [optional] 

### Return type

[**MediaFileBundle**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_file_contents**

    def get_media_file_contents(id, exclude_deleted=exclude_deleted, exclude_unrecognized=exclude_unrecognized, offset=offset, limit=limit) -> MediaFileContents 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.
exclude_deleted = True # bool |  (optional)
exclude_unrecognized = True # bool |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_media_file_contents(id, exclude_deleted=exclude_deleted, exclude_unrecognized=exclude_unrecognized, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **exclude_deleted** | **bool**|  | [optional] 
 **exclude_unrecognized** | **bool**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**MediaFileContents**](MediaFileContents.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_file_template**

    def get_media_file_template(id) -> MediaFileTemplate 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Template.

    try:
        api_response = api_instance.get_media_file_template(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_root**

    def get_media_root(id) -> MediaRoot 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this media root.

    try:
        api_response = api_instance.get_media_root(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. | 

### Return type

[**MediaRoot**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_root_permission**

    def get_media_root_permission(id) -> MediaRootPermission 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Media Root Permission.

    try:
        api_response = api_instance.get_media_root_permission(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. | 

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_tag**

    def get_media_tag(id, for_root=for_root) -> UnfilteredTag 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Tag.
for_root = 56 # int |  (optional)

    try:
        api_response = api_instance.get_media_tag(id, for_root=for_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 
 **for_root** | **int**|  | [optional] 

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_multiple_assets**

    def get_multiple_assets(multiple_assets_request) -> list[Asset] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    multiple_assets_request = elements_sdk.MultipleAssetsRequest() # MultipleAssetsRequest | 

    try:
        api_response = api_instance.get_multiple_assets(multiple_assets_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_assets_request** | [**MultipleAssetsRequest**](MultipleAssetsRequest.md)|  | 

### Return type

[**list[Asset]**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_multiple_bundles**

    def get_multiple_bundles(get_multiple_bundles_request) -> list[MediaFileBundle] 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    get_multiple_bundles_request = elements_sdk.GetMultipleBundlesRequest() # GetMultipleBundlesRequest | 

    try:
        api_response = api_instance.get_multiple_bundles(get_multiple_bundles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_multiple_bundles_request** | [**GetMultipleBundlesRequest**](GetMultipleBundlesRequest.md)|  | 

### Return type

[**list[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_multiple_files**

    def get_multiple_files(get_multiple_files_request) -> list[MediaFile] 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    get_multiple_files_request = elements_sdk.GetMultipleFilesRequest() # GetMultipleFilesRequest | 

    try:
        api_response = api_instance.get_multiple_files(get_multiple_files_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_multiple_files_request** | [**GetMultipleFilesRequest**](GetMultipleFilesRequest.md)|  | 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_my_media_root_permissions**

    def get_my_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset) -> list[MediaRootPermission] 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    root = 'root_example' # str | Filter the returned list by `root`. (optional)
id = 3.4 # float | Filter the returned list by `id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_my_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_my_media_root_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaRootPermission]**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_my_resolved_media_root_permissions**

    def get_my_resolved_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset) -> list[MediaRootPermission] 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    root = 'root_example' # str | Filter the returned list by `root`. (optional)
id = 3.4 # float | Filter the returned list by `id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_my_resolved_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_my_resolved_media_root_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaRootPermission]**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_proxy**

    def get_proxy(id) -> Proxy 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy.

    try:
        api_response = api_instance.get_proxy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy. | 

### Return type

[**Proxy**](Proxy.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_proxy_generator**

    def get_proxy_generator(id) -> ProxyGenerator 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_proxy_generator(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_generator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProxyGenerator**](ProxyGenerator.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_proxy_profile**

    def get_proxy_profile(id, for_root=for_root) -> ProxyProfile 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy profile.
for_root = 56 # int |  (optional)

    try:
        api_response = api_instance.get_proxy_profile(id, for_root=for_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 
 **for_root** | **int**|  | [optional] 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_proxy_profile_proxy_count**

    def get_proxy_profile_proxy_count(id) -> ProxyCount 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy profile.

    try:
        api_response = api_instance.get_proxy_profile_proxy_count(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_profile_proxy_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 

### Return type

[**ProxyCount**](ProxyCount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_subclip**

    def get_subclip(id) -> Subclip 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this subclip.

    try:
        api_response = api_instance.get_subclip(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_transcoder_profile**

    def get_transcoder_profile(id) -> TranscoderProfile 



### Required permissions    * User account permission: `tasks:view` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this transcoder profile.

    try:
        api_response = api_instance.get_transcoder_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_transcoder_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this transcoder profile. | 

### Return type

[**TranscoderProfile**](TranscoderProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_vantage_workflows**

    def get_vantage_workflows(id) -> VantageWorkflows 



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this external transcoder.

    try:
        api_response = api_instance.get_vantage_workflows(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_vantage_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. | 

### Return type

[**VantageWorkflows**](VantageWorkflows.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **instantiate_media_file_template**

    def instantiate_media_file_template(id, instantiate_file_template_request)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Template.
instantiate_file_template_request = elements_sdk.InstantiateFileTemplateRequest() # InstantiateFileTemplateRequest | 

    try:
        api_instance.instantiate_media_file_template(id, instantiate_file_template_request)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->instantiate_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 
 **instantiate_file_template_request** | [**InstantiateFileTemplateRequest**](InstantiateFileTemplateRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **locate_editor_project_paths**

    def locate_editor_project_paths(id) -> list[LocateResult] 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_response = api_instance.locate_editor_project_paths(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->locate_editor_project_paths: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

[**list[LocateResult]**](LocateResult.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **mark_media_directory_as_showroom**

    def mark_media_directory_as_showroom(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.mark_media_directory_as_showroom(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->mark_media_directory_as_showroom: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_asset**

    def patch_asset(id, asset_partial_update) -> Asset 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Asset.
asset_partial_update = elements_sdk.AssetPartialUpdate() # AssetPartialUpdate | 

    try:
        api_response = api_instance.patch_asset(id, asset_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 
 **asset_partial_update** | [**AssetPartialUpdate**](AssetPartialUpdate.md)|  | 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_asset_rating**

    def patch_asset_rating(id, asset_rating_partial_update) -> AssetRating 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Rating.
asset_rating_partial_update = elements_sdk.AssetRatingPartialUpdate() # AssetRatingPartialUpdate | 

    try:
        api_response = api_instance.patch_asset_rating(id, asset_rating_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Rating. | 
 **asset_rating_partial_update** | [**AssetRatingPartialUpdate**](AssetRatingPartialUpdate.md)|  | 

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_comment**

    def patch_comment(id, comment_partial_update) -> Comment 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Comment.
comment_partial_update = elements_sdk.CommentPartialUpdate() # CommentPartialUpdate | 

    try:
        api_response = api_instance.patch_comment(id, comment_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 
 **comment_partial_update** | [**CommentPartialUpdate**](CommentPartialUpdate.md)|  | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_custom_field**

    def patch_custom_field(id, custom_field_partial_update) -> CustomField 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Custom field.
custom_field_partial_update = elements_sdk.CustomFieldPartialUpdate() # CustomFieldPartialUpdate | 

    try:
        api_response = api_instance.patch_custom_field(id, custom_field_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. | 
 **custom_field_partial_update** | [**CustomFieldPartialUpdate**](CustomFieldPartialUpdate.md)|  | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_editor_project**

    def patch_editor_project(id, editor_project_partial_update) -> EditorProject 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.
editor_project_partial_update = elements_sdk.EditorProjectPartialUpdate() # EditorProjectPartialUpdate | 

    try:
        api_response = api_instance.patch_editor_project(id, editor_project_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **editor_project_partial_update** | [**EditorProjectPartialUpdate**](EditorProjectPartialUpdate.md)|  | 

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_external_transcoder**

    def patch_external_transcoder(id, external_transcoder_partial_update) -> ExternalTranscoder 



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this external transcoder.
external_transcoder_partial_update = elements_sdk.ExternalTranscoderPartialUpdate() # ExternalTranscoderPartialUpdate | 

    try:
        api_response = api_instance.patch_external_transcoder(id, external_transcoder_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. | 
 **external_transcoder_partial_update** | [**ExternalTranscoderPartialUpdate**](ExternalTranscoderPartialUpdate.md)|  | 

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_marker**

    def patch_marker(id, marker_partial_update) -> Marker 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this marker.
marker_partial_update = elements_sdk.MarkerPartialUpdate() # MarkerPartialUpdate | 

    try:
        api_response = api_instance.patch_marker(id, marker_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this marker. | 
 **marker_partial_update** | [**MarkerPartialUpdate**](MarkerPartialUpdate.md)|  | 

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_file**

    def patch_media_file(id, media_file_partial_update) -> MediaFile 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.
media_file_partial_update = elements_sdk.MediaFilePartialUpdate() # MediaFilePartialUpdate | 

    try:
        api_response = api_instance.patch_media_file(id, media_file_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **media_file_partial_update** | [**MediaFilePartialUpdate**](MediaFilePartialUpdate.md)|  | 

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_file_template**

    def patch_media_file_template(id, media_file_template_partial_update) -> MediaFileTemplate 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Template.
media_file_template_partial_update = elements_sdk.MediaFileTemplatePartialUpdate() # MediaFileTemplatePartialUpdate | 

    try:
        api_response = api_instance.patch_media_file_template(id, media_file_template_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 
 **media_file_template_partial_update** | [**MediaFileTemplatePartialUpdate**](MediaFileTemplatePartialUpdate.md)|  | 

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_root**

    def patch_media_root(id, media_root_partial_update) -> MediaRoot 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this media root.
media_root_partial_update = elements_sdk.MediaRootPartialUpdate() # MediaRootPartialUpdate | 

    try:
        api_response = api_instance.patch_media_root(id, media_root_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. | 
 **media_root_partial_update** | [**MediaRootPartialUpdate**](MediaRootPartialUpdate.md)|  | 

### Return type

[**MediaRoot**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_root_permission**

    def patch_media_root_permission(id, media_root_permission_partial_update) -> MediaRootPermission 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Media Root Permission.
media_root_permission_partial_update = elements_sdk.MediaRootPermissionPartialUpdate() # MediaRootPermissionPartialUpdate | 

    try:
        api_response = api_instance.patch_media_root_permission(id, media_root_permission_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. | 
 **media_root_permission_partial_update** | [**MediaRootPermissionPartialUpdate**](MediaRootPermissionPartialUpdate.md)|  | 

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_tag**

    def patch_media_tag(id, unfiltered_tag_partial_update) -> UnfilteredTag 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Tag.
unfiltered_tag_partial_update = elements_sdk.UnfilteredTagPartialUpdate() # UnfilteredTagPartialUpdate | 

    try:
        api_response = api_instance.patch_media_tag(id, unfiltered_tag_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 
 **unfiltered_tag_partial_update** | [**UnfilteredTagPartialUpdate**](UnfilteredTagPartialUpdate.md)|  | 

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_proxy_profile**

    def patch_proxy_profile(id, proxy_profile_partial_update) -> ProxyProfile 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy profile.
proxy_profile_partial_update = elements_sdk.ProxyProfilePartialUpdate() # ProxyProfilePartialUpdate | 

    try:
        api_response = api_instance.patch_proxy_profile(id, proxy_profile_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 
 **proxy_profile_partial_update** | [**ProxyProfilePartialUpdate**](ProxyProfilePartialUpdate.md)|  | 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_subclip**

    def patch_subclip(id, subclip_partial_update) -> Subclip 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this subclip.
subclip_partial_update = elements_sdk.SubclipPartialUpdate() # SubclipPartialUpdate | 

    try:
        api_response = api_instance.patch_subclip(id, subclip_partial_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 
 **subclip_partial_update** | [**SubclipPartialUpdate**](SubclipPartialUpdate.md)|  | 

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **recursively_tag_media_directory**

    def recursively_tag_media_directory(id, tag_media_directory_request)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.
tag_media_directory_request = elements_sdk.TagMediaDirectoryRequest() # TagMediaDirectoryRequest | 

    try:
        api_instance.recursively_tag_media_directory(id, tag_media_directory_request)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->recursively_tag_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **tag_media_directory_request** | [**TagMediaDirectoryRequest**](TagMediaDirectoryRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **reindex_media_directory**

    def reindex_media_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.reindex_media_directory(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->reindex_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **rename_custom_field**

    def rename_custom_field(id, rename_custom_field_request) -> TaskInfo 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Custom field.
rename_custom_field_request = elements_sdk.RenameCustomFieldRequest() # RenameCustomFieldRequest | 

    try:
        api_response = api_instance.rename_custom_field(id, rename_custom_field_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->rename_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. | 
 **rename_custom_field_request** | [**RenameCustomFieldRequest**](RenameCustomFieldRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **render_sequence**

    def render_sequence(render_endpoint_request) -> TaskInfo 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    render_endpoint_request = elements_sdk.RenderEndpointRequest() # RenderEndpointRequest | 

    try:
        api_response = api_instance.render_sequence(render_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->render_sequence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **render_endpoint_request** | [**RenderEndpointRequest**](RenderEndpointRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **render_subclip**

    def render_subclip(id, render_request) -> TaskInfo 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this subclip.
render_request = elements_sdk.RenderRequest() # RenderRequest | 

    try:
        api_response = api_instance.render_subclip(id, render_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->render_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 
 **render_request** | [**RenderRequest**](RenderRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **request_media_scan**

    def request_media_scan(scanner_scan_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    scanner_scan_endpoint_request = elements_sdk.ScannerScanEndpointRequest() # ScannerScanEndpointRequest | 

    try:
        api_instance.request_media_scan(scanner_scan_endpoint_request)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->request_media_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_scan_endpoint_request** | [**ScannerScanEndpointRequest**](ScannerScanEndpointRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **resolve_comment**

    def resolve_comment(id) -> Comment 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Comment.

    try:
        api_response = api_instance.resolve_comment(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->resolve_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **share_media_library_objects**

    def share_media_library_objects(media_library_share_request) -> OneTimeAccessToken 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    media_library_share_request = elements_sdk.MediaLibraryShareRequest() # MediaLibraryShareRequest | 

    try:
        api_response = api_instance.share_media_library_objects(media_library_share_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->share_media_library_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_library_share_request** | [**MediaLibraryShareRequest**](MediaLibraryShareRequest.md)|  | 

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **test_external_transcoder_connection**

    def test_external_transcoder_connection(test_external_transcoder_connection_request) -> TestExternalTranscoderConnectionResponse 



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    test_external_transcoder_connection_request = elements_sdk.TestExternalTranscoderConnectionRequest() # TestExternalTranscoderConnectionRequest | 

    try:
        api_response = api_instance.test_external_transcoder_connection(test_external_transcoder_connection_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->test_external_transcoder_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_external_transcoder_connection_request** | [**TestExternalTranscoderConnectionRequest**](TestExternalTranscoderConnectionRequest.md)|  | 

### Return type

[**TestExternalTranscoderConnectionResponse**](TestExternalTranscoderConnectionResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **transition_workflow**

    def transition_workflow(workflow_transition_request) -> WorkflowTransitionResponse 



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    workflow_transition_request = elements_sdk.WorkflowTransitionRequest() # WorkflowTransitionRequest | 

    try:
        api_response = api_instance.transition_workflow(workflow_transition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->transition_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_transition_request** | [**WorkflowTransitionRequest**](WorkflowTransitionRequest.md)|  | 

### Return type

[**WorkflowTransitionResponse**](WorkflowTransitionResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **unbookmark_media_directory**

    def unbookmark_media_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.unbookmark_media_directory(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->unbookmark_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **unmark_media_directory_as_showroom**

    def unmark_media_directory_as_showroom(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.

    try:
        api_instance.unmark_media_directory_as_showroom(id)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->unmark_media_directory_as_showroom: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **unresolve_comment**

    def unresolve_comment(id) -> Comment 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Comment.

    try:
        api_response = api_instance.unresolve_comment(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->unresolve_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_asset**

    def update_asset(id, asset) -> Asset 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Asset.
asset = elements_sdk.Asset() # Asset | 

    try:
        api_response = api_instance.update_asset(id, asset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 
 **asset** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_asset_rating**

    def update_asset_rating(id, asset_rating) -> AssetRating 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Rating.
asset_rating = elements_sdk.AssetRating() # AssetRating | 

    try:
        api_response = api_instance.update_asset_rating(id, asset_rating)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Rating. | 
 **asset_rating** | [**AssetRating**](AssetRating.md)|  | 

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_comment**

    def update_comment(id, comment) -> Comment 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Comment.
comment = elements_sdk.Comment() # Comment | 

    try:
        api_response = api_instance.update_comment(id, comment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_custom_field**

    def update_custom_field(id, custom_field) -> CustomField 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Custom field.
custom_field = elements_sdk.CustomField() # CustomField | 

    try:
        api_response = api_instance.update_custom_field(id, custom_field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. | 
 **custom_field** | [**CustomField**](CustomField.md)|  | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_editor_project**

    def update_editor_project(id, editor_project) -> EditorProject 



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.
editor_project = elements_sdk.EditorProject() # EditorProject | 

    try:
        api_response = api_instance.update_editor_project(id, editor_project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **editor_project** | [**EditorProject**](EditorProject.md)|  | 

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_external_transcoder**

    def update_external_transcoder(id, external_transcoder) -> ExternalTranscoder 



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this external transcoder.
external_transcoder = elements_sdk.ExternalTranscoder() # ExternalTranscoder | 

    try:
        api_response = api_instance.update_external_transcoder(id, external_transcoder)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. | 
 **external_transcoder** | [**ExternalTranscoder**](ExternalTranscoder.md)|  | 

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_marker**

    def update_marker(id, marker) -> Marker 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this marker.
marker = elements_sdk.Marker() # Marker | 

    try:
        api_response = api_instance.update_marker(id, marker)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this marker. | 
 **marker** | [**Marker**](Marker.md)|  | 

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_file**

    def update_media_file(id, media_file) -> MediaFile 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this File.
media_file = elements_sdk.MediaFile() # MediaFile | 

    try:
        api_response = api_instance.update_media_file(id, media_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **media_file** | [**MediaFile**](MediaFile.md)|  | 

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_file_template**

    def update_media_file_template(id, media_file_template) -> MediaFileTemplate 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Template.
media_file_template = elements_sdk.MediaFileTemplate() # MediaFileTemplate | 

    try:
        api_response = api_instance.update_media_file_template(id, media_file_template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 
 **media_file_template** | [**MediaFileTemplate**](MediaFileTemplate.md)|  | 

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_root**

    def update_media_root(id, media_root) -> MediaRoot 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this media root.
media_root = elements_sdk.MediaRoot() # MediaRoot | 

    try:
        api_response = api_instance.update_media_root(id, media_root)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. | 
 **media_root** | [**MediaRoot**](MediaRoot.md)|  | 

### Return type

[**MediaRoot**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_root_permission**

    def update_media_root_permission(id, media_root_permission) -> MediaRootPermission 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Media Root Permission.
media_root_permission = elements_sdk.MediaRootPermission() # MediaRootPermission | 

    try:
        api_response = api_instance.update_media_root_permission(id, media_root_permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. | 
 **media_root_permission** | [**MediaRootPermission**](MediaRootPermission.md)|  | 

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_tag**

    def update_media_tag(id, unfiltered_tag) -> UnfilteredTag 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this Tag.
unfiltered_tag = elements_sdk.UnfilteredTag() # UnfilteredTag | 

    try:
        api_response = api_instance.update_media_tag(id, unfiltered_tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 
 **unfiltered_tag** | [**UnfilteredTag**](UnfilteredTag.md)|  | 

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_proxy_profile**

    def update_proxy_profile(id, proxy_profile) -> ProxyProfile 



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this proxy profile.
proxy_profile = elements_sdk.ProxyProfile() # ProxyProfile | 

    try:
        api_response = api_instance.update_proxy_profile(id, proxy_profile)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 
 **proxy_profile** | [**ProxyProfile**](ProxyProfile.md)|  | 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_subclip**

    def update_subclip(id, subclip) -> Subclip 



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.MediaLibraryApi(api_client)
    id = 56 # int | A unique integer value identifying this subclip.
subclip = elements_sdk.Subclip() # Subclip | 

    try:
        api_response = api_instance.update_subclip(id, subclip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 
 **subclip** | [**Subclip**](Subclip.md)|  | 

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

