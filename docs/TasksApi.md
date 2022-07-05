# elements_sdk.TasksApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**get_python_environments**](TasksApi.md#get_python_environments) | **GET** `/api/2/python/environments` | 



***

# **get_python_environments**

    def get_python_environments() -> list[PythonEnvironment] 



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
    api_instance = elements_sdk.TasksApi(api_client)
    
    try:
        api_response = api_instance.get_python_environments()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_python_environments: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**list[PythonEnvironment]**](PythonEnvironment.md)

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

