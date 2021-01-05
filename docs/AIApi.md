# elements_sdk.AIApi

All URIs are relative to *http://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_ai_dataset_model_creation**](AIApi.md#abort_ai_dataset_model_creation) | **POST** `/api/2/ai/models/{id}/abort` | 
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
[**get_ai_annotation**](AIApi.md#get_ai_annotation) | **GET** `/api/2/ai/annotations/{id}` | 
[**get_ai_annotation_image**](AIApi.md#get_ai_annotation_image) | **GET** `/api/2/ai/annotations/{id}/image` | 
[**get_ai_category**](AIApi.md#get_ai_category) | **GET** `/api/2/ai/categories/{id}` | 
[**get_ai_connection**](AIApi.md#get_ai_connection) | **GET** `/api/2/ai/connections/{id}` | 
[**get_ai_dataset**](AIApi.md#get_ai_dataset) | **GET** `/api/2/ai/datasets/{id}` | 
[**get_ai_dataset_model_stats**](AIApi.md#get_ai_dataset_model_stats) | **GET** `/api/2/ai/models/{id}/stats` | 
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
[**patch_ai_category**](AIApi.md#patch_ai_category) | **PATCH** `/api/2/ai/categories/{id}` | 
[**patch_ai_dataset**](AIApi.md#patch_ai_dataset) | **PATCH** `/api/2/ai/datasets/{id}` | 
[**patch_ai_model**](AIApi.md#patch_ai_model) | **PATCH** `/api/2/ai/models/{id}` | 
[**update_ai_category**](AIApi.md#update_ai_category) | **PUT** `/api/2/ai/categories/{id}` | 
[**update_ai_dataset**](AIApi.md#update_ai_dataset) | **PUT** `/api/2/ai/datasets/{id}` | 
[**update_ai_model**](AIApi.md#update_ai_model) | **PUT** `/api/2/ai/models/{id}` | 



***

# **abort_ai_dataset_model_creation**

    def abort_ai_dataset_model_creation(id) -> object 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Model.

    try:
        api_response = api_instance.abort_ai_dataset_model_creation(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->abort_ai_dataset_model_creation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Model. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_ai_annotation_track**

    def create_ai_annotation_track(data) -> list[AIAnnotation] 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    data = elements_sdk.AIAnnotationCreateRequest() # AIAnnotationCreateRequest | 

    try:
        api_response = api_instance.create_ai_annotation_track(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->create_ai_annotation_track: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AIAnnotationCreateRequest**](AIAnnotationCreateRequest.md)|  | 

### Return type

[**list[AIAnnotation]**](AIAnnotation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_ai_category**

    def create_ai_category(data) -> AICategoryDetail 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    data = elements_sdk.AICategoryDetail() # AICategoryDetail | 

    try:
        api_response = api_instance.create_ai_category(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->create_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AICategoryDetail**](AICategoryDetail.md)|  | 

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_ai_dataset**

    def create_ai_dataset(data) -> AIDatasetWithPreview 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    data = elements_sdk.AIDatasetWithPreview() # AIDatasetWithPreview | 

    try:
        api_response = api_instance.create_ai_dataset(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->create_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AIDatasetWithPreview**](AIDatasetWithPreview.md)|  | 

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_ai_dataset_model**

    def create_ai_dataset_model(data) -> AIModel 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    data = elements_sdk.AIModel() # AIModel | 

    try:
        api_response = api_instance.create_ai_dataset_model(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->create_ai_dataset_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AIModel**](AIModel.md)|  | 

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_ai_metadata**

    def create_ai_metadata(data) -> object 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    data = elements_sdk.AIProcessingRequest() # AIProcessingRequest | 

    try:
        api_response = api_instance.create_ai_metadata(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->create_ai_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AIProcessingRequest**](AIProcessingRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_ai_model**

    def create_ai_model(data) -> AIModel 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    data = elements_sdk.AIModel() # AIModel | 

    try:
        api_response = api_instance.create_ai_model(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->create_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AIModel**](AIModel.md)|  | 

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_ai_annotation**

    def delete_ai_annotation(id) -> object 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Annotation.

    try:
        api_response = api_instance.delete_ai_annotation(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->delete_ai_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Annotation. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_ai_annotation_track**

    def delete_ai_annotation_track(id) -> object 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Annotation.

    try:
        api_response = api_instance.delete_ai_annotation_track(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->delete_ai_annotation_track: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Annotation. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_ai_category**

    def delete_ai_category(id) -> object 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Category.

    try:
        api_response = api_instance.delete_ai_category(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->delete_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Category. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_ai_dataset**

    def delete_ai_dataset(id) -> object 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Dataset.

    try:
        api_response = api_instance.delete_ai_dataset(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->delete_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Dataset. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_ai_model**

    def delete_ai_model(id) -> object 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Model.

    try:
        api_response = api_instance.delete_ai_model(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->delete_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Model. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_annotation**

    def get_ai_annotation(id) -> AIAnnotation 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Annotation.

    try:
        api_response = api_instance.get_ai_annotation(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_annotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Annotation. | 

### Return type

[**AIAnnotation**](AIAnnotation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_annotation_image**

    def get_ai_annotation_image(id) -> object 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Annotation.

    try:
        api_response = api_instance.get_ai_annotation_image(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_annotation_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Annotation. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_category**

    def get_ai_category(id) -> AICategoryDetail 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Category.

    try:
        api_response = api_instance.get_ai_category(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Category. | 

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_connection**

    def get_ai_connection(id) -> AIConnection 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 56 # int | A unique integer value identifying this AI Connection.

    try:
        api_response = api_instance.get_ai_connection(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AI Connection. | 

### Return type

[**AIConnection**](AIConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_dataset**

    def get_ai_dataset(id) -> AIDatasetWithPreview 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Dataset.

    try:
        api_response = api_instance.get_ai_dataset(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Dataset. | 

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_dataset_model_stats**

    def get_ai_dataset_model_stats(id) -> AIModelStats 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Model.

    try:
        api_response = api_instance.get_ai_dataset_model_stats(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_dataset_model_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Model. | 

### Return type

[**AIModelStats**](AIModelStats.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_image**

    def get_ai_image(id) -> AIImage 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Image.

    try:
        api_response = api_instance.get_ai_image(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Image. | 

### Return type

[**AIImage**](AIImage.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_image_content**

    def get_ai_image_content(id) -> object 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Image.

    try:
        api_response = api_instance.get_ai_image_content(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_image_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Image. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_metadata**

    def get_ai_metadata(id) -> AIMetadata 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 56 # int | A unique integer value identifying this AI Metadata.

    try:
        api_response = api_instance.get_ai_metadata(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AI Metadata. | 

### Return type

[**AIMetadata**](AIMetadata.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_ai_model**

    def get_ai_model(id) -> AIModel 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Model.

    try:
        api_response = api_instance.get_ai_model(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Model. | 

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_annotation_tracks**

    def get_all_ai_annotation_tracks(category=category, image__dataset=image__dataset, track=track, image=image, ordering=ordering, limit=limit, offset=offset) -> list[AIAnnotation] 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    category = 'category_example' # str | Filter the returned list by `category`. (optional)
image__dataset = 'image__dataset_example' # str | Filter the returned list by `image__dataset`. (optional)
track = 'track_example' # str | Filter the returned list by `track`. (optional)
image = 'image_example' # str | Filter the returned list by `image`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_annotation_tracks(category=category, image__dataset=image__dataset, track=track, image=image, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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

[**list[AIAnnotation]**](AIAnnotation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_annotations**

    def get_all_ai_annotations(category=category, image__dataset=image__dataset, track=track, image=image, ordering=ordering, limit=limit, offset=offset) -> list[AIAnnotation] 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    category = 'category_example' # str | Filter the returned list by `category`. (optional)
image__dataset = 'image__dataset_example' # str | Filter the returned list by `image__dataset`. (optional)
track = 'track_example' # str | Filter the returned list by `track`. (optional)
image = 'image_example' # str | Filter the returned list by `image`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_annotations(category=category, image__dataset=image__dataset, track=track, image=image, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_all_ai_annotations: %s\n" % e)
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

[**list[AIAnnotation]**](AIAnnotation.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_categories**

    def get_all_ai_categories(dataset=dataset, name=name, ordering=ordering, limit=limit, offset=offset) -> list[AICategory] 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    dataset = 'dataset_example' # str | Filter the returned list by `dataset`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_categories(dataset=dataset, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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

[**list[AICategory]**](AICategory.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_connections**

    def get_all_ai_connections(ordering=ordering, limit=limit, offset=offset) -> list[AIConnection] 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_connections(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_all_ai_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[AIConnection]**](AIConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_datasets**

    def get_all_ai_datasets(connection=connection, name=name, ordering=ordering, limit=limit, offset=offset) -> list[AIDatasetWithPreview] 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    connection = 'connection_example' # str | Filter the returned list by `connection`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_datasets(connection=connection, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_all_ai_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | **str**| Filter the returned list by &#x60;connection&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[AIDatasetWithPreview]**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_images**

    def get_all_ai_images(dataset=dataset, ordering=ordering, limit=limit, offset=offset) -> list[AIImage] 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    dataset = 'dataset_example' # str | Filter the returned list by `dataset`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_images(dataset=dataset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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

[**list[AIImage]**](AIImage.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_metadata**

    def get_all_ai_metadata(asset=asset, id=id, ordering=ordering, limit=limit, offset=offset) -> list[AIMetadata] 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    asset = 'asset_example' # str | Filter the returned list by `asset`. (optional)
id = 3.4 # float | Filter the returned list by `id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_metadata(asset=asset, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_all_ai_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Filter the returned list by &#x60;asset&#x60;. | [optional] 
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[AIMetadata]**](AIMetadata.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_ai_models**

    def get_all_ai_models(dataset=dataset, ordering=ordering, limit=limit, offset=offset) -> list[AIModel] 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    dataset = 'dataset_example' # str | Filter the returned list by `dataset`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_ai_models(dataset=dataset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
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

[**list[AIModel]**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_ai_category**

    def patch_ai_category(id, data) -> AICategoryDetail 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Category.
data = elements_sdk.AICategoryDetailPartialUpdate() # AICategoryDetailPartialUpdate | 

    try:
        api_response = api_instance.patch_ai_category(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->patch_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Category. | 
 **data** | [**AICategoryDetailPartialUpdate**](AICategoryDetailPartialUpdate.md)|  | 

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_ai_dataset**

    def patch_ai_dataset(id, data) -> AIDatasetWithPreview 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Dataset.
data = elements_sdk.AIDatasetWithPreviewPartialUpdate() # AIDatasetWithPreviewPartialUpdate | 

    try:
        api_response = api_instance.patch_ai_dataset(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->patch_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Dataset. | 
 **data** | [**AIDatasetWithPreviewPartialUpdate**](AIDatasetWithPreviewPartialUpdate.md)|  | 

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_ai_model**

    def patch_ai_model(id, data) -> AIModel 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Model.
data = elements_sdk.AIModelPartialUpdate() # AIModelPartialUpdate | 

    try:
        api_response = api_instance.patch_ai_model(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->patch_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Model. | 
 **data** | [**AIModelPartialUpdate**](AIModelPartialUpdate.md)|  | 

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_ai_category**

    def update_ai_category(id, data) -> AICategoryDetail 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Category.
data = elements_sdk.AICategoryDetail() # AICategoryDetail | 

    try:
        api_response = api_instance.update_ai_category(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->update_ai_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Category. | 
 **data** | [**AICategoryDetail**](AICategoryDetail.md)|  | 

### Return type

[**AICategoryDetail**](AICategoryDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_ai_dataset**

    def update_ai_dataset(id, data) -> AIDatasetWithPreview 



### Required permissions    * User account permission: None (read) / media:roots:manage (write) 

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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Dataset.
data = elements_sdk.AIDatasetWithPreview() # AIDatasetWithPreview | 

    try:
        api_response = api_instance.update_ai_dataset(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->update_ai_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Dataset. | 
 **data** | [**AIDatasetWithPreview**](AIDatasetWithPreview.md)|  | 

### Return type

[**AIDatasetWithPreview**](AIDatasetWithPreview.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_ai_model**

    def update_ai_model(id, data) -> AIModel 



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

configuration.host = "http://elements.local"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AIApi(api_client)
    id = 'id_example' # str | A UUID string identifying this AI Model.
data = elements_sdk.AIModel() # AIModel | 

    try:
        api_response = api_instance.update_ai_model(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->update_ai_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this AI Model. | 
 **data** | [**AIModel**](AIModel.md)|  | 

### Return type

[**AIModel**](AIModel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

