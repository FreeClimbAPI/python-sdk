# RemoveFromConference

The `RemoveFromConference` command removes a Participant from a Conference but does not hang up. Instead, the Call is simply unbridged and what happens next with the Call is determined by the PerCL returned in response to the `leaveConferenceUrl` attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from freeclimb.models.remove_from_conference import RemoveFromConference

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFromConference from a JSON string
remove_from_conference_instance = RemoveFromConference.from_json(json)
# print the JSON string representation of the object
print(RemoveFromConference.to_json())

# convert the object into a dict
remove_from_conference_dict = remove_from_conference_instance.to_dict()
# create an instance of RemoveFromConference from a dict
remove_from_conference_from_dict = RemoveFromConference.from_dict(remove_from_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


