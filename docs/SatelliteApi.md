# elements_sdk.SatelliteApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_satellite_host**](SatelliteApi.md#activate_satellite_host) | **POST** `/api/2/rdc/hosts/{id}/activate` | 
[**announce_satellite_host**](SatelliteApi.md#announce_satellite_host) | **POST** `/api/2/rdc/hosts/announce` | 
[**create_satellite_session**](SatelliteApi.md#create_satellite_session) | **POST** `/api/2/rdc/sessions` | 
[**delete_satellite_session**](SatelliteApi.md#delete_satellite_session) | **DELETE** `/api/2/rdc/sessions/{id}` | 
[**get_all_satellite_hosts**](SatelliteApi.md#get_all_satellite_hosts) | **GET** `/api/2/rdc/hosts` | 
[**get_all_satellite_sessions**](SatelliteApi.md#get_all_satellite_sessions) | **GET** `/api/2/rdc/sessions` | 
[**get_satellite_host**](SatelliteApi.md#get_satellite_host) | **GET** `/api/2/rdc/hosts/{id}` | 
[**get_satellite_session**](SatelliteApi.md#get_satellite_session) | **GET** `/api/2/rdc/sessions/{id}` | 


# **activate_satellite_host**
    def RDCActivation activate_satellite_host(id)



### Required permissions    * User account permission: `rdc:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from elements_sdk.model.rdc_activation import RDCActivation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)
    id = 1 # int | A unique integer value identifying this Satellite host.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.activate_satellite_host(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->activate_satellite_host: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite host. |

### Return type

[**RDCActivation**](RDCActivation.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

# **announce_satellite_host**
    def RDCHost announce_satellite_host()



### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from elements_sdk.model.rdc_host import RDCHost
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.announce_satellite_host()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->announce_satellite_host: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RDCHost**](RDCHost.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

# **create_satellite_session**
    def RDCSession create_satellite_session(rdc_session_create)



### Required permissions    * License component: rdc 

### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from elements_sdk.model.rdc_session import RDCSession
from elements_sdk.model.rdc_session_create import RDCSessionCreate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)
    rdc_session_create = RDCSessionCreate(
        id=1,
        user=ElementsUserMiniReference(
            id=1,
        ),
    ) # RDCSessionCreate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_satellite_session(rdc_session_create)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->create_satellite_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdc_session_create** | [**RDCSessionCreate**](RDCSessionCreate.md)|  |

### Return type

[**RDCSession**](RDCSession.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

# **delete_satellite_session**
    def delete_satellite_session(id)



### Required permissions    * License component: rdc 

### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)
    id = 1 # int | A unique integer value identifying this Satellite session.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_satellite_session(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->delete_satellite_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite session. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

# **get_all_satellite_hosts**
    def [RDCHost] get_all_satellite_hosts()



### Required permissions    * User account permission: `rdc:access`   * License component: rdc 

### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from elements_sdk.model.rdc_host import RDCHost
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_satellite_hosts(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->get_all_satellite_hosts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[RDCHost]**](RDCHost.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

# **get_all_satellite_sessions**
    def [RDCSession] get_all_satellite_sessions()



### Required permissions    * License component: rdc 

### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from elements_sdk.model.rdc_session import RDCSession
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_satellite_sessions(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->get_all_satellite_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[RDCSession]**](RDCSession.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

# **get_satellite_host**
    def RDCHost get_satellite_host(id)



### Required permissions    * User account permission: `rdc:access`   * License component: rdc 

### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from elements_sdk.model.rdc_host import RDCHost
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)
    id = 1 # int | A unique integer value identifying this Satellite host.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_satellite_host(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->get_satellite_host: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite host. |

### Return type

[**RDCHost**](RDCHost.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

# **get_satellite_session**
    def RDCSession get_satellite_session(id)



### Required permissions    * License component: rdc 

### Example


```python
import elements_sdk
from elements_sdk.api import satellite_api
from elements_sdk.model.rdc_session import RDCSession
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = satellite_api.SatelliteApi(api_client)
    id = 1 # int | A unique integer value identifying this Satellite session.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_satellite_session(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SatelliteApi->get_satellite_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite session. |

### Return type

[**RDCSession**](RDCSession.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

