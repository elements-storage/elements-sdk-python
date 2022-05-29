# elements_sdk.ClickApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_click_upload**](ClickApi.md#abort_click_upload) | **DELETE** `/api/2/click/uploads/{upload_id}` | 
[**continue_click_upload_in_background**](ClickApi.md#continue_click_upload_in_background) | **POST** `/api/2/click/uploads/{upload_id}/background` | 
[**create_click_gallery**](ClickApi.md#create_click_gallery) | **POST** `/api/2/click/connections/{connection_id}/galleries` | 
[**create_click_gallery_link**](ClickApi.md#create_click_gallery_link) | **POST** `/api/2/click/connections/{connection_id}/gallery-links` | 
[**delete_click_gallery_link**](ClickApi.md#delete_click_gallery_link) | **DELETE** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
[**get_all_click_galleries**](ClickApi.md#get_all_click_galleries) | **GET** `/api/2/click/connections/{connection_id}/galleries` | 
[**get_all_click_gallery_links**](ClickApi.md#get_all_click_gallery_links) | **GET** `/api/2/click/connections/{connection_id}/gallery-links` | 
[**get_click_gallery**](ClickApi.md#get_click_gallery) | **GET** `/api/2/click/connections/{connection_id}/galleries/{id}` | 
[**get_click_gallery_link**](ClickApi.md#get_click_gallery_link) | **GET** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
[**patch_click_gallery**](ClickApi.md#patch_click_gallery) | **PATCH** `/api/2/click/connections/{connection_id}/galleries/{id}` | 
[**send_click_gallery_link_email**](ClickApi.md#send_click_gallery_link_email) | **POST** `/api/2/click/connections/{connection_id}/gallery-links/{link_id}/send` | 
[**start_click_upload**](ClickApi.md#start_click_upload) | **POST** `/api/2/click/uploads` | 
[**update_click_gallery**](ClickApi.md#update_click_gallery) | **PUT** `/api/2/click/connections/{connection_id}/galleries/{id}` | 



***

# **abort_click_upload**

    def abort_click_upload(upload_id)



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    upload_id = 'upload_id_example' # str | 

    try:
        api_instance.abort_click_upload(upload_id)
    except ApiException as e:
        print("Exception when calling ClickApi->abort_click_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **continue_click_upload_in_background**

    def continue_click_upload_in_background(upload_id, click_background_upload_endpoint_request)



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    upload_id = 'upload_id_example' # str | 
click_background_upload_endpoint_request = elements_sdk.ClickBackgroundUploadEndpointRequest() # ClickBackgroundUploadEndpointRequest | 

    try:
        api_instance.continue_click_upload_in_background(upload_id, click_background_upload_endpoint_request)
    except ApiException as e:
        print("Exception when calling ClickApi->continue_click_upload_in_background: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **click_background_upload_endpoint_request** | [**ClickBackgroundUploadEndpointRequest**](ClickBackgroundUploadEndpointRequest.md)|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_click_gallery**

    def create_click_gallery(connection_id, click_gallery) -> ClickGallery 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
click_gallery = elements_sdk.ClickGallery() # ClickGallery | 

    try:
        api_response = api_instance.create_click_gallery(connection_id, click_gallery)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->create_click_gallery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **click_gallery** | [**ClickGallery**](ClickGallery.md)|  | 

### Return type

[**ClickGallery**](ClickGallery.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_click_gallery_link**

    def create_click_gallery_link(connection_id, click_gallery_link) -> ClickGalleryLink 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
click_gallery_link = elements_sdk.ClickGalleryLink() # ClickGalleryLink | 

    try:
        api_response = api_instance.create_click_gallery_link(connection_id, click_gallery_link)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->create_click_gallery_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **click_gallery_link** | [**ClickGalleryLink**](ClickGalleryLink.md)|  | 

### Return type

[**ClickGalleryLink**](ClickGalleryLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_click_gallery_link**

    def delete_click_gallery_link(connection_id, id)



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
id = 'id_example' # str | 

    try:
        api_instance.delete_click_gallery_link(connection_id, id)
    except ApiException as e:
        print("Exception when calling ClickApi->delete_click_gallery_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_click_galleries**

    def get_all_click_galleries(connection_id, ordering=ordering, limit=limit, offset=offset) -> InlineResponse200 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_click_galleries(connection_id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->get_all_click_galleries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_click_gallery_links**

    def get_all_click_gallery_links(connection_id, ordering=ordering, limit=limit, offset=offset) -> InlineResponse2001 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_click_gallery_links(connection_id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->get_all_click_gallery_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_click_gallery**

    def get_click_gallery(connection_id, id) -> ClickGallery 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
id = 'id_example' # str | 

    try:
        api_response = api_instance.get_click_gallery(connection_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->get_click_gallery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ClickGallery**](ClickGallery.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_click_gallery_link**

    def get_click_gallery_link(connection_id, id) -> ClickGalleryLink 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
id = 'id_example' # str | 

    try:
        api_response = api_instance.get_click_gallery_link(connection_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->get_click_gallery_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ClickGalleryLink**](ClickGalleryLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_click_gallery**

    def patch_click_gallery(connection_id, id, click_gallery) -> ClickGallery 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
id = 'id_example' # str | 
click_gallery = elements_sdk.ClickGallery() # ClickGallery | 

    try:
        api_response = api_instance.patch_click_gallery(connection_id, id, click_gallery)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->patch_click_gallery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **id** | **str**|  | 
 **click_gallery** | [**ClickGallery**](ClickGallery.md)|  | 

### Return type

[**ClickGallery**](ClickGallery.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **send_click_gallery_link_email**

    def send_click_gallery_link_email(connection_id, link_id)



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
link_id = 'link_id_example' # str | 

    try:
        api_instance.send_click_gallery_link_email(connection_id, link_id)
    except ApiException as e:
        print("Exception when calling ClickApi->send_click_gallery_link_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **link_id** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_click_upload**

    def start_click_upload(click_start_upload_endpoint_request) -> TaskInfo 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    click_start_upload_endpoint_request = elements_sdk.ClickStartUploadEndpointRequest() # ClickStartUploadEndpointRequest | 

    try:
        api_response = api_instance.start_click_upload(click_start_upload_endpoint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->start_click_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **click_start_upload_endpoint_request** | [**ClickStartUploadEndpointRequest**](ClickStartUploadEndpointRequest.md)|  | 

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_click_gallery**

    def update_click_gallery(connection_id, id, add_assets_to_click_gallery) -> AddAssetsToClickGallery 



### Required permissions    * User account permission: `cloud:access` 

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
    api_instance = elements_sdk.ClickApi(api_client)
    connection_id = 'connection_id_example' # str | 
id = 'id_example' # str | 
add_assets_to_click_gallery = elements_sdk.AddAssetsToClickGallery() # AddAssetsToClickGallery | 

    try:
        api_response = api_instance.update_click_gallery(connection_id, id, add_assets_to_click_gallery)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClickApi->update_click_gallery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **id** | **str**|  | 
 **add_assets_to_click_gallery** | [**AddAssetsToClickGallery**](AddAssetsToClickGallery.md)|  | 

### Return type

[**AddAssetsToClickGallery**](AddAssetsToClickGallery.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

