# elements_sdk.PrivateApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**create_qumulo_integration**](PrivateApi.md#create_qumulo_integration) | **POST** `/api/2/private/qumulo-integrations` | 
[**delete_qumulo_integration**](PrivateApi.md#delete_qumulo_integration) | **DELETE** `/api/2/private/qumulo-integrations/{id}` | 
[**export_non_proxied_assets**](PrivateApi.md#export_non_proxied_assets) | **GET** `/api/2/private/export/non-proxied/{root_id}` | 
[**export_non_proxied_assets_for_path**](PrivateApi.md#export_non_proxied_assets_for_path) | **GET** `/api/2/private/export/non-proxied/{root_id}/{path}` | 
[**export_updates**](PrivateApi.md#export_updates) | **GET** `/api/2/private/export/updates/{root_id}` | 
[**fast_lane_login_page**](PrivateApi.md#fast_lane_login_page) | **GET** `/auth/fast-lane/{token}` | 
[**fast_lane_login_with_password**](PrivateApi.md#fast_lane_login_with_password) | **POST** `/auth/fast-lane/{token}` | 
[**get**](PrivateApi.md#get) | **GET** `/api/2/private/bootstrap` | 
[**get_agent_auth_token**](PrivateApi.md#get_agent_auth_token) | **GET** `/api/2/private/elements-agent-auth` | 
[**get_all_qumulo_integrations**](PrivateApi.md#get_all_qumulo_integrations) | **GET** `/api/2/private/qumulo-integrations` | 
[**get_client_side_url**](PrivateApi.md#get_client_side_url) | **POST** `/api/2/private/client-side-url` | 
[**get_help_page**](PrivateApi.md#get_help_page) | **GET** `/api/2/help/{id}` | 
[**get_locale**](PrivateApi.md#get_locale) | **GET** `/api/2/private/locale/{lang}` | 
[**get_proxy_fs_size**](PrivateApi.md#get_proxy_fs_size) | **GET** `/api/2/private/media/proxyfs-size` | 
[**get_qumulo_integration**](PrivateApi.md#get_qumulo_integration) | **GET** `/api/2/private/qumulo-integrations/{id}` | 
[**get_samba_dfree_string**](PrivateApi.md#get_samba_dfree_string) | **POST** `/api/2/private/dfree` | 
[**get_stored_image**](PrivateApi.md#get_stored_image) | **GET** `/api/2/image/{name}` | 
[**install_license**](PrivateApi.md#install_license) | **POST** `/api/2/license/install` | 
[**language_server_request**](PrivateApi.md#language_server_request) | **POST** `/api/2/language-server/{language}` | 
[**locate_file**](PrivateApi.md#locate_file) | **POST** `/api/2/private/locate` | 
[**locate_markers**](PrivateApi.md#locate_markers) | **POST** `/api/2/panel/locate-markers` | 
[**locate_proxies**](PrivateApi.md#locate_proxies) | **POST** `/api/2/panel/locate-proxies` | 
[**lookup_upload_folder_by_path**](PrivateApi.md#lookup_upload_folder_by_path) | **GET** `/api/2/private/media/lookup-upload-folder` | 
[**patch_qumulo_integration**](PrivateApi.md#patch_qumulo_integration) | **PATCH** `/api/2/private/qumulo-integrations/{id}` | 
[**start_benchmark_session**](PrivateApi.md#start_benchmark_session) | **POST** `/api/2/private/benchmark` | 
[**submit_node_status**](PrivateApi.md#submit_node_status) | **POST** `/api/2/private/node-stats` | 
[**update_qumulo_integration**](PrivateApi.md#update_qumulo_integration) | **PUT** `/api/2/private/qumulo-integrations/{id}` | 


# **create_qumulo_integration**
    def QumuloIntegration create_qumulo_integration(qumulo_integration_update)



### Required permissions    * User account permission: `system:admin-access`   * License component: qumulo 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.qumulo_integration_update import QumuloIntegrationUpdate
from elements_sdk.model.qumulo_integration import QumuloIntegration
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
    qumulo_integration_update = QumuloIntegrationUpdate(
        known_addresses=[
            "known_addresses_example",
        ],
        name="name_example",
        address="address_example",
        username="username_example",
        password="password_example",
        address_override="address_override_example",
    ) # QumuloIntegrationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_qumulo_integration(qumulo_integration_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->create_qumulo_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qumulo_integration_update** | [**QumuloIntegrationUpdate**](QumuloIntegrationUpdate.md)|  |

### Return type

[**QumuloIntegration**](QumuloIntegration.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_qumulo_integration**
    def delete_qumulo_integration(id)



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
    id = 1 # int | A unique integer value identifying this qumulo integration.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_qumulo_integration(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->delete_qumulo_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this qumulo integration. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

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

# **get_agent_auth_token**
    def get_agent_auth_token()



### Required permissions    * only for the ELEMENTS Agent 

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
        api_instance.get_agent_auth_token()
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_agent_auth_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_qumulo_integrations**
    def [QumuloIntegration] get_all_qumulo_integrations()



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.qumulo_integration import QumuloIntegration
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
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_qumulo_integrations(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_all_qumulo_integrations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[QumuloIntegration]**](QumuloIntegration.md)

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

# **get_qumulo_integration**
    def QumuloIntegration get_qumulo_integration(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.qumulo_integration import QumuloIntegration
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
    id = 1 # int | A unique integer value identifying this qumulo integration.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_qumulo_integration(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_qumulo_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this qumulo integration. |

### Return type

[**QumuloIntegration**](QumuloIntegration.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_samba_dfree_string**
    def get_samba_dfree_string()



### Required permissions    * only for the ELEMENTS Agent 

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
        api_instance.get_samba_dfree_string()
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->get_samba_dfree_string: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

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

# **lookup_upload_folder_by_path**
    def MediaFile lookup_upload_folder_by_path()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.media_file import MediaFile
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
    path = "path_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.lookup_upload_folder_by_path(path=path)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->lookup_upload_folder_by_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional]

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_qumulo_integration**
    def QumuloIntegration patch_qumulo_integration(id, qumulo_integration_partial_update)



### Required permissions    * User account permission: `system:admin-access`   * License component: qumulo 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.qumulo_integration import QumuloIntegration
from elements_sdk.model.qumulo_integration_partial_update import QumuloIntegrationPartialUpdate
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
    id = 1 # int | A unique integer value identifying this qumulo integration.
    qumulo_integration_partial_update = QumuloIntegrationPartialUpdate(
        known_addresses=[
            "known_addresses_example",
        ],
        name="name_example",
        address="address_example",
        username="username_example",
        password="password_example",
        address_override="address_override_example",
    ) # QumuloIntegrationPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_qumulo_integration(id, qumulo_integration_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->patch_qumulo_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this qumulo integration. |
 **qumulo_integration_partial_update** | [**QumuloIntegrationPartialUpdate**](QumuloIntegrationPartialUpdate.md)|  |

### Return type

[**QumuloIntegration**](QumuloIntegration.md)

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
        node=StorageNode(
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
                    supports_sharing_smb_allow_execute=True,
                    supports_sharing_smb_locking_options=True,
                    supports_sharing_smb_hidden=True,
                    supports_sharing_nfs_permissions=True,
                ),
            ),
            status=StorageNodeStatus(
                online=True,
                report={},
                ha_online=True,
                ha_status="ha_status_example",
                ha_ips=[
                    "ha_ips_example",
                ],
            ),
            task_queues=[
                "media",
            ],
            unique_id="unique_id_example",
            name="name_example",
            address="address_example",
            ipmi=1,
            ipmi_address="ipmi_address_example",
            ipmi_username="ipmi_username_example",
            ipmi_password="ipmi_password_example",
            proxy_queue=True,
            email_queue=True,
            apply_configuration_queue=True,
            solr_indexer_enabled=True,
            discovery_enabled=True,
            discovery_address_override="discovery_address_override_example",
            ntp_enabled=True,
            type=1,
            allow_root_login=True,
            permission_mask="permission_mask_example",
            address_override="address_override_example",
            auto_scan_interfaces=True,
            onefs_host="onefs_host_example",
            onefs_username="onefs_username_example",
            onefs_password="onefs_password_example",
            onefs_zone="onefs_zone_example",
            volume_queues=[
                1,
            ],
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



### Required permissions    * only for the ELEMENTS Agent 

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

# **update_qumulo_integration**
    def QumuloIntegration update_qumulo_integration(id, qumulo_integration_update)



### Required permissions    * User account permission: `system:admin-access`   * License component: qumulo 

### Example


```python
import elements_sdk
from elements_sdk.api import private_api
from elements_sdk.model.qumulo_integration_update import QumuloIntegrationUpdate
from elements_sdk.model.qumulo_integration import QumuloIntegration
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
    id = 1 # int | A unique integer value identifying this qumulo integration.
    qumulo_integration_update = QumuloIntegrationUpdate(
        known_addresses=[
            "known_addresses_example",
        ],
        name="name_example",
        address="address_example",
        username="username_example",
        password="password_example",
        address_override="address_override_example",
    ) # QumuloIntegrationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_qumulo_integration(id, qumulo_integration_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling PrivateApi->update_qumulo_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this qumulo integration. |
 **qumulo_integration_update** | [**QumuloIntegrationUpdate**](QumuloIntegrationUpdate.md)|  |

### Return type

[**QumuloIntegration**](QumuloIntegration.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

