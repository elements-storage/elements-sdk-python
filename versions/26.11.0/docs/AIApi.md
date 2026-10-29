# elements_sdk.AIApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_metadata**](AIApi.md#get_ai_metadata) | **GET** `/api/2/ai/metadata/{id}` | 
[**get_all_ai_metadata**](AIApi.md#get_all_ai_metadata) | **GET** `/api/2/ai/metadata` | 


# **get_ai_metadata**
    def AIMetadata get_ai_metadata(id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_metadata import AIMetadata
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = ai_api.AIApi(api_client)
    id = 1 # int | A unique integer value identifying this AI Metadata.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_metadata(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AI Metadata. |

### Return type

[**AIMetadata**](AIMetadata.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_metadata**
    def [AIMetadata] get_all_ai_metadata()



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_metadata import AIMetadata
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = ai_api.AIApi(api_client)
    asset = 1 # int | Filter the returned list by `asset` (exact match). (optional)
    id = 1 # int | Filter the returned list by `id` (exact match). (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_metadata(asset=asset, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60; (exact match). | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60; (exact match). | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIMetadata]**](AIMetadata.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

