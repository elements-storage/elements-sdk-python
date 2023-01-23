# elements_sdk.AuthApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**check_auth_ticket**](AuthApi.md#check_auth_ticket) | **POST** `/api/2/auth/ticket/check` | 
[**create_api_token**](AuthApi.md#create_api_token) | **POST** `/api/2/api-tokens` | 
[**create_auth_ticket**](AuthApi.md#create_auth_ticket) | **POST** `/api/2/auth/ticket` | 
[**create_saml_provider**](AuthApi.md#create_saml_provider) | **POST** `/api/2/auth/saml` | 
[**delete_access_token**](AuthApi.md#delete_access_token) | **DELETE** `/api/2/auth/access-tokens/{id}` | 
[**delete_api_token**](AuthApi.md#delete_api_token) | **DELETE** `/api/2/api-tokens/{id}` | 
[**delete_saml_provider**](AuthApi.md#delete_saml_provider) | **DELETE** `/api/2/auth/saml/{id}` | 
[**generate_password**](AuthApi.md#generate_password) | **POST** `/api/2/auth/generate-password` | 
[**get_access_token**](AuthApi.md#get_access_token) | **GET** `/api/2/auth/access-tokens/{id}` | 
[**get_all_access_tokens**](AuthApi.md#get_all_access_tokens) | **GET** `/api/2/auth/access-tokens` | 
[**get_all_api_tokens**](AuthApi.md#get_all_api_tokens) | **GET** `/api/2/api-tokens` | 
[**get_all_saml_providers**](AuthApi.md#get_all_saml_providers) | **GET** `/api/2/auth/saml` | 
[**get_api_token**](AuthApi.md#get_api_token) | **GET** `/api/2/api-tokens/{id}` | 
[**get_saml_provider**](AuthApi.md#get_saml_provider) | **GET** `/api/2/auth/saml/{id}` | 
[**get_saml_service_provider_metadata**](AuthApi.md#get_saml_service_provider_metadata) | **GET** `/api/2/auth/saml/{id}/metadata` | 
[**login**](AuthApi.md#login) | **POST** `/api/2/auth/login` | 
[**logout**](AuthApi.md#logout) | **POST** `/api/2/auth/logout` | 
[**logout_page**](AuthApi.md#logout_page) | **GET** `/api/2/auth/logout` | 
[**parse_samlidp_metadata**](AuthApi.md#parse_samlidp_metadata) | **POST** `/api/2/auth/saml/parse-idp-metadata` | 
[**patch_api_token**](AuthApi.md#patch_api_token) | **PATCH** `/api/2/api-tokens/{id}` | 
[**patch_saml_provider**](AuthApi.md#patch_saml_provider) | **PATCH** `/api/2/auth/saml/{id}` | 
[**receive_saml_auth_assertion**](AuthApi.md#receive_saml_auth_assertion) | **POST** `/api/2/auth/saml/{id}/assertion` | 
[**refresh_samlidp_metadata**](AuthApi.md#refresh_samlidp_metadata) | **POST** `/api/2/auth/saml/{id}/refresh-idp-metadata` | 
[**reset_password**](AuthApi.md#reset_password) | **POST** `/api/2/auth/reset-password` | 
[**return_from_saml_auth**](AuthApi.md#return_from_saml_auth) | **GET** `/api/2/auth/saml/{id}/sso/return` | 
[**return_from_saml_logout**](AuthApi.md#return_from_saml_logout) | **GET** `/api/2/auth/saml/{id}/sls/return` | 
[**send_access_token_email_notification**](AuthApi.md#send_access_token_email_notification) | **POST** `/api/2/auth/access-tokens/{id}/email` | 
[**start_impersonation**](AuthApi.md#start_impersonation) | **POST** `/api/2/auth/impersonation` | 
[**start_saml_auth**](AuthApi.md#start_saml_auth) | **GET** `/api/2/auth/saml/{id}/sso` | 
[**start_saml_logout**](AuthApi.md#start_saml_logout) | **GET** `/api/2/auth/saml/{id}/sls` | 
[**stop_impersonation**](AuthApi.md#stop_impersonation) | **POST** `/api/2/auth/impersonation/stop` | 
[**update_api_token**](AuthApi.md#update_api_token) | **PUT** `/api/2/api-tokens/{id}` | 
[**update_saml_provider**](AuthApi.md#update_saml_provider) | **PUT** `/api/2/auth/saml/{id}` | 


# **check_auth_ticket**
    def ElementsUserDetail check_auth_ticket(ticket)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.elements_user_detail import ElementsUserDetail
from elements_sdk.model.ticket import Ticket
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    ticket = Ticket(
        ticket="ticket_example",
    ) # Ticket | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.check_auth_ticket(ticket)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->check_auth_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**Ticket**](Ticket.md)|  |

### Return type

[**ElementsUserDetail**](ElementsUserDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_api_token**
    def APITokenWithSecret create_api_token(api_token_with_secret_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.api_token_with_secret_update import APITokenWithSecretUpdate
from elements_sdk.model.api_token_with_secret import APITokenWithSecret
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    api_token_with_secret_update = APITokenWithSecretUpdate(
        token="token_example",
        name="name_example",
    ) # APITokenWithSecretUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_api_token(api_token_with_secret_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->create_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_with_secret_update** | [**APITokenWithSecretUpdate**](APITokenWithSecretUpdate.md)|  |

### Return type

[**APITokenWithSecret**](APITokenWithSecret.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_auth_ticket**
    def Ticket create_auth_ticket()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.ticket import Ticket
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_auth_ticket()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->create_auth_ticket: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Ticket**](Ticket.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_saml_provider**
    def SAMLProvider create_saml_provider(saml_provider_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.saml_provider_update import SAMLProviderUpdate
from elements_sdk.model.saml_provider import SAMLProvider
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    saml_provider_update = SAMLProviderUpdate(
        name="name_example",
        entity_id="entity_id_example",
        sso_url="sso_url_example",
        slo_url="slo_url_example",
        certificate="certificate_example",
        sp_certificate="sp_certificate_example",
        sp_certificate_key="sp_certificate_key_example",
        nameid_format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    ) # SAMLProviderUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_saml_provider(saml_provider_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->create_saml_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_provider_update** | [**SAMLProviderUpdate**](SAMLProviderUpdate.md)|  |

### Return type

[**SAMLProvider**](SAMLProvider.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_access_token**
    def delete_access_token(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this one time access token.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_access_token(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->delete_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this one time access token. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_api_token**
    def delete_api_token(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this api token.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_api_token(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->delete_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this api token. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_saml_provider**
    def delete_saml_provider(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_saml_provider(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->delete_saml_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **generate_password**
    def GeneratePasswordEndpointResponse generate_password()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.generate_password_endpoint_response import GeneratePasswordEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_password()
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->generate_password: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneratePasswordEndpointResponse**](GeneratePasswordEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_access_token**
    def OneTimeAccessToken get_access_token(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.one_time_access_token import OneTimeAccessToken
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this one time access token.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_access_token(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->get_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this one time access token. |

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_access_tokens**
    def [OneTimeAccessToken] get_all_access_tokens()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.one_time_access_token import OneTimeAccessToken
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    shared_bundles = "shared_bundles_example" # str | Filter the returned list by `shared_bundles`. (optional)
    shared_directories = "shared_directories_example" # str | Filter the returned list by `shared_directories`. (optional)
    shared_bundles__asset = 3.14 # float | Filter the returned list by `shared_bundles__asset`. (optional)
    user = 3.14 # float | Filter the returned list by `user`. (optional)
    created_by = 3.14 # float | Filter the returned list by `created_by`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_access_tokens(shared_bundles=shared_bundles, shared_directories=shared_directories, shared_bundles__asset=shared_bundles__asset, user=user, created_by=created_by, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->get_all_access_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_bundles** | **str**| Filter the returned list by &#x60;shared_bundles&#x60;. | [optional]
 **shared_directories** | **str**| Filter the returned list by &#x60;shared_directories&#x60;. | [optional]
 **shared_bundles__asset** | **float**| Filter the returned list by &#x60;shared_bundles__asset&#x60;. | [optional]
 **user** | **float**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **created_by** | **float**| Filter the returned list by &#x60;created_by&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[OneTimeAccessToken]**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_api_tokens**
    def [APIToken] get_all_api_tokens()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.api_token import APIToken
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_api_tokens(name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->get_all_api_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[APIToken]**](APIToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_saml_providers**
    def [SAMLProvider] get_all_saml_providers()



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.saml_provider import SAMLProvider
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_saml_providers(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->get_all_saml_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[SAMLProvider]**](SAMLProvider.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_api_token**
    def APIToken get_api_token(id)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.api_token import APIToken
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this api token.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_api_token(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->get_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this api token. |

### Return type

[**APIToken**](APIToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_saml_provider**
    def SAMLProvider get_saml_provider(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.saml_provider import SAMLProvider
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_saml_provider(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->get_saml_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

[**SAMLProvider**](SAMLProvider.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_saml_service_provider_metadata**
    def get_saml_service_provider_metadata(id)



### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_saml_service_provider_metadata(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->get_saml_service_provider_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **login**
    def AuthLoginEndpointResponse login(auth_login_endpoint_request)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.auth_login_endpoint_request import AuthLoginEndpointRequest
from elements_sdk.model.auth_login_endpoint_response import AuthLoginEndpointResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    auth_login_endpoint_request = AuthLoginEndpointRequest(
        username="username_example",
        password="password_example",
        otp="otp_example",
        new_password="new_password_example",
    ) # AuthLoginEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.login(auth_login_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login_endpoint_request** | [**AuthLoginEndpointRequest**](AuthLoginEndpointRequest.md)|  |

### Return type

[**AuthLoginEndpointResponse**](AuthLoginEndpointResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **logout**
    def logout()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.logout()
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->logout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **logout_page**
    def logout_page()



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.logout_page()
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->logout_page: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **parse_samlidp_metadata**
    def ParsedSAMLIDPMetadata parse_samlidp_metadata(parse_samlidp_metadata_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.parse_samlidp_metadata_request import ParseSAMLIDPMetadataRequest
from elements_sdk.model.parsed_samlidp_metadata import ParsedSAMLIDPMetadata
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    parse_samlidp_metadata_request = ParseSAMLIDPMetadataRequest(
        url="url_example",
    ) # ParseSAMLIDPMetadataRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.parse_samlidp_metadata(parse_samlidp_metadata_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->parse_samlidp_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parse_samlidp_metadata_request** | [**ParseSAMLIDPMetadataRequest**](ParseSAMLIDPMetadataRequest.md)|  |

### Return type

[**ParsedSAMLIDPMetadata**](ParsedSAMLIDPMetadata.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_api_token**
    def APIToken patch_api_token(id, api_token_partial_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.api_token import APIToken
from elements_sdk.model.api_token_partial_update import APITokenPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this api token.
    api_token_partial_update = APITokenPartialUpdate(
        name="name_example",
    ) # APITokenPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_api_token(id, api_token_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->patch_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this api token. |
 **api_token_partial_update** | [**APITokenPartialUpdate**](APITokenPartialUpdate.md)|  |

### Return type

[**APIToken**](APIToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_saml_provider**
    def SAMLProvider patch_saml_provider(id, saml_provider_partial_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.saml_provider_partial_update import SAMLProviderPartialUpdate
from elements_sdk.model.saml_provider import SAMLProvider
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.
    saml_provider_partial_update = SAMLProviderPartialUpdate(
        name="name_example",
        entity_id="entity_id_example",
        sso_url="sso_url_example",
        slo_url="slo_url_example",
        certificate="certificate_example",
        sp_certificate="sp_certificate_example",
        sp_certificate_key="sp_certificate_key_example",
        nameid_format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    ) # SAMLProviderPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_saml_provider(id, saml_provider_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->patch_saml_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |
 **saml_provider_partial_update** | [**SAMLProviderPartialUpdate**](SAMLProviderPartialUpdate.md)|  |

### Return type

[**SAMLProvider**](SAMLProvider.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **receive_saml_auth_assertion**
    def receive_saml_auth_assertion(id)



### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_instance.receive_saml_auth_assertion(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->receive_saml_auth_assertion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **refresh_samlidp_metadata**
    def ParsedSAMLIDPMetadata refresh_samlidp_metadata(id, parse_samlidp_metadata_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.parse_samlidp_metadata_request import ParseSAMLIDPMetadataRequest
from elements_sdk.model.parsed_samlidp_metadata import ParsedSAMLIDPMetadata
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.
    parse_samlidp_metadata_request = ParseSAMLIDPMetadataRequest(
        url="url_example",
    ) # ParseSAMLIDPMetadataRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.refresh_samlidp_metadata(id, parse_samlidp_metadata_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->refresh_samlidp_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |
 **parse_samlidp_metadata_request** | [**ParseSAMLIDPMetadataRequest**](ParseSAMLIDPMetadataRequest.md)|  |

### Return type

[**ParsedSAMLIDPMetadata**](ParsedSAMLIDPMetadata.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **reset_password**
    def reset_password(password_reset_endpoint_request)



### Required permissions    * <class 'rest_framework.permissions.AllowAny'> 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.password_reset_endpoint_request import PasswordResetEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    password_reset_endpoint_request = PasswordResetEndpointRequest(
        token="token_example",
        password="password_example",
    ) # PasswordResetEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.reset_password(password_reset_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->reset_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_endpoint_request** | [**PasswordResetEndpointRequest**](PasswordResetEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **return_from_saml_auth**
    def return_from_saml_auth(id)



### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_instance.return_from_saml_auth(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->return_from_saml_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **return_from_saml_logout**
    def return_from_saml_logout(id)



### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_instance.return_from_saml_logout(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->return_from_saml_logout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **send_access_token_email_notification**
    def send_access_token_email_notification(id, send_link_email_request)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.send_link_email_request import SendLinkEmailRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this one time access token.
    send_link_email_request = SendLinkEmailRequest(
        email="email_example",
        subject="subject_example",
        text="text_example",
    ) # SendLinkEmailRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.send_access_token_email_notification(id, send_link_email_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->send_access_token_email_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this one time access token. |
 **send_link_email_request** | [**SendLinkEmailRequest**](SendLinkEmailRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_impersonation**
    def start_impersonation(impersonation_endpoint_request)



### Required permissions    * User account permission: `system:admin-access` 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.impersonation_endpoint_request import ImpersonationEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    impersonation_endpoint_request = ImpersonationEndpointRequest(
        user=1,
    ) # ImpersonationEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.start_impersonation(impersonation_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->start_impersonation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **impersonation_endpoint_request** | [**ImpersonationEndpointRequest**](ImpersonationEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_saml_auth**
    def start_saml_auth(id)



### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_instance.start_saml_auth(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->start_saml_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_saml_logout**
    def start_saml_logout(id)



### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.

    # example passing only required values which don't have defaults set
    try:
        api_instance.start_saml_logout(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->start_saml_logout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **stop_impersonation**
    def stop_impersonation()



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.stop_impersonation()
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->stop_impersonation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_api_token**
    def APIToken update_api_token(id, api_token_update)



### Required permissions    * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.api_token import APIToken
from elements_sdk.model.api_token_update import APITokenUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this api token.
    api_token_update = APITokenUpdate(
        name="name_example",
    ) # APITokenUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_api_token(id, api_token_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->update_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this api token. |
 **api_token_update** | [**APITokenUpdate**](APITokenUpdate.md)|  |

### Return type

[**APIToken**](APIToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_saml_provider**
    def SAMLProvider update_saml_provider(id, saml_provider_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import auth_api
from elements_sdk.model.saml_provider_update import SAMLProviderUpdate
from elements_sdk.model.saml_provider import SAMLProvider
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = auth_api.AuthApi(api_client)
    id = 1 # int | A unique integer value identifying this SAML Provider.
    saml_provider_update = SAMLProviderUpdate(
        name="name_example",
        entity_id="entity_id_example",
        sso_url="sso_url_example",
        slo_url="slo_url_example",
        certificate="certificate_example",
        sp_certificate="sp_certificate_example",
        sp_certificate_key="sp_certificate_key_example",
        nameid_format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
    ) # SAMLProviderUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_saml_provider(id, saml_provider_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling AuthApi->update_saml_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. |
 **saml_provider_update** | [**SAMLProviderUpdate**](SAMLProviderUpdate.md)|  |

### Return type

[**SAMLProvider**](SAMLProvider.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

