# UpdateConferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Description for this conference. Maximum 64 characters. | [optional] 
**play_beep** | [**PlayBeep**](PlayBeep.md) |  | [optional] 
**status** | [**UpdateConferenceRequestStatus**](UpdateConferenceRequestStatus.md) |  | [optional] 

## Example

```python
from freeclimb.models.update_conference_request import UpdateConferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConferenceRequest from a JSON string
update_conference_request_instance = UpdateConferenceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateConferenceRequest.to_json())

# convert the object into a dict
update_conference_request_dict = update_conference_request_instance.to_dict()
# create an instance of UpdateConferenceRequest from a dict
update_conference_request_from_dict = UpdateConferenceRequest.from_dict(update_conference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


