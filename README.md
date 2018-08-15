# Wavefront API Client
<p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header `"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;"` to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2
- Package version: 2.3.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install wavefront-api-client
```

Or you can install the latest version directly from Github
```sh
pip install git+https://github.com/wavefrontHQ/python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/wavefrontHQ/python-client.git`)

Then import the package:
```python
import wavefront_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wavefront_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

_config = wavefront_api_client.Configuration()
_config.host = 'https://YOUR_INSTANCE.wavefront.com'

api_instance = wavefront_api_client.AlertApi(
    wavefront_api_client.ApiClient(configuration=_config,
                                   header_name='Authorization',
                                   header_value='Bearer ' + 'YOUR_API_TOKEN'))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific alert
    api_response = api_instance.add_alert_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_tag: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertApi* | [**add_alert_tag**](docs/AlertApi.md#add_alert_tag) | **PUT** /api/v2/alert/{id}/tag/{tagValue} | Add a tag to a specific alert
*AlertApi* | [**create_alert**](docs/AlertApi.md#create_alert) | **POST** /api/v2/alert | Create a specific alert
*AlertApi* | [**delete_alert**](docs/AlertApi.md#delete_alert) | **DELETE** /api/v2/alert/{id} | Delete a specific alert
*AlertApi* | [**get_alert**](docs/AlertApi.md#get_alert) | **GET** /api/v2/alert/{id} | Get a specific alert
*AlertApi* | [**get_alert_history**](docs/AlertApi.md#get_alert_history) | **GET** /api/v2/alert/{id}/history | Get the version history of a specific alert
*AlertApi* | [**get_alert_tags**](docs/AlertApi.md#get_alert_tags) | **GET** /api/v2/alert/{id}/tag | Get all tags associated with a specific alert
*AlertApi* | [**get_alert_version**](docs/AlertApi.md#get_alert_version) | **GET** /api/v2/alert/{id}/history/{version} | Get a specific historical version of a specific alert
*AlertApi* | [**get_alerts_summary**](docs/AlertApi.md#get_alerts_summary) | **GET** /api/v2/alert/summary | Count alerts of various statuses for a customer
*AlertApi* | [**get_all_alert**](docs/AlertApi.md#get_all_alert) | **GET** /api/v2/alert | Get all alerts for a customer
*AlertApi* | [**remove_alert_tag**](docs/AlertApi.md#remove_alert_tag) | **DELETE** /api/v2/alert/{id}/tag/{tagValue} | Remove a tag from a specific alert
*AlertApi* | [**set_alert_tags**](docs/AlertApi.md#set_alert_tags) | **POST** /api/v2/alert/{id}/tag | Set all tags associated with a specific alert
*AlertApi* | [**snooze_alert**](docs/AlertApi.md#snooze_alert) | **POST** /api/v2/alert/{id}/snooze | Snooze a specific alert for some number of seconds
*AlertApi* | [**undelete_alert**](docs/AlertApi.md#undelete_alert) | **POST** /api/v2/alert/{id}/undelete | Undelete a specific alert
*AlertApi* | [**unsnooze_alert**](docs/AlertApi.md#unsnooze_alert) | **POST** /api/v2/alert/{id}/unsnooze | Unsnooze a specific alert
*AlertApi* | [**update_alert**](docs/AlertApi.md#update_alert) | **PUT** /api/v2/alert/{id} | Update a specific alert
*CloudIntegrationApi* | [**create_cloud_integration**](docs/CloudIntegrationApi.md#create_cloud_integration) | **POST** /api/v2/cloudintegration | Create a cloud integration
*CloudIntegrationApi* | [**delete_cloud_integration**](docs/CloudIntegrationApi.md#delete_cloud_integration) | **DELETE** /api/v2/cloudintegration/{id} | Delete a specific cloud integration
*CloudIntegrationApi* | [**disable_cloud_integration**](docs/CloudIntegrationApi.md#disable_cloud_integration) | **POST** /api/v2/cloudintegration/{id}/disable | Disable a specific cloud integration
*CloudIntegrationApi* | [**enable_cloud_integration**](docs/CloudIntegrationApi.md#enable_cloud_integration) | **POST** /api/v2/cloudintegration/{id}/enable | Enable a specific cloud integration
*CloudIntegrationApi* | [**get_all_cloud_integration**](docs/CloudIntegrationApi.md#get_all_cloud_integration) | **GET** /api/v2/cloudintegration | Get all cloud integrations for a customer
*CloudIntegrationApi* | [**get_cloud_integration**](docs/CloudIntegrationApi.md#get_cloud_integration) | **GET** /api/v2/cloudintegration/{id} | Get a specific cloud integration
*CloudIntegrationApi* | [**undelete_cloud_integration**](docs/CloudIntegrationApi.md#undelete_cloud_integration) | **POST** /api/v2/cloudintegration/{id}/undelete | Undelete a specific cloud integration
*CloudIntegrationApi* | [**update_cloud_integration**](docs/CloudIntegrationApi.md#update_cloud_integration) | **PUT** /api/v2/cloudintegration/{id} | Update a specific cloud integration
*DashboardApi* | [**add_dashboard_tag**](docs/DashboardApi.md#add_dashboard_tag) | **PUT** /api/v2/dashboard/{id}/tag/{tagValue} | Add a tag to a specific dashboard
*DashboardApi* | [**create_dashboard**](docs/DashboardApi.md#create_dashboard) | **POST** /api/v2/dashboard | Create a specific dashboard
*DashboardApi* | [**delete_dashboard**](docs/DashboardApi.md#delete_dashboard) | **DELETE** /api/v2/dashboard/{id} | Delete a specific dashboard
*DashboardApi* | [**get_all_dashboard**](docs/DashboardApi.md#get_all_dashboard) | **GET** /api/v2/dashboard | Get all dashboards for a customer
*DashboardApi* | [**get_dashboard**](docs/DashboardApi.md#get_dashboard) | **GET** /api/v2/dashboard/{id} | Get a specific dashboard
*DashboardApi* | [**get_dashboard_history**](docs/DashboardApi.md#get_dashboard_history) | **GET** /api/v2/dashboard/{id}/history | Get the version history of a specific dashboard
*DashboardApi* | [**get_dashboard_tags**](docs/DashboardApi.md#get_dashboard_tags) | **GET** /api/v2/dashboard/{id}/tag | Get all tags associated with a specific dashboard
*DashboardApi* | [**get_dashboard_version**](docs/DashboardApi.md#get_dashboard_version) | **GET** /api/v2/dashboard/{id}/history/{version} | Get a specific version of a specific dashboard
*DashboardApi* | [**remove_dashboard_tag**](docs/DashboardApi.md#remove_dashboard_tag) | **DELETE** /api/v2/dashboard/{id}/tag/{tagValue} | Remove a tag from a specific dashboard
*DashboardApi* | [**set_dashboard_tags**](docs/DashboardApi.md#set_dashboard_tags) | **POST** /api/v2/dashboard/{id}/tag | Set all tags associated with a specific dashboard
*DashboardApi* | [**undelete_dashboard**](docs/DashboardApi.md#undelete_dashboard) | **POST** /api/v2/dashboard/{id}/undelete | Undelete a specific dashboard
*DashboardApi* | [**update_dashboard**](docs/DashboardApi.md#update_dashboard) | **PUT** /api/v2/dashboard/{id} | Update a specific dashboard
*DerivedMetricApi* | [**add_tag_to_derived_metric**](docs/DerivedMetricApi.md#add_tag_to_derived_metric) | **PUT** /api/v2/derivedmetric/{id}/tag/{tagValue} | Add a tag to a specific Derived Metric
*DerivedMetricApi* | [**create_derived_metric**](docs/DerivedMetricApi.md#create_derived_metric) | **POST** /api/v2/derivedmetric | Create a specific derived metric definition
*DerivedMetricApi* | [**delete_derived_metric**](docs/DerivedMetricApi.md#delete_derived_metric) | **DELETE** /api/v2/derivedmetric/{id} | Delete a specific derived metric definition
*DerivedMetricApi* | [**get_all_derived_metrics**](docs/DerivedMetricApi.md#get_all_derived_metrics) | **GET** /api/v2/derivedmetric | Get all derived metric definitions for a customer
*DerivedMetricApi* | [**get_derived_metric**](docs/DerivedMetricApi.md#get_derived_metric) | **GET** /api/v2/derivedmetric/{id} | Get a specific registered query
*DerivedMetricApi* | [**get_derived_metric_by_version**](docs/DerivedMetricApi.md#get_derived_metric_by_version) | **GET** /api/v2/derivedmetric/{id}/history/{version} | Get a specific historical version of a specific derived metric definition
*DerivedMetricApi* | [**get_derived_metric_history**](docs/DerivedMetricApi.md#get_derived_metric_history) | **GET** /api/v2/derivedmetric/{id}/history | Get the version history of a specific derived metric definition
*DerivedMetricApi* | [**get_derived_metric_tags**](docs/DerivedMetricApi.md#get_derived_metric_tags) | **GET** /api/v2/derivedmetric/{id}/tag | Get all tags associated with a specific derived metric definition
*DerivedMetricApi* | [**remove_tag_from_derived_metric**](docs/DerivedMetricApi.md#remove_tag_from_derived_metric) | **DELETE** /api/v2/derivedmetric/{id}/tag/{tagValue} | Remove a tag from a specific Derived Metric
*DerivedMetricApi* | [**set_derived_metric_tags**](docs/DerivedMetricApi.md#set_derived_metric_tags) | **POST** /api/v2/derivedmetric/{id}/tag | Set all tags associated with a specific derived metric definition
*DerivedMetricApi* | [**undelete_derived_metric**](docs/DerivedMetricApi.md#undelete_derived_metric) | **POST** /api/v2/derivedmetric/{id}/undelete | Undelete a specific derived metric definition
*DerivedMetricApi* | [**update_derived_metric**](docs/DerivedMetricApi.md#update_derived_metric) | **PUT** /api/v2/derivedmetric/{id} | Update a specific derived metric definition
*EventApi* | [**add_event_tag**](docs/EventApi.md#add_event_tag) | **PUT** /api/v2/event/{id}/tag/{tagValue} | Add a tag to a specific event
*EventApi* | [**close_event**](docs/EventApi.md#close_event) | **POST** /api/v2/event/{id}/close | Close a specific event
*EventApi* | [**create_event**](docs/EventApi.md#create_event) | **POST** /api/v2/event | Create a specific event
*EventApi* | [**delete_event**](docs/EventApi.md#delete_event) | **DELETE** /api/v2/event/{id} | Delete a specific event
*EventApi* | [**get_all_events_with_time_range**](docs/EventApi.md#get_all_events_with_time_range) | **GET** /api/v2/event | List all the events for a customer within a time range
*EventApi* | [**get_event**](docs/EventApi.md#get_event) | **GET** /api/v2/event/{id} | Get a specific event
*EventApi* | [**get_event_tags**](docs/EventApi.md#get_event_tags) | **GET** /api/v2/event/{id}/tag | Get all tags associated with a specific event
*EventApi* | [**remove_event_tag**](docs/EventApi.md#remove_event_tag) | **DELETE** /api/v2/event/{id}/tag/{tagValue} | Remove a tag from a specific event
*EventApi* | [**set_event_tags**](docs/EventApi.md#set_event_tags) | **POST** /api/v2/event/{id}/tag | Set all tags associated with a specific event
*EventApi* | [**update_event**](docs/EventApi.md#update_event) | **PUT** /api/v2/event/{id} | Update a specific event
*ExternalLinkApi* | [**create_external_link**](docs/ExternalLinkApi.md#create_external_link) | **POST** /api/v2/extlink | Create a specific external link
*ExternalLinkApi* | [**delete_external_link**](docs/ExternalLinkApi.md#delete_external_link) | **DELETE** /api/v2/extlink/{id} | Delete a specific external link
*ExternalLinkApi* | [**get_all_external_link**](docs/ExternalLinkApi.md#get_all_external_link) | **GET** /api/v2/extlink | Get all external links for a customer
*ExternalLinkApi* | [**get_external_link**](docs/ExternalLinkApi.md#get_external_link) | **GET** /api/v2/extlink/{id} | Get a specific external link
*ExternalLinkApi* | [**update_external_link**](docs/ExternalLinkApi.md#update_external_link) | **PUT** /api/v2/extlink/{id} | Update a specific external link
*IntegrationApi* | [**get_all_integration**](docs/IntegrationApi.md#get_all_integration) | **GET** /api/v2/integration | Gets a flat list of all Wavefront integrations available, along with their status
*IntegrationApi* | [**get_all_integration_in_manifests**](docs/IntegrationApi.md#get_all_integration_in_manifests) | **GET** /api/v2/integration/manifests | Gets all Wavefront integrations as structured in their integration manifests, along with their status
*IntegrationApi* | [**get_all_integration_statuses**](docs/IntegrationApi.md#get_all_integration_statuses) | **GET** /api/v2/integration/status | Gets the status of all Wavefront integrations
*IntegrationApi* | [**get_integration**](docs/IntegrationApi.md#get_integration) | **GET** /api/v2/integration/{id} | Gets a single Wavefront integration by its id, along with its status
*IntegrationApi* | [**get_integration_status**](docs/IntegrationApi.md#get_integration_status) | **GET** /api/v2/integration/{id}/status | Gets the status of a single Wavefront integration
*IntegrationApi* | [**install_integration**](docs/IntegrationApi.md#install_integration) | **POST** /api/v2/integration/{id}/install | Installs a Wavefront integration
*IntegrationApi* | [**uninstall_integration**](docs/IntegrationApi.md#uninstall_integration) | **POST** /api/v2/integration/{id}/uninstall | Uninstalls a Wavefront integration
*MaintenanceWindowApi* | [**create_maintenance_window**](docs/MaintenanceWindowApi.md#create_maintenance_window) | **POST** /api/v2/maintenancewindow | Create a maintenance window
*MaintenanceWindowApi* | [**delete_maintenance_window**](docs/MaintenanceWindowApi.md#delete_maintenance_window) | **DELETE** /api/v2/maintenancewindow/{id} | Delete a specific maintenance window
*MaintenanceWindowApi* | [**get_all_maintenance_window**](docs/MaintenanceWindowApi.md#get_all_maintenance_window) | **GET** /api/v2/maintenancewindow | Get all maintenance windows for a customer
*MaintenanceWindowApi* | [**get_maintenance_window**](docs/MaintenanceWindowApi.md#get_maintenance_window) | **GET** /api/v2/maintenancewindow/{id} | Get a specific maintenance window
*MaintenanceWindowApi* | [**update_maintenance_window**](docs/MaintenanceWindowApi.md#update_maintenance_window) | **PUT** /api/v2/maintenancewindow/{id} | Update a specific maintenance window
*MessageApi* | [**user_get_messages**](docs/MessageApi.md#user_get_messages) | **GET** /api/v2/message | Gets messages applicable to the current user, i.e. within time range and distribution scope
*MessageApi* | [**user_read_message**](docs/MessageApi.md#user_read_message) | **POST** /api/v2/message/{id}/read | Mark a specific message as read
*MetricApi* | [**get_metric_details**](docs/MetricApi.md#get_metric_details) | **GET** /api/v2/chart/metric/detail | Get more details on a metric, including reporting sources and approximate last time reported
*NotificantApi* | [**create_notificant**](docs/NotificantApi.md#create_notificant) | **POST** /api/v2/notificant | Create a notification target
*NotificantApi* | [**delete_notificant**](docs/NotificantApi.md#delete_notificant) | **DELETE** /api/v2/notificant/{id} | Delete a specific notification target
*NotificantApi* | [**get_all_notificants**](docs/NotificantApi.md#get_all_notificants) | **GET** /api/v2/notificant | Get all notification targets for a customer
*NotificantApi* | [**get_notificant**](docs/NotificantApi.md#get_notificant) | **GET** /api/v2/notificant/{id} | Get a specific notification target
*NotificantApi* | [**test_notificant**](docs/NotificantApi.md#test_notificant) | **POST** /api/v2/notificant/test/{id} | Test a specific notification target
*NotificantApi* | [**update_notificant**](docs/NotificantApi.md#update_notificant) | **PUT** /api/v2/notificant/{id} | Update a specific notification target
*ProxyApi* | [**delete_proxy**](docs/ProxyApi.md#delete_proxy) | **DELETE** /api/v2/proxy/{id} | Delete a specific proxy
*ProxyApi* | [**get_all_proxy**](docs/ProxyApi.md#get_all_proxy) | **GET** /api/v2/proxy | Get all proxies for a customer
*ProxyApi* | [**get_proxy**](docs/ProxyApi.md#get_proxy) | **GET** /api/v2/proxy/{id} | Get a specific proxy
*ProxyApi* | [**undelete_proxy**](docs/ProxyApi.md#undelete_proxy) | **POST** /api/v2/proxy/{id}/undelete | Undelete a specific proxy
*ProxyApi* | [**update_proxy**](docs/ProxyApi.md#update_proxy) | **PUT** /api/v2/proxy/{id} | Update the name of a specific proxy
*QueryApi* | [**query_api**](docs/QueryApi.md#query_api) | **GET** /api/v2/chart/api | Perform a charting query against Wavefront servers that returns the appropriate points in the specified time window and granularity
*QueryApi* | [**query_raw**](docs/QueryApi.md#query_raw) | **GET** /api/v2/chart/raw | Perform a raw data query against Wavefront servers that returns second granularity points grouped by tags
*SavedSearchApi* | [**create_saved_search**](docs/SavedSearchApi.md#create_saved_search) | **POST** /api/v2/savedsearch | Create a saved search
*SavedSearchApi* | [**delete_saved_search**](docs/SavedSearchApi.md#delete_saved_search) | **DELETE** /api/v2/savedsearch/{id} | Delete a specific saved search
*SavedSearchApi* | [**get_all_entity_type_saved_searches**](docs/SavedSearchApi.md#get_all_entity_type_saved_searches) | **GET** /api/v2/savedsearch/type/{entitytype} | Get all saved searches for a specific entity type for a user
*SavedSearchApi* | [**get_all_saved_searches**](docs/SavedSearchApi.md#get_all_saved_searches) | **GET** /api/v2/savedsearch | Get all saved searches for a user
*SavedSearchApi* | [**get_saved_search**](docs/SavedSearchApi.md#get_saved_search) | **GET** /api/v2/savedsearch/{id} | Get a specific saved search
*SavedSearchApi* | [**update_saved_search**](docs/SavedSearchApi.md#update_saved_search) | **PUT** /api/v2/savedsearch/{id} | Update a specific saved search
*SearchApi* | [**search_alert_deleted_entities**](docs/SearchApi.md#search_alert_deleted_entities) | **POST** /api/v2/search/alert/deleted | Search over a customer&#39;s deleted alerts
*SearchApi* | [**search_alert_deleted_for_facet**](docs/SearchApi.md#search_alert_deleted_for_facet) | **POST** /api/v2/search/alert/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted alerts
*SearchApi* | [**search_alert_deleted_for_facets**](docs/SearchApi.md#search_alert_deleted_for_facets) | **POST** /api/v2/search/alert/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted alerts
*SearchApi* | [**search_alert_entities**](docs/SearchApi.md#search_alert_entities) | **POST** /api/v2/search/alert | Search over a customer&#39;s non-deleted alerts
*SearchApi* | [**search_alert_for_facet**](docs/SearchApi.md#search_alert_for_facet) | **POST** /api/v2/search/alert/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted alerts
*SearchApi* | [**search_alert_for_facets**](docs/SearchApi.md#search_alert_for_facets) | **POST** /api/v2/search/alert/facets | Lists the values of one or more facets over the customer&#39;s non-deleted alerts
*SearchApi* | [**search_cloud_integration_deleted_entities**](docs/SearchApi.md#search_cloud_integration_deleted_entities) | **POST** /api/v2/search/cloudintegration/deleted | Search over a customer&#39;s deleted cloud integrations
*SearchApi* | [**search_cloud_integration_deleted_for_facet**](docs/SearchApi.md#search_cloud_integration_deleted_for_facet) | **POST** /api/v2/search/cloudintegration/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted cloud integrations
*SearchApi* | [**search_cloud_integration_deleted_for_facets**](docs/SearchApi.md#search_cloud_integration_deleted_for_facets) | **POST** /api/v2/search/cloudintegration/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted cloud integrations
*SearchApi* | [**search_cloud_integration_entities**](docs/SearchApi.md#search_cloud_integration_entities) | **POST** /api/v2/search/cloudintegration | Search over a customer&#39;s non-deleted cloud integrations
*SearchApi* | [**search_cloud_integration_for_facet**](docs/SearchApi.md#search_cloud_integration_for_facet) | **POST** /api/v2/search/cloudintegration/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted cloud integrations
*SearchApi* | [**search_cloud_integration_for_facets**](docs/SearchApi.md#search_cloud_integration_for_facets) | **POST** /api/v2/search/cloudintegration/facets | Lists the values of one or more facets over the customer&#39;s non-deleted cloud integrations
*SearchApi* | [**search_dashboard_deleted_entities**](docs/SearchApi.md#search_dashboard_deleted_entities) | **POST** /api/v2/search/dashboard/deleted | Search over a customer&#39;s deleted dashboards
*SearchApi* | [**search_dashboard_deleted_for_facet**](docs/SearchApi.md#search_dashboard_deleted_for_facet) | **POST** /api/v2/search/dashboard/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted dashboards
*SearchApi* | [**search_dashboard_deleted_for_facets**](docs/SearchApi.md#search_dashboard_deleted_for_facets) | **POST** /api/v2/search/dashboard/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted dashboards
*SearchApi* | [**search_dashboard_entities**](docs/SearchApi.md#search_dashboard_entities) | **POST** /api/v2/search/dashboard | Search over a customer&#39;s non-deleted dashboards
*SearchApi* | [**search_dashboard_for_facet**](docs/SearchApi.md#search_dashboard_for_facet) | **POST** /api/v2/search/dashboard/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted dashboards
*SearchApi* | [**search_dashboard_for_facets**](docs/SearchApi.md#search_dashboard_for_facets) | **POST** /api/v2/search/dashboard/facets | Lists the values of one or more facets over the customer&#39;s non-deleted dashboards
*SearchApi* | [**search_external_link_entities**](docs/SearchApi.md#search_external_link_entities) | **POST** /api/v2/search/extlink | Search over a customer&#39;s external links
*SearchApi* | [**search_external_links_for_facet**](docs/SearchApi.md#search_external_links_for_facet) | **POST** /api/v2/search/extlink/{facet} | Lists the values of a specific facet over the customer&#39;s external links
*SearchApi* | [**search_external_links_for_facets**](docs/SearchApi.md#search_external_links_for_facets) | **POST** /api/v2/search/extlink/facets | Lists the values of one or more facets over the customer&#39;s external links
*SearchApi* | [**search_maintenance_window_entities**](docs/SearchApi.md#search_maintenance_window_entities) | **POST** /api/v2/search/maintenancewindow | Search over a customer&#39;s maintenance windows
*SearchApi* | [**search_maintenance_window_for_facet**](docs/SearchApi.md#search_maintenance_window_for_facet) | **POST** /api/v2/search/maintenancewindow/{facet} | Lists the values of a specific facet over the customer&#39;s maintenance windows
*SearchApi* | [**search_maintenance_window_for_facets**](docs/SearchApi.md#search_maintenance_window_for_facets) | **POST** /api/v2/search/maintenancewindow/facets | Lists the values of one or more facets over the customer&#39;s maintenance windows
*SearchApi* | [**search_notficant_for_facets**](docs/SearchApi.md#search_notficant_for_facets) | **POST** /api/v2/search/notificant/facets | Lists the values of one or more facets over the customer&#39;s notificants
*SearchApi* | [**search_notificant_entities**](docs/SearchApi.md#search_notificant_entities) | **POST** /api/v2/search/notificant | Search over a customer&#39;s notificants
*SearchApi* | [**search_notificant_for_facet**](docs/SearchApi.md#search_notificant_for_facet) | **POST** /api/v2/search/notificant/{facet} | Lists the values of a specific facet over the customer&#39;s notificants
*SearchApi* | [**search_proxy_deleted_entities**](docs/SearchApi.md#search_proxy_deleted_entities) | **POST** /api/v2/search/proxy/deleted | Search over a customer&#39;s deleted proxies
*SearchApi* | [**search_proxy_deleted_for_facet**](docs/SearchApi.md#search_proxy_deleted_for_facet) | **POST** /api/v2/search/proxy/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted proxies
*SearchApi* | [**search_proxy_deleted_for_facets**](docs/SearchApi.md#search_proxy_deleted_for_facets) | **POST** /api/v2/search/proxy/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted proxies
*SearchApi* | [**search_proxy_entities**](docs/SearchApi.md#search_proxy_entities) | **POST** /api/v2/search/proxy | Search over a customer&#39;s non-deleted proxies
*SearchApi* | [**search_proxy_for_facet**](docs/SearchApi.md#search_proxy_for_facet) | **POST** /api/v2/search/proxy/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted proxies
*SearchApi* | [**search_proxy_for_facets**](docs/SearchApi.md#search_proxy_for_facets) | **POST** /api/v2/search/proxy/facets | Lists the values of one or more facets over the customer&#39;s non-deleted proxies
*SearchApi* | [**search_registered_query_deleted_entities**](docs/SearchApi.md#search_registered_query_deleted_entities) | **POST** /api/v2/search/derivedmetric/deleted | Search over a customer&#39;s deleted derived metric definitions
*SearchApi* | [**search_registered_query_deleted_for_facet**](docs/SearchApi.md#search_registered_query_deleted_for_facet) | **POST** /api/v2/search/derivedmetric/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted derived metric definitions
*SearchApi* | [**search_registered_query_deleted_for_facets**](docs/SearchApi.md#search_registered_query_deleted_for_facets) | **POST** /api/v2/search/derivedmetric/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted derived metric definitions
*SearchApi* | [**search_registered_query_entities**](docs/SearchApi.md#search_registered_query_entities) | **POST** /api/v2/search/derivedmetric | Search over a customer&#39;s non-deleted derived metric definitions
*SearchApi* | [**search_registered_query_for_facet**](docs/SearchApi.md#search_registered_query_for_facet) | **POST** /api/v2/search/derivedmetric/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted derived metric definitions
*SearchApi* | [**search_registered_query_for_facets**](docs/SearchApi.md#search_registered_query_for_facets) | **POST** /api/v2/search/derivedmetric/facets | Lists the values of one or more facets over the customer&#39;s non-deleted derived metric definition
*SearchApi* | [**search_report_event_entities**](docs/SearchApi.md#search_report_event_entities) | **POST** /api/v2/search/event | Search over a customer&#39;s events
*SearchApi* | [**search_report_event_for_facet**](docs/SearchApi.md#search_report_event_for_facet) | **POST** /api/v2/search/event/{facet} | Lists the values of a specific facet over the customer&#39;s events
*SearchApi* | [**search_report_event_for_facets**](docs/SearchApi.md#search_report_event_for_facets) | **POST** /api/v2/search/event/facets | Lists the values of one or more facets over the customer&#39;s events
*SearchApi* | [**search_tagged_source_entities**](docs/SearchApi.md#search_tagged_source_entities) | **POST** /api/v2/search/source | Search over a customer&#39;s sources
*SearchApi* | [**search_tagged_source_for_facet**](docs/SearchApi.md#search_tagged_source_for_facet) | **POST** /api/v2/search/source/{facet} | Lists the values of a specific facet over the customer&#39;s sources
*SearchApi* | [**search_tagged_source_for_facets**](docs/SearchApi.md#search_tagged_source_for_facets) | **POST** /api/v2/search/source/facets | Lists the values of one or more facets over the customer&#39;s sources
*SearchApi* | [**search_user_entities**](docs/SearchApi.md#search_user_entities) | **POST** /api/v2/search/user | Search over a customer&#39;s users
*SearchApi* | [**search_user_for_facet**](docs/SearchApi.md#search_user_for_facet) | **POST** /api/v2/search/user/{facet} | Lists the values of a specific facet over the customer&#39;s users
*SearchApi* | [**search_user_for_facets**](docs/SearchApi.md#search_user_for_facets) | **POST** /api/v2/search/user/facets | Lists the values of one or more facets over the customer&#39;s users
*SearchApi* | [**search_web_hook_entities**](docs/SearchApi.md#search_web_hook_entities) | **POST** /api/v2/search/webhook | Search over a customer&#39;s webhooks
*SearchApi* | [**search_web_hook_for_facet**](docs/SearchApi.md#search_web_hook_for_facet) | **POST** /api/v2/search/webhook/{facet} | Lists the values of a specific facet over the customer&#39;s webhooks
*SearchApi* | [**search_webhook_for_facets**](docs/SearchApi.md#search_webhook_for_facets) | **POST** /api/v2/search/webhook/facets | Lists the values of one or more facets over the customer&#39;s webhooks
*SourceApi* | [**add_source_tag**](docs/SourceApi.md#add_source_tag) | **PUT** /api/v2/source/{id}/tag/{tagValue} | Add a tag to a specific source
*SourceApi* | [**create_source**](docs/SourceApi.md#create_source) | **POST** /api/v2/source | Create metadata (description or tags) for a specific source
*SourceApi* | [**delete_source**](docs/SourceApi.md#delete_source) | **DELETE** /api/v2/source/{id} | Delete metadata (description and tags) for a specific source
*SourceApi* | [**get_all_source**](docs/SourceApi.md#get_all_source) | **GET** /api/v2/source | Get all sources for a customer
*SourceApi* | [**get_source**](docs/SourceApi.md#get_source) | **GET** /api/v2/source/{id} | Get a specific source for a customer
*SourceApi* | [**get_source_tags**](docs/SourceApi.md#get_source_tags) | **GET** /api/v2/source/{id}/tag | Get all tags associated with a specific source
*SourceApi* | [**remove_description**](docs/SourceApi.md#remove_description) | **DELETE** /api/v2/source/{id}/description | Remove description from a specific source
*SourceApi* | [**remove_source_tag**](docs/SourceApi.md#remove_source_tag) | **DELETE** /api/v2/source/{id}/tag/{tagValue} | Remove a tag from a specific source
*SourceApi* | [**set_description**](docs/SourceApi.md#set_description) | **POST** /api/v2/source/{id}/description | Set description associated with a specific source
*SourceApi* | [**set_source_tags**](docs/SourceApi.md#set_source_tags) | **POST** /api/v2/source/{id}/tag | Set all tags associated with a specific source
*SourceApi* | [**update_source**](docs/SourceApi.md#update_source) | **PUT** /api/v2/source/{id} | Update metadata (description or tags) for a specific source.
*UserApi* | [**create_or_update_user**](docs/UserApi.md#create_or_update_user) | **POST** /api/v2/user | Creates or updates a user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /api/v2/user/{id} | Deletes a user identified by id
*UserApi* | [**get_all_user**](docs/UserApi.md#get_all_user) | **GET** /api/v2/user | Get all users
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /api/v2/user/{id} | Retrieves a user by identifier (email addr)
*UserApi* | [**grant_user_permission**](docs/UserApi.md#grant_user_permission) | **POST** /api/v2/user/{id}/grant | Grants a specific user permission
*UserApi* | [**revoke_user_permission**](docs/UserApi.md#revoke_user_permission) | **POST** /api/v2/user/{id}/revoke | Revokes a specific user permission
*WebhookApi* | [**create_webhook**](docs/WebhookApi.md#create_webhook) | **POST** /api/v2/webhook | Create a specific webhook
*WebhookApi* | [**delete_webhook**](docs/WebhookApi.md#delete_webhook) | **DELETE** /api/v2/webhook/{id} | Delete a specific webhook
*WebhookApi* | [**get_all_webhooks**](docs/WebhookApi.md#get_all_webhooks) | **GET** /api/v2/webhook | Get all webhooks for a customer
*WebhookApi* | [**get_webhook**](docs/WebhookApi.md#get_webhook) | **GET** /api/v2/webhook/{id} | Get a specific webhook
*WebhookApi* | [**update_webhook**](docs/WebhookApi.md#update_webhook) | **PUT** /api/v2/webhook/{id} | Update a specific webhook


## Documentation For Models

 - [AWSBaseCredentials](docs/AWSBaseCredentials.md)
 - [Alert](docs/Alert.md)
 - [AvroBackedStandardizedDTO](docs/AvroBackedStandardizedDTO.md)
 - [AzureActivityLogConfiguration](docs/AzureActivityLogConfiguration.md)
 - [AzureBaseCredentials](docs/AzureBaseCredentials.md)
 - [AzureConfiguration](docs/AzureConfiguration.md)
 - [Chart](docs/Chart.md)
 - [ChartSettings](docs/ChartSettings.md)
 - [ChartSourceQuery](docs/ChartSourceQuery.md)
 - [CloudIntegration](docs/CloudIntegration.md)
 - [CloudTrailConfiguration](docs/CloudTrailConfiguration.md)
 - [CloudWatchConfiguration](docs/CloudWatchConfiguration.md)
 - [CustomerFacingUserObject](docs/CustomerFacingUserObject.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardParameterValue](docs/DashboardParameterValue.md)
 - [DashboardSection](docs/DashboardSection.md)
 - [DashboardSectionRow](docs/DashboardSectionRow.md)
 - [DerivedMetricDefinition](docs/DerivedMetricDefinition.md)
 - [EC2Configuration](docs/EC2Configuration.md)
 - [Event](docs/Event.md)
 - [EventSearchRequest](docs/EventSearchRequest.md)
 - [EventTimeRange](docs/EventTimeRange.md)
 - [ExternalLink](docs/ExternalLink.md)
 - [FacetResponse](docs/FacetResponse.md)
 - [FacetSearchRequestContainer](docs/FacetSearchRequestContainer.md)
 - [FacetsResponseContainer](docs/FacetsResponseContainer.md)
 - [FacetsSearchRequestContainer](docs/FacetsSearchRequestContainer.md)
 - [GCPBillingConfiguration](docs/GCPBillingConfiguration.md)
 - [GCPConfiguration](docs/GCPConfiguration.md)
 - [HistoryEntry](docs/HistoryEntry.md)
 - [HistoryResponse](docs/HistoryResponse.md)
 - [Integration](docs/Integration.md)
 - [IntegrationAlias](docs/IntegrationAlias.md)
 - [IntegrationDashboard](docs/IntegrationDashboard.md)
 - [IntegrationManifestGroup](docs/IntegrationManifestGroup.md)
 - [IntegrationMetrics](docs/IntegrationMetrics.md)
 - [IntegrationStatus](docs/IntegrationStatus.md)
 - [IteratorEntryStringJsonNode](docs/IteratorEntryStringJsonNode.md)
 - [IteratorJsonNode](docs/IteratorJsonNode.md)
 - [IteratorString](docs/IteratorString.md)
 - [JsonNode](docs/JsonNode.md)
 - [LogicalType](docs/LogicalType.md)
 - [MaintenanceWindow](docs/MaintenanceWindow.md)
 - [Message](docs/Message.md)
 - [MetricDetails](docs/MetricDetails.md)
 - [MetricDetailsResponse](docs/MetricDetailsResponse.md)
 - [MetricStatus](docs/MetricStatus.md)
 - [Notificant](docs/Notificant.md)
 - [Number](docs/Number.md)
 - [PagedAlert](docs/PagedAlert.md)
 - [PagedAlertWithStats](docs/PagedAlertWithStats.md)
 - [PagedCloudIntegration](docs/PagedCloudIntegration.md)
 - [PagedCustomerFacingUserObject](docs/PagedCustomerFacingUserObject.md)
 - [PagedDashboard](docs/PagedDashboard.md)
 - [PagedDerivedMetricDefinition](docs/PagedDerivedMetricDefinition.md)
 - [PagedDerivedMetricDefinitionWithStats](docs/PagedDerivedMetricDefinitionWithStats.md)
 - [PagedEvent](docs/PagedEvent.md)
 - [PagedExternalLink](docs/PagedExternalLink.md)
 - [PagedIntegration](docs/PagedIntegration.md)
 - [PagedMaintenanceWindow](docs/PagedMaintenanceWindow.md)
 - [PagedMessage](docs/PagedMessage.md)
 - [PagedNotificant](docs/PagedNotificant.md)
 - [PagedProxy](docs/PagedProxy.md)
 - [PagedSavedSearch](docs/PagedSavedSearch.md)
 - [PagedSource](docs/PagedSource.md)
 - [Point](docs/Point.md)
 - [Proxy](docs/Proxy.md)
 - [QueryEvent](docs/QueryEvent.md)
 - [QueryResult](docs/QueryResult.md)
 - [RawTimeseries](docs/RawTimeseries.md)
 - [ResponseContainer](docs/ResponseContainer.md)
 - [ResponseContainerAlert](docs/ResponseContainerAlert.md)
 - [ResponseContainerCloudIntegration](docs/ResponseContainerCloudIntegration.md)
 - [ResponseContainerDashboard](docs/ResponseContainerDashboard.md)
 - [ResponseContainerDerivedMetricDefinition](docs/ResponseContainerDerivedMetricDefinition.md)
 - [ResponseContainerEvent](docs/ResponseContainerEvent.md)
 - [ResponseContainerExternalLink](docs/ResponseContainerExternalLink.md)
 - [ResponseContainerFacetResponse](docs/ResponseContainerFacetResponse.md)
 - [ResponseContainerFacetsResponseContainer](docs/ResponseContainerFacetsResponseContainer.md)
 - [ResponseContainerHistoryResponse](docs/ResponseContainerHistoryResponse.md)
 - [ResponseContainerIntegration](docs/ResponseContainerIntegration.md)
 - [ResponseContainerIntegrationStatus](docs/ResponseContainerIntegrationStatus.md)
 - [ResponseContainerListIntegrationManifestGroup](docs/ResponseContainerListIntegrationManifestGroup.md)
 - [ResponseContainerMaintenanceWindow](docs/ResponseContainerMaintenanceWindow.md)
 - [ResponseContainerMapStringInteger](docs/ResponseContainerMapStringInteger.md)
 - [ResponseContainerMapStringIntegrationStatus](docs/ResponseContainerMapStringIntegrationStatus.md)
 - [ResponseContainerMessage](docs/ResponseContainerMessage.md)
 - [ResponseContainerNotificant](docs/ResponseContainerNotificant.md)
 - [ResponseContainerPagedAlert](docs/ResponseContainerPagedAlert.md)
 - [ResponseContainerPagedAlertWithStats](docs/ResponseContainerPagedAlertWithStats.md)
 - [ResponseContainerPagedCloudIntegration](docs/ResponseContainerPagedCloudIntegration.md)
 - [ResponseContainerPagedCustomerFacingUserObject](docs/ResponseContainerPagedCustomerFacingUserObject.md)
 - [ResponseContainerPagedDashboard](docs/ResponseContainerPagedDashboard.md)
 - [ResponseContainerPagedDerivedMetricDefinition](docs/ResponseContainerPagedDerivedMetricDefinition.md)
 - [ResponseContainerPagedDerivedMetricDefinitionWithStats](docs/ResponseContainerPagedDerivedMetricDefinitionWithStats.md)
 - [ResponseContainerPagedEvent](docs/ResponseContainerPagedEvent.md)
 - [ResponseContainerPagedExternalLink](docs/ResponseContainerPagedExternalLink.md)
 - [ResponseContainerPagedIntegration](docs/ResponseContainerPagedIntegration.md)
 - [ResponseContainerPagedMaintenanceWindow](docs/ResponseContainerPagedMaintenanceWindow.md)
 - [ResponseContainerPagedMessage](docs/ResponseContainerPagedMessage.md)
 - [ResponseContainerPagedNotificant](docs/ResponseContainerPagedNotificant.md)
 - [ResponseContainerPagedProxy](docs/ResponseContainerPagedProxy.md)
 - [ResponseContainerPagedSavedSearch](docs/ResponseContainerPagedSavedSearch.md)
 - [ResponseContainerPagedSource](docs/ResponseContainerPagedSource.md)
 - [ResponseContainerProxy](docs/ResponseContainerProxy.md)
 - [ResponseContainerSavedSearch](docs/ResponseContainerSavedSearch.md)
 - [ResponseContainerSource](docs/ResponseContainerSource.md)
 - [ResponseContainerTagsResponse](docs/ResponseContainerTagsResponse.md)
 - [ResponseStatus](docs/ResponseStatus.md)
 - [SavedSearch](docs/SavedSearch.md)
 - [SearchQuery](docs/SearchQuery.md)
 - [SortableSearchRequest](docs/SortableSearchRequest.md)
 - [Sorting](docs/Sorting.md)
 - [Source](docs/Source.md)
 - [SourceLabelPair](docs/SourceLabelPair.md)
 - [SourceSearchRequestContainer](docs/SourceSearchRequestContainer.md)
 - [StatsModel](docs/StatsModel.md)
 - [TagsResponse](docs/TagsResponse.md)
 - [TargetInfo](docs/TargetInfo.md)
 - [TeslaConfiguration](docs/TeslaConfiguration.md)
 - [Timeseries](docs/Timeseries.md)
 - [UserModel](docs/UserModel.md)
 - [UserToCreate](docs/UserToCreate.md)
 - [WFTags](docs/WFTags.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-AUTH-TOKEN
- **Location**: HTTP header


## Author



