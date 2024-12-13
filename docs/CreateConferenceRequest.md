# CreateConferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A description for this Conference. Maximum 64 characters. | [optional] 
**play_beep** | [**PlayBeep**](PlayBeep.md) |  | [optional] 
**record** | **bool** | Setting to &#x60;true&#x60; records the entire Conference. | [optional] 
**wait_url** | **str** | If specified, a URL for the audio file that provides custom hold music for the Conference when it is in the populated state. Otherwise, FreeClimb uses a system default audio file. This is always fetched using HTTP GET and is fetched just once &amp;mdash; when the Conference is created. | [optional] 
**status_callback_url** | **str** | This URL is invoked when the status of the Conference changes. For more information, see **statusCallbackUrl** (below). | [optional] 

## Example

```python
from freeclimb.models.create_conference_request import CreateConferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConferenceRequest from a JSON string
create_conference_request_instance = CreateConferenceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConferenceRequest.to_json())

# convert the object into a dict
create_conference_request_dict = create_conference_request_instance.to_dict()
# create an instance of CreateConferenceRequest from a dict
create_conference_request_from_dict = CreateConferenceRequest.from_dict(create_conference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


