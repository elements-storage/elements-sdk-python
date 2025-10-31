# elements_sdk.StatusApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_alert**](StatusApi.md#acknowledge_alert) | **POST** `/api/2/alerts/{id}/acknowledge` | 
[**get_active_alerts**](StatusApi.md#get_active_alerts) | **GET** `/api/2/alerts/active` | 
[**get_alert**](StatusApi.md#get_alert) | **GET** `/api/2/alerts/{id}` | 
[**get_all_alerts**](StatusApi.md#get_all_alerts) | **GET** `/api/2/alerts` | 
[**get_telegraf_stats**](StatusApi.md#get_telegraf_stats) | **GET** `/api/2/telegraf-stats` | 
[**silence_alert**](StatusApi.md#silence_alert) | **POST** `/api/2/alerts/{id}/silence` | 
[**submit_kapacitor_alert**](StatusApi.md#submit_kapacitor_alert) | **POST** `/api/2/alerts/submit` | 


# **acknowledge_alert**
    def Alert acknowledge_alert(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import status_api
from elements_sdk.model.alert import Alert
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = status_api.StatusApi(api_client)
    id = 1 # int | A unique integer value identifying this alert.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.acknowledge_alert(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StatusApi->acknowledge_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this alert. |

### Return type

[**Alert**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_active_alerts**
    def [Alert] get_active_alerts()



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import status_api
from elements_sdk.model.alert import Alert
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = status_api.StatusApi(api_client)
    is_open = "is_open_example" # str | Filter the returned list by `is_open`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_active_alerts(is_open=is_open, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StatusApi->get_active_alerts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_open** | **str**| Filter the returned list by &#x60;is_open&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Alert]**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_alert**
    def Alert get_alert(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import status_api
from elements_sdk.model.alert import Alert
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = status_api.StatusApi(api_client)
    id = 1 # int | A unique integer value identifying this alert.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_alert(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StatusApi->get_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this alert. |

### Return type

[**Alert**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_alerts**
    def [Alert] get_all_alerts()



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import status_api
from elements_sdk.model.alert import Alert
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = status_api.StatusApi(api_client)
    is_open = "is_open_example" # str | Filter the returned list by `is_open`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_alerts(is_open=is_open, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StatusApi->get_all_alerts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_open** | **str**| Filter the returned list by &#x60;is_open&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Alert]**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_telegraf_stats**
    def get_telegraf_stats()



### Example


```python
import elements_sdk
from elements_sdk.api import status_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = status_api.StatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_telegraf_stats()
    except elements_sdk.ApiException as e:
        print("Exception when calling StatusApi->get_telegraf_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **silence_alert**
    def Alert silence_alert(id)



### Required permissions    * User account permission: `system:status:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import status_api
from elements_sdk.model.alert import Alert
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = status_api.StatusApi(api_client)
    id = 1 # int | A unique integer value identifying this alert.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.silence_alert(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling StatusApi->silence_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this alert. |

### Return type

[**Alert**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **submit_kapacitor_alert**
    def submit_kapacitor_alert(kapacitor_alert)



### Required permissions    * localhost only 

### Example


```python
import elements_sdk
from elements_sdk.api import status_api
from elements_sdk.model.kapacitor_alert import KapacitorAlert
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = status_api.StatusApi(api_client)
    kapacitor_alert = KapacitorAlert(
        id="id_example",
        level="level_example",
        message="message_example",
        details="details_example",
        data={
            "key": "key_example",
        },
    ) # KapacitorAlert | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.submit_kapacitor_alert(kapacitor_alert)
    except elements_sdk.ApiException as e:
        print("Exception when calling StatusApi->submit_kapacitor_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kapacitor_alert** | [**KapacitorAlert**](KapacitorAlert.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

