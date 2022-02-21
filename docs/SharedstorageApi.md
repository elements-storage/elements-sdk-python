# elements_sdk.SharedstorageApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shared_storage_value**](SharedstorageApi.md#get_shared_storage_value) | **GET** `/api/2/private/shared-storage/{name}` | 
[**get_user_storage_value**](SharedstorageApi.md#get_user_storage_value) | **GET** `/api/2/private/user-storage/{name}` | 
[**set_shared_storage_value**](SharedstorageApi.md#set_shared_storage_value) | **POST** `/api/2/private/shared-storage/{name}` | 
[**set_user_storage_value**](SharedstorageApi.md#set_user_storage_value) | **POST** `/api/2/private/user-storage/{name}` | 


# **get_shared_storage_value**
    def StorageResponse get_shared_storage_value(name)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import sharedstorage_api
from elements_sdk.model.storage_response import StorageResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = sharedstorage_api.SharedstorageApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_shared_storage_value(name)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SharedstorageApi->get_shared_storage_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**StorageResponse**](StorageResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_user_storage_value**
    def StorageResponse get_user_storage_value(name)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import sharedstorage_api
from elements_sdk.model.storage_response import StorageResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = sharedstorage_api.SharedstorageApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_storage_value(name)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SharedstorageApi->get_user_storage_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**StorageResponse**](StorageResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **set_shared_storage_value**
    def StorageResponse set_shared_storage_value(name, storage_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import sharedstorage_api
from elements_sdk.model.storage_request import StorageRequest
from elements_sdk.model.storage_response import StorageResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = sharedstorage_api.SharedstorageApi(api_client)
    name = "name_example" # str | 
    storage_request = StorageRequest(
        value="value_example",
        initiator="initiator_example",
    ) # StorageRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_shared_storage_value(name, storage_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SharedstorageApi->set_shared_storage_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **storage_request** | [**StorageRequest**](StorageRequest.md)|  |

### Return type

[**StorageResponse**](StorageResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **set_user_storage_value**
    def StorageResponse set_user_storage_value(name, storage_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import sharedstorage_api
from elements_sdk.model.storage_request import StorageRequest
from elements_sdk.model.storage_response import StorageResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = sharedstorage_api.SharedstorageApi(api_client)
    name = "name_example" # str | 
    storage_request = StorageRequest(
        value="value_example",
        initiator="initiator_example",
    ) # StorageRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_user_storage_value(name, storage_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling SharedstorageApi->set_user_storage_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **storage_request** | [**StorageRequest**](StorageRequest.md)|  |

### Return type

[**StorageResponse**](StorageResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

