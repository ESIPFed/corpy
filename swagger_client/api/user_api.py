# coding: utf-8

"""
    ORR Ont API Documentation

    The main ORR documentation is located at: http://mmisw.org/orrdoc/ ``` ###################################################### # NOTE #   OUT-OF-DATE for the time being. # Currently the swagger spec is maintained in the # https://github.com/mmisw/mmiorr-docs repo, which # is served at http://mmisw.org/orrdoc/api/ ###################################################### ``` __Note__: - We are in the process of writing this API documentation.   Please [let us know](https://github.com/mmisw/mmiorr-docs/issues) if you have any   questions or suggestions.  - Besides the documentation itself, this page also allows to directly exercise the API. - Actual requests from this page are against the endpoint at   `http://cor.esipfed.org/sparql`. This may change in a future version in   particular regarding a more general way of exercising the API (regardless   of concrete endpoint), or by allowing the selection of the particular endpoint.  - You can use the \"Authorize\" button above and enter your COR credentials to login   in this API interface. In this way you will be able to perform not only the basic   `GET` operations, but see expanded responses according to your access priviliges   and ontology visibility settings, as well as perform other operations as listed below.   # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_user(self, **kwargs):  # noqa: E501
        """Registers a user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostUser body: User object that needs to be registered
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_user_with_http_info(self, **kwargs):  # noqa: E501
        """Registers a user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostUser body: User object that needs to be registered
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user(self, user_name, **kwargs):  # noqa: E501
        """Unregisters a user  # noqa: E501

        Only users with administrative privilege can perform this operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_name: Identifier of the user (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_with_http_info(user_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_with_http_info(user_name, **kwargs)  # noqa: E501
            return data

    def delete_user_with_http_info(self, user_name, **kwargs):  # noqa: E501
        """Unregisters a user  # noqa: E501

        Only users with administrative privilege can perform this operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_with_http_info(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_name: Identifier of the user (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_name' is set
        if ('user_name' not in params or
                params['user_name'] is None):
            raise ValueError("Missing the required parameter `user_name` when calling `delete_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_name' in params:
            path_params['userName'] = params['user_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/user/{userName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user(self, user_name, **kwargs):  # noqa: E501
        """Updates information about a registered user  # noqa: E501

        Only the same user and users with administrative privilege can perform this operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_name: The identifier of the user to be updated. (required)
        :param PutUser body: Object with information for the user to be updated.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_with_http_info(user_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_with_http_info(user_name, **kwargs)  # noqa: E501
            return data

    def update_user_with_http_info(self, user_name, **kwargs):  # noqa: E501
        """Updates information about a registered user  # noqa: E501

        Only the same user and users with administrative privilege can perform this operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_with_http_info(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_name: The identifier of the user to be updated. (required)
        :param PutUser body: Object with information for the user to be updated.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_name' is set
        if ('user_name' not in params or
                params['user_name'] is None):
            raise ValueError("Missing the required parameter `user_name` when calling `update_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_name' in params:
            path_params['userName'] = params['user_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/user/{userName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_get(self, **kwargs):  # noqa: E501
        """Gets information about registered users  # noqa: E501

        Gets information about registered users. This will include additional information depending on privileges of requesting user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.user_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def user_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets information about registered users  # noqa: E501

        Gets information about registered users. This will include additional information depending on privileges of requesting user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_get" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[User]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_user_name_get(self, user_name, **kwargs):  # noqa: E501
        """Gets basic information of a particular user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_user_name_get(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_name: The login (short name) of the user. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_user_name_get_with_http_info(user_name, **kwargs)  # noqa: E501
        else:
            (data) = self.user_user_name_get_with_http_info(user_name, **kwargs)  # noqa: E501
            return data

    def user_user_name_get_with_http_info(self, user_name, **kwargs):  # noqa: E501
        """Gets basic information of a particular user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_user_name_get_with_http_info(user_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_name: The login (short name) of the user. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_user_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_name' is set
        if ('user_name' not in params or
                params['user_name'] is None):
            raise ValueError("Missing the required parameter `user_name` when calling `user_user_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_name' in params:
            path_params['userName'] = params['user_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/{userName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)