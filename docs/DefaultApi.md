# freeclimb.DefaultApi

All URIs are relative to *https://www.freeclimb.com/apiserver*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_an_account**](DefaultApi.md#get_an_account) | **GET** /Accounts/{accountId} | Get an Account
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
[**get_an_application**](DefaultApi.md#get_an_application) | **GET** /Accounts/{accountId}/Applications/{applicationId} | Get an Application
[**get_an_incoming_number**](DefaultApi.md#get_an_incoming_number) | **GET** /Accounts/{accountId}/IncomingPhoneNumbers/{phoneNumberId} | Get an Incoming Number
[**get_an_sms_message**](DefaultApi.md#get_an_sms_message) | **GET** /Accounts/{accountId}/Messages/{messageId} | Get an SMS Message
[**get_head_member**](DefaultApi.md#get_head_member) | **GET** /Accounts/{accountId}/Queues/{queueId}/Members/Front | Get Head Member
[**list_active_queues**](DefaultApi.md#list_active_queues) | **GET** /Accounts/{accountId}/Queues | List Active Queues
[**list_all_account_logs**](DefaultApi.md#list_all_account_logs) | **GET** /Accounts/{accountId}/Logs | List All Account Logs
[**list_an_application**](DefaultApi.md#list_an_application) | **GET** /Accounts/{accountId}/Applications | List applications
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


# **get_an_account**
> AccountResult get_an_account()

Get an Account

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    
    try:
        # Get an Account
        api_response = api_instance.get_an_account()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_an_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **buy_a_phone_number**
> IncomingNumberResult buy_a_phone_number(buy_incoming_number_request)

Buy a Phone Number

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    buy_incoming_number_request = freeclimb.BuyIncomingNumberRequest() # BuyIncomingNumberRequest | Incoming Number transaction details

    try:
        # Buy a Phone Number
        api_response = api_instance.buy_a_phone_number(buy_incoming_number_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->buy_a_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ConferenceResult create_a_conference(create_conference_request=create_conference_request)

Create a Conference

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    create_conference_request = freeclimb.CreateConferenceRequest() # CreateConferenceRequest | Conference to create (optional)

    try:
        # Create a Conference
        api_response = api_instance.create_a_conference(create_conference_request=create_conference_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_a_conference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueResult create_a_queue(queue_request=queue_request)

Create a Queue

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_request = freeclimb.QueueRequest() # QueueRequest | Queue details used to create a queue (optional)

    try:
        # Create a Queue
        api_response = api_instance.create_a_queue(queue_request=queue_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_a_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ApplicationResult create_an_application(application_request=application_request)

Create an application

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    application_request = freeclimb.ApplicationRequest() # ApplicationRequest | Application Details (optional)

    try:
        # Create an application
        api_response = api_instance.create_an_application(application_request=application_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_an_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> delete_a_recording(recording_id)

Delete a Recording

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    recording_id = 'recording_id_example' # str | String that uniquely identifies this recording resource.

    try:
        # Delete a Recording
        api_instance.delete_a_recording(recording_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_a_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> delete_an_application(application_id)

Delete an application

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    application_id = 'application_id_example' # str | String that uniquely identifies this application resource.

    try:
        # Delete an application
        api_instance.delete_an_application(application_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_an_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> delete_an_incoming_number(phone_number_id)

Delete an Incoming Number

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | String that uniquely identifies this phone number resource.

    try:
        # Delete an Incoming Number
        api_instance.delete_an_incoming_number(phone_number_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_an_incoming_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueMember dequeue_a_member(queue_id, call_id)

Dequeue a Member

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_id = 'queue_id_example' # str | String that uniquely identifies the Queue that the Member belongs to.
call_id = 'call_id_example' # str | ID if the Call that the Member belongs to

    try:
        # Dequeue a Member
        api_response = api_instance.dequeue_a_member(queue_id, call_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->dequeue_a_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueMember dequeue_head_member(queue_id)

Dequeue Head Member

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_id = 'queue_id_example' # str | String that uniquely identifies this queue resource.

    try:
        # Dequeue Head Member
        api_response = api_instance.dequeue_head_member(queue_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->dequeue_head_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> file download_a_recording_file(recording_id)

Download a Recording File

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    recording_id = 'recording_id_example' # str | String that uniquely identifies this recording resource.

    try:
        # Download a Recording File
        api_response = api_instance.download_a_recording_file(recording_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->download_a_recording_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| String that uniquely identifies this recording resource. | 

### Return type

**file**

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
> LogList filter_logs(filter_logs_request)

Filter Logs

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    filter_logs_request = freeclimb.FilterLogsRequest() # FilterLogsRequest | Filter logs request paramters

    try:
        # Filter Logs
        api_response = api_instance.filter_logs(filter_logs_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->filter_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> CallResult get_a_call(call_id)

Get a Call

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    call_id = 'call_id_example' # str | String that uniquely identifies this call resource.

    try:
        # Get a Call
        api_response = api_instance.get_a_call(call_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_a_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ConferenceResult get_a_conference(conference_id)

Get a Conference

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    conference_id = 'conference_id_example' # str | A string that uniquely identifies this conference resource.

    try:
        # Get a Conference
        api_response = api_instance.get_a_conference(conference_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_a_conference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueMember get_a_member(queue_id, call_id)

Get a Member

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_id = 'queue_id_example' # str | String that uniquely identifies the Queue that the Member belongs to.
call_id = 'call_id_example' # str | ID of the Call that the Member belongs to

    try:
        # Get a Member
        api_response = api_instance.get_a_member(queue_id, call_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_a_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ConferenceParticipantResult get_a_participant(conference_id, call_id)

Get a Participant

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    conference_id = 'conference_id_example' # str | ID of the conference this participant is in.
call_id = 'call_id_example' # str | ID of the Call associated with this participant.

    try:
        # Get a Participant
        api_response = api_instance.get_a_participant(conference_id, call_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_a_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueResult get_a_queue(queue_id)

Get a Queue

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_id = 'queue_id_example' # str | A string that uniquely identifies this queue resource.

    try:
        # Get a Queue
        api_response = api_instance.get_a_queue(queue_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_a_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> RecordingResult get_a_recording(recording_id)

Get a Recording

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    recording_id = 'recording_id_example' # str | String that uniquely identifies this recording resource.

    try:
        # Get a Recording
        api_response = api_instance.get_a_recording(recording_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_a_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_an_application**
> ApplicationResult get_an_application(application_id)

Get an Application

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    application_id = 'application_id_example' # str | A string that uniquely identifies this application resource.

    try:
        # Get an Application
        api_response = api_instance.get_an_application(application_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_an_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> IncomingNumberResult get_an_incoming_number(phone_number_id)

Get an Incoming Number

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | String that uniquely identifies this phone number resource.

    try:
        # Get an Incoming Number
        api_response = api_instance.get_an_incoming_number(phone_number_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_an_incoming_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> MessageResult get_an_sms_message(message_id)

Get an SMS Message

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    message_id = 'message_id_example' # str | String that uniquely identifies this Message resource.

    try:
        # Get an SMS Message
        api_response = api_instance.get_an_sms_message(message_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_an_sms_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueMember get_head_member(queue_id)

Get Head Member

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_id = 'queue_id_example' # str | String that uniquely identifies the Queue that the Member belongs to.

    try:
        # Get Head Member
        api_response = api_instance.get_head_member(queue_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_head_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueList list_active_queues(alias=alias)

List Active Queues

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    alias = 'alias_example' # str | Return only the Queue resources with aliases that exactly match this name. (optional)

    try:
        # List Active Queues
        api_response = api_instance.list_active_queues(alias=alias)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_active_queues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> LogList list_all_account_logs()

List All Account Logs

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    
    try:
        # List All Account Logs
        api_response = api_instance.list_all_account_logs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_all_account_logs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **list_an_application**
> ApplicationList list_an_application(alias=alias)

List applications

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    alias = 'alias_example' # str | Return only applications with aliases that exactly match this value. (optional)

    try:
        # List applications
        api_response = api_instance.list_an_application(alias=alias)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_an_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AvailableNumberList list_available_numbers(alias=alias, phone_number=phone_number)

List available numbers

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    alias = 'alias_example' # str | Filter on numbers based on the formatted string of the phone number. (optional)
phone_number = 'phone_number_example' # str | PCRE-compatible regular expression to filter against `phoneNumber` field, which is in E.164 format. (optional)

    try:
        # List available numbers
        api_response = api_instance.list_available_numbers(alias=alias, phone_number=phone_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_available_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Filter on numbers based on the formatted string of the phone number. | [optional] 
 **phone_number** | **str**| PCRE-compatible regular expression to filter against &#x60;phoneNumber&#x60; field, which is in E.164 format. | [optional] 

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
> LogList list_call_logs(call_id)

List Call Logs

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    call_id = 'call_id_example' # str | String that uniquely identifies this call resource.

    try:
        # List Call Logs
        api_response = api_instance.list_call_logs(call_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_call_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> RecordingList list_call_recordings(call_id, date_created=date_created)

List Call Recordings

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    call_id = 'call_id_example' # str | String that uniquely identifies this call resource.
date_created = 'date_created_example' # str | Only show recordings created on the specified date, in the form *YYYY-MM-DD*. (optional)

    try:
        # List Call Recordings
        api_response = api_instance.list_call_recordings(call_id, date_created=date_created)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_call_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> CallList list_calls(to=to, _from=_from, status=status, start_time=start_time, end_time=end_time, parent_call_id=parent_call_id)

List Calls

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    to = 'to_example' # str | Only show Calls to this phone number. (optional)
_from = '_from_example' # str | Only show Calls from this phone number. (optional)
status = 'status_example' # str | Only show Calls currently in this status. May be `queued`, `ringing`, `inProgress`, `canceled`, `completed`, `failed`, `busy`, or `noAnswer`. (optional)
start_time = 'start_time_example' # str | Only show Calls that started at or after this time, given as YYYY-MM-DD hh:mm:ss. (optional)
end_time = 'end_time_example' # str | Only show Calls that ended at or before this time, given as YYYY-MM- DD hh:mm:ss. (optional)
parent_call_id = 'parent_call_id_example' # str | Only show Calls spawned by the call with this ID. (optional)

    try:
        # List Calls
        api_response = api_instance.list_calls(to=to, _from=_from, status=status, start_time=start_time, end_time=end_time, parent_call_id=parent_call_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| Only show Calls to this phone number. | [optional] 
 **_from** | **str**| Only show Calls from this phone number. | [optional] 
 **status** | **str**| Only show Calls currently in this status. May be &#x60;queued&#x60;, &#x60;ringing&#x60;, &#x60;inProgress&#x60;, &#x60;canceled&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, &#x60;busy&#x60;, or &#x60;noAnswer&#x60;. | [optional] 
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
> ConferenceList list_conferences(status=status, alias=alias, date_created=date_created, date_updated=date_updated)

List Conferences

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    status = 'status_example' # str | Only show conferences that currently have the specified status. Valid values: `empty`, `populated`, `inProgress`, or `terminated`. (optional)
alias = 'alias_example' # str | List Conferences whose alias exactly matches this string. (optional)
date_created = 'date_created_example' # str | Only show Conferences that were created on the specified date, in the form *YYYY-MM-DD*. (optional)
date_updated = 'date_updated_example' # str | Only show Conferences that were last updated on the specified date, in the form *YYYY-MM-DD*. (optional)

    try:
        # List Conferences
        api_response = api_instance.list_conferences(status=status, alias=alias, date_created=date_created, date_updated=date_updated)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_conferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> IncomingNumberList list_incoming_numbers(phone_number=phone_number, alias=alias)

List Incoming Numbers

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    phone_number = 'phone_number_example' # str | Only show incoming phone number resources that match this PCRE-compatible regular expression. (optional)
alias = 'alias_example' # str | Only show incoming phone numbers with aliases that exactly match this value. (optional)

    try:
        # List Incoming Numbers
        api_response = api_instance.list_incoming_numbers(phone_number=phone_number, alias=alias)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| Only show incoming phone number resources that match this PCRE-compatible regular expression. | [optional] 
 **alias** | **str**| Only show incoming phone numbers with aliases that exactly match this value. | [optional] 

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
> QueueMemberList list_members(queue_id)

List Members

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_id = 'queue_id_example' # str | String that uniquely identifies the Queue that the Member belongs to.

    try:
        # List Members
        api_response = api_instance.list_members(queue_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ConferenceParticipantList list_participants(conference_id, talk=talk, listen=listen)

List Participants

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    conference_id = 'conference_id_example' # str | ID of the conference this participant is in.
talk = True # bool | Only show Participants with the talk privilege. (optional)
listen = True # bool | Only show Participants with the listen privilege. (optional)

    try:
        # List Participants
        api_response = api_instance.list_participants(conference_id, talk=talk, listen=listen)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> RecordingList list_recordings(call_id=call_id, conference_id=conference_id, date_created=date_created)

List Recordings

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    call_id = 'call_id_example' # str | Show only Recordings made during the Call with this ID. (optional)
conference_id = 'conference_id_example' # str | Show only Recordings made during the conference with this ID. (optional)
date_created = 'date_created_example' # str | Only show Recordings created on this date, formatted as *YYYY-MM-DD*. (optional)

    try:
        # List Recordings
        api_response = api_instance.list_recordings(call_id=call_id, conference_id=conference_id, date_created=date_created)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> MessagesList list_sms_messages(to=to, _from=_from, begin_time=begin_time, end_time=end_time, direction=direction, account_id=account_id)

List SMS Messages

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    to = 'to_example' # str | Only show Messages to this phone number. (optional)
_from = '_from_example' # str | Only show Messages from this phone number. (optional)
begin_time = 'begin_time_example' # str | Only show Messages sent at or after this time (GMT), given as *YYYY-MM-DD hh:mm:ss*. (optional)
end_time = 'end_time_example' # str | Only show messages sent at or before this time (GMT), given as *YYYY-MM-DD hh:mm*.. (optional)
direction = 'direction_example' # str | Either `inbound` or `outbound`. Only show Messages that were either *sent from* or *received by* FreeClimb. (optional)
account_id = 'account_id_example' # str | String that uniquely identifies this account resource. (optional)

    try:
        # List SMS Messages
        api_response = api_instance.list_sms_messages(to=to, _from=_from, begin_time=begin_time, end_time=end_time, direction=direction, account_id=account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_sms_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| Only show Messages to this phone number. | [optional] 
 **_from** | **str**| Only show Messages from this phone number. | [optional] 
 **begin_time** | **str**| Only show Messages sent at or after this time (GMT), given as *YYYY-MM-DD hh:mm:ss*. | [optional] 
 **end_time** | **str**| Only show messages sent at or before this time (GMT), given as *YYYY-MM-DD hh:mm*.. | [optional] 
 **direction** | **str**| Either &#x60;inbound&#x60; or &#x60;outbound&#x60;. Only show Messages that were either *sent from* or *received by* FreeClimb. | [optional] 
 **account_id** | **str**| String that uniquely identifies this account resource. | [optional] 

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
> CallResult make_a_call(make_call_request=make_call_request)

Make a Call

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    make_call_request = freeclimb.MakeCallRequest() # MakeCallRequest | Call details for making a call (optional)

    try:
        # Make a Call
        api_response = api_instance.make_a_call(make_call_request=make_call_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->make_a_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> remove_a_participant(conference_id, call_id)

Remove a Participant

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    conference_id = 'conference_id_example' # str | ID of the conference this participant is in.
call_id = 'call_id_example' # str | ID of the Call associated with this participant.

    try:
        # Remove a Participant
        api_instance.remove_a_participant(conference_id, call_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->remove_a_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> MessageResult send_an_sms_message(message_request)

Send an SMS Message

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    message_request = freeclimb.MessageRequest() # MessageRequest | Details to create a message

    try:
        # Send an SMS Message
        api_response = api_instance.send_an_sms_message(message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->send_an_sms_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> file stream_a_recording_file(recording_id)

Stream a Recording File

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    recording_id = 'recording_id_example' # str | String that uniquely identifies this recording resource.

    try:
        # Stream a Recording File
        api_response = api_instance.stream_a_recording_file(recording_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->stream_a_recording_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| String that uniquely identifies this recording resource. | 

### Return type

**file**

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
> ConferenceResult update_a_conference(conference_id, update_conference_request=update_conference_request)

Update a Conference

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    conference_id = 'conference_id_example' # str | String that uniquely identifies this conference resource.
update_conference_request = freeclimb.UpdateConferenceRequest() # UpdateConferenceRequest | Conference Details to update (optional)

    try:
        # Update a Conference
        api_response = api_instance.update_a_conference(conference_id, update_conference_request=update_conference_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_a_conference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> update_a_live_call(call_id, update_call_request)

Update a Live Call

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    call_id = 'call_id_example' # str | String that uniquely identifies this call resource.
update_call_request = freeclimb.UpdateCallRequest() # UpdateCallRequest | Call details to update

    try:
        # Update a Live Call
        api_instance.update_a_live_call(call_id, update_call_request)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_a_live_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ConferenceParticipantResult update_a_participant(conference_id, call_id, update_conference_participant_request=update_conference_participant_request)

Update a Participant

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    conference_id = 'conference_id_example' # str | ID of the conference this participant is in.
call_id = 'call_id_example' # str | ID of the Call associated with this participant.
update_conference_participant_request = freeclimb.UpdateConferenceParticipantRequest() # UpdateConferenceParticipantRequest | Conference participant details to update (optional)

    try:
        # Update a Participant
        api_response = api_instance.update_a_participant(conference_id, call_id, update_conference_participant_request=update_conference_participant_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_a_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> QueueResult update_a_queue(queue_id, queue_request=queue_request)

Update a Queue

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    queue_id = 'queue_id_example' # str | A string that uniquely identifies this Queue resource.
queue_request = freeclimb.QueueRequest() # QueueRequest | Queue Details to update (optional)

    try:
        # Update a Queue
        api_response = api_instance.update_a_queue(queue_id, queue_request=queue_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_a_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> update_an_account(account_request=account_request)

Manage an account

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    account_request = freeclimb.AccountRequest() # AccountRequest | Account details to update (optional)

    try:
        # Manage an account
        api_instance.update_an_account(account_request=account_request)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_an_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ApplicationResult update_an_application(application_id, application_request=application_request)

Update an application

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    application_id = 'application_id_example' # str | A string that uniquely identifies this application resource.
application_request = freeclimb.ApplicationRequest() # ApplicationRequest | Application details to update. (optional)

    try:
        # Update an application
        api_response = api_instance.update_an_application(application_id, application_request=application_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_an_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> IncomingNumberResult update_an_incoming_number(phone_number_id, incoming_number_request=incoming_number_request)

Update an Incoming Number

### Example

* Basic Authentication (fc):
```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint
configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'API_KEY'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"

# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freeclimb.DefaultApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | String that uniquely identifies this phone number resource.
incoming_number_request = freeclimb.IncomingNumberRequest() # IncomingNumberRequest | Incoming Number details to update (optional)

    try:
        # Update an Incoming Number
        api_response = api_instance.update_an_incoming_number(phone_number_id, incoming_number_request=incoming_number_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_an_incoming_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

