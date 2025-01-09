# ApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A human readable description of the application, with maximum length 64 characters. | [optional] 
**voice_url** | **str** | The URL that FreeClimb will request when an inbound call arrives on a phone number assigned to this application. Used only for inbound calls. | [optional] 
**voice_fallback_url** | **str** | The URL that FreeClimb will request if it times out waiting for a response from the voiceUrl. Used for inbound calls only. Note: A PerCL response is expected to control the inbound call. | [optional] 
**call_connect_url** | **str** | The URL that FreeClimb will request when an outbound call request is complete. Used for outbound calls only.  Note: A PerCL response is expected if the outbound call is connected (status&#x3D;InProgress) to control the call. | [optional] 
**status_callback_url** | **str** | The URL that FreeClimb will request to pass call status (such as call ended) to the application.  Note: This is a notification only; any PerCL returned will be ignored. | [optional] 
**sms_url** | **str** | The URL that FreeClimb will request when a phone number assigned to this application receives an incoming SMS message. Used for inbound SMS only.  Note: Any PerCL returned will be ignored. | [optional] 
**sms_fallback_url** | **str** | The URL that FreeClimb will request if it times out waiting for a response from the smsUrl. Used for inbound SMS only.  Note: Any PerCL returned will be ignored. | [optional] 

## Example

```python
from freeclimb.models.application_request import ApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRequest from a JSON string
application_request_instance = ApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationRequest.to_json())

# convert the object into a dict
application_request_dict = application_request_instance.to_dict()
# create an instance of ApplicationRequest from a dict
application_request_from_dict = ApplicationRequest.from_dict(application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


