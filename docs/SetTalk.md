# SetTalk

The `SetTalk` command enables or disables the talk privilege for this Conference Participant. If 'true', no audio from that Participant is shared with the other Participants of the Conference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**talk** | **bool** | Specifying &#x60;false&#x60; mutes the Participant. | [optional] 

## Example

```python
from freeclimb.models.set_talk import SetTalk

# TODO update the JSON string below
json = "{}"
# create an instance of SetTalk from a JSON string
set_talk_instance = SetTalk.from_json(json)
# print the JSON string representation of the object
print(SetTalk.to_json())

# convert the object into a dict
set_talk_dict = set_talk_instance.to_dict()
# create an instance of SetTalk from a dict
set_talk_from_dict = SetTalk.from_dict(set_talk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


