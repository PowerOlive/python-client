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

from wavefront_api_client.models.integration_alias import IntegrationAlias  # noqa: F401,E501
from wavefront_api_client.models.integration_dashboard import IntegrationDashboard  # noqa: F401,E501
from wavefront_api_client.models.integration_metrics import IntegrationMetrics  # noqa: F401,E501
from wavefront_api_client.models.integration_status import IntegrationStatus  # noqa: F401,E501


class Integration(object):
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
        'icon': 'str',
        'version': 'str',
        'name': 'str',
        'id': 'str',
        'metrics': 'IntegrationMetrics',
        'description': 'str',
        'base_url': 'str',
        'status': 'IntegrationStatus',
        'creator_id': 'str',
        'updater_id': 'str',
        'created_epoch_millis': 'int',
        'updated_epoch_millis': 'int',
        'dashboards': 'list[IntegrationDashboard]',
        'alias_of': 'str',
        'alias_integrations': 'list[IntegrationAlias]',
        'deleted': 'bool',
        'overview': 'str',
        'setup': 'str'
    }

    attribute_map = {
        'icon': 'icon',
        'version': 'version',
        'name': 'name',
        'id': 'id',
        'metrics': 'metrics',
        'description': 'description',
        'base_url': 'baseUrl',
        'status': 'status',
        'creator_id': 'creatorId',
        'updater_id': 'updaterId',
        'created_epoch_millis': 'createdEpochMillis',
        'updated_epoch_millis': 'updatedEpochMillis',
        'dashboards': 'dashboards',
        'alias_of': 'aliasOf',
        'alias_integrations': 'aliasIntegrations',
        'deleted': 'deleted',
        'overview': 'overview',
        'setup': 'setup'
    }

    def __init__(self, icon=None, version=None, name=None, id=None, metrics=None, description=None, base_url=None, status=None, creator_id=None, updater_id=None, created_epoch_millis=None, updated_epoch_millis=None, dashboards=None, alias_of=None, alias_integrations=None, deleted=None, overview=None, setup=None):  # noqa: E501
        """Integration - a model defined in Swagger"""  # noqa: E501

        self._icon = None
        self._version = None
        self._name = None
        self._id = None
        self._metrics = None
        self._description = None
        self._base_url = None
        self._status = None
        self._creator_id = None
        self._updater_id = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._dashboards = None
        self._alias_of = None
        self._alias_integrations = None
        self._deleted = None
        self._overview = None
        self._setup = None
        self.discriminator = None

        self.icon = icon
        self.version = version
        self.name = name
        if id is not None:
            self.id = id
        if metrics is not None:
            self.metrics = metrics
        self.description = description
        if base_url is not None:
            self.base_url = base_url
        if status is not None:
            self.status = status
        if creator_id is not None:
            self.creator_id = creator_id
        if updater_id is not None:
            self.updater_id = updater_id
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if dashboards is not None:
            self.dashboards = dashboards
        if alias_of is not None:
            self.alias_of = alias_of
        if alias_integrations is not None:
            self.alias_integrations = alias_integrations
        if deleted is not None:
            self.deleted = deleted
        if overview is not None:
            self.overview = overview
        if setup is not None:
            self.setup = setup

    @property
    def icon(self):
        """Gets the icon of this Integration.  # noqa: E501

        URI path to the integration icon  # noqa: E501

        :return: The icon of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Integration.

        URI path to the integration icon  # noqa: E501

        :param icon: The icon of this Integration.  # noqa: E501
        :type: str
        """
        if icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def version(self):
        """Gets the version of this Integration.  # noqa: E501

        Integration version string  # noqa: E501

        :return: The version of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Integration.

        Integration version string  # noqa: E501

        :param version: The version of this Integration.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def name(self):
        """Gets the name of this Integration.  # noqa: E501

        Integration name  # noqa: E501

        :return: The name of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Integration.

        Integration name  # noqa: E501

        :param name: The name of this Integration.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this Integration.  # noqa: E501


        :return: The id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Integration.


        :param id: The id of this Integration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metrics(self):
        """Gets the metrics of this Integration.  # noqa: E501


        :return: The metrics of this Integration.  # noqa: E501
        :rtype: IntegrationMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this Integration.


        :param metrics: The metrics of this Integration.  # noqa: E501
        :type: IntegrationMetrics
        """

        self._metrics = metrics

    @property
    def description(self):
        """Gets the description of this Integration.  # noqa: E501

        Integration description  # noqa: E501

        :return: The description of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Integration.

        Integration description  # noqa: E501

        :param description: The description of this Integration.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def base_url(self):
        """Gets the base_url of this Integration.  # noqa: E501

        Base URL for this integration's assets  # noqa: E501

        :return: The base_url of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this Integration.

        Base URL for this integration's assets  # noqa: E501

        :param base_url: The base_url of this Integration.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def status(self):
        """Gets the status of this Integration.  # noqa: E501


        :return: The status of this Integration.  # noqa: E501
        :rtype: IntegrationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Integration.


        :param status: The status of this Integration.  # noqa: E501
        :type: IntegrationStatus
        """

        self._status = status

    @property
    def creator_id(self):
        """Gets the creator_id of this Integration.  # noqa: E501


        :return: The creator_id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Integration.


        :param creator_id: The creator_id of this Integration.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def updater_id(self):
        """Gets the updater_id of this Integration.  # noqa: E501


        :return: The updater_id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this Integration.


        :param updater_id: The updater_id of this Integration.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this Integration.  # noqa: E501


        :return: The created_epoch_millis of this Integration.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this Integration.


        :param created_epoch_millis: The created_epoch_millis of this Integration.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this Integration.  # noqa: E501


        :return: The updated_epoch_millis of this Integration.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this Integration.


        :param updated_epoch_millis: The updated_epoch_millis of this Integration.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def dashboards(self):
        """Gets the dashboards of this Integration.  # noqa: E501

        A list of dashboards belonging to this integration  # noqa: E501

        :return: The dashboards of this Integration.  # noqa: E501
        :rtype: list[IntegrationDashboard]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Sets the dashboards of this Integration.

        A list of dashboards belonging to this integration  # noqa: E501

        :param dashboards: The dashboards of this Integration.  # noqa: E501
        :type: list[IntegrationDashboard]
        """

        self._dashboards = dashboards

    @property
    def alias_of(self):
        """Gets the alias_of of this Integration.  # noqa: E501

        If set, designates this integration as an alias integration, of the integration whose id is specified.  # noqa: E501

        :return: The alias_of of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._alias_of

    @alias_of.setter
    def alias_of(self, alias_of):
        """Sets the alias_of of this Integration.

        If set, designates this integration as an alias integration, of the integration whose id is specified.  # noqa: E501

        :param alias_of: The alias_of of this Integration.  # noqa: E501
        :type: str
        """

        self._alias_of = alias_of

    @property
    def alias_integrations(self):
        """Gets the alias_integrations of this Integration.  # noqa: E501

        If set, a list of objects describing integrations that alias this one.  # noqa: E501

        :return: The alias_integrations of this Integration.  # noqa: E501
        :rtype: list[IntegrationAlias]
        """
        return self._alias_integrations

    @alias_integrations.setter
    def alias_integrations(self, alias_integrations):
        """Sets the alias_integrations of this Integration.

        If set, a list of objects describing integrations that alias this one.  # noqa: E501

        :param alias_integrations: The alias_integrations of this Integration.  # noqa: E501
        :type: list[IntegrationAlias]
        """

        self._alias_integrations = alias_integrations

    @property
    def deleted(self):
        """Gets the deleted of this Integration.  # noqa: E501


        :return: The deleted of this Integration.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Integration.


        :param deleted: The deleted of this Integration.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def overview(self):
        """Gets the overview of this Integration.  # noqa: E501

        Descriptive text giving an overview of integration functionality  # noqa: E501

        :return: The overview of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this Integration.

        Descriptive text giving an overview of integration functionality  # noqa: E501

        :param overview: The overview of this Integration.  # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def setup(self):
        """Gets the setup of this Integration.  # noqa: E501

        How the integration will be set-up  # noqa: E501

        :return: The setup of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._setup

    @setup.setter
    def setup(self, setup):
        """Sets the setup of this Integration.

        How the integration will be set-up  # noqa: E501

        :param setup: The setup of this Integration.  # noqa: E501
        :type: str
        """

        self._setup = setup

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
        if not isinstance(other, Integration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
