# elements_sdk.AWSApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_account**](AWSApi.md#create_aws_account) | **POST** `/api/2/aws-accounts` | 
[**delete_aws_account**](AWSApi.md#delete_aws_account) | **DELETE** `/api/2/aws-accounts/{id}` | 
[**get_all_aws_accounts**](AWSApi.md#get_all_aws_accounts) | **GET** `/api/2/aws-accounts` | 
[**get_aws_account**](AWSApi.md#get_aws_account) | **GET** `/api/2/aws-accounts/{id}` | 
[**get_aws_account_sns_topics**](AWSApi.md#get_aws_account_sns_topics) | **GET** `/api/2/aws-accounts/{id}/sns/topics` | 
[**patch_aws_account**](AWSApi.md#patch_aws_account) | **PATCH** `/api/2/aws-accounts/{id}` | 
[**update_aws_account**](AWSApi.md#update_aws_account) | **PUT** `/api/2/aws-accounts/{id}` | 


# **create_aws_account**
    def CloudAccountMini create_aws_account(cloud_account_mini_update)



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import aws_api
from elements_sdk.model.cloud_account_mini import CloudAccountMini
from elements_sdk.model.cloud_account_mini_update import CloudAccountMiniUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = aws_api.AWSApi(api_client)
    cloud_account_mini_update = CloudAccountMiniUpdate(
        provider="azure",
        name="name_example",
    ) # CloudAccountMiniUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_aws_account(cloud_account_mini_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AWSApi->create_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account_mini_update** | [**CloudAccountMiniUpdate**](CloudAccountMiniUpdate.md)|  |

### Return type

[**CloudAccountMini**](CloudAccountMini.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_aws_account**
    def delete_aws_account(id)



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import aws_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = aws_api.AWSApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_aws_account(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AWSApi->delete_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_aws_accounts**
    def [CloudAccountMini] get_all_aws_accounts()



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import aws_api
from elements_sdk.model.cloud_account_mini import CloudAccountMini
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = aws_api.AWSApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    id = 3.14 # float | Filter the returned list by `id`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_aws_accounts(name=name, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
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

[**[CloudAccountMini]**](CloudAccountMini.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_aws_account**
    def CloudAccountMini get_aws_account(id)



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import aws_api
from elements_sdk.model.cloud_account_mini import CloudAccountMini
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = aws_api.AWSApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aws_account(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AWSApi->get_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |

### Return type

[**CloudAccountMini**](CloudAccountMini.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_aws_account_sns_topics**
    def ListTopics get_aws_account_sns_topics(id)



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import aws_api
from elements_sdk.model.list_topics import ListTopics
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = aws_api.AWSApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.
    region = "region_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aws_account_sns_topics(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AWSApi->get_aws_account_sns_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aws_account_sns_topics(id, region=region)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AWSApi->get_aws_account_sns_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |
 **region** | **str**|  | [optional]

### Return type

[**ListTopics**](ListTopics.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_aws_account**
    def CloudAccountMini patch_aws_account(id, cloud_account_mini_partial_update)



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import aws_api
from elements_sdk.model.cloud_account_mini_partial_update import CloudAccountMiniPartialUpdate
from elements_sdk.model.cloud_account_mini import CloudAccountMini
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = aws_api.AWSApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.
    cloud_account_mini_partial_update = CloudAccountMiniPartialUpdate(
        provider="azure",
        name="name_example",
    ) # CloudAccountMiniPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_aws_account(id, cloud_account_mini_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AWSApi->patch_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |
 **cloud_account_mini_partial_update** | [**CloudAccountMiniPartialUpdate**](CloudAccountMiniPartialUpdate.md)|  |

### Return type

[**CloudAccountMini**](CloudAccountMini.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_aws_account**
    def CloudAccountMini update_aws_account(id, cloud_account_mini_update)



### Required permissions    * User account permission: `tasks:manage` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import aws_api
from elements_sdk.model.cloud_account_mini import CloudAccountMini
from elements_sdk.model.cloud_account_mini_update import CloudAccountMiniUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = aws_api.AWSApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud account.
    cloud_account_mini_update = CloudAccountMiniUpdate(
        provider="azure",
        name="name_example",
    ) # CloudAccountMiniUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_aws_account(id, cloud_account_mini_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AWSApi->update_aws_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud account. |
 **cloud_account_mini_update** | [**CloudAccountMiniUpdate**](CloudAccountMiniUpdate.md)|  |

### Return type

[**CloudAccountMini**](CloudAccountMini.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

