# SetDTMFPassThrough

The `SetDTMFPassThrough` command enables or disables the dtmfPassThrough privilege for this Conference Participant. If 'true', DTMFs will be passed through from this Participant to all other Participants in the Conference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtmf_pass_through** | **bool** | Specifying &#x60;false&#x60; mutes the Participant&#39;s dtmf audio. | [optional] 

## Example

```python
from freeclimb.models.set_dtmf_pass_through import SetDTMFPassThrough

# TODO update the JSON string below
json = "{}"
# create an instance of SetDTMFPassThrough from a JSON string
set_dtmf_pass_through_instance = SetDTMFPassThrough.from_json(json)
# print the JSON string representation of the object
print(SetDTMFPassThrough.to_json())

# convert the object into a dict
set_dtmf_pass_through_dict = set_dtmf_pass_through_instance.to_dict()
# create an instance of SetDTMFPassThrough from a dict
set_dtmf_pass_through_from_dict = SetDTMFPassThrough.from_dict(set_dtmf_pass_through_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


