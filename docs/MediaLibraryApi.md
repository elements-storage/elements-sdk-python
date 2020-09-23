# elements_sdk.MediaLibraryApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_subclip_clipboard**](MediaLibraryApi.md#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
[**combine_assets_into_set**](MediaLibraryApi.md#combine_assets_into_set) | **POST** `/api/2/media/assets/combine` | 
[**create_asset**](MediaLibraryApi.md#create_asset) | **POST** `/api/2/media/assets` | 
[**create_asset_rating**](MediaLibraryApi.md#create_asset_rating) | **POST** `/api/2/media/ratings` | 
[**create_comment**](MediaLibraryApi.md#create_comment) | **POST** `/api/2/media/comments` | 
[**create_custom_field**](MediaLibraryApi.md#create_custom_field) | **POST** `/api/2/media/custom-fields` | 
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
[**delete_marker**](MediaLibraryApi.md#delete_marker) | **DELETE** `/api/2/media/markers/{id}` | 
[**delete_media_file_template**](MediaLibraryApi.md#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
[**delete_media_root**](MediaLibraryApi.md#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
[**delete_media_root_permission**](MediaLibraryApi.md#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
[**delete_media_tag**](MediaLibraryApi.md#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
[**delete_media_update**](MediaLibraryApi.md#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
[**delete_proxy**](MediaLibraryApi.md#delete_proxy) | **DELETE** `/api/2/media/proxies/{id}` | 
[**delete_proxy_profile**](MediaLibraryApi.md#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
[**delete_subclip**](MediaLibraryApi.md#delete_subclip) | **DELETE** `/api/2/media/subclips/{id}` | 
[**delete_subclip_clipboard_entry**](MediaLibraryApi.md#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
[**discover_media**](MediaLibraryApi.md#discover_media) | **POST** `/api/2/scanner/discover` | 
[**get_all_asset_project_links**](MediaLibraryApi.md#get_all_asset_project_links) | **GET** `/api/2/media/assets/project-links` | 
[**get_all_asset_ratings**](MediaLibraryApi.md#get_all_asset_ratings) | **GET** `/api/2/media/ratings` | 
[**get_all_asset_tape_backups**](MediaLibraryApi.md#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
[**get_all_assets**](MediaLibraryApi.md#get_all_assets) | **GET** `/api/2/media/assets` | 
[**get_all_bundles_for_media_root**](MediaLibraryApi.md#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
[**get_all_click_links**](MediaLibraryApi.md#get_all_click_links) | **GET** `/api/2/media/assets/click-links` | 
[**get_all_comments**](MediaLibraryApi.md#get_all_comments) | **GET** `/api/2/media/comments` | 
[**get_all_custom_fields**](MediaLibraryApi.md#get_all_custom_fields) | **GET** `/api/2/media/custom-fields` | 
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
[**get_all_proxies**](MediaLibraryApi.md#get_all_proxies) | **GET** `/api/2/media/proxies` | 
[**get_all_proxy_profiles**](MediaLibraryApi.md#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
[**get_all_subclip_clipboard_entries**](MediaLibraryApi.md#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
[**get_all_subclips**](MediaLibraryApi.md#get_all_subclips) | **GET** `/api/2/media/subclips` | 
[**get_all_transcoder_profiles**](MediaLibraryApi.md#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
[**get_asset**](MediaLibraryApi.md#get_asset) | **GET** `/api/2/media/assets/{id}` | 
[**get_asset_rating**](MediaLibraryApi.md#get_asset_rating) | **GET** `/api/2/media/ratings/{id}` | 
[**get_comment**](MediaLibraryApi.md#get_comment) | **GET** `/api/2/media/comments/{id}` | 
[**get_custom_field**](MediaLibraryApi.md#get_custom_field) | **GET** `/api/2/media/custom-fields/{id}` | 
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
[**get_proxy_profile**](MediaLibraryApi.md#get_proxy_profile) | **GET** `/api/2/media/proxy-profiles/{id}` | 
[**get_proxy_profile_proxy_count**](MediaLibraryApi.md#get_proxy_profile_proxy_count) | **GET** `/api/2/media/proxy-profiles/{id}/proxy-count` | 
[**get_subclip**](MediaLibraryApi.md#get_subclip) | **GET** `/api/2/media/subclips/{id}` | 
[**get_transcoder_profile**](MediaLibraryApi.md#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
[**patch_asset**](MediaLibraryApi.md#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
[**patch_asset_rating**](MediaLibraryApi.md#patch_asset_rating) | **PATCH** `/api/2/media/ratings/{id}` | 
[**patch_comment**](MediaLibraryApi.md#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
[**patch_custom_field**](MediaLibraryApi.md#patch_custom_field) | **PATCH** `/api/2/media/custom-fields/{id}` | 
[**patch_marker**](MediaLibraryApi.md#patch_marker) | **PATCH** `/api/2/media/markers/{id}` | 
[**patch_media_file**](MediaLibraryApi.md#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
[**patch_media_file_template**](MediaLibraryApi.md#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
[**patch_media_root**](MediaLibraryApi.md#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
[**patch_media_root_permission**](MediaLibraryApi.md#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
[**patch_media_tag**](MediaLibraryApi.md#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
[**patch_proxy_profile**](MediaLibraryApi.md#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
[**patch_subclip**](MediaLibraryApi.md#patch_subclip) | **PATCH** `/api/2/media/subclips/{id}` | 
[**request_media_scan**](MediaLibraryApi.md#request_media_scan) | **POST** `/api/2/scanner/scan` | 
[**resolve_comment**](MediaLibraryApi.md#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
[**unresolve_comment**](MediaLibraryApi.md#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
[**update_asset**](MediaLibraryApi.md#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
[**update_asset_rating**](MediaLibraryApi.md#update_asset_rating) | **PUT** `/api/2/media/ratings/{id}` | 
[**update_comment**](MediaLibraryApi.md#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
[**update_custom_field**](MediaLibraryApi.md#update_custom_field) | **PUT** `/api/2/media/custom-fields/{id}` | 
[**update_marker**](MediaLibraryApi.md#update_marker) | **PUT** `/api/2/media/markers/{id}` | 
[**update_media_file**](MediaLibraryApi.md#update_media_file) | **PUT** `/api/2/media/files/{id}` | 
[**update_media_file_template**](MediaLibraryApi.md#update_media_file_template) | **PUT** `/api/2/media/files/templates/{id}` | 
[**update_media_root**](MediaLibraryApi.md#update_media_root) | **PUT** `/api/2/media/roots/{id}` | 
[**update_media_root_permission**](MediaLibraryApi.md#update_media_root_permission) | **PUT** `/api/2/media/root-permissions/{id}` | 
[**update_media_tag**](MediaLibraryApi.md#update_media_tag) | **PUT** `/api/2/media/tags/{id}` | 
[**update_proxy_profile**](MediaLibraryApi.md#update_proxy_profile) | **PUT** `/api/2/media/proxy-profiles/{id}` | 
[**update_subclip**](MediaLibraryApi.md#update_subclip) | **PUT** `/api/2/media/subclips/{id}` | 



***

# **clear_subclip_clipboard**
> object clear_subclip_clipboard()



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.clear_subclip_clipboard()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->clear_subclip_clipboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **combine_assets_into_set**
> object combine_assets_into_set(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.MultipleAssetsRequest() # MultipleAssetsRequest | 

    try:
        api_response = api_instance.combine_assets_into_set(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->combine_assets_into_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MultipleAssetsRequest**](MultipleAssetsRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_asset**
> Asset create_asset(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.Asset() # Asset | 

    try:
        api_response = api_instance.create_asset(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_asset_rating**
> AssetRating create_asset_rating(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.AssetRating() # AssetRating | 

    try:
        api_response = api_instance.create_asset_rating(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AssetRating**](AssetRating.md)|  | 

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_comment**
> Comment create_comment(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.Comment() # Comment | 

    try:
        api_response = api_instance.create_comment(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_custom_field**
> CustomField create_custom_field(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.CustomField() # CustomField | 

    try:
        api_response = api_instance.create_custom_field(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CustomField**](CustomField.md)|  | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_marker**
> Marker create_marker(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.Marker() # Marker | 

    try:
        api_response = api_instance.create_marker(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Marker**](Marker.md)|  | 

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_file_template**
> MediaFileTemplate create_media_file_template(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.MediaFileTemplate() # MediaFileTemplate | 

    try:
        api_response = api_instance.create_media_file_template(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MediaFileTemplate**](MediaFileTemplate.md)|  | 

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_root**
> MediaRoot create_media_root(data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
    data = elements_sdk.MediaRoot() # MediaRoot | 

    try:
        api_response = api_instance.create_media_root(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MediaRoot**](MediaRoot.md)|  | 

### Return type

[**MediaRoot**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_root_permission**
> MediaRootPermission create_media_root_permission(data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
    data = elements_sdk.MediaRootPermission() # MediaRootPermission | 

    try:
        api_response = api_instance.create_media_root_permission(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MediaRootPermission**](MediaRootPermission.md)|  | 

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_media_tag**
> Tag create_media_tag(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.Tag() # Tag | 

    try:
        api_response = api_instance.create_media_tag(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_proxy_profile**
> ProxyProfile create_proxy_profile(data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
    data = elements_sdk.ProxyProfile() # ProxyProfile | 

    try:
        api_response = api_instance.create_proxy_profile(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProxyProfile**](ProxyProfile.md)|  | 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_subclip**
> Subclip create_subclip(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.Subclip() # Subclip | 

    try:
        api_response = api_instance.create_subclip(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Subclip**](Subclip.md)|  | 

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_subclip_clipboard_entry**
> SubclipClipboardEntry create_subclip_clipboard_entry(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.SubclipClipboardEntry() # SubclipClipboardEntry | 

    try:
        api_response = api_instance.create_subclip_clipboard_entry(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->create_subclip_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubclipClipboardEntry**](SubclipClipboardEntry.md)|  | 

### Return type

[**SubclipClipboardEntry**](SubclipClipboardEntry.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_asset**
> object delete_asset(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_asset(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_asset_rating**
> object delete_asset_rating(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_asset_rating(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Rating. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_comment**
> object delete_comment(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_comment(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_custom_field**
> object delete_custom_field(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
    id = 56 # int | A unique integer value identifying this CustomField.

    try:
        api_response = api_instance.delete_custom_field(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this CustomField. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_marker**
> object delete_marker(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_marker(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this marker. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_file_template**
> object delete_media_file_template(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_media_file_template(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_root**
> object delete_media_root(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
        api_response = api_instance.delete_media_root(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_root_permission**
> object delete_media_root_permission(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
        api_response = api_instance.delete_media_root_permission(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_tag**
> object delete_media_tag(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_media_tag(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_media_update**
> object delete_media_update(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
        api_response = api_instance.delete_media_update(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Update. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_proxy**
> object delete_proxy(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_proxy(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_proxy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_proxy_profile**
> object delete_proxy_profile(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
        api_response = api_instance.delete_proxy_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_subclip**
> object delete_subclip(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_subclip(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_subclip_clipboard_entry**
> object delete_subclip_clipboard_entry(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.delete_subclip_clipboard_entry(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_subclip_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip clipboard entry. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **discover_media**
> object discover_media(data)



### Required permissions    * User account permission: media:access 

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
    data = elements_sdk.ScannerDiscoverEndpointRequest() # ScannerDiscoverEndpointRequest | 

    try:
        api_response = api_instance.discover_media(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->discover_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ScannerDiscoverEndpointRequest**](ScannerDiscoverEndpointRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_asset_project_links**
> list[AssetProjectLink] get_all_asset_project_links(asset=asset, project=project, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
> list[AssetRating] get_all_asset_ratings(user=user, asset=asset, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
> list[AssetBackup] get_all_asset_tape_backups(asset=asset, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media   * License component: ltfs 

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

    try:
        api_response = api_instance.get_all_asset_tape_backups(asset=asset, ordering=ordering, limit=limit, offset=offset)
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

### Return type

[**list[AssetBackup]**](AssetBackup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_assets**
> list[Asset] get_all_assets(sync_id=sync_id, display_name=display_name, set=set, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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

    try:
        api_response = api_instance.get_all_assets(sync_id=sync_id, display_name=display_name, set=set, ordering=ordering, limit=limit, offset=offset)
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

### Return type

[**list[Asset]**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_bundles_for_media_root**
> list[MediaFileBundle] get_all_bundles_for_media_root(root, asset=asset, ordering=ordering, limit=limit, offset=offset)



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
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_bundles_for_media_root(root, asset=asset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_bundles_for_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**|  | 
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_click_links**
> list[AssetCloudLink] get_all_click_links(asset=asset, connection=connection, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
> list[Comment] get_all_comments(asset=asset, root=root, user=user, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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

    try:
        api_response = api_instance.get_all_comments(asset=asset, root=root, user=user, ordering=ordering, limit=limit, offset=offset)
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

### Return type

[**list[Comment]**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_custom_fields**
> list[CustomField] get_all_custom_fields(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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

# **get_all_markers**
> list[Marker] get_all_markers(asset=asset, user=user, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
> list[MediaFileBundle] get_all_media_file_bundles(asset=asset, ordering=ordering, limit=limit, offset=offset)



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
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_file_bundles(asset=asset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_file_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_file_templates**
> list[MediaFileTemplate] get_all_media_file_templates(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
> list[MediaFile] get_all_media_files(bundle=bundle, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
parent = 'parent_example' # str | Filter the returned list by `parent`. (optional)
path = 'path_example' # str | Filter the returned list by `path`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_dir = 'is_dir_example' # str | Filter the returned list by `is_dir`. (optional)
is_showroom = 'is_showroom_example' # str | Filter the returned list by `is_showroom`. (optional)
present = 'present_example' # str | Filter the returned list by `present`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_files(bundle=bundle, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**| Filter the returned list by &#x60;bundle&#x60;. | [optional] 
 **parent** | **str**| Filter the returned list by &#x60;parent&#x60;. | [optional] 
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional] 
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional] 
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_files_for_bundles**
> list[MediaFile] get_all_media_files_for_bundles(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.AllMediaFilesForBundlesRequest() # AllMediaFilesForBundlesRequest | 

    try:
        api_response = api_instance.get_all_media_files_for_bundles(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_for_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AllMediaFilesForBundlesRequest**](AllMediaFilesForBundlesRequest.md)|  | 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_files_for_media_root**
> list[MediaFile] get_all_media_files_for_media_root(root, bundle=bundle, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
parent = 'parent_example' # str | Filter the returned list by `parent`. (optional)
path = 'path_example' # str | Filter the returned list by `path`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
is_dir = 'is_dir_example' # str | Filter the returned list by `is_dir`. (optional)
is_showroom = 'is_showroom_example' # str | Filter the returned list by `is_showroom`. (optional)
present = 'present_example' # str | Filter the returned list by `present`. (optional)
volume = 'volume_example' # str | Filter the returned list by `volume`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_files_for_media_root(root, bundle=bundle, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, volume=volume, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_for_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**|  | 
 **bundle** | **str**| Filter the returned list by &#x60;bundle&#x60;. | [optional] 
 **parent** | **str**| Filter the returned list by &#x60;parent&#x60;. | [optional] 
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional] 
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional] 
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_root_permissions**
> list[MediaRootPermission] get_all_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
> list[MediaRoot] get_all_media_roots(path=path, volume=volume, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_roots(path=path, volume=volume, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_roots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional] 
 **volume** | **str**| Filter the returned list by &#x60;volume&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaRoot]**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_tags**
> list[Tag] get_all_media_tags(name=name, name__icontains=name__icontains, root=root, root__isnull=root__isnull, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
root = 'root_example' # str | Filter the returned list by `root`. (optional)
root__isnull = 'root__isnull_example' # str | Filter the returned list by `root__isnull`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_media_tags(name=name, name__icontains=name__icontains, root=root, root__isnull=root__isnull, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **name__icontains** | **str**| Filter the returned list by &#x60;name__icontains&#x60;. | [optional] 
 **root** | **str**| Filter the returned list by &#x60;root&#x60;. | [optional] 
 **root__isnull** | **str**| Filter the returned list by &#x60;root__isnull&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Tag]**](Tag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_media_updates**
> list[MediaUpdate] get_all_media_updates(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
        api_response = api_instance.get_all_media_updates(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_updates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[MediaUpdate]**](MediaUpdate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_proxies**
> list[Proxy] get_all_proxies(asset=asset, profile=profile, generated=generated, failed=failed, variant_id=variant_id, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
profile = 'profile_example' # str | Filter the returned list by `profile`. (optional)
generated = 'generated_example' # str | Filter the returned list by `generated`. (optional)
failed = 'failed_example' # str | Filter the returned list by `failed`. (optional)
variant_id = 'variant_id_example' # str | Filter the returned list by `variant_id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_proxies(asset=asset, profile=profile, generated=generated, failed=failed, variant_id=variant_id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_proxies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **profile** | **str**| Filter the returned list by &#x60;profile&#x60;. | [optional] 
 **generated** | **str**| Filter the returned list by &#x60;generated&#x60;. | [optional] 
 **failed** | **str**| Filter the returned list by &#x60;failed&#x60;. | [optional] 
 **variant_id** | **str**| Filter the returned list by &#x60;variant_id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Proxy]**](Proxy.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_proxy_profiles**
> list[ProxyProfile] get_all_proxy_profiles(name=name, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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

    try:
        api_response = api_instance.get_all_proxy_profiles(name=name, ordering=ordering, limit=limit, offset=offset)
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

### Return type

[**list[ProxyProfile]**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_subclip_clipboard_entries**
> list[SubclipClipboardEntry] get_all_subclip_clipboard_entries(cut=cut, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
> list[Subclip] get_all_subclips(asset=asset, root=root, name=name, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_subclips(asset=asset, root=root, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_subclips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
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
> list[TranscoderProfile] get_all_transcoder_profiles(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access   * License component: media 

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
> Asset get_asset(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.get_asset(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_asset_rating**
> AssetRating get_asset_rating(id)



### Required permissions    * User account permission: media:access   * License component: media 

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

# **get_comment**
> Comment get_comment(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.get_comment(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_custom_field**
> CustomField get_custom_field(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
    id = 56 # int | A unique integer value identifying this CustomField.

    try:
        api_response = api_instance.get_custom_field(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this CustomField. | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_latest_media_update**
> MediaUpdate get_latest_media_update(ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
        api_response = api_instance.get_latest_media_update(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_latest_media_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**MediaUpdate**](MediaUpdate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_marker**
> Marker get_marker(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
> MediaFile get_media_file(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.get_media_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_file_bundle**
> MediaFileBundle get_media_file_bundle(id)



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
        api_response = api_instance.get_media_file_bundle(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. | 

### Return type

[**MediaFileBundle**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_media_file_contents**
> MediaFileContents get_media_file_contents(id, exclude_deleted=exclude_deleted, exclude_unrecognized=exclude_unrecognized, offset=offset, limit=limit)



### Required permissions    * User account permission: media:access   * License component: media 

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
> MediaFileTemplate get_media_file_template(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
> MediaRoot get_media_root(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
> MediaRootPermission get_media_root_permission(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
> Tag get_media_tag(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
        api_response = api_instance.get_media_tag(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 

### Return type

[**Tag**](Tag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_multiple_assets**
> list[Asset] get_multiple_assets(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.MultipleAssetsRequest() # MultipleAssetsRequest | 

    try:
        api_response = api_instance.get_multiple_assets(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MultipleAssetsRequest**](MultipleAssetsRequest.md)|  | 

### Return type

[**list[Asset]**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_multiple_bundles**
> list[MediaFileBundle] get_multiple_bundles(data)



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
    data = elements_sdk.GetMultipleBundlesRequest() # GetMultipleBundlesRequest | 

    try:
        api_response = api_instance.get_multiple_bundles(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GetMultipleBundlesRequest**](GetMultipleBundlesRequest.md)|  | 

### Return type

[**list[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_multiple_files**
> list[MediaFile] get_multiple_files(data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    data = elements_sdk.GetMultipleFilesRequest() # GetMultipleFilesRequest | 

    try:
        api_response = api_instance.get_multiple_files(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GetMultipleFilesRequest**](GetMultipleFilesRequest.md)|  | 

### Return type

[**list[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_my_media_root_permissions**
> list[MediaRootPermission] get_my_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
> list[MediaRootPermission] get_my_resolved_media_root_permissions(root=root, id=id, ordering=ordering, limit=limit, offset=offset)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
> Proxy get_proxy(id)



### Required permissions    * User account permission: media:access   * License component: media 

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

# **get_proxy_profile**
> ProxyProfile get_proxy_profile(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
        api_response = api_instance.get_proxy_profile(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_proxy_profile_proxy_count**
> ProxyCount get_proxy_profile_proxy_count(id)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
> Subclip get_subclip(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
> TranscoderProfile get_transcoder_profile(id)



### Required permissions    * User account permission: media:access   * License component: media 

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

# **patch_asset**
> Asset patch_asset(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Asset() # Asset | 

    try:
        api_response = api_instance.patch_asset(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_asset_rating**
> AssetRating patch_asset_rating(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.AssetRating() # AssetRating | 

    try:
        api_response = api_instance.patch_asset_rating(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Rating. | 
 **data** | [**AssetRating**](AssetRating.md)|  | 

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_comment**
> Comment patch_comment(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Comment() # Comment | 

    try:
        api_response = api_instance.patch_comment(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_custom_field**
> CustomField patch_custom_field(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    id = 56 # int | A unique integer value identifying this CustomField.
data = elements_sdk.CustomField() # CustomField | 

    try:
        api_response = api_instance.patch_custom_field(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this CustomField. | 
 **data** | [**CustomField**](CustomField.md)|  | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_marker**
> Marker patch_marker(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Marker() # Marker | 

    try:
        api_response = api_instance.patch_marker(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this marker. | 
 **data** | [**Marker**](Marker.md)|  | 

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_file**
> MediaFile patch_media_file(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.MediaFile() # MediaFile | 

    try:
        api_response = api_instance.patch_media_file(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **data** | [**MediaFile**](MediaFile.md)|  | 

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_file_template**
> MediaFileTemplate patch_media_file_template(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.MediaFileTemplate() # MediaFileTemplate | 

    try:
        api_response = api_instance.patch_media_file_template(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 
 **data** | [**MediaFileTemplate**](MediaFileTemplate.md)|  | 

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_root**
> MediaRoot patch_media_root(id, data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
data = elements_sdk.MediaRoot() # MediaRoot | 

    try:
        api_response = api_instance.patch_media_root(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. | 
 **data** | [**MediaRoot**](MediaRoot.md)|  | 

### Return type

[**MediaRoot**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_root_permission**
> MediaRootPermission patch_media_root_permission(id, data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
data = elements_sdk.MediaRootPermission() # MediaRootPermission | 

    try:
        api_response = api_instance.patch_media_root_permission(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. | 
 **data** | [**MediaRootPermission**](MediaRootPermission.md)|  | 

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_media_tag**
> Tag patch_media_tag(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Tag() # Tag | 

    try:
        api_response = api_instance.patch_media_tag(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_proxy_profile**
> ProxyProfile patch_proxy_profile(id, data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
data = elements_sdk.ProxyProfile() # ProxyProfile | 

    try:
        api_response = api_instance.patch_proxy_profile(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 
 **data** | [**ProxyProfile**](ProxyProfile.md)|  | 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_subclip**
> Subclip patch_subclip(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Subclip() # Subclip | 

    try:
        api_response = api_instance.patch_subclip(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 
 **data** | [**Subclip**](Subclip.md)|  | 

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **request_media_scan**
> object request_media_scan(data)



### Required permissions    * User account permission: media:access 

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
    data = elements_sdk.ScannerScanEndpointRequest() # ScannerScanEndpointRequest | 

    try:
        api_response = api_instance.request_media_scan(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->request_media_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ScannerScanEndpointRequest**](ScannerScanEndpointRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **resolve_comment**
> Comment resolve_comment(id)



### Required permissions    * User account permission: media:access   * License component: media 

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

# **unresolve_comment**
> Comment unresolve_comment(id)



### Required permissions    * User account permission: media:access   * License component: media 

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
> Asset update_asset(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Asset() # Asset | 

    try:
        api_response = api_instance.update_asset(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. | 
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_asset_rating**
> AssetRating update_asset_rating(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.AssetRating() # AssetRating | 

    try:
        api_response = api_instance.update_asset_rating(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Rating. | 
 **data** | [**AssetRating**](AssetRating.md)|  | 

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_comment**
> Comment update_comment(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Comment() # Comment | 

    try:
        api_response = api_instance.update_comment(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_custom_field**
> CustomField update_custom_field(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
    id = 56 # int | A unique integer value identifying this CustomField.
data = elements_sdk.CustomField() # CustomField | 

    try:
        api_response = api_instance.update_custom_field(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this CustomField. | 
 **data** | [**CustomField**](CustomField.md)|  | 

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_marker**
> Marker update_marker(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Marker() # Marker | 

    try:
        api_response = api_instance.update_marker(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this marker. | 
 **data** | [**Marker**](Marker.md)|  | 

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_file**
> MediaFile update_media_file(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.MediaFile() # MediaFile | 

    try:
        api_response = api_instance.update_media_file(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. | 
 **data** | [**MediaFile**](MediaFile.md)|  | 

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_file_template**
> MediaFileTemplate update_media_file_template(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.MediaFileTemplate() # MediaFileTemplate | 

    try:
        api_response = api_instance.update_media_file_template(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. | 
 **data** | [**MediaFileTemplate**](MediaFileTemplate.md)|  | 

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_root**
> MediaRoot update_media_root(id, data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
data = elements_sdk.MediaRoot() # MediaRoot | 

    try:
        api_response = api_instance.update_media_root(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. | 
 **data** | [**MediaRoot**](MediaRoot.md)|  | 

### Return type

[**MediaRoot**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_root_permission**
> MediaRootPermission update_media_root_permission(id, data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
data = elements_sdk.MediaRootPermission() # MediaRootPermission | 

    try:
        api_response = api_instance.update_media_root_permission(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. | 
 **data** | [**MediaRootPermission**](MediaRootPermission.md)|  | 

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_media_tag**
> Tag update_media_tag(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Tag() # Tag | 

    try:
        api_response = api_instance.update_media_tag(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_proxy_profile**
> ProxyProfile update_proxy_profile(id, data)



### Required permissions    * User account permission: media:access (read) / media:roots:manage (write)   * License component: media 

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
data = elements_sdk.ProxyProfile() # ProxyProfile | 

    try:
        api_response = api_instance.update_proxy_profile(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. | 
 **data** | [**ProxyProfile**](ProxyProfile.md)|  | 

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_subclip**
> Subclip update_subclip(id, data)



### Required permissions    * User account permission: media:access   * License component: media 

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
data = elements_sdk.Subclip() # Subclip | 

    try:
        api_response = api_instance.update_subclip(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MediaLibraryApi->update_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip. | 
 **data** | [**Subclip**](Subclip.md)|  | 

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

