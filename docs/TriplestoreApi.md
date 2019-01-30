# swagger_client.TriplestoreApi

All URIs are relative to *https://mmisw.org/ont/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_triplestore_size**](TriplestoreApi.md#get_triplestore_size) | **GET** /ts | Gets the size of the store or the size of a particular named graph
[**load_ont_in_triplestore**](TriplestoreApi.md#load_ont_in_triplestore) | **POST** /ts | Loads an ontology in the triplestore
[**reload_onts_in_triplestore**](TriplestoreApi.md#reload_onts_in_triplestore) | **PUT** /ts | Reloads an ontology or all ontologies in the triplestore
[**unload_onts_in_triplestore**](TriplestoreApi.md#unload_onts_in_triplestore) | **DELETE** /ts | Unloads an ontology or all ontologies from the triplestore


# **get_triplestore_size**
> get_triplestore_size(iri=iri, context=context)

Gets the size of the store or the size of a particular named graph

Provide one of the `iri` or `context` parameters to get the size of a particular graph. If none of these parameters is provided, the size of the whole triplestore will be responded. Only admins can perform this operation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TriplestoreApi()
iri = 'iri_example' # str | IRI of particular context  (optional)
context = 'context_example' # str | IRI of particular context  (optional)

try:
    # Gets the size of the store or the size of a particular named graph
    api_instance.get_triplestore_size(iri=iri, context=context)
except ApiException as e:
    print("Exception when calling TriplestoreApi->get_triplestore_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**| IRI of particular context  | [optional] 
 **context** | **str**| IRI of particular context  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_ont_in_triplestore**
> load_ont_in_triplestore(iri)

Loads an ontology in the triplestore

Only admins can perform this operation. 

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
api_instance = swagger_client.TriplestoreApi(swagger_client.ApiClient(configuration))
iri = 'iri_example' # str | IRI of the ontology to be loaded 

try:
    # Loads an ontology in the triplestore
    api_instance.load_ont_in_triplestore(iri)
except ApiException as e:
    print("Exception when calling TriplestoreApi->load_ont_in_triplestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**| IRI of the ontology to be loaded  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_onts_in_triplestore**
> reload_onts_in_triplestore(iri=iri)

Reloads an ontology or all ontologies in the triplestore

Provide the `iri` parameter to reload a particular ontology. Otherwise all registered ontologies will be reloaded in the triplestore. Only admins can perform this operation. 

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
api_instance = swagger_client.TriplestoreApi(swagger_client.ApiClient(configuration))
iri = 'iri_example' # str | IRI of the ontology to be reloaded  (optional)

try:
    # Reloads an ontology or all ontologies in the triplestore
    api_instance.reload_onts_in_triplestore(iri=iri)
except ApiException as e:
    print("Exception when calling TriplestoreApi->reload_onts_in_triplestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**| IRI of the ontology to be reloaded  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unload_onts_in_triplestore**
> unload_onts_in_triplestore(iri=iri)

Unloads an ontology or all ontologies from the triplestore

Provide the `iri` parameter to unload a particular ontology. Otherwise all registered ontologies will be unloaded from the triplestore. Only admins can perform this operation. 

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
api_instance = swagger_client.TriplestoreApi(swagger_client.ApiClient(configuration))
iri = 'iri_example' # str | IRI of the ontology to be unloaded  (optional)

try:
    # Unloads an ontology or all ontologies from the triplestore
    api_instance.unload_onts_in_triplestore(iri=iri)
except ApiException as e:
    print("Exception when calling TriplestoreApi->unload_onts_in_triplestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**| IRI of the ontology to be unloaded  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

