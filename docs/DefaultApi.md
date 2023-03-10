# freeclimb.DefaultApi

All URIs are relative to *https://www.freeclimb.com/apiserver*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_a_phone_number**](DefaultApi.md#buy_a_phone_number) | **POST** /Accounts/{accountId}/IncomingPhoneNumbers | Buy a Phone Number
[**create_a_conference**](DefaultApi.md#create_a_conference) | **POST** /Accounts/{accountId}/Conferences | Create a Conference
[**create_a_queue**](DefaultApi.md#create_a_queue) | **POST** /Accounts/{accountId}/Queues | Create a Queue
[**create_an_application**](DefaultApi.md#create_an_application) | **POST** /Accounts/{accountId}/Applications | Create an application
[**delete_a_recording**](DefaultApi.md#delete_a_recording) | **DELETE** /Accounts/{accountId}/Recordings/{recordingId} | Delete a Recording
[**delete_an_application**](DefaultApi.md#delete_an_application) | **DELETE** /Accounts/{accountId}/Applications/{applicationId} | Delete an application
[**delete_an_incoming_number**](DefaultApi.md#delete_an_incoming_number) | **DELETE** /Accounts/{accountId}/IncomingPhoneNumbers/{phoneNumberId} | Delete an Incoming Number
[**dequeue_a_member**](DefaultApi.md#dequeue_a_member) | **POST** /Accounts/{accountId}/Queues/{queueId}/Members/{callId} | Dequeue a Member
[**dequeue_head_member**](DefaultApi.md#dequeue_head_member) | **POST** /Accounts/{accountId}/Queues/{queueId}/Members/Front | Dequeue Head Member
[**download_a_recording_file**](DefaultApi.md#download_a_recording_file) | **GET** /Accounts/{accountId}/Recordings/{recordingId}/Download | Download a Recording File
[**filter_logs**](DefaultApi.md#filter_logs) | **POST** /Accounts/{accountId}/Logs | Filter Logs
[**get_a_call**](DefaultApi.md#get_a_call) | **GET** /Accounts/{accountId}/Calls/{callId} | Get a Call
[**get_a_conference**](DefaultApi.md#get_a_conference) | **GET** /Accounts/{accountId}/Conferences/{conferenceId} | Get a Conference
[**get_a_member**](DefaultApi.md#get_a_member) | **GET** /Accounts/{accountId}/Queues/{queueId}/Members/{callId} | Get a Member
[**get_a_participant**](DefaultApi.md#get_a_participant) | **GET** /Accounts/{accountId}/Conferences/{conferenceId}/Participants/{callId} | Get a Participant
[**get_a_queue**](DefaultApi.md#get_a_queue) | **GET** /Accounts/{accountId}/Queues/{queueId} | Get a Queue
[**get_a_recording**](DefaultApi.md#get_a_recording) | **GET** /Accounts/{accountId}/Recordings/{recordingId} | Get a Recording
[**get_an_account**](DefaultApi.md#get_an_account) | **GET** /Accounts/{accountId} | Get an Account
[**get_an_application**](DefaultApi.md#get_an_application) | **GET** /Accounts/{accountId}/Applications/{applicationId} | Get an Application
[**get_an_incoming_number**](DefaultApi.md#get_an_incoming_number) | **GET** /Accounts/{accountId}/IncomingPhoneNumbers/{phoneNumberId} | Get an Incoming Number
[**get_an_sms_message**](DefaultApi.md#get_an_sms_message) | **GET** /Accounts/{accountId}/Messages/{messageId} | Get an SMS Message
[**get_head_member**](DefaultApi.md#get_head_member) | **GET** /Accounts/{accountId}/Queues/{queueId}/Members/Front | Get Head Member
[**list_active_queues**](DefaultApi.md#list_active_queues) | **GET** /Accounts/{accountId}/Queues | List Active Queues
[**list_all_account_logs**](DefaultApi.md#list_all_account_logs) | **GET** /Accounts/{accountId}/Logs | List All Account Logs
[**list_applications**](DefaultApi.md#list_applications) | **GET** /Accounts/{accountId}/Applications | List applications
[**list_available_numbers**](DefaultApi.md#list_available_numbers) | **GET** /AvailablePhoneNumbers | List available numbers
[**list_call_logs**](DefaultApi.md#list_call_logs) | **GET** /Accounts/{accountId}/Calls/{callId}/Logs | List Call Logs
[**list_call_recordings**](DefaultApi.md#list_call_recordings) | **GET** /Accounts/{accountId}/Calls/{callId}/Recordings | List Call Recordings
[**list_calls**](DefaultApi.md#list_calls) | **GET** /Accounts/{accountId}/Calls | List Calls
[**list_conferences**](DefaultApi.md#list_conferences) | **GET** /Accounts/{accountId}/Conferences | List Conferences
[**list_incoming_numbers**](DefaultApi.md#list_incoming_numbers) | **GET** /Accounts/{accountId}/IncomingPhoneNumbers | List Incoming Numbers
[**list_members**](DefaultApi.md#list_members) | **GET** /Accounts/{accountId}/Queues/{queueId}/Members | List Members
[**list_participants**](DefaultApi.md#list_participants) | **GET** /Accounts/{accountId}/Conferences/{conferenceId}/Participants | List Participants
[**list_recordings**](DefaultApi.md#list_recordings) | **GET** /Accounts/{accountId}/Recordings | List Recordings
[**list_sms_messages**](DefaultApi.md#list_sms_messages) | **GET** /Accounts/{accountId}/Messages | List SMS Messages
[**make_a_call**](DefaultApi.md#make_a_call) | **POST** /Accounts/{accountId}/Calls | Make a Call
[**remove_a_participant**](DefaultApi.md#remove_a_participant) | **DELETE** /Accounts/{accountId}/Conferences/{conferenceId}/Participants/{callId} | Remove a Participant
[**send_an_sms_message**](DefaultApi.md#send_an_sms_message) | **POST** /Accounts/{accountId}/Messages | Send an SMS Message
[**stream_a_recording_file**](DefaultApi.md#stream_a_recording_file) | **GET** /Accounts/{accountId}/Recordings/{recordingId}/Stream | Stream a Recording File
[**update_a_conference**](DefaultApi.md#update_a_conference) | **POST** /Accounts/{accountId}/Conferences/{conferenceId} | Update a Conference
[**update_a_live_call**](DefaultApi.md#update_a_live_call) | **POST** /Accounts/{accountId}/Calls/{callId} | Update a Live Call
[**update_a_participant**](DefaultApi.md#update_a_participant) | **POST** /Accounts/{accountId}/Conferences/{conferenceId}/Participants/{callId} | Update a Participant
[**update_a_queue**](DefaultApi.md#update_a_queue) | **POST** /Accounts/{accountId}/Queues/{queueId} | Update a Queue
[**update_an_account**](DefaultApi.md#update_an_account) | **POST** /Accounts/{accountId} | Manage an account
[**update_an_application**](DefaultApi.md#update_an_application) | **POST** /Accounts/{accountId}/Applications/{applicationId} | Update an application
[**update_an_incoming_number**](DefaultApi.md#update_an_incoming_number) | **POST** /Accounts/{accountId}/IncomingPhoneNumbers/{phoneNumberId} | Update an Incoming Number


# **buy_a_phone_number**
> IncomingNumberResult buy_a_phone_number(account_id, buy_incoming_number_request)

Buy a Phone Number

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.buy_incoming_number_request import BuyIncomingNumberRequest
from freeclimb.model.incoming_number_result import IncomingNumberResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    buy_incoming_number_request = BuyIncomingNumberRequest(
        phone_number="phone_number_example",
        alias="alias_example",
        application_id="application_id_example",
    ) # BuyIncomingNumberRequest | Incoming Number transaction details

    # example passing only required values which don't have defaults set
    try:
        # Buy a Phone Number
        api_response = api_instance.buy_a_phone_number(account_id, buy_incoming_number_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->buy_a_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **buy_incoming_number_request** | [**BuyIncomingNumberRequest**](BuyIncomingNumberRequest.md)| Incoming Number transaction details |

### Return type

[**IncomingNumberResult**](IncomingNumberResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Incoming Number transaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_a_conference**
> ConferenceResult create_a_conference(account_id)

Create a Conference

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.create_conference_request import CreateConferenceRequest
from freeclimb.model.conference_result import ConferenceResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    create_conference_request = CreateConferenceRequest(
        alias="alias_example",
        play_beep=PlayBeep("always"),
        record=True,
        wait_url="wait_url_example",
        status_callback_url="status_callback_url_example",
    ) # CreateConferenceRequest | Conference to create (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Conference
        api_response = api_instance.create_a_conference(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->create_a_conference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Conference
        api_response = api_instance.create_a_conference(account_id, create_conference_request=create_conference_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->create_a_conference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **create_conference_request** | [**CreateConferenceRequest**](CreateConferenceRequest.md)| Conference to create | [optional]

### Return type

[**ConferenceResult**](ConferenceResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of created conference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_a_queue**
> QueueResult create_a_queue(account_id)

Create a Queue

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_result import QueueResult
from freeclimb.model.queue_request import QueueRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_request = QueueRequest(
        alias="alias_example",
        max_size=100,
    ) # QueueRequest | Queue details used to create a queue (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Queue
        api_response = api_instance.create_a_queue(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->create_a_queue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Queue
        api_response = api_instance.create_a_queue(account_id, queue_request=queue_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->create_a_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_request** | [**QueueRequest**](QueueRequest.md)| Queue details used to create a queue | [optional]

### Return type

[**QueueResult**](QueueResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfuly created queue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_an_application**
> ApplicationResult create_an_application(account_id)

Create an application

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.application_request import ApplicationRequest
from freeclimb.model.application_result import ApplicationResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    application_request = ApplicationRequest(
        alias="alias_example",
        voice_url="voice_url_example",
        voice_fallback_url="voice_fallback_url_example",
        call_connect_url="call_connect_url_example",
        status_callback_url="status_callback_url_example",
        sms_url="sms_url_example",
        sms_fallback_url="sms_fallback_url_example",
    ) # ApplicationRequest | Application Details (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an application
        api_response = api_instance.create_an_application(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->create_an_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an application
        api_response = api_instance.create_an_application(account_id, application_request=application_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->create_an_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)| Application Details | [optional]

### Return type

[**ApplicationResult**](ApplicationResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Application successfuly created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_recording**
> delete_a_recording(account_id, recording_id)

Delete a Recording

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    recording_id = "recordingId_example" # str | String that uniquely identifies this recording resource.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Recording
        api_instance.delete_a_recording(account_id, recording_id)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->delete_a_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **recording_id** | **str**| String that uniquely identifies this recording resource. |

### Return type

void (empty response body)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Recording Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_application**
> delete_an_application(account_id, application_id)

Delete an application

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    application_id = "applicationId_example" # str | String that uniquely identifies this application resource.

    # example passing only required values which don't have defaults set
    try:
        # Delete an application
        api_instance.delete_an_application(account_id, application_id)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->delete_an_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **application_id** | **str**| String that uniquely identifies this application resource. |

### Return type

void (empty response body)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful application deletion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_incoming_number**
> delete_an_incoming_number(account_id, phone_number_id)

Delete an Incoming Number

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    phone_number_id = "phoneNumberId_example" # str | String that uniquely identifies this phone number resource.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Incoming Number
        api_instance.delete_an_incoming_number(account_id, phone_number_id)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->delete_an_incoming_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **phone_number_id** | **str**| String that uniquely identifies this phone number resource. |

### Return type

void (empty response body)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Incoming Number deletion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dequeue_a_member**
> QueueMember dequeue_a_member(account_id, queue_id, call_id)

Dequeue a Member

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_member import QueueMember
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_id = "queueId_example" # str | String that uniquely identifies the Queue that the Member belongs to.
    call_id = "callId_example" # str | ID if the Call that the Member belongs to

    # example passing only required values which don't have defaults set
    try:
        # Dequeue a Member
        api_response = api_instance.dequeue_a_member(account_id, queue_id, call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->dequeue_a_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_id** | **str**| String that uniquely identifies the Queue that the Member belongs to. |
 **call_id** | **str**| ID if the Call that the Member belongs to |

### Return type

[**QueueMember**](QueueMember.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted dequeue request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dequeue_head_member**
> QueueMember dequeue_head_member(account_id, queue_id)

Dequeue Head Member

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_member import QueueMember
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_id = "queueId_example" # str | String that uniquely identifies this queue resource.

    # example passing only required values which don't have defaults set
    try:
        # Dequeue Head Member
        api_response = api_instance.dequeue_head_member(account_id, queue_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->dequeue_head_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_id** | **str**| String that uniquely identifies this queue resource. |

### Return type

[**QueueMember**](QueueMember.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted dequeue request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_a_recording_file**
> file_type download_a_recording_file(account_id, recording_id)

Download a Recording File

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    recording_id = "recordingId_example" # str | String that uniquely identifies this recording resource.

    # example passing only required values which don't have defaults set
    try:
        # Download a Recording File
        api_response = api_instance.download_a_recording_file(account_id, recording_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->download_a_recording_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **recording_id** | **str**| String that uniquely identifies this recording resource. |

### Return type

**file_type**

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/x-wav


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Download a Recording file represented with audio/x-wav mime-type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_logs**
> LogList filter_logs(account_id, filter_logs_request)

Filter Logs

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.log_list import LogList
from freeclimb.model.filter_logs_request import FilterLogsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    filter_logs_request = FilterLogsRequest(
        pql="pql_example",
    ) # FilterLogsRequest | Filter logs request paramters

    # example passing only required values which don't have defaults set
    try:
        # Filter Logs
        api_response = api_instance.filter_logs(account_id, filter_logs_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->filter_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **filter_logs_request** | [**FilterLogsRequest**](FilterLogsRequest.md)| Filter logs request paramters |

### Return type

[**LogList**](LogList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved log list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_call**
> CallResult get_a_call(account_id, call_id)

Get a Call

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.call_result import CallResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    call_id = "callId_example" # str | String that uniquely identifies this call resource.

    # example passing only required values which don't have defaults set
    try:
        # Get a Call
        api_response = api_instance.get_a_call(account_id, call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_a_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **call_id** | **str**| String that uniquely identifies this call resource. |

### Return type

[**CallResult**](CallResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Call Resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_conference**
> ConferenceResult get_a_conference(account_id, conference_id)

Get a Conference

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.conference_result import ConferenceResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    conference_id = "conferenceId_example" # str | A string that uniquely identifies this conference resource.

    # example passing only required values which don't have defaults set
    try:
        # Get a Conference
        api_response = api_instance.get_a_conference(account_id, conference_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_a_conference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **conference_id** | **str**| A string that uniquely identifies this conference resource. |

### Return type

[**ConferenceResult**](ConferenceResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved conference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_member**
> QueueMember get_a_member(account_id, queue_id, call_id)

Get a Member

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_member import QueueMember
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_id = "queueId_example" # str | String that uniquely identifies the Queue that the Member belongs to.
    call_id = "callId_example" # str | ID of the Call that the Member belongs to

    # example passing only required values which don't have defaults set
    try:
        # Get a Member
        api_response = api_instance.get_a_member(account_id, queue_id, call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_a_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_id** | **str**| String that uniquely identifies the Queue that the Member belongs to. |
 **call_id** | **str**| ID of the Call that the Member belongs to |

### Return type

[**QueueMember**](QueueMember.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved a queue member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_participant**
> ConferenceParticipantResult get_a_participant(account_id, conference_id, call_id)

Get a Participant

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.conference_participant_result import ConferenceParticipantResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    conference_id = "conferenceId_example" # str | ID of the conference this participant is in.
    call_id = "callId_example" # str | ID of the Call associated with this participant.

    # example passing only required values which don't have defaults set
    try:
        # Get a Participant
        api_response = api_instance.get_a_participant(account_id, conference_id, call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_a_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **conference_id** | **str**| ID of the conference this participant is in. |
 **call_id** | **str**| ID of the Call associated with this participant. |

### Return type

[**ConferenceParticipantResult**](ConferenceParticipantResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved conference participant |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_queue**
> QueueResult get_a_queue(account_id, queue_id)

Get a Queue

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_result import QueueResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_id = "queueId_example" # str | A string that uniquely identifies this queue resource.

    # example passing only required values which don't have defaults set
    try:
        # Get a Queue
        api_response = api_instance.get_a_queue(account_id, queue_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_a_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_id** | **str**| A string that uniquely identifies this queue resource. |

### Return type

[**QueueResult**](QueueResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved queue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_recording**
> RecordingResult get_a_recording(account_id, recording_id)

Get a Recording

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.recording_result import RecordingResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    recording_id = "recordingId_example" # str | String that uniquely identifies this recording resource.

    # example passing only required values which don't have defaults set
    try:
        # Get a Recording
        api_response = api_instance.get_a_recording(account_id, recording_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_a_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **recording_id** | **str**| String that uniquely identifies this recording resource. |

### Return type

[**RecordingResult**](RecordingResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_account**
> AccountResult get_an_account(account_id)

Get an Account

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.account_result import AccountResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account

    # example passing only required values which don't have defaults set
    try:
        # Get an Account
        api_response = api_instance.get_an_account(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_an_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |

### Return type

[**AccountResult**](AccountResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account Details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_application**
> ApplicationResult get_an_application(account_id, application_id)

Get an Application

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.application_result import ApplicationResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    application_id = "applicationId_example" # str | A string that uniquely identifies this application resource.

    # example passing only required values which don't have defaults set
    try:
        # Get an Application
        api_response = api_instance.get_an_application(account_id, application_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_an_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **application_id** | **str**| A string that uniquely identifies this application resource. |

### Return type

[**ApplicationResult**](ApplicationResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_incoming_number**
> IncomingNumberResult get_an_incoming_number(account_id, phone_number_id)

Get an Incoming Number

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.incoming_number_result import IncomingNumberResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    phone_number_id = "phoneNumberId_example" # str | String that uniquely identifies this phone number resource.

    # example passing only required values which don't have defaults set
    try:
        # Get an Incoming Number
        api_response = api_instance.get_an_incoming_number(account_id, phone_number_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_an_incoming_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **phone_number_id** | **str**| String that uniquely identifies this phone number resource. |

### Return type

[**IncomingNumberResult**](IncomingNumberResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Incoming Phone Number result. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_sms_message**
> MessageResult get_an_sms_message(account_id, message_id)

Get an SMS Message

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.message_result import MessageResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    message_id = "messageId_example" # str | String that uniquely identifies this Message resource.

    # example passing only required values which don't have defaults set
    try:
        # Get an SMS Message
        api_response = api_instance.get_an_sms_message(account_id, message_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_an_sms_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **message_id** | **str**| String that uniquely identifies this Message resource. |

### Return type

[**MessageResult**](MessageResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specific SMS message that’s been processed by FreeClimb |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_head_member**
> QueueMember get_head_member(account_id, queue_id)

Get Head Member

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_member import QueueMember
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_id = "queueId_example" # str | String that uniquely identifies the Queue that the Member belongs to.

    # example passing only required values which don't have defaults set
    try:
        # Get Head Member
        api_response = api_instance.get_head_member(account_id, queue_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->get_head_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_id** | **str**| String that uniquely identifies the Queue that the Member belongs to. |

### Return type

[**QueueMember**](QueueMember.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved queue member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_active_queues**
> QueueList list_active_queues(account_id)

List Active Queues

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_list import QueueList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    alias = "alias_example" # str | Return only the Queue resources with aliases that exactly match this name. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Active Queues
        api_response = api_instance.list_active_queues(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_active_queues: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Active Queues
        api_response = api_instance.list_active_queues(account_id, alias=alias)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_active_queues: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **alias** | **str**| Return only the Queue resources with aliases that exactly match this name. | [optional]

### Return type

[**QueueList**](QueueList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfuly retrieved queue list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_account_logs**
> LogList list_all_account_logs(account_id)

List All Account Logs

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.log_list import LogList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account

    # example passing only required values which don't have defaults set
    try:
        # List All Account Logs
        api_response = api_instance.list_all_account_logs(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_all_account_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |

### Return type

[**LogList**](LogList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved log list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applications**
> ApplicationList list_applications(account_id)

List applications

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.application_list import ApplicationList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    alias = "alias_example" # str | Return only applications with aliases that exactly match this value. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List applications
        api_response = api_instance.list_applications(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_applications: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List applications
        api_response = api_instance.list_applications(account_id, alias=alias)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **alias** | **str**| Return only applications with aliases that exactly match this value. | [optional]

### Return type

[**ApplicationList**](ApplicationList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Applications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_numbers**
> AvailableNumberList list_available_numbers()

List available numbers

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.available_number_list import AvailableNumberList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    phone_number = "phoneNumber_example" # str | PCRE-compatible regular expression to filter against `phoneNumber` field, which is in E.164 format. (optional)
    region = "region_example" # str | State or province of this phone number. (optional)
    country = "country_example" # str | Country of this phone number. (optional)
    voice_enabled = True # bool | Indicates whether the phone number can handle Calls. Typically set to true for all numbers. (optional) if omitted the server will use the default value of True
    sms_enabled = True # bool | Indication of whether the phone number can handle sending and receiving SMS messages. Typically set to true for all numbers. (optional) if omitted the server will use the default value of True
    capabilities_voice = True # bool |  (optional)
    capabilities_sms = True # bool |  (optional)
    capabilities_toll_free = True # bool |  (optional)
    capabilities_ten_dlc = True # bool |  (optional)
    capabilities_short_code = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List available numbers
        api_response = api_instance.list_available_numbers(phone_number=phone_number, region=region, country=country, voice_enabled=voice_enabled, sms_enabled=sms_enabled, capabilities_voice=capabilities_voice, capabilities_sms=capabilities_sms, capabilities_toll_free=capabilities_toll_free, capabilities_ten_dlc=capabilities_ten_dlc, capabilities_short_code=capabilities_short_code)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_available_numbers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| PCRE-compatible regular expression to filter against &#x60;phoneNumber&#x60; field, which is in E.164 format. | [optional]
 **region** | **str**| State or province of this phone number. | [optional]
 **country** | **str**| Country of this phone number. | [optional]
 **voice_enabled** | **bool**| Indicates whether the phone number can handle Calls. Typically set to true for all numbers. | [optional] if omitted the server will use the default value of True
 **sms_enabled** | **bool**| Indication of whether the phone number can handle sending and receiving SMS messages. Typically set to true for all numbers. | [optional] if omitted the server will use the default value of True
 **capabilities_voice** | **bool**|  | [optional]
 **capabilities_sms** | **bool**|  | [optional]
 **capabilities_toll_free** | **bool**|  | [optional]
 **capabilities_ten_dlc** | **bool**|  | [optional]
 **capabilities_short_code** | **bool**|  | [optional]

### Return type

[**AvailableNumberList**](AvailableNumberList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available Numbers List |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_logs**
> LogList list_call_logs(account_id, call_id)

List Call Logs

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.log_list import LogList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    call_id = "callId_example" # str | String that uniquely identifies this call resource.

    # example passing only required values which don't have defaults set
    try:
        # List Call Logs
        api_response = api_instance.list_call_logs(account_id, call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_call_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **call_id** | **str**| String that uniquely identifies this call resource. |

### Return type

[**LogList**](LogList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs for this call |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_recordings**
> RecordingList list_call_recordings(account_id, call_id)

List Call Recordings

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.recording_list import RecordingList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    call_id = "callId_example" # str | String that uniquely identifies this call resource.
    date_created = "dateCreated_example" # str | Only show recordings created on the specified date, in the form *YYYY-MM-DD*. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Call Recordings
        api_response = api_instance.list_call_recordings(account_id, call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_call_recordings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Call Recordings
        api_response = api_instance.list_call_recordings(account_id, call_id, date_created=date_created)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_call_recordings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **call_id** | **str**| String that uniquely identifies this call resource. |
 **date_created** | **str**| Only show recordings created on the specified date, in the form *YYYY-MM-DD*. | [optional]

### Return type

[**RecordingList**](RecordingList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of recordings for a call |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_calls**
> CallList list_calls(account_id)

List Calls

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.call_status import CallStatus
from freeclimb.model.call_list import CallList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    active = False # bool | If active is set to true then all calls of the nature queued, ringing, inProgress are returned in the query. (optional) if omitted the server will use the default value of False
    to = "to_example" # str | Only show Calls to this phone number. (optional)
    _from = "from_example" # str | Only show Calls from this phone number. (optional)
    status = CallStatus("queued") # CallStatus | Only show Calls currently in this status. May be `queued`, `ringing`, `inProgress`, `canceled`, `completed`, `failed`, `busy`, or `noAnswer`. (optional)
    start_time = "startTime_example" # str | Only show Calls that started at or after this time, given as YYYY-MM-DD hh:mm:ss. (optional)
    end_time = "endTime_example" # str | Only show Calls that ended at or before this time, given as YYYY-MM- DD hh:mm:ss. (optional)
    parent_call_id = "parentCallId_example" # str | Only show Calls spawned by the call with this ID. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Calls
        api_response = api_instance.list_calls(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_calls: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Calls
        api_response = api_instance.list_calls(account_id, active=active, to=to, _from=_from, status=status, start_time=start_time, end_time=end_time, parent_call_id=parent_call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_calls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **active** | **bool**| If active is set to true then all calls of the nature queued, ringing, inProgress are returned in the query. | [optional] if omitted the server will use the default value of False
 **to** | **str**| Only show Calls to this phone number. | [optional]
 **_from** | **str**| Only show Calls from this phone number. | [optional]
 **status** | **CallStatus**| Only show Calls currently in this status. May be &#x60;queued&#x60;, &#x60;ringing&#x60;, &#x60;inProgress&#x60;, &#x60;canceled&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, &#x60;busy&#x60;, or &#x60;noAnswer&#x60;. | [optional]
 **start_time** | **str**| Only show Calls that started at or after this time, given as YYYY-MM-DD hh:mm:ss. | [optional]
 **end_time** | **str**| Only show Calls that ended at or before this time, given as YYYY-MM- DD hh:mm:ss. | [optional]
 **parent_call_id** | **str**| Only show Calls spawned by the call with this ID. | [optional]

### Return type

[**CallList**](CallList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieved call list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conferences**
> ConferenceList list_conferences(account_id)

List Conferences

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.conference_list import ConferenceList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    status = "status_example" # str | Only show conferences that currently have the specified status. Valid values: `empty`, `populated`, `inProgress`, or `terminated`. (optional)
    alias = "alias_example" # str | List Conferences whose alias exactly matches this string. (optional)
    date_created = "dateCreated_example" # str | Only show Conferences that were created on the specified date, in the form *YYYY-MM-DD*. (optional)
    date_updated = "dateUpdated_example" # str | Only show Conferences that were last updated on the specified date, in the form *YYYY-MM-DD*. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Conferences
        api_response = api_instance.list_conferences(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_conferences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Conferences
        api_response = api_instance.list_conferences(account_id, status=status, alias=alias, date_created=date_created, date_updated=date_updated)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_conferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **status** | **str**| Only show conferences that currently have the specified status. Valid values: &#x60;empty&#x60;, &#x60;populated&#x60;, &#x60;inProgress&#x60;, or &#x60;terminated&#x60;. | [optional]
 **alias** | **str**| List Conferences whose alias exactly matches this string. | [optional]
 **date_created** | **str**| Only show Conferences that were created on the specified date, in the form *YYYY-MM-DD*. | [optional]
 **date_updated** | **str**| Only show Conferences that were last updated on the specified date, in the form *YYYY-MM-DD*. | [optional]

### Return type

[**ConferenceList**](ConferenceList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Conferences |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incoming_numbers**
> IncomingNumberList list_incoming_numbers(account_id)

List Incoming Numbers

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.incoming_number_list import IncomingNumberList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    phone_number = "phoneNumber_example" # str | Only show incoming phone number resources that match this PCRE-compatible regular expression. (optional)
    alias = "alias_example" # str | Only show incoming phone numbers with aliases that exactly match this value. (optional)
    region = "region_example" # str | State or province of this phone number. (optional)
    country = "country_example" # str | Country of this phone number. (optional)
    application_id = "applicationId_example" # str | ID of the Application that FreeClimb should contact if a Call or SMS arrives for this phone number or a Call from this number is placed. An incoming phone number is not useful until associated with an applicationId. (optional)
    has_application = False # bool | Indication of whether the phone number has an application linked to it. (optional) if omitted the server will use the default value of False
    voice_enabled = True # bool | Indicates whether the phone number can handle Calls. Typically set to true for all numbers. (optional) if omitted the server will use the default value of True
    sms_enabled = True # bool | Indication of whether the phone number can handle sending and receiving SMS messages. Typically set to true for all numbers. (optional) if omitted the server will use the default value of True
    capabilities_voice = True # bool |  (optional)
    capabilities_sms = True # bool |  (optional)
    capabilities_toll_free = True # bool |  (optional)
    capabilities_ten_dlc = True # bool |  (optional)
    capabilities_short_code = True # bool |  (optional)
    offnet = True # bool, none_type | Indication of whether the phone number was registered as an offnet number. This field will be rendered only for requests to the IncomingPhone number resource. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Incoming Numbers
        api_response = api_instance.list_incoming_numbers(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_numbers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Incoming Numbers
        api_response = api_instance.list_incoming_numbers(account_id, phone_number=phone_number, alias=alias, region=region, country=country, application_id=application_id, has_application=has_application, voice_enabled=voice_enabled, sms_enabled=sms_enabled, capabilities_voice=capabilities_voice, capabilities_sms=capabilities_sms, capabilities_toll_free=capabilities_toll_free, capabilities_ten_dlc=capabilities_ten_dlc, capabilities_short_code=capabilities_short_code, offnet=offnet)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_numbers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **phone_number** | **str**| Only show incoming phone number resources that match this PCRE-compatible regular expression. | [optional]
 **alias** | **str**| Only show incoming phone numbers with aliases that exactly match this value. | [optional]
 **region** | **str**| State or province of this phone number. | [optional]
 **country** | **str**| Country of this phone number. | [optional]
 **application_id** | **str**| ID of the Application that FreeClimb should contact if a Call or SMS arrives for this phone number or a Call from this number is placed. An incoming phone number is not useful until associated with an applicationId. | [optional]
 **has_application** | **bool**| Indication of whether the phone number has an application linked to it. | [optional] if omitted the server will use the default value of False
 **voice_enabled** | **bool**| Indicates whether the phone number can handle Calls. Typically set to true for all numbers. | [optional] if omitted the server will use the default value of True
 **sms_enabled** | **bool**| Indication of whether the phone number can handle sending and receiving SMS messages. Typically set to true for all numbers. | [optional] if omitted the server will use the default value of True
 **capabilities_voice** | **bool**|  | [optional]
 **capabilities_sms** | **bool**|  | [optional]
 **capabilities_toll_free** | **bool**|  | [optional]
 **capabilities_ten_dlc** | **bool**|  | [optional]
 **capabilities_short_code** | **bool**|  | [optional]
 **offnet** | **bool, none_type**| Indication of whether the phone number was registered as an offnet number. This field will be rendered only for requests to the IncomingPhone number resource. | [optional]

### Return type

[**IncomingNumberList**](IncomingNumberList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Incoming Phone Numbers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> QueueMemberList list_members(account_id, queue_id)

List Members

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_member_list import QueueMemberList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_id = "queueId_example" # str | String that uniquely identifies the Queue that the Member belongs to.

    # example passing only required values which don't have defaults set
    try:
        # List Members
        api_response = api_instance.list_members(account_id, queue_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_id** | **str**| String that uniquely identifies the Queue that the Member belongs to. |

### Return type

[**QueueMemberList**](QueueMemberList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved queue member list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_participants**
> ConferenceParticipantList list_participants(account_id, conference_id)

List Participants

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.conference_participant_list import ConferenceParticipantList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    conference_id = "conferenceId_example" # str | ID of the conference this participant is in.
    talk = True # bool | Only show Participants with the talk privilege. (optional)
    listen = True # bool | Only show Participants with the listen privilege. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Participants
        api_response = api_instance.list_participants(account_id, conference_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Participants
        api_response = api_instance.list_participants(account_id, conference_id, talk=talk, listen=listen)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **conference_id** | **str**| ID of the conference this participant is in. |
 **talk** | **bool**| Only show Participants with the talk privilege. | [optional]
 **listen** | **bool**| Only show Participants with the listen privilege. | [optional]

### Return type

[**ConferenceParticipantList**](ConferenceParticipantList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved conference participant list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recordings**
> RecordingList list_recordings(account_id)

List Recordings

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.recording_list import RecordingList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    call_id = "callId_example" # str | Show only Recordings made during the Call with this ID. (optional)
    conference_id = "conferenceId_example" # str | Show only Recordings made during the conference with this ID. (optional)
    date_created = "dateCreated_example" # str | Only show Recordings created on this date, formatted as *YYYY-MM-DD*. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Recordings
        api_response = api_instance.list_recordings(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_recordings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Recordings
        api_response = api_instance.list_recordings(account_id, call_id=call_id, conference_id=conference_id, date_created=date_created)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_recordings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **call_id** | **str**| Show only Recordings made during the Call with this ID. | [optional]
 **conference_id** | **str**| Show only Recordings made during the conference with this ID. | [optional]
 **date_created** | **str**| Only show Recordings created on this date, formatted as *YYYY-MM-DD*. | [optional]

### Return type

[**RecordingList**](RecordingList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Recordings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sms_messages**
> MessagesList list_sms_messages(account_id)

List SMS Messages

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.message_direction import MessageDirection
from freeclimb.model.messages_list import MessagesList
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    to = "to_example" # str | Only show Messages to this phone number. (optional)
    _from = "from_example" # str | Only show Messages from this phone number. (optional)
    begin_time = "beginTime_example" # str | Only show Messages sent at or after this time (GMT), given as *YYYY-MM-DD hh:mm:ss*. (optional)
    end_time = "endTime_example" # str | Only show messages sent at or before this time (GMT), given as *YYYY-MM-DD hh:mm*.. (optional)
    direction = MessageDirection("inbound") # MessageDirection | Either `inbound` or `outbound`. Only show Messages that were either *sent from* or *received by* FreeClimb. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List SMS Messages
        api_response = api_instance.list_sms_messages(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_sms_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List SMS Messages
        api_response = api_instance.list_sms_messages(account_id, to=to, _from=_from, begin_time=begin_time, end_time=end_time, direction=direction)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->list_sms_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **to** | **str**| Only show Messages to this phone number. | [optional]
 **_from** | **str**| Only show Messages from this phone number. | [optional]
 **begin_time** | **str**| Only show Messages sent at or after this time (GMT), given as *YYYY-MM-DD hh:mm:ss*. | [optional]
 **end_time** | **str**| Only show messages sent at or before this time (GMT), given as *YYYY-MM-DD hh:mm*.. | [optional]
 **direction** | **MessageDirection**| Either &#x60;inbound&#x60; or &#x60;outbound&#x60;. Only show Messages that were either *sent from* or *received by* FreeClimb. | [optional]

### Return type

[**MessagesList**](MessagesList.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of messages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_a_call**
> CallResult make_a_call(account_id)

Make a Call

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.make_call_request import MakeCallRequest
from freeclimb.model.call_result import CallResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    make_call_request = MakeCallRequest(
        _from="_from_example",
        to="to_example",
        application_id="application_id_example",
        send_digits="send_digits_example",
        if_machine="if_machine_example",
        if_machine_url="if_machine_url_example",
        timeout=30,
        parent_call_id="parent_call_id_example",
        privacy_mode=True,
        call_connect_url="call_connect_url_example",
    ) # MakeCallRequest | Call details for making a call (optional)

    # example passing only required values which don't have defaults set
    try:
        # Make a Call
        api_response = api_instance.make_a_call(account_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->make_a_call: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Make a Call
        api_response = api_instance.make_a_call(account_id, make_call_request=make_call_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->make_a_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **make_call_request** | [**MakeCallRequest**](MakeCallRequest.md)| Call details for making a call | [optional]

### Return type

[**CallResult**](CallResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Call that was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_a_participant**
> remove_a_participant(account_id, conference_id, call_id)

Remove a Participant

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    conference_id = "conferenceId_example" # str | ID of the conference this participant is in.
    call_id = "callId_example" # str | ID of the Call associated with this participant.

    # example passing only required values which don't have defaults set
    try:
        # Remove a Participant
        api_instance.remove_a_participant(account_id, conference_id, call_id)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->remove_a_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **conference_id** | **str**| ID of the conference this participant is in. |
 **call_id** | **str**| ID of the Call associated with this participant. |

### Return type

void (empty response body)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted conference participant |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_an_sms_message**
> MessageResult send_an_sms_message(account_id, message_request)

Send an SMS Message

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.message_result import MessageResult
from freeclimb.model.message_request import MessageRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    message_request = MessageRequest(None) # MessageRequest | Details to create a message

    # example passing only required values which don't have defaults set
    try:
        # Send an SMS Message
        api_response = api_instance.send_an_sms_message(account_id, message_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->send_an_sms_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **message_request** | [**MessageRequest**](MessageRequest.md)| Details to create a message |

### Return type

[**MessageResult**](MessageResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The message has been accepted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_a_recording_file**
> file_type stream_a_recording_file(account_id, recording_id)

Stream a Recording File

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    recording_id = "recordingId_example" # str | String that uniquely identifies this recording resource.

    # example passing only required values which don't have defaults set
    try:
        # Stream a Recording File
        api_response = api_instance.stream_a_recording_file(account_id, recording_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->stream_a_recording_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **recording_id** | **str**| String that uniquely identifies this recording resource. |

### Return type

**file_type**

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/x-wav


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Streaming a Recording represented with audio/x-wav mime-type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_conference**
> ConferenceResult update_a_conference(account_id, conference_id)

Update a Conference

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.update_conference_request import UpdateConferenceRequest
from freeclimb.model.conference_result import ConferenceResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    conference_id = "conferenceId_example" # str | String that uniquely identifies this conference resource.
    update_conference_request = UpdateConferenceRequest(
        alias="alias_example",
        play_beep=PlayBeep("always"),
        status=UpdateConferenceRequestStatus("empty"),
    ) # UpdateConferenceRequest | Conference Details to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Conference
        api_response = api_instance.update_a_conference(account_id, conference_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_a_conference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Conference
        api_response = api_instance.update_a_conference(account_id, conference_id, update_conference_request=update_conference_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_a_conference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **conference_id** | **str**| String that uniquely identifies this conference resource. |
 **update_conference_request** | [**UpdateConferenceRequest**](UpdateConferenceRequest.md)| Conference Details to update | [optional]

### Return type

[**ConferenceResult**](ConferenceResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conference Details to Update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_live_call**
> update_a_live_call(account_id, call_id, update_call_request)

Update a Live Call

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.update_call_request import UpdateCallRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    call_id = "callId_example" # str | String that uniquely identifies this call resource.
    update_call_request = UpdateCallRequest(
        status=UpdateCallRequestStatus("canceled"),
    ) # UpdateCallRequest | Call details to update

    # example passing only required values which don't have defaults set
    try:
        # Update a Live Call
        api_instance.update_a_live_call(account_id, call_id, update_call_request)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_a_live_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **call_id** | **str**| String that uniquely identifies this call resource. |
 **update_call_request** | [**UpdateCallRequest**](UpdateCallRequest.md)| Call details to update |

### Return type

void (empty response body)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully queued call |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_participant**
> ConferenceParticipantResult update_a_participant(account_id, conference_id, call_id)

Update a Participant

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.update_conference_participant_request import UpdateConferenceParticipantRequest
from freeclimb.model.conference_participant_result import ConferenceParticipantResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    conference_id = "conferenceId_example" # str | ID of the conference this participant is in.
    call_id = "callId_example" # str | ID of the Call associated with this participant.
    update_conference_participant_request = UpdateConferenceParticipantRequest(
        talk=True,
        listen=True,
    ) # UpdateConferenceParticipantRequest | Conference participant details to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Participant
        api_response = api_instance.update_a_participant(account_id, conference_id, call_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_a_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Participant
        api_response = api_instance.update_a_participant(account_id, conference_id, call_id, update_conference_participant_request=update_conference_participant_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_a_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **conference_id** | **str**| ID of the conference this participant is in. |
 **call_id** | **str**| ID of the Call associated with this participant. |
 **update_conference_participant_request** | [**UpdateConferenceParticipantRequest**](UpdateConferenceParticipantRequest.md)| Conference participant details to update | [optional]

### Return type

[**ConferenceParticipantResult**](ConferenceParticipantResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved conference participant |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_queue**
> QueueResult update_a_queue(account_id, queue_id)

Update a Queue

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.queue_result import QueueResult
from freeclimb.model.queue_request import QueueRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    queue_id = "queueId_example" # str | A string that uniquely identifies this Queue resource.
    queue_request = QueueRequest(
        alias="alias_example",
        max_size=100,
    ) # QueueRequest | Queue Details to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Queue
        api_response = api_instance.update_a_queue(account_id, queue_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_a_queue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Queue
        api_response = api_instance.update_a_queue(account_id, queue_id, queue_request=queue_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_a_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **queue_id** | **str**| A string that uniquely identifies this Queue resource. |
 **queue_request** | [**QueueRequest**](QueueRequest.md)| Queue Details to update | [optional]

### Return type

[**QueueResult**](QueueResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated queue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_account**
> update_an_account(account_id)

Manage an account

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.account_request import AccountRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    account_request = AccountRequest(
        alias="alias_example",
        label="label_example",
    ) # AccountRequest | Account details to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Manage an account
        api_instance.update_an_account(account_id)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_an_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Manage an account
        api_instance.update_an_account(account_id, account_request=account_request)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_an_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **account_request** | [**AccountRequest**](AccountRequest.md)| Account details to update | [optional]

### Return type

void (empty response body)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Account update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_application**
> ApplicationResult update_an_application(account_id, application_id)

Update an application

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.application_request import ApplicationRequest
from freeclimb.model.application_result import ApplicationResult
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    application_id = "applicationId_example" # str | A string that uniquely identifies this application resource.
    application_request = ApplicationRequest(
        alias="alias_example",
        voice_url="voice_url_example",
        voice_fallback_url="voice_fallback_url_example",
        call_connect_url="call_connect_url_example",
        status_callback_url="status_callback_url_example",
        sms_url="sms_url_example",
        sms_fallback_url="sms_fallback_url_example",
    ) # ApplicationRequest | Application details to update. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an application
        api_response = api_instance.update_an_application(account_id, application_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_an_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an application
        api_response = api_instance.update_an_application(account_id, application_id, application_request=application_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_an_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **application_id** | **str**| A string that uniquely identifies this application resource. |
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)| Application details to update. | [optional]

### Return type

[**ApplicationResult**](ApplicationResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_incoming_number**
> IncomingNumberResult update_an_incoming_number(account_id, phone_number_id)

Update an Incoming Number

### Example

* Basic Authentication (fc):

```python
import time
import freeclimb
from freeclimb.api import default_api
from freeclimb.model.incoming_number_result import IncomingNumberResult
from freeclimb.model.incoming_number_request import IncomingNumberRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | ID of the account
    phone_number_id = "phoneNumberId_example" # str | String that uniquely identifies this phone number resource.
    incoming_number_request = IncomingNumberRequest(
        application_id="application_id_example",
        alias="alias_example",
    ) # IncomingNumberRequest | Incoming Number details to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Incoming Number
        api_response = api_instance.update_an_incoming_number(account_id, phone_number_id)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_an_incoming_number: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Incoming Number
        api_response = api_instance.update_an_incoming_number(account_id, phone_number_id, incoming_number_request=incoming_number_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->update_an_incoming_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account |
 **phone_number_id** | **str**| String that uniquely identifies this phone number resource. |
 **incoming_number_request** | [**IncomingNumberRequest**](IncomingNumberRequest.md)| Incoming Number details to update | [optional]

### Return type

[**IncomingNumberResult**](IncomingNumberResult.md)

### Authorization

[fc](../README.md#fc)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Incoming Phone Number |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

