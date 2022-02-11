# elements_sdk.IntegrationsApi

All URIs are relative to *https://elements.local*

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


# **delete_slack_connection**
> delete_slack_connection(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_slack_connection(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->delete_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_teams_connection**
> delete_teams_connection(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_teams_connection(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->delete_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_slack_connections**
> [SlackConnection] get_all_slack_connections()



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_connection import SlackConnection
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_slack_connections(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_all_slack_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[SlackConnection]**](SlackConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_teams_connections**
> [TeamsConnection] get_all_teams_connections()



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.teams_connection import TeamsConnection
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_teams_connections(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_all_teams_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[TeamsConnection]**](TeamsConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_slack_channels**
> [SlackChannel] get_slack_channels(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_channel import SlackChannel
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_slack_channels(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |

### Return type

[**[SlackChannel]**](SlackChannel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_slack_connection**
> SlackConnection get_slack_connection(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_connection import SlackConnection
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_slack_connection(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |

### Return type

[**SlackConnection**](SlackConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_slack_emoji**
> [SlackEmoji] get_slack_emoji(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_emoji import SlackEmoji
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_slack_emoji(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_emoji: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |

### Return type

[**[SlackEmoji]**](SlackEmoji.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_slack_users**
> [SlackUser] get_slack_users(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_user import SlackUser
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_slack_users(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_slack_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |

### Return type

[**[SlackUser]**](SlackUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_teams_channels**
> [TeamsRecipient] get_teams_channels(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.teams_recipient import TeamsRecipient
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_teams_channels(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_teams_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |

### Return type

[**[TeamsRecipient]**](TeamsRecipient.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_teams_connection**
> TeamsConnection get_teams_connection(id)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.teams_connection import TeamsConnection
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_teams_connection(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |

### Return type

[**TeamsConnection**](TeamsConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_teams_users**
> [TeamsRecipient] get_teams_users(id)



### Required permissions    * User account permission: `tasks:manage` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.teams_recipient import TeamsRecipient
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_teams_users(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->get_teams_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |

### Return type

[**[TeamsRecipient]**](TeamsRecipient.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_slack_connection**
> SlackConnection patch_slack_connection(id, slack_connection_partial_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_connection_partial_update import SlackConnectionPartialUpdate
from elements_sdk.model.slack_connection import SlackConnection
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.
    slack_connection_partial_update = SlackConnectionPartialUpdate(
        name="name_example",
    ) # SlackConnectionPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_slack_connection(id, slack_connection_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->patch_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |
 **slack_connection_partial_update** | [**SlackConnectionPartialUpdate**](SlackConnectionPartialUpdate.md)|  |

### Return type

[**SlackConnection**](SlackConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_teams_connection**
> TeamsConnection patch_teams_connection(id, teams_connection_partial_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.teams_connection import TeamsConnection
from elements_sdk.model.teams_connection_partial_update import TeamsConnectionPartialUpdate
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.
    teams_connection_partial_update = TeamsConnectionPartialUpdate(
        name="name_example",
    ) # TeamsConnectionPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_teams_connection(id, teams_connection_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->patch_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |
 **teams_connection_partial_update** | [**TeamsConnectionPartialUpdate**](TeamsConnectionPartialUpdate.md)|  |

### Return type

[**TeamsConnection**](TeamsConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **send_slack_message**
> send_slack_message(id, slack_message)



### Required permissions    * User account permission: `tasks:manage` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_message import SlackMessage
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.
    slack_message = SlackMessage(
        recipient="recipient_example",
        text="text_example",
        username="username_example",
        emoji="emoji_example",
    ) # SlackMessage | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.send_slack_message(id, slack_message)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->send_slack_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |
 **slack_message** | [**SlackMessage**](SlackMessage.md)|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **send_teams_message**
> send_teams_message(id, teams_message)



### Required permissions    * User account permission: `tasks:manage` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.teams_message import TeamsMessage
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.
    teams_message = TeamsMessage(
        recipient="recipient_example",
        text="text_example",
    ) # TeamsMessage | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.send_teams_message(id, teams_message)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->send_teams_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |
 **teams_message** | [**TeamsMessage**](TeamsMessage.md)|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_slack_connection_flow**
> start_slack_connection_flow()



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.start_slack_connection_flow(ordering=ordering, limit=limit, offset=offset)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->start_slack_connection_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_slack_connection_token_refresh_flow**
> start_slack_connection_token_refresh_flow(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.

    # example passing only required values which don't have defaults set
    try:
        api_instance.start_slack_connection_token_refresh_flow(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->start_slack_connection_token_refresh_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No body |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_teams_connection_flow**
> start_teams_connection_flow()



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    team = "team_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.start_teams_connection_flow(ordering=ordering, limit=limit, offset=offset, team=team)
    except elements_sdk.ApiException as e:
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

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**301** | Redirects to setup page |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **start_teams_connection_token_refresh_flow**
> start_teams_connection_token_refresh_flow(id)



### Required permissions    * User account permission: `system:admin-access` 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.
    team = "team_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.start_teams_connection_token_refresh_flow(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->start_teams_connection_token_refresh_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.start_teams_connection_token_refresh_flow(id, team=team)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->start_teams_connection_token_refresh_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |
 **team** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**301** | Redirects to setup page |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_slack_connection**
> SlackConnection update_slack_connection(id, slack_connection_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.slack_connection_update import SlackConnectionUpdate
from elements_sdk.model.slack_connection import SlackConnection
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Slack connection.
    slack_connection_update = SlackConnectionUpdate(
        name="name_example",
    ) # SlackConnectionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_slack_connection(id, slack_connection_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->update_slack_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Slack connection. |
 **slack_connection_update** | [**SlackConnectionUpdate**](SlackConnectionUpdate.md)|  |

### Return type

[**SlackConnection**](SlackConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_teams_connection**
> TeamsConnection update_teams_connection(id, teams_connection_update)



### Required permissions    * User account permission: `None` (read) / `system:admin-access` (write) 

### Example

* Api Key Authentication (Bearer):
```python
import elements_sdk
from elements_sdk.api import integrations_api
from elements_sdk.model.teams_connection_update import TeamsConnectionUpdate
from elements_sdk.model.teams_connection import TeamsConnection
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    id = 1 # int | A unique integer value identifying this Teams connection.
    teams_connection_update = TeamsConnectionUpdate(
        name="name_example",
    ) # TeamsConnectionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_teams_connection(id, teams_connection_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->update_teams_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Teams connection. |
 **teams_connection_update** | [**TeamsConnectionUpdate**](TeamsConnectionUpdate.md)|  |

### Return type

[**TeamsConnection**](TeamsConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

