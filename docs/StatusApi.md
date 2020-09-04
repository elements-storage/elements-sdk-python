# elements_sdk.StatusApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert**](StatusApi.md#get_alert) | **GET** `/api/2/alerts/{id}` | 
[**get_all_alerts**](StatusApi.md#get_all_alerts) | **GET** `/api/2/alerts` | 
[**patch_alert**](StatusApi.md#patch_alert) | **PATCH** `/api/2/alerts/{id}` | 
[**update_alert**](StatusApi.md#update_alert) | **PUT** `/api/2/alerts/{id}` | 



***

# **get_alert**
> Alert get_alert(id)



### Required permissions   * User account permission: system:status:view 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StatusApi(api_client)
    id = 56 # int | A unique integer value identifying this alert.

    try:
        api_response = api_instance.get_alert(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this alert. | 

### Return type

[**Alert**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_alerts**
> list[Alert] get_all_alerts(is_open=is_open, id=id, ordering=ordering, limit=limit, offset=offset)



### Required permissions   * User account permission: system:status:view 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StatusApi(api_client)
    is_open = 'is_open_example' # str | Filter the returned list by `is_open`. (optional)
id = 3.4 # float | Filter the returned list by `id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_alerts(is_open=is_open, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_all_alerts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_open** | **str**| Filter the returned list by &#x60;is_open&#x60;. | [optional] 
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Alert]**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_alert**
> Alert patch_alert(id, data)



### Required permissions   * User account permission: system:status:view 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StatusApi(api_client)
    id = 56 # int | A unique integer value identifying this alert.
data = elements_sdk.Alert() # Alert | 

    try:
        api_response = api_instance.patch_alert(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->patch_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this alert. | 
 **data** | [**Alert**](Alert.md)|  | 

### Return type

[**Alert**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_alert**
> Alert update_alert(id, data)



### Required permissions   * User account permission: system:status:view 

### Example

* Api Key Authentication (Bearer):

```python
import elements_sdk
from elements_sdk.rest import ApiException
from pprint import pprint

configuration = elements_sdk.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

configuration.host = "https://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.StatusApi(api_client)
    id = 56 # int | A unique integer value identifying this alert.
data = elements_sdk.Alert() # Alert | 

    try:
        api_response = api_instance.update_alert(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->update_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this alert. | 
 **data** | [**Alert**](Alert.md)|  | 

### Return type

[**Alert**](Alert.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

