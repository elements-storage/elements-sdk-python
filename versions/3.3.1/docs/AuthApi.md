# elements_sdk.AuthApi

All URIs are relative to *http://localhost*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**check_auth_ticket**](AuthApi.md#check_auth_ticket) | **POST** `/api/2/auth/ticket/check` | 
[**create_auth_ticket**](AuthApi.md#create_auth_ticket) | **POST** `/api/2/auth/ticket` | 
[**delete_access_token**](AuthApi.md#delete_access_token) | **DELETE** `/api/2/auth/access-tokens/{id}` | 
[**generate_password**](AuthApi.md#generate_password) | **POST** `/api/2/auth/generate-password` | 
[**get_access_token**](AuthApi.md#get_access_token) | **GET** `/api/2/auth/access-tokens/{id}` | 
[**get_all_access_tokens**](AuthApi.md#get_all_access_tokens) | **GET** `/api/2/auth/access-tokens` | 
[**login**](AuthApi.md#login) | **POST** `/api/2/auth/login` | 
[**logout**](AuthApi.md#logout) | **POST** `/api/2/auth/logout` | 
[**reset_password**](AuthApi.md#reset_password) | **POST** `/api/2/auth/reset-password` | 
[**send_access_token_email_notification**](AuthApi.md#send_access_token_email_notification) | **POST** `/api/2/auth/access-tokens/{id}/email` | 
[**start_impersonation**](AuthApi.md#start_impersonation) | **POST** `/api/2/auth/impersonation` | 
[**stop_impersonation**](AuthApi.md#stop_impersonation) | **POST** `/api/2/auth/impersonation/stop` | 



***

# **check_auth_ticket**

    def check_auth_ticket(data) -> ElementsUserDetail 



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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    data = elements_sdk.Ticket() # Ticket | 

    try:
        api_response = api_instance.check_auth_ticket(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->check_auth_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Ticket**](Ticket.md)|  | 

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_auth_ticket**

    def create_auth_ticket() -> Ticket 



### Required permissions    * Authenticated user 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    
    try:
        api_response = api_instance.create_auth_ticket()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->create_auth_ticket: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**Ticket**](Ticket.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_access_token**

    def delete_access_token(id) -> object 



### Required permissions    * Authenticated user 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    id = 56 # int | A unique integer value identifying this one time access token.

    try:
        api_response = api_instance.delete_access_token(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->delete_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this one time access token. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **generate_password**

    def generate_password() -> GeneratePasswordEndpointResponse 



### Required permissions    * Authenticated user 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    
    try:
        api_response = api_instance.generate_password()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->generate_password: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

[**GeneratePasswordEndpointResponse**](GeneratePasswordEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_access_token**

    def get_access_token(id) -> OneTimeAccessToken 



### Required permissions    * Authenticated user 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    id = 56 # int | A unique integer value identifying this one time access token.

    try:
        api_response = api_instance.get_access_token(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->get_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this one time access token. | 

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_access_tokens**

    def get_all_access_tokens(shared_bundles=shared_bundles, shared_directories=shared_directories, shared_bundles__asset=shared_bundles__asset, user=user, created_by=created_by, ordering=ordering, limit=limit, offset=offset) -> list[OneTimeAccessToken] 



### Required permissions    * Authenticated user 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    shared_bundles = 'shared_bundles_example' # str | Filter the returned list by `shared_bundles`. (optional)
shared_directories = 'shared_directories_example' # str | Filter the returned list by `shared_directories`. (optional)
shared_bundles__asset = 'shared_bundles__asset_example' # str | Filter the returned list by `shared_bundles__asset`. (optional)
user = 'user_example' # str | Filter the returned list by `user`. (optional)
created_by = 'created_by_example' # str | Filter the returned list by `created_by`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_access_tokens(shared_bundles=shared_bundles, shared_directories=shared_directories, shared_bundles__asset=shared_bundles__asset, user=user, created_by=created_by, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->get_all_access_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_bundles** | **str**| Filter the returned list by &#x60;shared_bundles&#x60;. | [optional] 
 **shared_directories** | **str**| Filter the returned list by &#x60;shared_directories&#x60;. | [optional] 
 **shared_bundles__asset** | **str**| Filter the returned list by &#x60;shared_bundles__asset&#x60;. | [optional] 
 **user** | **str**| Filter the returned list by &#x60;user&#x60;. | [optional] 
 **created_by** | **str**| Filter the returned list by &#x60;created_by&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[OneTimeAccessToken]**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **login**

    def login(data) -> AuthLoginEndpointResponse 



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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    data = elements_sdk.AuthLoginEndpointRequest() # AuthLoginEndpointRequest | 

    try:
        api_response = api_instance.login(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AuthLoginEndpointRequest**](AuthLoginEndpointRequest.md)|  | 

### Return type

[**AuthLoginEndpointResponse**](AuthLoginEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **logout**

    def logout() -> object 



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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    
    try:
        api_response = api_instance.logout()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->logout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **reset_password**

    def reset_password(data) -> object 



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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    data = elements_sdk.PasswordResetEndpointRequest() # PasswordResetEndpointRequest | 

    try:
        api_response = api_instance.reset_password(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->reset_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PasswordResetEndpointRequest**](PasswordResetEndpointRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **send_access_token_email_notification**

    def send_access_token_email_notification(id, data) -> object 



### Required permissions    * Authenticated user 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    id = 56 # int | A unique integer value identifying this one time access token.
data = elements_sdk.SendLinkEmailRequest() # SendLinkEmailRequest | 

    try:
        api_response = api_instance.send_access_token_email_notification(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->send_access_token_email_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this one time access token. | 
 **data** | [**SendLinkEmailRequest**](SendLinkEmailRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_impersonation**

    def start_impersonation(data) -> object 



### Required permissions    * User account permission: `system:admin-access` 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    data = elements_sdk.ImpersonationEndpointRequest() # ImpersonationEndpointRequest | 

    try:
        api_response = api_instance.start_impersonation(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->start_impersonation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImpersonationEndpointRequest**](ImpersonationEndpointRequest.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **stop_impersonation**

    def stop_impersonation() -> object 



### Required permissions    * Authenticated user 

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

configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with elements_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = elements_sdk.AuthApi(api_client)
    
    try:
        api_response = api_instance.stop_impersonation()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->stop_impersonation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameters.

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

