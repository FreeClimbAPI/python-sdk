# UpdateConferenceParticipantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**talk** | **bool** | (Optional) Default is &#x60;true&#x60;. Setting to &#x60;false&#x60; mutes the Participant. FreeClimb returns an error and ignores any other value. | [optional] 
**listen** | **bool** | (Optional) Default is &#x60;true&#x60;. Setting to &#x60;false&#x60; silences the Conference for this Participant. FreeClimb returns an error and ignores any other value. | [optional] 
**dtmf_pass_through** | **bool** | (Optional) Default is &#x60;true&#x60;. Setting to &#x60;false&#x60; mutes dtmf audio for this Participant. FreeClimb returns an error and ignores any other value. | [optional] 

## Example

```python
from freeclimb.models.update_conference_participant_request import UpdateConferenceParticipantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConferenceParticipantRequest from a JSON string
update_conference_participant_request_instance = UpdateConferenceParticipantRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateConferenceParticipantRequest.to_json())

# convert the object into a dict
update_conference_participant_request_dict = update_conference_participant_request_instance.to_dict()
# create an instance of UpdateConferenceParticipantRequest from a dict
update_conference_participant_request_from_dict = UpdateConferenceParticipantRequest.from_dict(update_conference_participant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


