# elements_sdk.AIApi

All URIs are relative to *https://elements.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_ai_dataset_model_creation**](AIApi.md#abort_ai_dataset_model_creation) | **POST** `/api/2/ai/models/{id}/abort` | 
[**activate_ai_model**](AIApi.md#activate_ai_model) | **POST** `/api/2/ai/models/{id}/activate` | 
[**create_ai_annotation_track**](AIApi.md#create_ai_annotation_track) | **POST** `/api/2/ai/annotations/tracks/create` | 
[**create_ai_category**](AIApi.md#create_ai_category) | **POST** `/api/2/ai/categories` | 
[**create_ai_dataset**](AIApi.md#create_ai_dataset) | **POST** `/api/2/ai/datasets` | 
[**create_ai_dataset_model**](AIApi.md#create_ai_dataset_model) | **POST** `/api/2/ai/models/create` | 
[**create_ai_metadata**](AIApi.md#create_ai_metadata) | **POST** `/api/2/ai/metadata/create` | 
[**create_ai_model**](AIApi.md#create_ai_model) | **POST** `/api/2/ai/models` | 
[**delete_ai_annotation**](AIApi.md#delete_ai_annotation) | **DELETE** `/api/2/ai/annotations/{id}` | 
[**delete_ai_annotation_track**](AIApi.md#delete_ai_annotation_track) | **DELETE** `/api/2/ai/annotations/tracks/{id}` | 
[**delete_ai_category**](AIApi.md#delete_ai_category) | **DELETE** `/api/2/ai/categories/{id}` | 
[**delete_ai_dataset**](AIApi.md#delete_ai_dataset) | **DELETE** `/api/2/ai/datasets/{id}` | 
[**delete_ai_model**](AIApi.md#delete_ai_model) | **DELETE** `/api/2/ai/models/{id}` | 
[**export_ai_dataset**](AIApi.md#export_ai_dataset) | **POST** `/api/2/ai/datasets/{id}/export` | 
[**export_ai_model**](AIApi.md#export_ai_model) | **POST** `/api/2/ai/models/{id}/export` | 
[**get_ai_annotation**](AIApi.md#get_ai_annotation) | **GET** `/api/2/ai/annotations/{id}` | 
[**get_ai_annotation_image**](AIApi.md#get_ai_annotation_image) | **GET** `/api/2/ai/annotations/{id}/image` | 
[**get_ai_category**](AIApi.md#get_ai_category) | **GET** `/api/2/ai/categories/{id}` | 
[**get_ai_connection**](AIApi.md#get_ai_connection) | **GET** `/api/2/ai/connections/{id}` | 
[**get_ai_dataset**](AIApi.md#get_ai_dataset) | **GET** `/api/2/ai/datasets/{id}` | 
[**get_ai_image**](AIApi.md#get_ai_image) | **GET** `/api/2/ai/images/{id}` | 
[**get_ai_image_content**](AIApi.md#get_ai_image_content) | **GET** `/api/2/ai/images/{id}/content` | 
[**get_ai_metadata**](AIApi.md#get_ai_metadata) | **GET** `/api/2/ai/metadata/{id}` | 
[**get_ai_model**](AIApi.md#get_ai_model) | **GET** `/api/2/ai/models/{id}` | 
[**get_all_ai_annotation_tracks**](AIApi.md#get_all_ai_annotation_tracks) | **GET** `/api/2/ai/annotations/tracks` | 
[**get_all_ai_annotations**](AIApi.md#get_all_ai_annotations) | **GET** `/api/2/ai/annotations` | 
[**get_all_ai_categories**](AIApi.md#get_all_ai_categories) | **GET** `/api/2/ai/categories` | 
[**get_all_ai_connections**](AIApi.md#get_all_ai_connections) | **GET** `/api/2/ai/connections` | 
[**get_all_ai_datasets**](AIApi.md#get_all_ai_datasets) | **GET** `/api/2/ai/datasets` | 
[**get_all_ai_images**](AIApi.md#get_all_ai_images) | **GET** `/api/2/ai/images` | 
[**get_all_ai_metadata**](AIApi.md#get_all_ai_metadata) | **GET** `/api/2/ai/metadata` | 
[**get_all_ai_models**](AIApi.md#get_all_ai_models) | **GET** `/api/2/ai/models` | 
[**import_ai_datasets**](AIApi.md#import_ai_datasets) | **POST** `/api/2/ai/datasets/import` | 
[**import_ai_models**](AIApi.md#import_ai_models) | **POST** `/api/2/ai/datasets/{id}/import-models` | 
[**patch_ai_annotation**](AIApi.md#patch_ai_annotation) | **PATCH** `/api/2/ai/annotations/{id}` | 
[**patch_ai_category**](AIApi.md#patch_ai_category) | **PATCH** `/api/2/ai/categories/{id}` | 
[**patch_ai_dataset**](AIApi.md#patch_ai_dataset) | **PATCH** `/api/2/ai/datasets/{id}` | 
[**patch_ai_model**](AIApi.md#patch_ai_model) | **PATCH** `/api/2/ai/models/{id}` | 
[**run_ai_model_inference**](AIApi.md#run_ai_model_inference) | **POST** `/api/2/ai/models/{id}/inference` | 
[**update_ai_annotation**](AIApi.md#update_ai_annotation) | **PUT** `/api/2/ai/annotations/{id}` | 
[**update_ai_category**](AIApi.md#update_ai_category) | **PUT** `/api/2/ai/categories/{id}` | 
[**update_ai_dataset**](AIApi.md#update_ai_dataset) | **PUT** `/api/2/ai/datasets/{id}` | 
[**update_ai_model**](AIApi.md#update_ai_model) | **PUT** `/api/2/ai/models/{id}` | 
[**upload_ai_image**](AIApi.md#upload_ai_image) | **POST** `/api/2/ai/images/upload` | 


# **abort_ai_dataset_model_creation**
> abort_ai_dataset_model_creation(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **activate_ai_model**
> activate_ai_model(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_annotation_track**
> [AIAnnotation] create_ai_annotation_track(ai_annotation_create_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_annotation import AIAnnotation
from elements_sdk.model.ai_annotation_create_request import AIAnnotationCreateRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    ai_annotation_create_request = AIAnnotationCreateRequest(
        proxy=1,
        category="category_example",
        frame=1,
        relative_left=3.14,
        relative_top=3.14,
        relative_width=3.14,
        relative_height=3.14,
    ) # AIAnnotationCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ai_annotation_track(ai_annotation_create_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->create_ai_annotation_track: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_annotation_create_request** | [**AIAnnotationCreateRequest**](AIAnnotationCreateRequest.md)|  |

### Return type

[**[AIAnnotation]**](AIAnnotation.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_category**
> AICategoryDetail create_ai_category(ai_category_detail_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_category_detail import AICategoryDetail
from elements_sdk.model.ai_category_detail_update import AICategoryDetailUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    ai_category_detail_update = AICategoryDetailUpdate(
        dataset=AIDatasetDetailReference(
            id="id_example",
            training_model=AIModel(
                id="id_example",
                progress=AIModelProgress(
                    status={
                        "key": "key_example",
                    },
                    eta=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
            ),
            last_finished_model=AIModel(
                id="id_example",
                progress=AIModelProgress(
                    status={
                        "key": "key_example",
                    },
                    eta=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
            ),
        ),
        name="name_example",
    ) # AICategoryDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ai_category(ai_category_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->create_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_category_detail_update** | [**AICategoryDetailUpdate**](AICategoryDetailUpdate.md)|  |

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_dataset**
> AIDatasetWithPreview create_ai_dataset(ai_dataset_with_preview_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from elements_sdk.model.ai_dataset_with_preview_update import AIDatasetWithPreviewUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_dataset_model**
> AIModel create_ai_dataset_model(ai_model_training_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_training_request import AIModelTrainingRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_metadata**
> create_ai_metadata(ai_processing_request)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_processing_request import AIProcessingRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_ai_model**
> AIModel create_ai_model(ai_model_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_update import AIModelUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ai_annotation**
> delete_ai_annotation(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Annotation.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ai_annotation(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->delete_ai_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Annotation. |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ai_annotation_track**
> delete_ai_annotation_track(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Annotation.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ai_annotation_track(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->delete_ai_annotation_track: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Annotation. |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ai_category**
> delete_ai_category(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Category.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_ai_category(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->delete_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Category. |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ai_dataset**
> delete_ai_dataset(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_ai_model**
> delete_ai_model(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_ai_dataset**
> AIDatasetExportResponse export_ai_dataset(id, ai_dataset_export_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_export_response import AIDatasetExportResponse
from elements_sdk.model.ai_dataset_export_request import AIDatasetExportRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_ai_model**
> AIModelExportResponse export_ai_model(id, ai_model_export_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model_export_response import AIModelExportResponse
from elements_sdk.model.ai_model_export_request import AIModelExportRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_annotation**
> AIAnnotation get_ai_annotation(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_annotation import AIAnnotation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Annotation.
    include_transforms_for_asset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_annotation(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_annotation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ai_annotation(id, include_transforms_for_asset=include_transforms_for_asset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Annotation. |
 **include_transforms_for_asset** | **int**|  | [optional]

### Return type

[**AIAnnotation**](AIAnnotation.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_annotation_image**
> get_ai_annotation_image(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Annotation.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_ai_annotation_image(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_annotation_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Annotation. |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_category**
> AICategoryDetail get_ai_category(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_category_detail import AICategoryDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Category.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_category(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Category. |

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_connection**
> AIConnection get_ai_connection(id)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_connection import AIConnection
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = 1 # int | A unique integer value identifying this AI Connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_connection(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AI Connection. |

### Return type

[**AIConnection**](AIConnection.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_dataset**
> AIDatasetWithPreview get_ai_dataset(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_image**
> AIImage get_ai_image(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_image import AIImage
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Image.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ai_image(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Image. |

### Return type

[**AIImage**](AIImage.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_image_content**
> get_ai_image_content(id)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Image.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_ai_image_content(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_ai_image_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Image. |

### Return type

void (empty response body)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_metadata**
> AIMetadata get_ai_metadata(id)



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_metadata import AIMetadata
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_ai_model**
> AIModel get_ai_model(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_annotation_tracks**
> [AIAnnotation] get_all_ai_annotation_tracks()



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_annotation import AIAnnotation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    category = "category_example" # str | Filter the returned list by `category`. (optional)
    image__dataset = "image__dataset_example" # str | Filter the returned list by `image__dataset`. (optional)
    track = "track_example" # str | Filter the returned list by `track`. (optional)
    image = "image_example" # str | Filter the returned list by `image`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_annotation_tracks(category=category, image__dataset=image__dataset, track=track, image=image, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_annotation_tracks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter the returned list by &#x60;category&#x60;. | [optional]
 **image__dataset** | **str**| Filter the returned list by &#x60;image__dataset&#x60;. | [optional]
 **track** | **str**| Filter the returned list by &#x60;track&#x60;. | [optional]
 **image** | **str**| Filter the returned list by &#x60;image&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIAnnotation]**](AIAnnotation.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_annotations**
> [AIAnnotation] get_all_ai_annotations()



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_annotation import AIAnnotation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    category = "category_example" # str | Filter the returned list by `category`. (optional)
    image__dataset = "image__dataset_example" # str | Filter the returned list by `image__dataset`. (optional)
    image__asset = 3.14 # float | Filter the returned list by `image__asset`. (optional)
    track = "track_example" # str | Filter the returned list by `track`. (optional)
    image = "image_example" # str | Filter the returned list by `image`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    include_transforms_for_asset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_annotations(category=category, image__dataset=image__dataset, image__asset=image__asset, track=track, image=image, ordering=ordering, limit=limit, offset=offset, include_transforms_for_asset=include_transforms_for_asset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_annotations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter the returned list by &#x60;category&#x60;. | [optional]
 **image__dataset** | **str**| Filter the returned list by &#x60;image__dataset&#x60;. | [optional]
 **image__asset** | **float**| Filter the returned list by &#x60;image__asset&#x60;. | [optional]
 **track** | **str**| Filter the returned list by &#x60;track&#x60;. | [optional]
 **image** | **str**| Filter the returned list by &#x60;image&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **include_transforms_for_asset** | **int**|  | [optional]

### Return type

[**[AIAnnotation]**](AIAnnotation.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_categories**
> [AICategory] get_all_ai_categories()



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_category import AICategory
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    dataset = "dataset_example" # str | Filter the returned list by `dataset`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_categories(dataset=dataset, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter the returned list by &#x60;dataset&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AICategory]**](AICategory.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_connections**
> [AIConnection] get_all_ai_connections()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_connection import AIConnection
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_connections(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIConnection]**](AIConnection.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_datasets**
> [AIDatasetWithPreview] get_all_ai_datasets()



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    connection = 3.14 # float | Filter the returned list by `connection`. (optional)
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
 **connection** | **float**| Filter the returned list by &#x60;connection&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIDatasetWithPreview]**](AIDatasetWithPreview.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_images**
> [AIImage] get_all_ai_images()



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_image import AIImage
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    dataset = "dataset_example" # str | Filter the returned list by `dataset`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_ai_images(dataset=dataset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->get_all_ai_images: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter the returned list by &#x60;dataset&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIImage]**](AIImage.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_metadata**
> [AIMetadata] get_all_ai_metadata()



### Required permissions    * User account permission: `media:access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_metadata import AIMetadata
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    asset = 3.14 # float | Filter the returned list by `asset`. (optional)
    id = 3.14 # float | Filter the returned list by `id`. (optional)
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
 **asset** | **float**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AIMetadata]**](AIMetadata.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_ai_models**
> [AIModel] get_all_ai_models()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **import_ai_datasets**
> ImportAIDatasetResponse import_ai_datasets(import_ai_dataset_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.import_ai_dataset_response import ImportAIDatasetResponse
from elements_sdk.model.import_ai_dataset_request import ImportAIDatasetRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **import_ai_models**
> ImportAIModelResponse import_ai_models(id, import_ai_model_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.import_ai_model_request import ImportAIModelRequest
from elements_sdk.model.import_ai_model_response import ImportAIModelResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ai_annotation**
> AIAnnotation patch_ai_annotation(id, ai_annotation_partial_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_annotation_partial_update import AIAnnotationPartialUpdate
from elements_sdk.model.ai_annotation import AIAnnotation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Annotation.
    ai_annotation_partial_update = AIAnnotationPartialUpdate(
        image=AIImageReference(
            id="id_example",
        ),
        category=AICategoryMiniReference(
            id="id_example",
        ),
        relative_left=3.14,
        relative_top=3.14,
        relative_width=3.14,
        relative_height=3.14,
        track="track_example",
        created_by=1,
    ) # AIAnnotationPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ai_annotation(id, ai_annotation_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->patch_ai_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Annotation. |
 **ai_annotation_partial_update** | [**AIAnnotationPartialUpdate**](AIAnnotationPartialUpdate.md)|  |

### Return type

[**AIAnnotation**](AIAnnotation.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ai_category**
> AICategoryDetail patch_ai_category(id, ai_category_detail_partial_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_category_detail import AICategoryDetail
from elements_sdk.model.ai_category_detail_partial_update import AICategoryDetailPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Category.
    ai_category_detail_partial_update = AICategoryDetailPartialUpdate(
        dataset=AIDatasetDetailReference(
            id="id_example",
            training_model=AIModel(
                id="id_example",
                progress=AIModelProgress(
                    status={
                        "key": "key_example",
                    },
                    eta=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
            ),
            last_finished_model=AIModel(
                id="id_example",
                progress=AIModelProgress(
                    status={
                        "key": "key_example",
                    },
                    eta=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
            ),
        ),
        name="name_example",
    ) # AICategoryDetailPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_ai_category(id, ai_category_detail_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->patch_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Category. |
 **ai_category_detail_partial_update** | [**AICategoryDetailPartialUpdate**](AICategoryDetailPartialUpdate.md)|  |

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ai_dataset**
> AIDatasetWithPreview patch_ai_dataset(id, ai_dataset_with_preview_partial_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from elements_sdk.model.ai_dataset_with_preview_partial_update import AIDatasetWithPreviewPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_ai_model**
> AIModel patch_ai_model(id, ai_model_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_partial_update import AIModelPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **run_ai_model_inference**
> AIModelInferenceResponse run_ai_model_inference(id, ai_model_inference_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model_inference_request import AIModelInferenceRequest
from elements_sdk.model.ai_model_inference_response import AIModelInferenceResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ai_annotation**
> AIAnnotation update_ai_annotation(id, ai_annotation_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_annotation_update import AIAnnotationUpdate
from elements_sdk.model.ai_annotation import AIAnnotation
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Annotation.
    ai_annotation_update = AIAnnotationUpdate(
        image=AIImageReference(
            id="id_example",
        ),
        category=AICategoryMiniReference(
            id="id_example",
        ),
        relative_left=3.14,
        relative_top=3.14,
        relative_width=3.14,
        relative_height=3.14,
        track="track_example",
        created_by=1,
    ) # AIAnnotationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_ai_annotation(id, ai_annotation_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->update_ai_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Annotation. |
 **ai_annotation_update** | [**AIAnnotationUpdate**](AIAnnotationUpdate.md)|  |

### Return type

[**AIAnnotation**](AIAnnotation.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ai_category**
> AICategoryDetail update_ai_category(id, ai_category_detail_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_category_detail import AICategoryDetail
from elements_sdk.model.ai_category_detail_update import AICategoryDetailUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    id = "id_example" # str | A UUID string identifying this AI Category.
    ai_category_detail_update = AICategoryDetailUpdate(
        dataset=AIDatasetDetailReference(
            id="id_example",
            training_model=AIModel(
                id="id_example",
                progress=AIModelProgress(
                    status={
                        "key": "key_example",
                    },
                    eta=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
            ),
            last_finished_model=AIModel(
                id="id_example",
                progress=AIModelProgress(
                    status={
                        "key": "key_example",
                    },
                    eta=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
            ),
        ),
        name="name_example",
    ) # AICategoryDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_ai_category(id, ai_category_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->update_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this AI Category. |
 **ai_category_detail_update** | [**AICategoryDetailUpdate**](AICategoryDetailUpdate.md)|  |

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ai_dataset**
> AIDatasetWithPreview update_ai_dataset(id, ai_dataset_with_preview_update)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_dataset_with_preview import AIDatasetWithPreview
from elements_sdk.model.ai_dataset_with_preview_update import AIDatasetWithPreviewUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_ai_model**
> AIModel update_ai_model(id, ai_model_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.ai_model import AIModel
from elements_sdk.model.ai_model_update import AIModelUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
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

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **upload_ai_image**
> AIImage upload_ai_image(upload_ai_image_request)



### Required permissions    * User account permission: `None` (read) / `media:roots:manage` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import ai_api
from elements_sdk.model.upload_ai_image_request import UploadAIImageRequest
from elements_sdk.model.ai_image import AIImage
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_api.AIApi(api_client)
    upload_ai_image_request = UploadAIImageRequest(
        content="content_example",
        category="category_example",
    ) # UploadAIImageRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.upload_ai_image(upload_ai_image_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AIApi->upload_ai_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_ai_image_request** | [**UploadAIImageRequest**](UploadAIImageRequest.md)|  |

### Return type

[**AIImage**](AIImage.md)

### Authorization

[Bearer](../#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

