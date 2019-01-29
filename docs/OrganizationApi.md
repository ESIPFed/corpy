# swagger_client.OrganizationApi

All URIs are relative to *http://cor.esipfed.org/ont/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_org**](OrganizationApi.md#add_org) | **POST** /org | Registers an organization
[**delete_org**](OrganizationApi.md#delete_org) | **DELETE** /org/{orgName} | Unregisters an organization
[**org_get**](OrganizationApi.md#org_get) | **GET** /org | Gets information about registered organizations
[**org_org_name_get**](OrganizationApi.md#org_org_name_get) | **GET** /org/{orgName} | Gets basic information of a particular organization
[**update_org**](OrganizationApi.md#update_org) | **PUT** /org/{orgName} | Updates information about a registered organization


# **add_org**
> add_org(body=body)

Registers an organization



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostOrg() # PostOrg | Organization object that needs to be registered (optional)

try:
    # Registers an organization
    api_instance.add_org(body=body)
except ApiException as e:
    print("Exception when calling OrganizationApi->add_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostOrg**](PostOrg.md)| Organization object that needs to be registered | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org**
> delete_org(org_name)

Unregisters an organization

Only users with administrative privilege can perform this operation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | Identifier of the organization

try:
    # Unregisters an organization
    api_instance.delete_org(org_name)
except ApiException as e:
    print("Exception when calling OrganizationApi->delete_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| Identifier of the organization | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get**
> list[Org] org_get()

Gets information about registered organizations

Gets basic information of all registered organizations. This will include additional information depending on privileges of requesting user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()

try:
    # Gets information about registered organizations
    api_response = api_instance.org_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Org]**](Org.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_org_name_get**
> Org org_org_name_get(org_name)

Gets basic information of a particular organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
org_name = 'org_name_example' # str | The code (short name) of the organization.

try:
    # Gets basic information of a particular organization
    api_response = api_instance.org_org_name_get(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_org_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| The code (short name) of the organization. | 

### Return type

[**Org**](Org.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org**
> update_org(org_name, body=body)

Updates information about a registered organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org_name = 'org_name_example' # str | The code (short name) of the organization to be updated.
body = swagger_client.PutOrg() # PutOrg | Object with information for the organization to be updated. (optional)

try:
    # Updates information about a registered organization
    api_instance.update_org(org_name, body=body)
except ApiException as e:
    print("Exception when calling OrganizationApi->update_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**| The code (short name) of the organization to be updated. | 
 **body** | [**PutOrg**](PutOrg.md)| Object with information for the organization to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

