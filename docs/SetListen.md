# SetListen

The `SetListen` command enables or disables the listen privilege for this Conference Participant. The Participant can hear what the other participants are saying only if this privilege is enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listen** | **bool** | Specifying &#x60;false&#x60; will silence the Conference for this Participant. | [optional] 

## Example

```python
from freeclimb.models.set_listen import SetListen

# TODO update the JSON string below
json = "{}"
# create an instance of SetListen from a JSON string
set_listen_instance = SetListen.from_json(json)
# print the JSON string representation of the object
print(SetListen.to_json())

# convert the object into a dict
set_listen_dict = set_listen_instance.to_dict()
# create an instance of SetListen from a dict
set_listen_from_dict = SetListen.from_dict(set_listen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


