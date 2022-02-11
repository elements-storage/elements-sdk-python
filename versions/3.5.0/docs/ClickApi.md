# elements_sdk.ClickApi

All URIs are relative to *https://elements.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_click_upload**](ClickApi.md#abort_click_upload) | **DELETE** `/api/2/click/uploads/{upload_id}` | 
[**add_assets_to_click_gallery**](ClickApi.md#add_assets_to_click_gallery) | **POST** `/api/2/click/connections/{connection_id}/galleries/{id}/add-assets` | 
[**continue_click_upload_in_background**](ClickApi.md#continue_click_upload_in_background) | **POST** `/api/2/click/uploads/{upload_id}/background` | 
[**create_click_gallery**](ClickApi.md#create_click_gallery) | **POST** `/api/2/click/connections/{connection_id}/galleries` | 
[**create_click_gallery_link**](ClickApi.md#create_click_gallery_link) | **POST** `/api/2/click/connections/{connection_id}/gallery-links` | 
[**delete_click_gallery_link**](ClickApi.md#delete_click_gallery_link) | **DELETE** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
[**get_all_click_galleries**](ClickApi.md#get_all_click_galleries) | **GET** `/api/2/click/connections/{connection_id}/galleries` | 
[**get_all_click_gallery_links**](ClickApi.md#get_all_click_gallery_links) | **GET** `/api/2/click/connections/{connection_id}/gallery-links` | 
[**get_click_gallery**](ClickApi.md#get_click_gallery) | **GET** `/api/2/click/connections/{connection_id}/galleries/{id}` | 
[**get_click_gallery_link**](ClickApi.md#get_click_gallery_link) | **GET** `/api/2/click/connections/{connection_id}/gallery-links/{id}` | 
[**send_click_gallery_link_email**](ClickApi.md#send_click_gallery_link_email) | **POST** `/api/2/click/connections/{connection_id}/gallery-links/{link_id}/send` | 
[**start_click_upload**](ClickApi.md#start_click_upload) | **POST** `/api/2/click/uploads` | 


# **abort_click_upload**
> abort_click_upload(upload_id)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    upload_id = "upload_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.abort_click_upload(upload_id)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->abort_click_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **add_assets_to_click_gallery**
> ClickGallery add_assets_to_click_gallery(connection_id, id, add_assets_to_click_gallery)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.add_assets_to_click_gallery import AddAssetsToClickGallery
from elements_sdk.model.click_gallery import ClickGallery
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    id = "0" # str | 
    add_assets_to_click_gallery = AddAssetsToClickGallery(
        assets=[
            "assets_example",
        ],
    ) # AddAssetsToClickGallery | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_assets_to_click_gallery(connection_id, id, add_assets_to_click_gallery)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->add_assets_to_click_gallery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  |
 **id** | **str**|  |
 **add_assets_to_click_gallery** | [**AddAssetsToClickGallery**](AddAssetsToClickGallery.md)|  |

### Return type

[**ClickGallery**](ClickGallery.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **continue_click_upload_in_background**
> continue_click_upload_in_background(upload_id, click_background_upload_endpoint_request)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.click_background_upload_endpoint_request import ClickBackgroundUploadEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    upload_id = "upload_id_example" # str | 
    click_background_upload_endpoint_request = ClickBackgroundUploadEndpointRequest(
        gallery=1,
        links_to_send=[
            1,
        ],
        notify_on_completion=True,
    ) # ClickBackgroundUploadEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.continue_click_upload_in_background(upload_id, click_background_upload_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->continue_click_upload_in_background: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  |
 **click_background_upload_endpoint_request** | [**ClickBackgroundUploadEndpointRequest**](ClickBackgroundUploadEndpointRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_click_gallery**
> ClickGallery create_click_gallery(connection_id, click_gallery_update)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.click_gallery_update import ClickGalleryUpdate
from elements_sdk.model.click_gallery import ClickGallery
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    click_gallery_update = ClickGalleryUpdate(
        name="name_example",
        description="description_example",
    ) # ClickGalleryUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_click_gallery(connection_id, click_gallery_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->create_click_gallery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  |
 **click_gallery_update** | [**ClickGalleryUpdate**](ClickGalleryUpdate.md)|  |

### Return type

[**ClickGallery**](ClickGallery.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_click_gallery_link**
> ClickGalleryLink create_click_gallery_link(connection_id, click_gallery_link)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.click_gallery_link import ClickGalleryLink
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    click_gallery_link = ClickGalleryLink(
        id=1,
        email="email_example",
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        gallery_id=1,
        notify_on_use=True,
        views_left=1,
        elements_user=ClickLinkUser(
            id="id_example",
            username="username_example",
            email="email_example",
            display_name="display_name_example",
        ),
        secret_key="secret_key_example",
    ) # ClickGalleryLink | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_click_gallery_link(connection_id, click_gallery_link)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->create_click_gallery_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  |
 **click_gallery_link** | [**ClickGalleryLink**](ClickGalleryLink.md)|  |

### Return type

[**ClickGalleryLink**](ClickGalleryLink.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_click_gallery_link**
> delete_click_gallery_link(connection_id, id)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_click_gallery_link(connection_id, id)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->delete_click_gallery_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  |
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_click_galleries**
> [ClickGallery] get_all_click_galleries(connection_id)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.click_gallery import ClickGallery
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_click_galleries(connection_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->get_all_click_galleries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_click_galleries(connection_id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

[**[ClickGallery]**](ClickGallery.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_click_gallery_links**
> InlineResponse200 get_all_click_gallery_links(connection_id)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.inline_response200 import InlineResponse200
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_click_gallery_links(connection_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->get_all_click_gallery_links: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_click_gallery_links(connection_id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_click_gallery**
> ClickGallery get_click_gallery(connection_id, id)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.click_gallery import ClickGallery
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_click_gallery(connection_id, id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->get_click_gallery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  |
 **id** | **str**|  |

### Return type

[**ClickGallery**](ClickGallery.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_click_gallery_link**
> ClickGalleryLink get_click_gallery_link(connection_id, id)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.click_gallery_link import ClickGalleryLink
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    id = "0" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_click_gallery_link(connection_id, id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->get_click_gallery_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  |
 **id** | **str**|  |

### Return type

[**ClickGalleryLink**](ClickGalleryLink.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **send_click_gallery_link_email**
> send_click_gallery_link_email(connection_id, link_id)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    connection_id = "connection_id_example" # str | 
    link_id = "link_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.send_click_gallery_link_email(connection_id, link_id)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->send_click_gallery_link_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  |
 **link_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_click_upload**
> TaskInfo start_click_upload(click_start_upload_endpoint_request)



### Required permissions    * User account permission: `cloud:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import click_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.click_start_upload_endpoint_request import ClickStartUploadEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = click_api.ClickApi(api_client)
    click_start_upload_endpoint_request = ClickStartUploadEndpointRequest(
        connection=1,
        assets=[
            1,
        ],
    ) # ClickStartUploadEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_click_upload(click_start_upload_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling ClickApi->start_click_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **click_start_upload_endpoint_request** | [**ClickStartUploadEndpointRequest**](ClickStartUploadEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

