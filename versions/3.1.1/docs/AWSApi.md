# elements_sdk.AWSApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_account**](AWSApi.md#create_aws_account) | **POST** `/api/2/aws-accounts` | 
[**delete_aws_account**](AWSApi.md#delete_aws_account) | **DELETE** `/api/2/aws-accounts/{id}` | 
[**get_all_aws_accounts**](AWSApi.md#get_all_aws_accounts) | **GET** `/api/2/aws-accounts` | 
[**get_aws_account**](AWSApi.md#get_aws_account) | **GET** `/api/2/aws-accounts/{id}` | 
[**get_aws_account_buckets**](AWSApi.md#get_aws_account_buckets) | **GET** `/api/2/aws-accounts/{id}/buckets` | 
[**get_aws_account_sns_topics**](AWSApi.md#get_aws_account_sns_topics) | **GET** `/api/2/aws-accounts/{id}/sns/topics` | 
[**patch_aws_account**](AWSApi.md#patch_aws_account) | **PATCH** `/api/2/aws-accounts/{id}` | 
[**test_aws_account_credentials**](AWSApi.md#test_aws_account_credentials) | **POST** `/api/2/aws-accounts/test-credentials` | 
[**update_aws_account**](AWSApi.md#update_aws_account) | **PUT** `/api/2/aws-accounts/{id}` | 



***

# **create_aws_account**

    def create_aws_account(data) -> AWSAccount 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    data = elements_sdk.AWSAccount() # AWSAccount | 

    try:
        api_response = api_instance.create_aws_account(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->create_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AWSAccount**](AWSAccount.md)|  | 

### Return type

[**AWSAccount**](AWSAccount.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **delete_aws_account**

    def delete_aws_account(id) -> object 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    id = 56 # int | A unique integer value identifying this AWS Account.

    try:
        api_response = api_instance.delete_aws_account(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->delete_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AWS Account. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **get_all_aws_accounts**

    def get_all_aws_accounts(name=name, id=id, ordering=ordering, limit=limit, offset=offset) -> list[AWSAccount] 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    name = 'name_example' # str | Filter the returned list by `name`. (optional)
id = 3.4 # float | Filter the returned list by `id`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_aws_accounts(name=name, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->get_all_aws_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[AWSAccount]**](AWSAccount.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **get_aws_account**

    def get_aws_account(id) -> AWSAccount 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    id = 56 # int | A unique integer value identifying this AWS Account.

    try:
        api_response = api_instance.get_aws_account(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->get_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AWS Account. | 

### Return type

[**AWSAccount**](AWSAccount.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **get_aws_account_buckets**

    def get_aws_account_buckets(id) -> ListBuckets 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    id = 56 # int | A unique integer value identifying this AWS Account.

    try:
        api_response = api_instance.get_aws_account_buckets(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->get_aws_account_buckets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AWS Account. | 

### Return type

[**ListBuckets**](ListBuckets.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **get_aws_account_sns_topics**

    def get_aws_account_sns_topics(id) -> ListTopics 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    id = 56 # int | A unique integer value identifying this AWS Account.

    try:
        api_response = api_instance.get_aws_account_sns_topics(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->get_aws_account_sns_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AWS Account. | 

### Return type

[**ListTopics**](ListTopics.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **patch_aws_account**

    def patch_aws_account(id, data) -> AWSAccount 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    id = 56 # int | A unique integer value identifying this AWS Account.
data = elements_sdk.AWSAccountPartialUpdate() # AWSAccountPartialUpdate | 

    try:
        api_response = api_instance.patch_aws_account(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->patch_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AWS Account. | 
 **data** | [**AWSAccountPartialUpdate**](AWSAccountPartialUpdate.md)|  | 

### Return type

[**AWSAccount**](AWSAccount.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **test_aws_account_credentials**

    def test_aws_account_credentials(data) -> TestAWSCredentialsResponse 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    data = elements_sdk.TestAWSCredentialsRequest() # TestAWSCredentialsRequest | 

    try:
        api_response = api_instance.test_aws_account_credentials(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->test_aws_account_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TestAWSCredentialsRequest**](TestAWSCredentialsRequest.md)|  | 

### Return type

[**TestAWSCredentialsResponse**](TestAWSCredentialsResponse.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


***

# **update_aws_account**

    def update_aws_account(id, data) -> AWSAccount 



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.AWSApi(api_client)
    id = 56 # int | A unique integer value identifying this AWS Account.
data = elements_sdk.AWSAccount() # AWSAccount | 

    try:
        api_response = api_instance.update_aws_account(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AWSApi->update_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this AWS Account. | 
 **data** | [**AWSAccount**](AWSAccount.md)|  | 

### Return type

[**AWSAccount**](AWSAccount.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

