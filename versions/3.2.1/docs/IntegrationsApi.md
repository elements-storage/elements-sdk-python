# elements_sdk.IntegrationsApi

All URIs are relative to *http://localhost*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_slack_connection**](IntegrationsApi.md#delete_slack_connection) | **DELETE** `/api/2/integrations/slack/{id}` | 
[**delete_teams_connection**](IntegrationsApi.md#delete_teams_connection) | **DELETE** `/api/2/integrations/teams/{id}` | 
[**get_all_slack_connections**](IntegrationsApi.md#get_all_slack_connections) | **GET** `/api/2/integrations/slack` | 
[**get_all_teams_connections**](IntegrationsApi.md#get_all_teams_connections) | **GET** `/api/2/integrations/teams` | 
[**get_slack_channels**](IntegrationsApi.md#get_slack_channels) | **GET** `/api/2/integrations/slack/{id}/channels` | 
[**get_slack_connection**](IntegrationsApi.md#get_slack_connection) | **GET** `/api/2/integrations/slack/{id}` | 
[**get_slack_emoji**](IntegrationsApi.md#get_slack_emoji) | **GET** `/api/2/integrations/slack/{id}/emoji` | 
[**get_slack_users**](IntegrationsApi.md#get_slack_users) | **GET** `/api/2/integrations/slack/{id}/users` | 
[**get_teams_channels**](IntegrationsApi.md#get_teams_channels) | **GET** `/api/2/integrations/teams/{id}/channels` | 
[**get_teams_connection**](IntegrationsApi.md#get_teams_connection) | **GET** `/api/2/integrations/teams/{id}` | 
[**get_teams_users**](IntegrationsApi.md#get_teams_users) | **GET** `/api/2/integrations/teams/{id}/users` | 
[**patch_slack_connection**](IntegrationsApi.md#patch_slack_connection) | **PATCH** `/api/2/integrations/slack/{id}` | 
[**patch_teams_connection**](IntegrationsApi.md#patch_teams_connection) | **PATCH** `/api/2/integrations/teams/{id}` | 
[**send_slack_message**](IntegrationsApi.md#send_slack_message) | **POST** `/api/2/integrations/slack/{id}/message` | 
[**send_teams_message**](IntegrationsApi.md#send_teams_message) | **POST** `/api/2/integrations/teams/{id}/send-message` | 
[**start_slack_connection_flow**](IntegrationsApi.md#start_slack_connection_flow) | **GET** `/api/2/integrations/slack/connect` | 
[**start_slack_connection_token_refresh_flow**](IntegrationsApi.md#start_slack_connection_token_refresh_flow) | **GET** `/api/2/integrations/slack/{id}/refresh-token` | 
[**start_teams_connection_flow**](IntegrationsApi.md#start_teams_connection_flow) | **GET** `/api/2/integrations/teams/connect` | 
[**start_teams_connection_token_refresh_flow**](IntegrationsApi.md#start_teams_connection_token_refresh_flow) | **GET** `/api/2/integrations/teams/{id}/refresh-token` | 
[**update_slack_connection**](IntegrationsApi.md#update_slack_connection) | **PUT** `/api/2/integrations/slack/{id}` | 
[**update_teams_connection**](IntegrationsApi.md#update_teams_connection) | **PUT** `/api/2/integrations/teams/{id}` | 



***

# **delete_slack_connection**

    def delete_slack_connection(id) -> object 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.

    try:
        api_response = api_instance.delete_slack_connection(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->delete_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_teams_connection**

    def delete_teams_connection(id) -> object 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.

    try:
        api_response = api_instance.delete_teams_connection(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->delete_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_slack_connections**

    def get_all_slack_connections(ordering=ordering, limit=limit, offset=offset) -> list[SlackConnection] 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_slack_connections(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_all_slack_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[SlackConnection]**](SlackConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_teams_connections**

    def get_all_teams_connections(ordering=ordering, limit=limit, offset=offset) -> list[TeamsConnection] 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_teams_connections(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_all_teams_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[TeamsConnection]**](TeamsConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_slack_channels**

    def get_slack_channels(id) -> list[SlackChannel] 



### Required permissions    * User account permission: `tasks:manage` 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.

    try:
        api_response = api_instance.get_slack_channels(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 

### Return type

[**list[SlackChannel]**](SlackChannel.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_slack_connection**

    def get_slack_connection(id) -> SlackConnection 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.

    try:
        api_response = api_instance.get_slack_connection(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 

### Return type

[**SlackConnection**](SlackConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_slack_emoji**

    def get_slack_emoji(id) -> list[SlackEmoji] 



### Required permissions    * User account permission: `tasks:manage` 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.

    try:
        api_response = api_instance.get_slack_emoji(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_emoji: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 

### Return type

[**list[SlackEmoji]**](SlackEmoji.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_slack_users**

    def get_slack_users(id) -> list[SlackUser] 



### Required permissions    * User account permission: `tasks:manage` 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.

    try:
        api_response = api_instance.get_slack_users(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 

### Return type

[**list[SlackUser]**](SlackUser.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_teams_channels**

    def get_teams_channels(id) -> list[TeamsRecipient] 



### Required permissions    * User account permission: `tasks:manage` 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.

    try:
        api_response = api_instance.get_teams_channels(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_teams_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 

### Return type

[**list[TeamsRecipient]**](TeamsRecipient.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_teams_connection**

    def get_teams_connection(id) -> TeamsConnection 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.

    try:
        api_response = api_instance.get_teams_connection(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 

### Return type

[**TeamsConnection**](TeamsConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_teams_users**

    def get_teams_users(id) -> list[TeamsRecipient] 



### Required permissions    * User account permission: `tasks:manage` 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.

    try:
        api_response = api_instance.get_teams_users(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->get_teams_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 

### Return type

[**list[TeamsRecipient]**](TeamsRecipient.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_slack_connection**

    def patch_slack_connection(id, data) -> SlackConnection 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.
data = elements_sdk.SlackConnectionPartialUpdate() # SlackConnectionPartialUpdate | 

    try:
        api_response = api_instance.patch_slack_connection(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->patch_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 
 **data** | [**SlackConnectionPartialUpdate**](SlackConnectionPartialUpdate.md)|  | 

### Return type

[**SlackConnection**](SlackConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_teams_connection**

    def patch_teams_connection(id, data) -> TeamsConnection 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.
data = elements_sdk.TeamsConnectionPartialUpdate() # TeamsConnectionPartialUpdate | 

    try:
        api_response = api_instance.patch_teams_connection(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->patch_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 
 **data** | [**TeamsConnectionPartialUpdate**](TeamsConnectionPartialUpdate.md)|  | 

### Return type

[**TeamsConnection**](TeamsConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **send_slack_message**

    def send_slack_message(id, data) -> object 



### Required permissions    * User account permission: `tasks:manage` 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.
data = elements_sdk.SlackMessage() # SlackMessage | 

    try:
        api_response = api_instance.send_slack_message(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->send_slack_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 
 **data** | [**SlackMessage**](SlackMessage.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **send_teams_message**

    def send_teams_message(id, data) -> object 



### Required permissions    * User account permission: `tasks:manage` 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.
data = elements_sdk.TeamsMessage() # TeamsMessage | 

    try:
        api_response = api_instance.send_teams_message(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->send_teams_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 
 **data** | [**TeamsMessage**](TeamsMessage.md)|  | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_slack_connection_flow**

    def start_slack_connection_flow(ordering=ordering, limit=limit, offset=offset) -> object 



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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.start_slack_connection_flow(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->start_slack_connection_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_slack_connection_token_refresh_flow**

    def start_slack_connection_token_refresh_flow(id) -> object 



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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.

    try:
        api_response = api_instance.start_slack_connection_token_refresh_flow(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->start_slack_connection_token_refresh_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_teams_connection_flow**

    def start_teams_connection_flow(ordering=ordering, limit=limit, offset=offset, team=team)



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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
team = 'team_example' # str |  (optional)

    try:
        api_instance.start_teams_connection_flow(ordering=ordering, limit=limit, offset=offset, team=team)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->start_teams_connection_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **team** | **str**|  | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **start_teams_connection_token_refresh_flow**

    def start_teams_connection_token_refresh_flow(id, team=team)



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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.
team = 'team_example' # str |  (optional)

    try:
        api_instance.start_teams_connection_token_refresh_flow(id, team=team)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->start_teams_connection_token_refresh_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 
 **team** | **str**|  | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_slack_connection**

    def update_slack_connection(id, data) -> SlackConnection 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Slack connection.
data = elements_sdk.SlackConnection() # SlackConnection | 

    try:
        api_response = api_instance.update_slack_connection(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->update_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. | 
 **data** | [**SlackConnection**](SlackConnection.md)|  | 

### Return type

[**SlackConnection**](SlackConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_teams_connection**

    def update_teams_connection(id, data) -> TeamsConnection 



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

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
    api_instance = elements_sdk.IntegrationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Teams connection.
data = elements_sdk.TeamsConnection() # TeamsConnection | 

    try:
        api_response = api_instance.update_teams_connection(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsApi->update_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. | 
 **data** | [**TeamsConnection**](TeamsConnection.md)|  | 

### Return type

[**TeamsConnection**](TeamsConnection.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

