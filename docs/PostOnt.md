# PostOnt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iri** | **str** | The IRI of the ontology.  | [optional] 
**original_iri** | **str** | In case of a fully-hosted registration, enter this field to indicate the original IRI in the provided contents to be used for the \&quot;migration\&quot; of corresponding entities to the new IRI.  | [optional] 
**name** | **str** | The name for the ontology. If omitted, the ORR will try to get this information from standard metadata in the submitted ontology contents.  | [optional] 
**org_name** | **str** | ID of the organization that will own the ontology registration. If omitted, the owner will be the submitting user.  | [optional] 
**visibility** | **str** | One of: &#x60;owner&#x60; or &#x60;public&#x60;. The default visibility is &#x60;owner&#x60;.  | [optional] 
**status** | **str** | One of: &#x60;draft&#x60;, &#x60;unstable&#x60;, &#x60;testing&#x60;, &#x60;stable&#x60;,  &#x60;deprecated&#x60;, &#x60;archaic&#x60;. There&#39;s no default value.  | [optional] 
**user_name** | **str** | Registered user making the request.  | [optional] 
**uploaded_filename** | **str** | Name of file previously uploaded via prior &#x60;POST /ont/upload&#x60; request.  | [optional] 
**uploaded_format** | **str** | Format of the file previously uploaded via prior &#x60;POST /ont/upload&#x60; request.  | [optional] 
**contents** | **str** | Direct contents of the ontology.  | [optional] 
**format** | **str** | Format of the &#x60;contents&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


