# coding: utf-8

"""
    ORR API Documentation

    The main ORR documentation is located at: https://mmisw.org/orrdoc/  __Please note__: - The ORR API is approaching a stable version but is still work in progress.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page lets you directly exercise and test the API.   Click on any operation header below to learn more details about it, and see a \"Try it out\" button.  - You can click on the \"Authorize\" button at the top right of this page   (or the `!` icon under the particular operation)   to retrieve an authentication token corresponding to your ORR instance credentials (username and password).   Once authorized, the authentication token will be automatically included in the corresponding request.   You will be able to not only perform the basic `GET` operations,   but also see expanded responses according to your access privileges   as well as perform other operations.  - The \"Try it out\" button will also show the corresponding API call that you can submit   from the command line using [`curl`](https://curl.haxx.se/).  - This API includes administrative operations related with the triple store.   The SPARQL endpoint itself   (located at `http://cor.esipfed.org/sparql` for the MMI ORR instance)   is not described here.   (General SPARQL information can be found [here](https://en.wikipedia.org/wiki/SPARQL),   and regarding the current service used by the ORR to support the SPARQL interface   [here](http://franz.com/agraph/support/documentation/current/http-protocol.html).)  - Actual requests from this page are against the specific endpoint at   `http://cor.esipfed.org/ont`. 

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


class OrganizationApi(object):
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

    def add_org(self, **kwargs):
        """
        Registers an organization
        Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_org(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostOrg body: Organization object that needs to be registered
        :return: OrgNew
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_org_with_http_info(**kwargs)
        else:
            (data) = self.add_org_with_http_info(**kwargs)
            return data

    def add_org_with_http_info(self, **kwargs):
        """
        Registers an organization
        Only admins can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_org_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostOrg body: Organization object that needs to be registered
        :return: OrgNew
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_org" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/org', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OrgNew',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_org(self, org_name, **kwargs):
        """
        Unregisters an organization
        Only users with administrative privilege can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_org(org_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_name: Identifier of the organization (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_org_with_http_info(org_name, **kwargs)
        else:
            (data) = self.delete_org_with_http_info(org_name, **kwargs)
            return data

    def delete_org_with_http_info(self, org_name, **kwargs):
        """
        Unregisters an organization
        Only users with administrative privilege can perform this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_org_with_http_info(org_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_name: Identifier of the organization (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_org" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if ('org_name' not in params) or (params['org_name'] is None):
            raise ValueError("Missing the required parameter `org_name` when calling `delete_org`")


        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']

        query_params = []

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

        return self.api_client.call_api('/org/{orgName}', 'DELETE',
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

    def org_get(self, **kwargs):
        """
        Gets information about registered organizations
        Gets basic information of all registered organizations. This will include additional information depending on privileges of requesting user. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.org_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Org]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.org_get_with_http_info(**kwargs)
        else:
            (data) = self.org_get_with_http_info(**kwargs)
            return data

    def org_get_with_http_info(self, **kwargs):
        """
        Gets information about registered organizations
        Gets basic information of all registered organizations. This will include additional information depending on privileges of requesting user. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.org_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Org]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method org_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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

        return self.api_client.call_api('/org', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Org]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def org_org_name_get(self, org_name, **kwargs):
        """
        Gets basic information of a particular organization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.org_org_name_get(org_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_name: The code (short name) of the organization. (required)
        :return: Org
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.org_org_name_get_with_http_info(org_name, **kwargs)
        else:
            (data) = self.org_org_name_get_with_http_info(org_name, **kwargs)
            return data

    def org_org_name_get_with_http_info(self, org_name, **kwargs):
        """
        Gets basic information of a particular organization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.org_org_name_get_with_http_info(org_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_name: The code (short name) of the organization. (required)
        :return: Org
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method org_org_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if ('org_name' not in params) or (params['org_name'] is None):
            raise ValueError("Missing the required parameter `org_name` when calling `org_org_name_get`")


        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']

        query_params = []

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

        return self.api_client.call_api('/org/{orgName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Org',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_org(self, org_name, **kwargs):
        """
        Updates information about a registered organization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_org(org_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_name: The code (short name) of the organization to be updated. (required)
        :param PutOrg body: Object with information for the organization to be updated.
        :return: OrgUpdated
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_org_with_http_info(org_name, **kwargs)
        else:
            (data) = self.update_org_with_http_info(org_name, **kwargs)
            return data

    def update_org_with_http_info(self, org_name, **kwargs):
        """
        Updates information about a registered organization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_org_with_http_info(org_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str org_name: The code (short name) of the organization to be updated. (required)
        :param PutOrg body: Object with information for the organization to be updated.
        :return: OrgUpdated
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_org" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if ('org_name' not in params) or (params['org_name'] is None):
            raise ValueError("Missing the required parameter `org_name` when calling `update_org`")


        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/org/{orgName}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OrgUpdated',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
