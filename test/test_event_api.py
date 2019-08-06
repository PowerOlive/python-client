# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.event_api import EventApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.event_api.EventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_event_tag(self):
        """Test case for add_event_tag

        Add a tag to a specific event  # noqa: E501
        """
        pass

    def test_close_event(self):
        """Test case for close_event

        Close a specific event  # noqa: E501
        """
        pass

    def test_create_event(self):
        """Test case for create_event

        Create a specific event  # noqa: E501
        """
        pass

    def test_delete_event(self):
        """Test case for delete_event

        Delete a specific event  # noqa: E501
        """
        pass

    def test_get_all_events_with_time_range(self):
        """Test case for get_all_events_with_time_range

        List all the events for a customer within a time range  # noqa: E501
        """
        pass

    def test_get_event(self):
        """Test case for get_event

        Get a specific event  # noqa: E501
        """
        pass

    def test_get_event_tags(self):
        """Test case for get_event_tags

        Get all tags associated with a specific event  # noqa: E501
        """
        pass

    def test_remove_event_tag(self):
        """Test case for remove_event_tag

        Remove a tag from a specific event  # noqa: E501
        """
        pass

    def test_set_event_tags(self):
        """Test case for set_event_tags

        Set all tags associated with a specific event  # noqa: E501
        """
        pass

    def test_update_event(self):
        """Test case for update_event

        Update a specific event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()