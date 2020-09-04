# elements_sdk.TapeArchiveApi

All URIs are relative to *https://elements.local*
>
Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tape**](TapeArchiveApi.md#create_tape) | **POST** `/api/2/archive/tape/tapes` | 
[**create_tapegroup**](TapeArchiveApi.md#create_tapegroup) | **POST** `/api/2/archive/tape/groups` | 
[**delete_tape**](TapeArchiveApi.md#delete_tape) | **DELETE** `/api/2/archive/tape/tapes/{id}` | 
[**delete_tapegroup**](TapeArchiveApi.md#delete_tapegroup) | **DELETE** `/api/2/archive/tape/groups/{id}` | 
[**get_all_archivedfileentries**](TapeArchiveApi.md#get_all_archivedfileentries) | **GET** `/api/2/archive/tape/files` | 
[**get_all_tapegroups**](TapeArchiveApi.md#get_all_tapegroups) | **GET** `/api/2/archive/tape/groups` | 
[**get_all_tapes**](TapeArchiveApi.md#get_all_tapes) | **GET** `/api/2/archive/tape/tapes` | 
[**get_archivedfileentry**](TapeArchiveApi.md#get_archivedfileentry) | **GET** `/api/2/archive/tape/files/{id}` | 
[**get_tape**](TapeArchiveApi.md#get_tape) | **GET** `/api/2/archive/tape/tapes/{id}` | 
[**get_tapegroup**](TapeArchiveApi.md#get_tapegroup) | **GET** `/api/2/archive/tape/groups/{id}` | 
[**patch_tape**](TapeArchiveApi.md#patch_tape) | **PATCH** `/api/2/archive/tape/tapes/{id}` | 
[**patch_tapegroup**](TapeArchiveApi.md#patch_tapegroup) | **PATCH** `/api/2/archive/tape/groups/{id}` | 
[**update_tape**](TapeArchiveApi.md#update_tape) | **PUT** `/api/2/archive/tape/tapes/{id}` | 
[**update_tapegroup**](TapeArchiveApi.md#update_tapegroup) | **PUT** `/api/2/archive/tape/groups/{id}` | 



***

# **create_tape**
> Tape create_tape(data)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    data = elements_sdk.Tape() # Tape | 

    try:
        api_response = api_instance.create_tape(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->create_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tape**](Tape.md)|  | 

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **create_tapegroup**
> TapeGroup create_tapegroup(data)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    data = elements_sdk.TapeGroup() # TapeGroup | 

    try:
        api_response = api_instance.create_tapegroup(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->create_tapegroup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TapeGroup**](TapeGroup.md)|  | 

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_tape**
> object delete_tape(id)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape.

    try:
        api_response = api_instance.delete_tape(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->delete_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **delete_tapegroup**
> object delete_tapegroup(id)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape group.

    try:
        api_response = api_instance.delete_tapegroup(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->delete_tapegroup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. | 

### Return type

**object**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_archivedfileentries**
> list[TapeFile] get_all_archivedfileentries(id=id, is_dir=is_dir, name=name, fullpath=fullpath, parent=parent, ordering=ordering, limit=limit, offset=offset)



### Required permissions   * User account permission: ltfs:search (read) / ltfs:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 3.4 # float | Filter the returned list by `id`. (optional)
is_dir = 'is_dir_example' # str | Filter the returned list by `is_dir`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
fullpath = 'fullpath_example' # str | Filter the returned list by `fullpath`. (optional)
parent = 'parent_example' # str | Filter the returned list by `parent`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_archivedfileentries(id=id, is_dir=is_dir, name=name, fullpath=fullpath, parent=parent, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->get_all_archivedfileentries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **fullpath** | **str**| Filter the returned list by &#x60;fullpath&#x60;. | [optional] 
 **parent** | **str**| Filter the returned list by &#x60;parent&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[TapeFile]**](TapeFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_tapegroups**
> list[TapeGroup] get_all_tapegroups(id=id, name=name, ordering=ordering, limit=limit, offset=offset)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 3.4 # float | Filter the returned list by `id`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_tapegroups(id=id, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->get_all_tapegroups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[TapeGroup]**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_all_tapes**
> list[Tape] get_all_tapes(id=id, name=name, group=group, group__isnull=group__isnull, ordering=ordering, limit=limit, offset=offset)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 3.4 # float | Filter the returned list by `id`. (optional)
name = 'name_example' # str | Filter the returned list by `name`. (optional)
group = 'group_example' # str | Filter the returned list by `group`. (optional)
group__isnull = 'group__isnull_example' # str | Filter the returned list by `group__isnull`. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.get_all_tapes(id=id, name=name, group=group, group__isnull=group__isnull, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->get_all_tapes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Filter the returned list by &#x60;id&#x60;. | [optional] 
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional] 
 **group** | **str**| Filter the returned list by &#x60;group&#x60;. | [optional] 
 **group__isnull** | **str**| Filter the returned list by &#x60;group__isnull&#x60;. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**list[Tape]**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_archivedfileentry**
> TapeFile get_archivedfileentry(id)



### Required permissions   * User account permission: ltfs:search (read) / ltfs:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this Archived file entry.

    try:
        api_response = api_instance.get_archivedfileentry(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->get_archivedfileentry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Archived file entry. | 

### Return type

[**TapeFile**](TapeFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_tape**
> Tape get_tape(id)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape.

    try:
        api_response = api_instance.get_tape(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->get_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. | 

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **get_tapegroup**
> TapeGroup get_tapegroup(id)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape group.

    try:
        api_response = api_instance.get_tapegroup(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->get_tapegroup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. | 

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_tape**
> Tape patch_tape(id, data)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape.
data = elements_sdk.Tape() # Tape | 

    try:
        api_response = api_instance.patch_tape(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->patch_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. | 
 **data** | [**Tape**](Tape.md)|  | 

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **patch_tapegroup**
> TapeGroup patch_tapegroup(id, data)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape group.
data = elements_sdk.TapeGroup() # TapeGroup | 

    try:
        api_response = api_instance.patch_tapegroup(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->patch_tapegroup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. | 
 **data** | [**TapeGroup**](TapeGroup.md)|  | 

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_tape**
> Tape update_tape(id, data)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape.
data = elements_sdk.Tape() # Tape | 

    try:
        api_response = api_instance.update_tape(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->update_tape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape. | 
 **data** | [**Tape**](Tape.md)|  | 

### Return type

[**Tape**](Tape.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


***

# **update_tapegroup**
> TapeGroup update_tapegroup(id, data)



### Required permissions   * User account permission: None (read) / ltfs:tapegroups:manage (write)   * License component: ltfs 

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
    api_instance = elements_sdk.TapeArchiveApi(api_client)
    id = 56 # int | A unique integer value identifying this tape group.
data = elements_sdk.TapeGroup() # TapeGroup | 

    try:
        api_response = api_instance.update_tapegroup(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeArchiveApi->update_tapegroup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tape group. | 
 **data** | [**TapeGroup**](TapeGroup.md)|  | 

### Return type

[**TapeGroup**](TapeGroup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

