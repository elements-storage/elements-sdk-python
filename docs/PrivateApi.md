# elements_sdk.PrivateApi

All URIs are relative to *https://elements.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stored_image**](PrivateApi.md#delete_stored_image) | **DELETE** `/api/2/image/{name}` | 
[**delete_veritone_tdo**](PrivateApi.md#delete_veritone_tdo) | **DELETE** `/api/2/veritone/connections/{id}/tdo/{tdo_id}` | 
[**export_non_proxied_assets**](PrivateApi.md#export_non_proxied_assets) | **GET** `/api/2/private/export/non-proxied/{root_id}` | 
[**export_non_proxied_assets_for_path**](PrivateApi.md#export_non_proxied_assets_for_path) | **GET** `/api/2/private/export/non-proxied/{root_id}/{path}` | 
[**export_updates**](PrivateApi.md#export_updates) | **GET** `/api/2/private/export/updates/{root_id}` | 
[**get**](PrivateApi.md#get) | **GET** `/api/2/private/bootstrap` | 
[**get_all_veritone_connections**](PrivateApi.md#get_all_veritone_connections) | **GET** `/api/2/veritone/connections` | 
[**get_all_veritone_metadata**](PrivateApi.md#get_all_veritone_metadata) | **GET** `/api/2/veritone/metadata` | 
[**get_client_side_url**](PrivateApi.md#get_client_side_url) | **POST** `/api/2/private/client-side-url` | 
[**get_help_page**](PrivateApi.md#get_help_page) | **GET** `/api/2/help/{id}` | 
[**get_locale**](PrivateApi.md#get_locale) | **GET** `/api/2/private/locale/{lang}` | 
[**get_proxy_fs_size**](PrivateApi.md#get_proxy_fs_size) | **GET** `/api/2/private/media/proxyfs-size` | 
[**get_stored_image**](PrivateApi.md#get_stored_image) | **GET** `/api/2/image/{name}` | 
[**get_veritone_connection**](PrivateApi.md#get_veritone_connection) | **GET** `/api/2/veritone/connections/{id}` | 
[**get_veritone_engines**](PrivateApi.md#get_veritone_engines) | **GET** `/api/2/veritone/connections/{id}/engines` | 
[**get_veritone_jobs**](PrivateApi.md#get_veritone_jobs) | **GET** `/api/2/veritone/connections/{id}/jobs` | 
[**get_veritone_metadata**](PrivateApi.md#get_veritone_metadata) | **GET** `/api/2/veritone/metadata/{id}` | 
[**install_license**](PrivateApi.md#install_license) | **POST** `/api/2/license/install` | 
[**language_server_request**](PrivateApi.md#language_server_request) | **POST** `/api/2/language-server/{language}` | 
[**locate_file**](PrivateApi.md#locate_file) | **POST** `/api/2/private/locate` | 
[**locate_proxies**](PrivateApi.md#locate_proxies) | **POST** `/api/2/panel/locate-proxies` | 
[**upload_stored_image**](PrivateApi.md#upload_stored_image) | **POST** `/api/2/private/images/upload` | 
[**upload_to_veritone**](PrivateApi.md#upload_to_veritone) | **POST** `/api/2/veritone/connections/{id}/upload` | 


# **delete_stored_image**
> delete_stored_image(name)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
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
    api_instance = private_api.PrivateApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_stored_image(name)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->delete_stored_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_veritone_tdo**
> delete_veritone_tdo(id, tdo_id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
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
    api_instance = private_api.PrivateApi(api_client)
    id = 1 # int | A unique integer value identifying this Veritone connection.
    tdo_id = "tdo_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_veritone_tdo(id, tdo_id)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->delete_veritone_tdo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Veritone connection. |
 **tdo_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_non_proxied_assets**
> export_non_proxied_assets(root_id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
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
    api_instance = private_api.PrivateApi(api_client)
    root_id = "root_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.export_non_proxied_assets(root_id)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->export_non_proxied_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_non_proxied_assets_for_path**
> export_non_proxied_assets_for_path(path, root_id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
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
    api_instance = private_api.PrivateApi(api_client)
    path = "path_example" # str | 
    root_id = "root_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.export_non_proxied_assets_for_path(path, root_id)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->export_non_proxied_assets_for_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **root_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_updates**
> export_updates(root_id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
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
    api_instance = private_api.PrivateApi(api_client)
    root_id = "root_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.export_updates(root_id)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->export_updates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get**
> BootstrapData get()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.bootstrap_data import BootstrapData
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
    api_instance = private_api.PrivateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BootstrapData**](BootstrapData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_veritone_connections**
> [VeritoneConnection] get_all_veritone_connections()



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.veritone_connection import VeritoneConnection
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
    api_instance = private_api.PrivateApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_veritone_connections(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_all_veritone_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[VeritoneConnection]**](VeritoneConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_veritone_metadata**
> [VeritoneMetadata] get_all_veritone_metadata()



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.veritone_metadata import VeritoneMetadata
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
    api_instance = private_api.PrivateApi(api_client)
    asset = 3.14 # float | Filter the returned list by `asset`. (optional)
    is_parsed = "is_parsed_example" # str | Filter the returned list by `is_parsed`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_veritone_metadata(asset=asset, is_parsed=is_parsed, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_all_veritone_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **float**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **is_parsed** | **str**| Filter the returned list by &#x60;is_parsed&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[VeritoneMetadata]**](VeritoneMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_client_side_url**
> ClientSidePathEndpointResponse get_client_side_url(client_side_path_endpoint_request)



### Required permissions    * User account permission: `client:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.client_side_path_endpoint_request import ClientSidePathEndpointRequest
from elements_sdk.model.client_side_path_endpoint_response import ClientSidePathEndpointResponse
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
    api_instance = private_api.PrivateApi(api_client)
    client_side_path_endpoint_request = ClientSidePathEndpointRequest(
        server_side_path="server_side_path_example",
        platform="platform_example",
    ) # ClientSidePathEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_client_side_url(client_side_path_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_client_side_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_side_path_endpoint_request** | [**ClientSidePathEndpointRequest**](ClientSidePathEndpointRequest.md)|  |

### Return type

[**ClientSidePathEndpointResponse**](ClientSidePathEndpointResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_help_page**
> HelpEndpointResponse get_help_page(id)



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.help_endpoint_response import HelpEndpointResponse
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
    api_instance = private_api.PrivateApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_help_page(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_help_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**HelpEndpointResponse**](HelpEndpointResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_locale**
> LocaleEndpointResponse get_locale(lang)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.locale_endpoint_response import LocaleEndpointResponse
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
    api_instance = private_api.PrivateApi(api_client)
    lang = "lang_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_locale(lang)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_locale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**|  |

### Return type

[**LocaleEndpointResponse**](LocaleEndpointResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy_fs_size**
> ProxyFSSizeEndpointResponse get_proxy_fs_size()



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.proxy_fs_size_endpoint_response import ProxyFSSizeEndpointResponse
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
    api_instance = private_api.PrivateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_proxy_fs_size()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_proxy_fs_size: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProxyFSSizeEndpointResponse**](ProxyFSSizeEndpointResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_stored_image**
> get_stored_image(name)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
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
    api_instance = private_api.PrivateApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_stored_image(name)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_stored_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_veritone_connection**
> VeritoneConnection get_veritone_connection(id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.veritone_connection import VeritoneConnection
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
    api_instance = private_api.PrivateApi(api_client)
    id = 1 # int | A unique integer value identifying this Veritone connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_veritone_connection(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_veritone_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Veritone connection. |

### Return type

[**VeritoneConnection**](VeritoneConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_veritone_engines**
> VeritoneEngineList get_veritone_engines(id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.veritone_engine_list import VeritoneEngineList
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
    api_instance = private_api.PrivateApi(api_client)
    id = 1 # int | A unique integer value identifying this Veritone connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_veritone_engines(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_veritone_engines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Veritone connection. |

### Return type

[**VeritoneEngineList**](VeritoneEngineList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_veritone_jobs**
> VeritoneJobList get_veritone_jobs(id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.veritone_job_list import VeritoneJobList
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
    api_instance = private_api.PrivateApi(api_client)
    id = 1 # int | A unique integer value identifying this Veritone connection.
    offset = 1 # int |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_veritone_jobs(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_veritone_jobs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_veritone_jobs(id, offset=offset, limit=limit)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_veritone_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Veritone connection. |
 **offset** | **int**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**VeritoneJobList**](VeritoneJobList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_veritone_metadata**
> VeritoneMetadata get_veritone_metadata(id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.veritone_metadata import VeritoneMetadata
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
    api_instance = private_api.PrivateApi(api_client)
    id = 1 # int | A unique integer value identifying this Veritone metadata.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_veritone_metadata(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_veritone_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Veritone metadata. |

### Return type

[**VeritoneMetadata**](VeritoneMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **install_license**
> install_license(install_license_endpoint_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.install_license_endpoint_request import InstallLicenseEndpointRequest
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
    api_instance = private_api.PrivateApi(api_client)
    install_license_endpoint_request = InstallLicenseEndpointRequest(
        license="license_example",
        signature="signature_example",
    ) # InstallLicenseEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.install_license(install_license_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->install_license: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_license_endpoint_request** | [**InstallLicenseEndpointRequest**](InstallLicenseEndpointRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **language_server_request**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} language_server_request(language)



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
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
    api_instance = private_api.PrivateApi(api_client)
    language = "language_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.language_server_request(language)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->language_server_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **locate_file**
> LocateResult locate_file(locate_endpoint_request)



### Required permissions    * Authenticated user 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.locate_result import LocateResult
from elements_sdk.model.locate_endpoint_request import LocateEndpointRequest
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
    api_instance = private_api.PrivateApi(api_client)
    locate_endpoint_request = LocateEndpointRequest(
        path="path_example",
        asset=1,
    ) # LocateEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.locate_file(locate_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->locate_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locate_endpoint_request** | [**LocateEndpointRequest**](LocateEndpointRequest.md)|  |

### Return type

[**LocateResult**](LocateResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **locate_proxies**
> [LocateProxiesEndpointResponse] locate_proxies(locate_proxies_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.locate_proxies_endpoint_request import LocateProxiesEndpointRequest
from elements_sdk.model.locate_proxies_endpoint_response import LocateProxiesEndpointResponse
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
    api_instance = private_api.PrivateApi(api_client)
    locate_proxies_endpoint_request = LocateProxiesEndpointRequest(
        paths=[
            "paths_example",
        ],
    ) # LocateProxiesEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.locate_proxies(locate_proxies_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->locate_proxies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locate_proxies_endpoint_request** | [**LocateProxiesEndpointRequest**](LocateProxiesEndpointRequest.md)|  |

### Return type

[**[LocateProxiesEndpointResponse]**](LocateProxiesEndpointResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **upload_stored_image**
> upload_stored_image(upload_image_endpoint_request)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.upload_image_endpoint_request import UploadImageEndpointRequest
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
    api_instance = private_api.PrivateApi(api_client)
    upload_image_endpoint_request = UploadImageEndpointRequest(
        name="name_example",
        data="data_example",
    ) # UploadImageEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.upload_stored_image(upload_image_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->upload_stored_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_image_endpoint_request** | [**UploadImageEndpointRequest**](UploadImageEndpointRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **upload_to_veritone**
> upload_to_veritone(id, veritone_upload_request)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.veritone_upload_request import VeritoneUploadRequest
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
    api_instance = private_api.PrivateApi(api_client)
    id = 1 # int | A unique integer value identifying this Veritone connection.
    veritone_upload_request = VeritoneUploadRequest(
        root=1,
        file=1,
        bundle=1,
    ) # VeritoneUploadRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.upload_to_veritone(id, veritone_upload_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->upload_to_veritone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Veritone connection. |
 **veritone_upload_request** | [**VeritoneUploadRequest**](VeritoneUploadRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

