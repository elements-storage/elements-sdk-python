# elements_sdk.PrivateApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**export_non_proxied_assets**](PrivateApi.md#export_non_proxied_assets) | **GET** `/api/2/private/export/non-proxied/{root_id}` | 
[**export_non_proxied_assets_for_path**](PrivateApi.md#export_non_proxied_assets_for_path) | **GET** `/api/2/private/export/non-proxied/{root_id}/{path}` | 
[**export_updates**](PrivateApi.md#export_updates) | **GET** `/api/2/private/export/updates/{root_id}` | 
[**fast_lane_login_page**](PrivateApi.md#fast_lane_login_page) | **GET** `/auth/fast-lane/{token}` | 
[**fast_lane_login_with_password**](PrivateApi.md#fast_lane_login_with_password) | **POST** `/auth/fast-lane/{token}` | 
[**get**](PrivateApi.md#get) | **GET** `/api/2/private/bootstrap` | 
[**get_client_side_url**](PrivateApi.md#get_client_side_url) | **POST** `/api/2/private/client-side-url` | 
[**get_help_page**](PrivateApi.md#get_help_page) | **GET** `/api/2/help/{id}` | 
[**get_locale**](PrivateApi.md#get_locale) | **GET** `/api/2/private/locale/{lang}` | 
[**get_proxy_fs_size**](PrivateApi.md#get_proxy_fs_size) | **GET** `/api/2/private/media/proxyfs-size` | 
[**get_stored_image**](PrivateApi.md#get_stored_image) | **GET** `/api/2/image/{name}` | 
[**install_license**](PrivateApi.md#install_license) | **POST** `/api/2/license/install` | 
[**language_server_request**](PrivateApi.md#language_server_request) | **POST** `/api/2/language-server/{language}` | 
[**locate_file**](PrivateApi.md#locate_file) | **POST** `/api/2/private/locate` | 
[**locate_markers**](PrivateApi.md#locate_markers) | **POST** `/api/2/panel/locate-markers` | 
[**locate_proxies**](PrivateApi.md#locate_proxies) | **POST** `/api/2/panel/locate-proxies` | 
[**start_benchmark_session**](PrivateApi.md#start_benchmark_session) | **POST** `/api/2/private/benchmark` | 
[**submit_node_status**](PrivateApi.md#submit_node_status) | **POST** `/api/2/private/node-stats` | 


# **export_non_proxied_assets**
    def export_non_proxied_assets(root_id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_non_proxied_assets_for_path**
    def export_non_proxied_assets_for_path(path, root_id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_updates**
    def export_updates(root_id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **fast_lane_login_page**
    def AuthFastLaneEndpointResponse fast_lane_login_page(token)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.auth_fast_lane_endpoint_response import AuthFastLaneEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = private_api.PrivateApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fast_lane_login_page(token)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->fast_lane_login_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

[**AuthFastLaneEndpointResponse**](AuthFastLaneEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **fast_lane_login_with_password**
    def AuthFastLaneEndpointResponse fast_lane_login_with_password(token, auth_fast_lane_endpoint_request)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.auth_fast_lane_endpoint_response import AuthFastLaneEndpointResponse
from elements_sdk.model.auth_fast_lane_endpoint_request import AuthFastLaneEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = private_api.PrivateApi(api_client)
    token = "token_example" # str | 
    auth_fast_lane_endpoint_request = AuthFastLaneEndpointRequest(
        password="password_example",
    ) # AuthFastLaneEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fast_lane_login_with_password(token, auth_fast_lane_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->fast_lane_login_with_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |
 **auth_fast_lane_endpoint_request** | [**AuthFastLaneEndpointRequest**](AuthFastLaneEndpointRequest.md)|  |

### Return type

[**AuthFastLaneEndpointResponse**](AuthFastLaneEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get**
    def BootstrapData get()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.bootstrap_data import BootstrapData
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_client_side_url**
    def ClientSidePathEndpointResponse get_client_side_url(client_side_path_endpoint_request)



### Required permissions    * User account permission: `client:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.client_side_path_endpoint_request import ClientSidePathEndpointRequest
from elements_sdk.model.client_side_path_endpoint_response import ClientSidePathEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_help_page**
    def HelpEndpointResponse get_help_page(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.help_endpoint_response import HelpEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_locale**
    def LocaleEndpointResponse get_locale(lang)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.locale_endpoint_response import LocaleEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy_fs_size**
    def ProxyFSSizeEndpointResponse get_proxy_fs_size()



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.proxy_fs_size_endpoint_response import ProxyFSSizeEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_stored_image**
    def get_stored_image(name)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **install_license**
    def install_license(install_license_endpoint_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.install_license_endpoint_request import InstallLicenseEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **language_server_request**
    def {str: (bool, date, datetime, dict, float, int, list, str, none_type)} language_server_request(language)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **locate_file**
    def LocateResult locate_file(locate_endpoint_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.locate_result import LocateResult
from elements_sdk.model.locate_endpoint_request import LocateEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **locate_markers**
    def [LocateMarkersEndpointResponse] locate_markers(locate_markers_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.locate_markers_endpoint_response import LocateMarkersEndpointResponse
from elements_sdk.model.locate_markers_endpoint_request import LocateMarkersEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = private_api.PrivateApi(api_client)
    locate_markers_endpoint_request = LocateMarkersEndpointRequest(
        paths=[
            "paths_example",
        ],
    ) # LocateMarkersEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.locate_markers(locate_markers_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->locate_markers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locate_markers_endpoint_request** | [**LocateMarkersEndpointRequest**](LocateMarkersEndpointRequest.md)|  |

### Return type

[**[LocateMarkersEndpointResponse]**](LocateMarkersEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **locate_proxies**
    def [LocateProxiesEndpointResponse] locate_proxies(locate_proxies_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.locate_proxies_endpoint_request import LocateProxiesEndpointRequest
from elements_sdk.model.locate_proxies_endpoint_response import LocateProxiesEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = private_api.PrivateApi(api_client)
    locate_proxies_endpoint_request = LocateProxiesEndpointRequest(
        paths=[
            "paths_example",
        ],
    ) # LocateProxiesEndpointRequest | 
    for_root = 1 # int |  (optional)
    include_proxies = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.locate_proxies(locate_proxies_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->locate_proxies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.locate_proxies(locate_proxies_endpoint_request, for_root=for_root, include_proxies=include_proxies)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->locate_proxies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locate_proxies_endpoint_request** | [**LocateProxiesEndpointRequest**](LocateProxiesEndpointRequest.md)|  |
 **for_root** | **int**|  | [optional]
 **include_proxies** | **bool**|  | [optional]

### Return type

[**[LocateProxiesEndpointResponse]**](LocateProxiesEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_benchmark_session**
    def TaskInfo start_benchmark_session(benchmark_endpoint_request)



### Required permissions    * User account permission: `client:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.benchmark_endpoint_request import BenchmarkEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = private_api.PrivateApi(api_client)
    benchmark_endpoint_request = BenchmarkEndpointRequest(
        node=StorageNodeReference(
            id=1,
            backend=Backend(
                name="name_example",
                properties=BackendProperties(
                    supports_sharing_rw_permissions_priority=True,
                    supports_sharing_afp=True,
                    supports_sharing_smb_require_logon=True,
                    supports_sharing_smb_recycle_bin=True,
                    supports_sharing_smb_xattrs=True,
                    supports_sharing_smb_symlinks=True,
                    supports_sharing_smb_custom_options=True,
                    supports_sharing_nfs_permissions=True,
                ),
            ),
            status=StorageNodeStatus(
                online=True,
                report={
                    "key": "key_example",
                },
                ha_online=True,
                ha_status="ha_status_example",
                ha_ips=[
                    "ha_ips_example",
                ],
            ),
        ),
    ) # BenchmarkEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_benchmark_session(benchmark_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->start_benchmark_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **benchmark_endpoint_request** | [**BenchmarkEndpointRequest**](BenchmarkEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **submit_node_status**
    def submit_node_status()



### Required permissions    * localhost only 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = private_api.PrivateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.submit_node_status()
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->submit_node_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

