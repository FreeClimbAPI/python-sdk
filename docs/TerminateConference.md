# TerminateConference

The `TerminateConference` command terminates an existing Conference. Any active participants are hung up on by FreeClimb. If this is not the desired behavior, use the `RemoveFromConference` command to unbridge Calls that should not be hung up. Note: The Call requesting TerminateConference must be on the same Conference for this command to execute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from freeclimb.models.terminate_conference import TerminateConference

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateConference from a JSON string
terminate_conference_instance = TerminateConference.from_json(json)
# print the JSON string representation of the object
print(TerminateConference.to_json())

# convert the object into a dict
terminate_conference_dict = terminate_conference_instance.to_dict()
# create an instance of TerminateConference from a dict
terminate_conference_from_dict = TerminateConference.from_dict(terminate_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


