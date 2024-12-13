# ApplicationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**account_id** | **str** | ID of the account that owns this phone number. | [optional] 
**application_id** | **str** | ID of the Application that FreeClimb should contact if a Call or SMS arrives for this phone number or a Call from this number is placed. An incoming phone number is not useful until associated with an applicationId. | [optional] 
**alias** | **str** | Description for this phone number. Typically the conventionally-formatted version of the phone number. | [optional] 
**voice_url** | **str** | The URL FreeClimb will request when a phone number assigned to this Application receives a Call. Used for inbound calls only. | [optional] 
**voice_fallback_url** | **str** | The URL that FreeClimb will request if it times out waiting for a response from the voiceUrl. Used for inbound calls only. | [optional] 
**call_connect_url** | **str** | The URL to which FreeClimb will make a POST request informing the result of the outbound Call request. The status property of the request message specifies if the Call was connected or not. | [optional] 
**status_callback_url** | **str** | A URL to which FreeClimb will make a POST request when the Call ends to notify this app. | [optional] 
**sms_url** | **str** | The URL FreeClimb will request when a phone number assigned to this Application receives an incoming SMS message. Used for inbound SMS only. | [optional] 
**sms_fallback_url** | **str** | The URL that FreeClimb will request if it times out waiting for a response from the smsUrl. Used for inbound SMS only. | [optional] 

## Example

```python
from freeclimb.models.application_result import ApplicationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResult from a JSON string
application_result_instance = ApplicationResult.from_json(json)
# print the JSON string representation of the object
print(ApplicationResult.to_json())

# convert the object into a dict
application_result_dict = application_result_instance.to_dict()
# create an instance of ApplicationResult from a dict
application_result_from_dict = ApplicationResult.from_dict(application_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


