# swagger_client.OntologyApi

All URIs are relative to *http://cor.esipfed.org/ont/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ont**](OntologyApi.md#add_ont) | **POST** /ont | Registers a brand new ontology
[**delete_ont**](OntologyApi.md#delete_ont) | **DELETE** /ont | Deletes a particular version or a whole ontology entry
[**ont_get**](OntologyApi.md#ont_get) | **GET** /ont | Gets information about registered ontologies or terms
[**update_ont**](OntologyApi.md#update_ont) | **PUT** /ont | Updates a given ontology version or adds a new version
[**upload_ont**](OntologyApi.md#upload_ont) | **POST** /ont/upload | Uploads an ontology file for subsequent registration


# **add_ont**
> add_ont(body)

Registers a brand new ontology

Performs the registration of a brand new ontology in the registry by the URI given in the `uri` attribute of the object in the body. 

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
api_instance = swagger_client.OntologyApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostOnt() # PostOnt | Object with information for the ontology to be registered.  To provide the contents of the ontology you have two options:  - Specify a previously uploaded file (via `POST /ont/upload`) by   providing the corresponding reported filename (in the `uploadedFilename`   field) and format (`uploadedFormat`). There's no need to upload the file   itself again. - Embbed the complete contents in the `contents` field, and provide the associated   format in `format`.  See the `PostOnt` object description for more details. 

try:
    # Registers a brand new ontology
    api_instance.add_ont(body)
except ApiException as e:
    print("Exception when calling OntologyApi->add_ont: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostOnt**](PostOnt.md)| Object with information for the ontology to be registered.  To provide the contents of the ontology you have two options:  - Specify a previously uploaded file (via &#x60;POST /ont/upload&#x60;) by   providing the corresponding reported filename (in the &#x60;uploadedFilename&#x60;   field) and format (&#x60;uploadedFormat&#x60;). There&#39;s no need to upload the file   itself again. - Embbed the complete contents in the &#x60;contents&#x60; field, and provide the associated   format in &#x60;format&#x60;.  See the &#x60;PostOnt&#x60; object description for more details.  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ont**
> delete_ont(uri, user_name, version=version)

Deletes a particular version or a whole ontology entry

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
api_instance = swagger_client.OntologyApi(swagger_client.ApiClient(configuration))
uri = 'uri_example' # str | Ontology URI
user_name = 'user_name_example' # str | Registered user making the request. Must be an owner of the ontology. 
version = 'version_example' # str | Particular version to be deleted. If omitted, the whole entry by the given URI will be unregistered.  (optional)

try:
    # Deletes a particular version or a whole ontology entry
    api_instance.delete_ont(uri, user_name, version=version)
except ApiException as e:
    print("Exception when calling OntologyApi->delete_ont: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Ontology URI | 
 **user_name** | **str**| Registered user making the request. Must be an owner of the ontology.  | 
 **version** | **str**| Particular version to be deleted. If omitted, the whole entry by the given URI will be unregistered.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ont_get**
> list[Ont] ont_get(uri=uri, ouri=ouri, version=version, turi=turi, format=format)

Gets information about registered ontologies or terms

General ontology or term report according to given parameters, associated ontology visibility, and privilege of the requesting user. All parameters are optional.   Any given `uri`, `ouri`, or `turi` parameter indicates a request for a particular ontology or term.  If none of the `uri`, `ouri`, and `turi` parameters is given, this will indicate a query for a list of ontologies. In this case, only a metadata summary is provided for each reported ontology (in particular, no ontology contents per se is reported). Also, other supplied parameters will be used to query for the desired ontologies. For example, with the query paramenter and value `ownerName=acme`, all ontologies owned by the `acme` organization will be considered for reporting. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntologyApi()
uri = 'uri_example' # str | With this parameter the backend will first try an \"ontology request.\" If no ontlogy is registered by the given URI, then it will try a \"term request.\"  (optional)
ouri = 'ouri_example' # str | Use this parameter to exclusively make a \"ontology request.\"  (optional)
version = 'version_example' # str | Desired version in the case of an \"ontology request.\"  (optional)
turi = 'turi_example' # str | Use this parameter to exclusively make a \"term request.\"  (optional)
format = 'format_example' # str | Desired format for the response in the case of a single ontology or term request.  (optional)

try:
    # Gets information about registered ontologies or terms
    api_response = api_instance.ont_get(uri=uri, ouri=ouri, version=version, turi=turi, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->ont_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| With this parameter the backend will first try an \&quot;ontology request.\&quot; If no ontlogy is registered by the given URI, then it will try a \&quot;term request.\&quot;  | [optional] 
 **ouri** | **str**| Use this parameter to exclusively make a \&quot;ontology request.\&quot;  | [optional] 
 **version** | **str**| Desired version in the case of an \&quot;ontology request.\&quot;  | [optional] 
 **turi** | **str**| Use this parameter to exclusively make a \&quot;term request.\&quot;  | [optional] 
 **format** | **str**| Desired format for the response in the case of a single ontology or term request.  | [optional] 

### Return type

[**list[Ont]**](Ont.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ont**
> update_ont(body=body)

Updates a given ontology version or adds a new version

Use this operation to create a new version for a registered ontology, or to update an exisiting version. 

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
api_instance = swagger_client.OntologyApi(swagger_client.ApiClient(configuration))
body = swagger_client.PutOnt() # PutOnt | Ontology object that needs to be registered (optional)

try:
    # Updates a given ontology version or adds a new version
    api_instance.update_ont(body=body)
except ApiException as e:
    print("Exception when calling OntologyApi->update_ont: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutOnt**](PutOnt.md)| Ontology object that needs to be registered | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_ont**
> UploadedFileInfo upload_ont(file, format)

Uploads an ontology file for subsequent registration

This operation allows to upload an ontology file as a preliminary step for subsequent registration via a `POST /ont` request.   Before having to provide other required information for registration, this separated step helps not only in determining that the file is a valid ontology, but also in terms of the returned associated information that the user or client application can use for actual registration, for example, regarding possible ontology URIs found in the file. 

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
api_instance = swagger_client.OntologyApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | The file to be uploaded.
format = 'format_example' # str | Format of the file. The special value `\"guess\"` can be given to let the ORR automatically determine the format. (A future version of this API may allow this parameter to be skipped, in such case with the \"guess format\" behavior implied.) 

try:
    # Uploads an ontology file for subsequent registration
    api_response = api_instance.upload_ont(file, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->upload_ont: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file to be uploaded. | 
 **format** | **str**| Format of the file. The special value &#x60;\&quot;guess\&quot;&#x60; can be given to let the ORR automatically determine the format. (A future version of this API may allow this parameter to be skipped, in such case with the \&quot;guess format\&quot; behavior implied.)  | 

### Return type

[**UploadedFileInfo**](UploadedFileInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

