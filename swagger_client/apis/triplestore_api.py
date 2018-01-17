# coding: utf-8

"""
    ORR API Documentation

    The main ORR documentation is located at: https://mmisw.org/orrdoc/  __Please note__: - The ORR API is approaching a stable version but is still work in progress.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page lets you directly exercise and test the API.   Click on any operation header below to learn more details about it, and see a \"Try it out\" button.  - You can click on the \"Authorize\" button at the top right of this page   (or the `!` icon under the particular operation)   to retrieve an authentication token corresponding to your ORR instance credentials (username and password).   Once authorized, the authentication token will be automatically included in the corresponding request.   You will be able to not only perform the basic `GET` operations,   but also see expanded responses according to your access privileges   as well as perform other operations.  - The \"Try it out\" button will also show the corresponding API call that you can submit   from the command line using [`curl`](https://curl.haxx.se/).  - This API includes administrative operations related with the triple store.   The SPARQL endpoint itself   (located at `https://mmisw.org/sparql` for the MMI ORR instance)   is not described here.   (General SPARQL information can be found [here](https://en.wikipedia.org/wiki/SPARQL),   and regarding the current service used by the ORR to support the SPARQL interface   [here](http://franz.com/agraph/support/documentation/current/http-protocol.html).)  - Actual requests from this page are against the specific endpoint at   `https://mmisw.org/ont`. 

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TriplestoreApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_triplestore_size(self, **kwargs):
        """
        Gets the size of the store or the size of a particular named graph
        Provide one of the `iri` or `context` parameters to get the size of a particular graph. If none of these parameters is provided, the size of the whole triplestore will be responded. Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_triplestore_size(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of particular context 
        :param str context: IRI of particular context 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_triplestore_size_with_http_info(**kwargs)
        else:
            (data) = self.get_triplestore_size_with_http_info(**kwargs)
            return data

    def get_triplestore_size_with_http_info(self, **kwargs):
        """
        Gets the size of the store or the size of a particular named graph
        Provide one of the `iri` or `context` parameters to get the size of a particular graph. If none of these parameters is provided, the size of the whole triplestore will be responded. Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_triplestore_size_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of particular context 
        :param str context: IRI of particular context 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['iri', 'context']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_triplestore_size" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'iri' in params:
            query_params.append(('iri', params['iri']))
        if 'context' in params:
            query_params.append(('context', params['context']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ts', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def load_ont_in_triplestore(self, iri, **kwargs):
        """
        Loads an ontology in the triplestore
        Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.load_ont_in_triplestore(iri, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of the ontology to be loaded  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.load_ont_in_triplestore_with_http_info(iri, **kwargs)
        else:
            (data) = self.load_ont_in_triplestore_with_http_info(iri, **kwargs)
            return data

    def load_ont_in_triplestore_with_http_info(self, iri, **kwargs):
        """
        Loads an ontology in the triplestore
        Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.load_ont_in_triplestore_with_http_info(iri, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of the ontology to be loaded  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['iri']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method load_ont_in_triplestore" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'iri' is set
        if ('iri' not in params) or (params['iri'] is None):
            raise ValueError("Missing the required parameter `iri` when calling `load_ont_in_triplestore`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'iri' in params:
            query_params.append(('iri', params['iri']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/ts', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def reload_onts_in_triplestore(self, **kwargs):
        """
        Reloads an ontology or all ontologies in the triplestore
        Provide the `iri` parameter to reload a particular ontology. Otherwise all registered ontologies will be reloaded in the triplestore. Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reload_onts_in_triplestore(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of the ontology to be reloaded 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.reload_onts_in_triplestore_with_http_info(**kwargs)
        else:
            (data) = self.reload_onts_in_triplestore_with_http_info(**kwargs)
            return data

    def reload_onts_in_triplestore_with_http_info(self, **kwargs):
        """
        Reloads an ontology or all ontologies in the triplestore
        Provide the `iri` parameter to reload a particular ontology. Otherwise all registered ontologies will be reloaded in the triplestore. Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reload_onts_in_triplestore_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of the ontology to be reloaded 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['iri']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reload_onts_in_triplestore" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'iri' in params:
            query_params.append(('iri', params['iri']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/ts', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def unload_onts_in_triplestore(self, **kwargs):
        """
        Unloads an ontology or all ontologies from the triplestore
        Provide the `iri` parameter to unload a particular ontology. Otherwise all registered ontologies will be unloaded from the triplestore. Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unload_onts_in_triplestore(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of the ontology to be unloaded 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.unload_onts_in_triplestore_with_http_info(**kwargs)
        else:
            (data) = self.unload_onts_in_triplestore_with_http_info(**kwargs)
            return data

    def unload_onts_in_triplestore_with_http_info(self, **kwargs):
        """
        Unloads an ontology or all ontologies from the triplestore
        Provide the `iri` parameter to unload a particular ontology. Otherwise all registered ontologies will be unloaded from the triplestore. Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unload_onts_in_triplestore_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str iri: IRI of the ontology to be unloaded 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['iri']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unload_onts_in_triplestore" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'iri' in params:
            query_params.append(('iri', params['iri']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/ts', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)