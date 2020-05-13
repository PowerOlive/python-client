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


class RelatedData(object):
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
        'alert_description': 'str',
        'anomaly_chart_link': 'str',
        'common_dimensions': 'list[str]',
        'common_metrics': 'list[str]',
        'common_sources': 'list[str]',
        'enhanced_score': 'float',
        'related_id': 'str',
        'summary': 'str'
    }

    attribute_map = {
        'alert_description': 'alertDescription',
        'anomaly_chart_link': 'anomalyChartLink',
        'common_dimensions': 'commonDimensions',
        'common_metrics': 'commonMetrics',
        'common_sources': 'commonSources',
        'enhanced_score': 'enhancedScore',
        'related_id': 'relatedId',
        'summary': 'summary'
    }

    def __init__(self, alert_description=None, anomaly_chart_link=None, common_dimensions=None, common_metrics=None, common_sources=None, enhanced_score=None, related_id=None, summary=None):  # noqa: E501
        """RelatedData - a model defined in Swagger"""  # noqa: E501

        self._alert_description = None
        self._anomaly_chart_link = None
        self._common_dimensions = None
        self._common_metrics = None
        self._common_sources = None
        self._enhanced_score = None
        self._related_id = None
        self._summary = None
        self.discriminator = None

        if alert_description is not None:
            self.alert_description = alert_description
        if anomaly_chart_link is not None:
            self.anomaly_chart_link = anomaly_chart_link
        if common_dimensions is not None:
            self.common_dimensions = common_dimensions
        if common_metrics is not None:
            self.common_metrics = common_metrics
        if common_sources is not None:
            self.common_sources = common_sources
        if enhanced_score is not None:
            self.enhanced_score = enhanced_score
        if related_id is not None:
            self.related_id = related_id
        if summary is not None:
            self.summary = summary

    @property
    def alert_description(self):
        """Gets the alert_description of this RelatedData.  # noqa: E501

        If this event is generated by an alert, the description of that alert.  # noqa: E501

        :return: The alert_description of this RelatedData.  # noqa: E501
        :rtype: str
        """
        return self._alert_description

    @alert_description.setter
    def alert_description(self, alert_description):
        """Sets the alert_description of this RelatedData.

        If this event is generated by an alert, the description of that alert.  # noqa: E501

        :param alert_description: The alert_description of this RelatedData.  # noqa: E501
        :type: str
        """

        self._alert_description = alert_description

    @property
    def anomaly_chart_link(self):
        """Gets the anomaly_chart_link of this RelatedData.  # noqa: E501

        Chart Link of the anomaly to which this event is related  # noqa: E501

        :return: The anomaly_chart_link of this RelatedData.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_chart_link

    @anomaly_chart_link.setter
    def anomaly_chart_link(self, anomaly_chart_link):
        """Sets the anomaly_chart_link of this RelatedData.

        Chart Link of the anomaly to which this event is related  # noqa: E501

        :param anomaly_chart_link: The anomaly_chart_link of this RelatedData.  # noqa: E501
        :type: str
        """

        self._anomaly_chart_link = anomaly_chart_link

    @property
    def common_dimensions(self):
        """Gets the common_dimensions of this RelatedData.  # noqa: E501

        Set of common dimensions between the 2 events, presented in key=value format  # noqa: E501

        :return: The common_dimensions of this RelatedData.  # noqa: E501
        :rtype: list[str]
        """
        return self._common_dimensions

    @common_dimensions.setter
    def common_dimensions(self, common_dimensions):
        """Sets the common_dimensions of this RelatedData.

        Set of common dimensions between the 2 events, presented in key=value format  # noqa: E501

        :param common_dimensions: The common_dimensions of this RelatedData.  # noqa: E501
        :type: list[str]
        """

        self._common_dimensions = common_dimensions

    @property
    def common_metrics(self):
        """Gets the common_metrics of this RelatedData.  # noqa: E501

        Set of common metrics/labels between the 2 events or anomalies  # noqa: E501

        :return: The common_metrics of this RelatedData.  # noqa: E501
        :rtype: list[str]
        """
        return self._common_metrics

    @common_metrics.setter
    def common_metrics(self, common_metrics):
        """Sets the common_metrics of this RelatedData.

        Set of common metrics/labels between the 2 events or anomalies  # noqa: E501

        :param common_metrics: The common_metrics of this RelatedData.  # noqa: E501
        :type: list[str]
        """

        self._common_metrics = common_metrics

    @property
    def common_sources(self):
        """Gets the common_sources of this RelatedData.  # noqa: E501

        Set of common sources between the 2 events or anomalies  # noqa: E501

        :return: The common_sources of this RelatedData.  # noqa: E501
        :rtype: list[str]
        """
        return self._common_sources

    @common_sources.setter
    def common_sources(self, common_sources):
        """Sets the common_sources of this RelatedData.

        Set of common sources between the 2 events or anomalies  # noqa: E501

        :param common_sources: The common_sources of this RelatedData.  # noqa: E501
        :type: list[str]
        """

        self._common_sources = common_sources

    @property
    def enhanced_score(self):
        """Gets the enhanced_score of this RelatedData.  # noqa: E501

        Enhanced score to sort related events and anomalies  # noqa: E501

        :return: The enhanced_score of this RelatedData.  # noqa: E501
        :rtype: float
        """
        return self._enhanced_score

    @enhanced_score.setter
    def enhanced_score(self, enhanced_score):
        """Sets the enhanced_score of this RelatedData.

        Enhanced score to sort related events and anomalies  # noqa: E501

        :param enhanced_score: The enhanced_score of this RelatedData.  # noqa: E501
        :type: float
        """

        self._enhanced_score = enhanced_score

    @property
    def related_id(self):
        """Gets the related_id of this RelatedData.  # noqa: E501

        ID of the event to which this event is related  # noqa: E501

        :return: The related_id of this RelatedData.  # noqa: E501
        :rtype: str
        """
        return self._related_id

    @related_id.setter
    def related_id(self, related_id):
        """Sets the related_id of this RelatedData.

        ID of the event to which this event is related  # noqa: E501

        :param related_id: The related_id of this RelatedData.  # noqa: E501
        :type: str
        """

        self._related_id = related_id

    @property
    def summary(self):
        """Gets the summary of this RelatedData.  # noqa: E501

        Text summary of why the two events are related  # noqa: E501

        :return: The summary of this RelatedData.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this RelatedData.

        Text summary of why the two events are related  # noqa: E501

        :param summary: The summary of this RelatedData.  # noqa: E501
        :type: str
        """

        self._summary = summary

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
        if issubclass(RelatedData, dict):
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
        if not isinstance(other, RelatedData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
