# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wavefront_api_client.api_client import ApiClient


class AnomalyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_anomalies(self, **kwargs):  # noqa: E501
        """Get all anomalies for a customer during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_anomalies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_anomalies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_anomalies_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_anomalies_with_http_info(self, **kwargs):  # noqa: E501
        """Get all anomalies for a customer during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_anomalies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_ms', 'end_ms', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_anomalies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_ms' in params:
            query_params.append(('startMs', params['start_ms']))  # noqa: E501
        if 'end_ms' in params:
            query_params.append(('endMs', params['end_ms']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/anomaly', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_anomalies_for_chart_and_param_hash(self, dashboard_id, chart_hash, param_hash, **kwargs):  # noqa: E501
        """Get all anomalies for a chart with a set of dashboard parameters during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomalies_for_chart_and_param_hash(dashboard_id, chart_hash, param_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param str chart_hash: (required)
        :param str param_hash: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_anomalies_for_chart_and_param_hash_with_http_info(dashboard_id, chart_hash, param_hash, **kwargs)  # noqa: E501
        else:
            (data) = self.get_anomalies_for_chart_and_param_hash_with_http_info(dashboard_id, chart_hash, param_hash, **kwargs)  # noqa: E501
            return data

    def get_anomalies_for_chart_and_param_hash_with_http_info(self, dashboard_id, chart_hash, param_hash, **kwargs):  # noqa: E501
        """Get all anomalies for a chart with a set of dashboard parameters during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomalies_for_chart_and_param_hash_with_http_info(dashboard_id, chart_hash, param_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param str chart_hash: (required)
        :param str param_hash: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'chart_hash', 'param_hash', 'start_ms', 'end_ms', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_anomalies_for_chart_and_param_hash" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `get_anomalies_for_chart_and_param_hash`")  # noqa: E501
        # verify the required parameter 'chart_hash' is set
        if ('chart_hash' not in params or
                params['chart_hash'] is None):
            raise ValueError("Missing the required parameter `chart_hash` when calling `get_anomalies_for_chart_and_param_hash`")  # noqa: E501
        # verify the required parameter 'param_hash' is set
        if ('param_hash' not in params or
                params['param_hash'] is None):
            raise ValueError("Missing the required parameter `param_hash` when calling `get_anomalies_for_chart_and_param_hash`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']  # noqa: E501
        if 'chart_hash' in params:
            path_params['chartHash'] = params['chart_hash']  # noqa: E501
        if 'param_hash' in params:
            path_params['paramHash'] = params['param_hash']  # noqa: E501

        query_params = []
        if 'start_ms' in params:
            query_params.append(('startMs', params['start_ms']))  # noqa: E501
        if 'end_ms' in params:
            query_params.append(('endMs', params['end_ms']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/anomaly/{dashboardId}/chart/{chartHash}/{paramHash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chart_anomalies_for_chart(self, dashboard_id, chart_hash, **kwargs):  # noqa: E501
        """Get all anomalies for a chart during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_anomalies_for_chart(dashboard_id, chart_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param str chart_hash: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chart_anomalies_for_chart_with_http_info(dashboard_id, chart_hash, **kwargs)  # noqa: E501
        else:
            (data) = self.get_chart_anomalies_for_chart_with_http_info(dashboard_id, chart_hash, **kwargs)  # noqa: E501
            return data

    def get_chart_anomalies_for_chart_with_http_info(self, dashboard_id, chart_hash, **kwargs):  # noqa: E501
        """Get all anomalies for a chart during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_anomalies_for_chart_with_http_info(dashboard_id, chart_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param str chart_hash: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'chart_hash', 'start_ms', 'end_ms', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_anomalies_for_chart" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `get_chart_anomalies_for_chart`")  # noqa: E501
        # verify the required parameter 'chart_hash' is set
        if ('chart_hash' not in params or
                params['chart_hash'] is None):
            raise ValueError("Missing the required parameter `chart_hash` when calling `get_chart_anomalies_for_chart`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']  # noqa: E501
        if 'chart_hash' in params:
            path_params['chartHash'] = params['chart_hash']  # noqa: E501

        query_params = []
        if 'start_ms' in params:
            query_params.append(('startMs', params['start_ms']))  # noqa: E501
        if 'end_ms' in params:
            query_params.append(('endMs', params['end_ms']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/anomaly/{dashboardId}/chart/{chartHash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_chart_anomalies_of_one_dashboard(self, dashboard_id, **kwargs):  # noqa: E501
        """Get all anomalies for a dashboard that does not have any dashboard parameters during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_anomalies_of_one_dashboard(dashboard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_chart_anomalies_of_one_dashboard_with_http_info(dashboard_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_chart_anomalies_of_one_dashboard_with_http_info(dashboard_id, **kwargs)  # noqa: E501
            return data

    def get_chart_anomalies_of_one_dashboard_with_http_info(self, dashboard_id, **kwargs):  # noqa: E501
        """Get all anomalies for a dashboard that does not have any dashboard parameters during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chart_anomalies_of_one_dashboard_with_http_info(dashboard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'start_ms', 'end_ms', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chart_anomalies_of_one_dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `get_chart_anomalies_of_one_dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']  # noqa: E501

        query_params = []
        if 'start_ms' in params:
            query_params.append(('startMs', params['start_ms']))  # noqa: E501
        if 'end_ms' in params:
            query_params.append(('endMs', params['end_ms']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/anomaly/{dashboardId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboard_anomalies(self, dashboard_id, param_hash, **kwargs):  # noqa: E501
        """Get all anomalies for a dashboard with a particular set of dashboard parameters as identified by paramHash, during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_anomalies(dashboard_id, param_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param str param_hash: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboard_anomalies_with_http_info(dashboard_id, param_hash, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboard_anomalies_with_http_info(dashboard_id, param_hash, **kwargs)  # noqa: E501
            return data

    def get_dashboard_anomalies_with_http_info(self, dashboard_id, param_hash, **kwargs):  # noqa: E501
        """Get all anomalies for a dashboard with a particular set of dashboard parameters as identified by paramHash, during a time interval  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_anomalies_with_http_info(dashboard_id, param_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_id: (required)
        :param str param_hash: (required)
        :param int start_ms:
        :param int end_ms:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'param_hash', 'start_ms', 'end_ms', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dashboard_anomalies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `get_dashboard_anomalies`")  # noqa: E501
        # verify the required parameter 'param_hash' is set
        if ('param_hash' not in params or
                params['param_hash'] is None):
            raise ValueError("Missing the required parameter `param_hash` when calling `get_dashboard_anomalies`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboardId'] = params['dashboard_id']  # noqa: E501
        if 'param_hash' in params:
            path_params['paramHash'] = params['param_hash']  # noqa: E501

        query_params = []
        if 'start_ms' in params:
            query_params.append(('startMs', params['start_ms']))  # noqa: E501
        if 'end_ms' in params:
            query_params.append(('endMs', params['end_ms']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/anomaly/{dashboardId}/{paramHash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_related_anomalies(self, event_id, **kwargs):  # noqa: E501
        """Get all related anomalies for a firing event with a time span  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_related_anomalies(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :param str rendering_method:
        :param bool is_overlapped:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_related_anomalies_with_http_info(event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_related_anomalies_with_http_info(event_id, **kwargs)  # noqa: E501
            return data

    def get_related_anomalies_with_http_info(self, event_id, **kwargs):  # noqa: E501
        """Get all related anomalies for a firing event with a time span  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_related_anomalies_with_http_info(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :param str rendering_method:
        :param bool is_overlapped:
        :param int limit:
        :return: ResponseContainerPagedAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_id', 'rendering_method', 'is_overlapped', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_related_anomalies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_id' is set
        if ('event_id' not in params or
                params['event_id'] is None):
            raise ValueError("Missing the required parameter `event_id` when calling `get_related_anomalies`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_id' in params:
            path_params['eventId'] = params['event_id']  # noqa: E501

        query_params = []
        if 'rendering_method' in params:
            query_params.append(('renderingMethod', params['rendering_method']))  # noqa: E501
        if 'is_overlapped' in params:
            query_params.append(('isOverlapped', params['is_overlapped']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/anomaly/{eventId}/anomalies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
