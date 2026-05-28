# elements_sdk.AIApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_ai_dataset_model_creation**](AIApi.md#abort_ai_dataset_model_creation) | **POST** `/api/2/ai/models/{id}/abort` | 
[**activate_ai_model**](AIApi.md#activate_ai_model) | **POST** `/api/2/ai/models/{id}/activate` | 
[**create_ai_dataset**](AIApi.md#create_ai_dataset) | **POST** `/api/2/ai/datasets` | 
[**create_ai_dataset_model**](AIApi.md#create_ai_dataset_model) | **POST** `/api/2/ai/models/create` | 
[**create_ai_metadata**](AIApi.md#create_ai_metadata) | **POST** `/api/2/ai/metadata/create` | 
[**create_ai_model**](AIApi.md#create_ai_model) | **POST** `/api/2/ai/models` | 
[**delete_ai_dataset**](AIApi.md#delete_ai_dataset) | **DELETE** `/api/2/ai/datasets/{id}` | 
[**delete_ai_model**](AIApi.md#delete_ai_model) | **DELETE** `/api/2/ai/models/{id}` | 
[**export_ai_dataset**](AIApi.md#export_ai_dataset) | **POST** `/api/2/ai/datasets/{id}/export` | 
[**export_ai_model**](AIApi.md#export_ai_model) | **POST** `/api/2/ai/models/{id}/export` | 
[**get_ai_dataset**](AIApi.md#get_ai_dataset) | **GET** `/api/2/ai/datasets/{id}` | 
[**get_ai_metadata**](AIApi.md#get_ai_metadata) | **GET** `/api/2/ai/metadata/{id}` | 
[**get_ai_model**](AIApi.md#get_ai_model) | **GET** `/api/2/ai/models/{id}` | 
[**get_all_ai_datasets**](AIApi.md#get_all_ai_datasets) | **GET** `/api/2/ai/datasets` | 
[**get_all_ai_metadata**](AIApi.md#get_all_ai_metadata) | **GET** `/api/2/ai/metadata` | 
[**get_all_ai_models**](AIApi.md#get_all_ai_models) | **GET** `/api/2/ai/models` | 
[**import_ai_datasets**](AIApi.md#import_ai_datasets) | **POST** `/api/2/ai/datasets/import` | 
[**import_ai_models**](AIApi.md#import_ai_models) | **POST** `/api/2/ai/datasets/{id}/import-models` | 
[**patch_ai_dataset**](AIApi.md#patch_ai_dataset) | **PATCH** `/api/2/ai/datasets/{id}` | 
[**patch_ai_model**](AIApi.md#patch_ai_model) | **PATCH** `/api/2/ai/models/{id}` | 
[**run_ai_model_inference**](AIApi.md#run_ai_model_inference) | **POST** `/api/2/ai/models/{id}/inference` | 
[**update_ai_dataset**](AIApi.md#update_ai_dataset) | **PUT** `/api/2/ai/datasets/{id}` | 
[**update_ai_model**](AIApi.md#update_ai_model) | **PUT** `/api/2/ai/models/{id}` | 


# **abort_ai_dataset_model_creation**
    def abort_ai_dataset_model_creation(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
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
    id = "id_example" # str | A UUID string identifying this AI Model.

    # example passing only required values which don't have defaults set
    try:
        api_instance.abort_ai_dataset_model_creation(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->abort_ai_dataset_model_creation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **activate_ai_model**
    def activate_ai_model(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
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
    id = "id_example" # str | A UUID string identifying this AI Model.

    # example passing only required values which don't have defaults set
    try:
        api_instance.activate_ai_model(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->activate_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_dataset**
    def AIDatasetWithPreview create_ai_dataset(ai_dataset_with_preview_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from elements_sdk.model.ai_dataset_with_preview_update import AIDatasetWithPreviewUpdate
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
    ai_dataset_with_preview_update = AIDatasetWithPreviewUpdate(
        name="name_example",
        type="normal",
        connection=1,
    ) # AIDatasetWithPreviewUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ai_dataset(ai_dataset_with_preview_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->create_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_dataset_with_preview_update** | [**AIDatasetWithPreviewUpdate**](AIDatasetWithPreviewUpdate.md)|  |

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_dataset_model**
    def AIModel create_ai_dataset_model(ai_model_training_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_training_request import AIModelTrainingRequest
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
    ai_model_training_request = AIModelTrainingRequest(
        name="name_example",
        dataset="dataset_example",
        categories=[
            "categories_example",
        ],
        continue_from="continue_from_example",
        parameters={
            "key": "key_example",
        },
    ) # AIModelTrainingRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ai_dataset_model(ai_model_training_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->create_ai_dataset_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_model_training_request** | [**AIModelTrainingRequest**](AIModelTrainingRequest.md)|  |

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_metadata**
    def create_ai_metadata(ai_processing_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_processing_request import AIProcessingRequest
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
    ai_processing_request = AIProcessingRequest(
        assets=[
            1,
        ],
        directories=[
            1,
        ],
        datasets=[
            "datasets_example",
        ],
        preferred_proxy_profile=1,
    ) # AIProcessingRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_ai_metadata(ai_processing_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->create_ai_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_processing_request** | [**AIProcessingRequest**](AIProcessingRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_model**
    def AIModel create_ai_model(ai_model_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_update import AIModelUpdate
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
    ai_model_update = AIModelUpdate(
        dataset=AIDatasetReference(
            id="id_example",
        ),
        parameters={
            "key": "key_example",
        },
        name="name_example",
        training_task_id="training_task_id_example",
        threshold=3.14,
        epoch=-2147483648,
        preprocessing_task="preprocessing_task_example",
    ) # AIModelUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ai_model(ai_model_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->create_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_model_update** | [**AIModelUpdate**](AIModelUpdate.md)|  |

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ai_dataset**
    def delete_ai_dataset(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
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
    id = "id_example" # str | A UUID string identifying this AI Dataset.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ai_dataset(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->delete_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Dataset. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ai_model**
    def delete_ai_model(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
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
    id = "id_example" # str | A UUID string identifying this AI Model.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ai_model(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->delete_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_ai_dataset**
    def AIDatasetExportResponse export_ai_dataset(id, ai_dataset_export_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_export_response import AIDatasetExportResponse
from elements_sdk.model.ai_dataset_export_request import AIDatasetExportRequest
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
    id = "id_example" # str | A UUID string identifying this AI Dataset.
    ai_dataset_export_request = AIDatasetExportRequest(
        path="path_example",
    ) # AIDatasetExportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.export_ai_dataset(id, ai_dataset_export_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->export_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Dataset. |
 **ai_dataset_export_request** | [**AIDatasetExportRequest**](AIDatasetExportRequest.md)|  |

### Return type

[**AIDatasetExportResponse**](AIDatasetExportResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_ai_model**
    def AIModelExportResponse export_ai_model(id, ai_model_export_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model_export_response import AIModelExportResponse
from elements_sdk.model.ai_model_export_request import AIModelExportRequest
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
    id = "id_example" # str | A UUID string identifying this AI Model.
    ai_model_export_request = AIModelExportRequest(
        path="path_example",
    ) # AIModelExportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.export_ai_model(id, ai_model_export_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->export_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |
 **ai_model_export_request** | [**AIModelExportRequest**](AIModelExportRequest.md)|  |

### Return type

[**AIModelExportResponse**](AIModelExportResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_dataset**
    def AIDatasetWithPreview get_ai_dataset(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
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
    id = "id_example" # str | A UUID string identifying this AI Dataset.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_dataset(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Dataset. |

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

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

# **get_ai_model**
    def AIModel get_ai_model(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
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
    id = "id_example" # str | A UUID string identifying this AI Model.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_model(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_datasets**
    def [AIDatasetWithPreview] get_all_ai_datasets()



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
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
    connection = 1 # int | Filter the returned list by `connection`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_datasets(connection=connection, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | **int**| Filter the returned list by &#x60;connection&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIDatasetWithPreview]**](AIDatasetWithPreview.md)

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
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
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
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIMetadata]**](AIMetadata.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_models**
    def [AIModel] get_all_ai_models()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
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
    dataset = "dataset_example" # str | Filter the returned list by `dataset`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_models(dataset=dataset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter the returned list by &#x60;dataset&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIModel]**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **import_ai_datasets**
    def ImportAIDatasetResponse import_ai_datasets(import_ai_dataset_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.import_ai_dataset_response import ImportAIDatasetResponse
from elements_sdk.model.import_ai_dataset_request import ImportAIDatasetRequest
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
    import_ai_dataset_request = ImportAIDatasetRequest(
        connection=1,
        path="path_example",
        replace=True,
        rename="rename_example",
    ) # ImportAIDatasetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.import_ai_datasets(import_ai_dataset_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->import_ai_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_ai_dataset_request** | [**ImportAIDatasetRequest**](ImportAIDatasetRequest.md)|  |

### Return type

[**ImportAIDatasetResponse**](ImportAIDatasetResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **import_ai_models**
    def ImportAIModelResponse import_ai_models(id, import_ai_model_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.import_ai_model_request import ImportAIModelRequest
from elements_sdk.model.import_ai_model_response import ImportAIModelResponse
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
    id = "id_example" # str | A UUID string identifying this AI Dataset.
    import_ai_model_request = ImportAIModelRequest(
        path="path_example",
    ) # ImportAIModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.import_ai_models(id, import_ai_model_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->import_ai_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Dataset. |
 **import_ai_model_request** | [**ImportAIModelRequest**](ImportAIModelRequest.md)|  |

### Return type

[**ImportAIModelResponse**](ImportAIModelResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ai_dataset**
    def AIDatasetWithPreview patch_ai_dataset(id, ai_dataset_with_preview_partial_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from elements_sdk.model.ai_dataset_with_preview_partial_update import AIDatasetWithPreviewPartialUpdate
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
    id = "id_example" # str | A UUID string identifying this AI Dataset.
    ai_dataset_with_preview_partial_update = AIDatasetWithPreviewPartialUpdate(
        name="name_example",
        type="normal",
        connection=1,
    ) # AIDatasetWithPreviewPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ai_dataset(id, ai_dataset_with_preview_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->patch_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Dataset. |
 **ai_dataset_with_preview_partial_update** | [**AIDatasetWithPreviewPartialUpdate**](AIDatasetWithPreviewPartialUpdate.md)|  |

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ai_model**
    def AIModel patch_ai_model(id, ai_model_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_partial_update import AIModelPartialUpdate
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
    id = "id_example" # str | A UUID string identifying this AI Model.
    ai_model_partial_update = AIModelPartialUpdate(
        dataset=AIDatasetReference(
            id="id_example",
        ),
        parameters={
            "key": "key_example",
        },
        name="name_example",
        training_task_id="training_task_id_example",
        threshold=3.14,
        epoch=-2147483648,
        preprocessing_task="preprocessing_task_example",
    ) # AIModelPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ai_model(id, ai_model_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->patch_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |
 **ai_model_partial_update** | [**AIModelPartialUpdate**](AIModelPartialUpdate.md)|  |

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **run_ai_model_inference**
    def AIModelInferenceResponse run_ai_model_inference(id, ai_model_inference_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model_inference_request import AIModelInferenceRequest
from elements_sdk.model.ai_model_inference_response import AIModelInferenceResponse
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
    id = "id_example" # str | A UUID string identifying this AI Model.
    ai_model_inference_request = AIModelInferenceRequest(
        proxy=1,
        frame_start=1,
        frame_end=1,
        frame_step=1,
        skip_step=1,
        combine_threshold=1,
    ) # AIModelInferenceRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.run_ai_model_inference(id, ai_model_inference_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->run_ai_model_inference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |
 **ai_model_inference_request** | [**AIModelInferenceRequest**](AIModelInferenceRequest.md)|  |

### Return type

[**AIModelInferenceResponse**](AIModelInferenceResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ai_dataset**
    def AIDatasetWithPreview update_ai_dataset(id, ai_dataset_with_preview_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from elements_sdk.model.ai_dataset_with_preview_update import AIDatasetWithPreviewUpdate
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
    id = "id_example" # str | A UUID string identifying this AI Dataset.
    ai_dataset_with_preview_update = AIDatasetWithPreviewUpdate(
        name="name_example",
        type="normal",
        connection=1,
    ) # AIDatasetWithPreviewUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_ai_dataset(id, ai_dataset_with_preview_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->update_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Dataset. |
 **ai_dataset_with_preview_update** | [**AIDatasetWithPreviewUpdate**](AIDatasetWithPreviewUpdate.md)|  |

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ai_model**
    def AIModel update_ai_model(id, ai_model_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_update import AIModelUpdate
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
    id = "id_example" # str | A UUID string identifying this AI Model.
    ai_model_update = AIModelUpdate(
        dataset=AIDatasetReference(
            id="id_example",
        ),
        parameters={
            "key": "key_example",
        },
        name="name_example",
        training_task_id="training_task_id_example",
        threshold=3.14,
        epoch=-2147483648,
        preprocessing_task="preprocessing_task_example",
    ) # AIModelUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_ai_model(id, ai_model_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->update_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Model. |
 **ai_model_update** | [**AIModelUpdate**](AIModelUpdate.md)|  |

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

