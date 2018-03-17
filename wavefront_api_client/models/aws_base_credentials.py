# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AWSBaseCredentials(object):
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
        'role_arn': 'str',
        'external_id': 'str'
    }

    attribute_map = {
        'role_arn': 'roleArn',
        'external_id': 'externalId'
    }

    def __init__(self, role_arn=None, external_id=None):  # noqa: E501
        """AWSBaseCredentials - a model defined in Swagger"""  # noqa: E501

        self._role_arn = None
        self._external_id = None
        self.discriminator = None

        self.role_arn = role_arn
        self.external_id = external_id

    @property
    def role_arn(self):
        """Gets the role_arn of this AWSBaseCredentials.  # noqa: E501

        The Role ARN that the customer has created in AWS IAM to allow access to Wavefront  # noqa: E501

        :return: The role_arn of this AWSBaseCredentials.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this AWSBaseCredentials.

        The Role ARN that the customer has created in AWS IAM to allow access to Wavefront  # noqa: E501

        :param role_arn: The role_arn of this AWSBaseCredentials.  # noqa: E501
        :type: str
        """
        if role_arn is None:
            raise ValueError("Invalid value for `role_arn`, must not be `None`")  # noqa: E501

        self._role_arn = role_arn

    @property
    def external_id(self):
        """Gets the external_id of this AWSBaseCredentials.  # noqa: E501

        The external id corresponding to the Role ARN  # noqa: E501

        :return: The external_id of this AWSBaseCredentials.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AWSBaseCredentials.

        The external id corresponding to the Role ARN  # noqa: E501

        :param external_id: The external_id of this AWSBaseCredentials.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501

        self._external_id = external_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AWSBaseCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
