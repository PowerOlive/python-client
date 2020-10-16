# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MonitoredServiceDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'application': 'str',
        'created': 'int',
        'custom_dashboard_link': 'str',
        'hidden': 'bool',
        'last_reported': 'int',
        'last_updated': 'int',
        'satisfied_latency_millis': 'int',
        'service': 'str',
        'status': 'str',
        'update_user_id': 'str'
    }

    attribute_map = {
        'application': 'application',
        'created': 'created',
        'custom_dashboard_link': 'customDashboardLink',
        'hidden': 'hidden',
        'last_reported': 'lastReported',
        'last_updated': 'lastUpdated',
        'satisfied_latency_millis': 'satisfiedLatencyMillis',
        'service': 'service',
        'status': 'status',
        'update_user_id': 'updateUserId'
    }

    def __init__(self, application=None, created=None, custom_dashboard_link=None, hidden=None, last_reported=None, last_updated=None, satisfied_latency_millis=None, service=None, status=None, update_user_id=None):  # noqa: E501
        """MonitoredServiceDTO - a model defined in Swagger"""  # noqa: E501

        self._application = None
        self._created = None
        self._custom_dashboard_link = None
        self._hidden = None
        self._last_reported = None
        self._last_updated = None
        self._satisfied_latency_millis = None
        self._service = None
        self._status = None
        self._update_user_id = None
        self.discriminator = None

        self.application = application
        if created is not None:
            self.created = created
        if custom_dashboard_link is not None:
            self.custom_dashboard_link = custom_dashboard_link
        if hidden is not None:
            self.hidden = hidden
        if last_reported is not None:
            self.last_reported = last_reported
        if last_updated is not None:
            self.last_updated = last_updated
        if satisfied_latency_millis is not None:
            self.satisfied_latency_millis = satisfied_latency_millis
        self.service = service
        if status is not None:
            self.status = status
        if update_user_id is not None:
            self.update_user_id = update_user_id

    @property
    def application(self):
        """Gets the application of this MonitoredServiceDTO.  # noqa: E501

        Application Name of the monitored service  # noqa: E501

        :return: The application of this MonitoredServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this MonitoredServiceDTO.

        Application Name of the monitored service  # noqa: E501

        :param application: The application of this MonitoredServiceDTO.  # noqa: E501
        :type: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def created(self):
        """Gets the created of this MonitoredServiceDTO.  # noqa: E501

        Created epoch of monitored service  # noqa: E501

        :return: The created of this MonitoredServiceDTO.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MonitoredServiceDTO.

        Created epoch of monitored service  # noqa: E501

        :param created: The created of this MonitoredServiceDTO.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def custom_dashboard_link(self):
        """Gets the custom_dashboard_link of this MonitoredServiceDTO.  # noqa: E501

        Customer dashboard link  # noqa: E501

        :return: The custom_dashboard_link of this MonitoredServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._custom_dashboard_link

    @custom_dashboard_link.setter
    def custom_dashboard_link(self, custom_dashboard_link):
        """Sets the custom_dashboard_link of this MonitoredServiceDTO.

        Customer dashboard link  # noqa: E501

        :param custom_dashboard_link: The custom_dashboard_link of this MonitoredServiceDTO.  # noqa: E501
        :type: str
        """

        self._custom_dashboard_link = custom_dashboard_link

    @property
    def hidden(self):
        """Gets the hidden of this MonitoredServiceDTO.  # noqa: E501

        Monitored service is hidden or not  # noqa: E501

        :return: The hidden of this MonitoredServiceDTO.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this MonitoredServiceDTO.

        Monitored service is hidden or not  # noqa: E501

        :param hidden: The hidden of this MonitoredServiceDTO.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def last_reported(self):
        """Gets the last_reported of this MonitoredServiceDTO.  # noqa: E501

        Last reported epoch of monitored service  # noqa: E501

        :return: The last_reported of this MonitoredServiceDTO.  # noqa: E501
        :rtype: int
        """
        return self._last_reported

    @last_reported.setter
    def last_reported(self, last_reported):
        """Sets the last_reported of this MonitoredServiceDTO.

        Last reported epoch of monitored service  # noqa: E501

        :param last_reported: The last_reported of this MonitoredServiceDTO.  # noqa: E501
        :type: int
        """

        self._last_reported = last_reported

    @property
    def last_updated(self):
        """Gets the last_updated of this MonitoredServiceDTO.  # noqa: E501

        Last update epoch of monitored service  # noqa: E501

        :return: The last_updated of this MonitoredServiceDTO.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this MonitoredServiceDTO.

        Last update epoch of monitored service  # noqa: E501

        :param last_updated: The last_updated of this MonitoredServiceDTO.  # noqa: E501
        :type: int
        """

        self._last_updated = last_updated

    @property
    def satisfied_latency_millis(self):
        """Gets the satisfied_latency_millis of this MonitoredServiceDTO.  # noqa: E501

        Satisfied latency of monitored service  # noqa: E501

        :return: The satisfied_latency_millis of this MonitoredServiceDTO.  # noqa: E501
        :rtype: int
        """
        return self._satisfied_latency_millis

    @satisfied_latency_millis.setter
    def satisfied_latency_millis(self, satisfied_latency_millis):
        """Sets the satisfied_latency_millis of this MonitoredServiceDTO.

        Satisfied latency of monitored service  # noqa: E501

        :param satisfied_latency_millis: The satisfied_latency_millis of this MonitoredServiceDTO.  # noqa: E501
        :type: int
        """

        self._satisfied_latency_millis = satisfied_latency_millis

    @property
    def service(self):
        """Gets the service of this MonitoredServiceDTO.  # noqa: E501

        Service Name of the monitored service  # noqa: E501

        :return: The service of this MonitoredServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this MonitoredServiceDTO.

        Service Name of the monitored service  # noqa: E501

        :param service: The service of this MonitoredServiceDTO.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def status(self):
        """Gets the status of this MonitoredServiceDTO.  # noqa: E501

        Status of monitored service  # noqa: E501

        :return: The status of this MonitoredServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MonitoredServiceDTO.

        Status of monitored service  # noqa: E501

        :param status: The status of this MonitoredServiceDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def update_user_id(self):
        """Gets the update_user_id of this MonitoredServiceDTO.  # noqa: E501

        Last update user id of monitored service  # noqa: E501

        :return: The update_user_id of this MonitoredServiceDTO.  # noqa: E501
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        """Sets the update_user_id of this MonitoredServiceDTO.

        Last update user id of monitored service  # noqa: E501

        :param update_user_id: The update_user_id of this MonitoredServiceDTO.  # noqa: E501
        :type: str
        """

        self._update_user_id = update_user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MonitoredServiceDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MonitoredServiceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other