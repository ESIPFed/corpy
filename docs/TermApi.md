# swagger_client.TermApi

All URIs are relative to *http://cor.esipfed.org/ont/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_term**](TermApi.md#add_term) | **POST** /ont/term | Adds a term to an existing ORR vocabulary
[**term_get**](TermApi.md#term_get) | **GET** /term | Simplified semantic search queries against the triple store


# **add_term**
> add_term(body)

Adds a term to an existing ORR vocabulary

This operation allows to add a new term to an ORR vocabulary. This addition does not generate a new version of the vocabulary. 

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
api_instance = swagger_client.TermApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostTerm() # PostTerm | Object with information for the term to be added. See the `PostOnt` object description for more details. 

try:
    # Adds a term to an existing ORR vocabulary
    api_instance.add_term(body)
except ApiException as e:
    print("Exception when calling TermApi->add_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTerm**](PostTerm.md)| Object with information for the term to be added. See the &#x60;PostOnt&#x60; object description for more details.  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **term_get**
> term_get(containing=containing, _in=_in, predicate=predicate, subject=subject, object=object, limit=limit, offset=offset)

Simplified semantic search queries against the triple store

This endpoint route is intended to provide some common semantic search operations against the triple store.  **NOTE**: This is an experimental operation. The SPARQL interface remains the most complete and powerful semantic search mechanism.  Provide one of `containing` or `predicate` as main parameter, along with associated auxiliary and optional parameters as described. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TermApi()
containing = 'containing_example' # str | Searches the given string in the indicated parts of the triples as determined by the `in` parameter.  (optional)
_in = '_in_example' # str | Only used in combination with the `containing` parameter, the `in` parameter determines where to perform the search: subject, predicate, and/or object. Use the 1-character abbreviations: `s` for subject, `p` for predicate, `o` for object. Any combination of these characters can be used as value for the `in` parameter. For example, to search the given `containing` string in all parts of the triple use `spo`. The default value is `s`, meaning the search will only be on the subject.  (optional)
predicate = 'predicate_example' # str | Desired predicate to retrieve entities related with a given subject or object. The following common namespace prefixes are recognized: `skos:`, `owl:`, `rdfs:`, `rdf:`. So possible values of this parameter include `skos:relatedMatch` and `owl:sameAs`. If the value does not start with any of the recognized prefixes, then it is assumed to be a full IRI, e.g., `http://purl.org/dc/terms/description`.  This parameter is to be used in combination with one of the `subject` or `object` parameters. If `subject` is given, the underlying SPARQL query is basically `<subject> <predicate> ?object` and the resulting list of objects is returned. Otherwise the underlying SPARQL query is basically `?subject <predicate> <object>` and the resulting list of subjects is returned.  (optional)
subject = 'subject_example' # str | IRI of the subject for underlying SPARQL query. Required when any of the _predicate_ parameters is given and **no** object parameter is given.  (optional)
object = 'object_example' # str | IRI of the object for underlying SPARQL query. Required when any of the _predicate_ parameters is given and **no** subject parameter is given.  (optional)
limit = 56 # int | Maximum number of solutions to be returned. The default value is 30. A non-positive value means no limit, so all solutions will be returned.  (optional)
offset = 56 # int | Solutions returned will start after the specified number of solutions. Ignored if the value is non-positive. By default, no offset.  (optional)

try:
    # Simplified semantic search queries against the triple store
    api_instance.term_get(containing=containing, _in=_in, predicate=predicate, subject=subject, object=object, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling TermApi->term_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **containing** | **str**| Searches the given string in the indicated parts of the triples as determined by the &#x60;in&#x60; parameter.  | [optional] 
 **_in** | **str**| Only used in combination with the &#x60;containing&#x60; parameter, the &#x60;in&#x60; parameter determines where to perform the search: subject, predicate, and/or object. Use the 1-character abbreviations: &#x60;s&#x60; for subject, &#x60;p&#x60; for predicate, &#x60;o&#x60; for object. Any combination of these characters can be used as value for the &#x60;in&#x60; parameter. For example, to search the given &#x60;containing&#x60; string in all parts of the triple use &#x60;spo&#x60;. The default value is &#x60;s&#x60;, meaning the search will only be on the subject.  | [optional] 
 **predicate** | **str**| Desired predicate to retrieve entities related with a given subject or object. The following common namespace prefixes are recognized: &#x60;skos:&#x60;, &#x60;owl:&#x60;, &#x60;rdfs:&#x60;, &#x60;rdf:&#x60;. So possible values of this parameter include &#x60;skos:relatedMatch&#x60; and &#x60;owl:sameAs&#x60;. If the value does not start with any of the recognized prefixes, then it is assumed to be a full IRI, e.g., &#x60;http://purl.org/dc/terms/description&#x60;.  This parameter is to be used in combination with one of the &#x60;subject&#x60; or &#x60;object&#x60; parameters. If &#x60;subject&#x60; is given, the underlying SPARQL query is basically &#x60;&lt;subject&gt; &lt;predicate&gt; ?object&#x60; and the resulting list of objects is returned. Otherwise the underlying SPARQL query is basically &#x60;?subject &lt;predicate&gt; &lt;object&gt;&#x60; and the resulting list of subjects is returned.  | [optional] 
 **subject** | **str**| IRI of the subject for underlying SPARQL query. Required when any of the _predicate_ parameters is given and **no** object parameter is given.  | [optional] 
 **object** | **str**| IRI of the object for underlying SPARQL query. Required when any of the _predicate_ parameters is given and **no** subject parameter is given.  | [optional] 
 **limit** | **int**| Maximum number of solutions to be returned. The default value is 30. A non-positive value means no limit, so all solutions will be returned.  | [optional] 
 **offset** | **int**| Solutions returned will start after the specified number of solutions. Ignored if the value is non-positive. By default, no offset.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

