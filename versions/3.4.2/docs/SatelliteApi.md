# elements_sdk.SatelliteApi

All URIs are relative to *https://elements.local*
>
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



***

# **activate_satellite_host**

    def activate_satellite_host(id) -> RDCActivation 



### Required permissions    * User account permission: `rdc:access` 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    id = 56 # int | A unique integer value identifying this Satellite host.

    try:
        api_response = api_instance.activate_satellite_host(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteApi->activate_satellite_host: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite host. | 

### Return type

[**RDCActivation**](RDCActivation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **announce_satellite_host**

    def announce_satellite_host() -> RDCHost 



### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    
    try:
        api_response = api_instance.announce_satellite_host()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteApi->announce_satellite_host: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**RDCHost**](RDCHost.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_satellite_session**

    def create_satellite_session(rdc_session_create) -> RDCSession 



### Required permissions    * License component: rdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    rdc_session_create = elements_sdk.RDCSessionCreate() # RDCSessionCreate | 

    try:
        api_response = api_instance.create_satellite_session(rdc_session_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteApi->create_satellite_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdc_session_create** | [**RDCSessionCreate**](RDCSessionCreate.md)|  | 

### Return type

[**RDCSession**](RDCSession.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_satellite_session**

    def delete_satellite_session(id)



### Required permissions    * License component: rdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    id = 56 # int | A unique integer value identifying this Satellite session.

    try:
        api_instance.delete_satellite_session(id)
    except ApiException as e:
        print("Exception when calling SatelliteApi->delete_satellite_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite session. | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_satellite_hosts**

    def get_all_satellite_hosts(ordering=ordering, limit=limit, offset=offset) -> list[RDCHost] 



### Required permissions    * User account permission: `rdc:access`   * License component: rdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_satellite_hosts(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteApi->get_all_satellite_hosts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[RDCHost]**](RDCHost.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_satellite_sessions**

    def get_all_satellite_sessions(ordering=ordering, limit=limit, offset=offset) -> list[RDCSession] 



### Required permissions    * License component: rdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_satellite_sessions(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteApi->get_all_satellite_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[RDCSession]**](RDCSession.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_satellite_host**

    def get_satellite_host(id) -> RDCHost 



### Required permissions    * User account permission: `rdc:access`   * License component: rdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    id = 56 # int | A unique integer value identifying this Satellite host.

    try:
        api_response = api_instance.get_satellite_host(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteApi->get_satellite_host: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite host. | 

### Return type

[**RDCHost**](RDCHost.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_satellite_session**

    def get_satellite_session(id) -> RDCSession 



### Required permissions    * License component: rdc 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.SatelliteApi(api_client)
    id = 56 # int | A unique integer value identifying this Satellite session.

    try:
        api_response = api_instance.get_satellite_session(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SatelliteApi->get_satellite_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Satellite session. | 

### Return type

[**RDCSession**](RDCSession.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

