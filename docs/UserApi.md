# swagger_client.UserApi

All URIs are relative to *https://mmisw.org/ont/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UserApi.md#add_user) | **POST** /user | Registers a user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /user/{userName} | Unregisters a user
[**update_user**](UserApi.md#update_user) | **PUT** /user/{userName} | Updates information about a registered user
[**user_get**](UserApi.md#user_get) | **GET** /user | Gets information about registered users
[**user_user_name_get**](UserApi.md#user_user_name_get) | **GET** /user/{userName} | Gets basic information of a particular user


# **add_user**
> add_user(body=body)

Registers a user

This operation allows to register a new user in the system.  **NOTE**: This operation cannot be completed here if the endpoint is configured to required a ReCAPTCHA code, which is currently not captured in this interface. Please use the ORR Portal interface associated with the endpoint to register the new user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.PostUser() # PostUser | User object that needs to be registered (optional)

try:
    # Registers a user
    api_instance.add_user(body=body)
except ApiException as e:
    print("Exception when calling UserApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUser**](PostUser.md)| User object that needs to be registered | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_name)

Unregisters a user

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_name = 'user_name_example' # str | Identifier of the user

try:
    # Unregisters a user
    api_instance.delete_user(user_name)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user_name, body=body)

Updates information about a registered user

Only the same user and users with administrative privilege can perform this operation. 

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_name = 'user_name_example' # str | The identifier of the user to be updated.
body = swagger_client.PutUser() # PutUser | Object with information for the user to be updated. (optional)

try:
    # Updates information about a registered user
    api_instance.update_user(user_name, body=body)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| The identifier of the user to be updated. | 
 **body** | [**PutUser**](PutUser.md)| Object with information for the user to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> list[User] user_get()

Gets information about registered users

Gets information about registered users. This will include additional information depending on privileges of requesting user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try:
    # Gets information about registered users
    api_response = api_instance.user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_name_get**
> User user_user_name_get(user_name)

Gets basic information of a particular user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_name = 'user_name_example' # str | The login (short name) of the user.

try:
    # Gets basic information of a particular user
    api_response = api_instance.user_user_name_get(user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_user_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| The login (short name) of the user. | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

