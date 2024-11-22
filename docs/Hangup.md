# Hangup

The `Hangup` command terminates a Call. If `Hangup` is used as the first action in a PerCL response, it does not prevent FreeClimb from answering the Call and billing your account. See the `Reject` command to hang up at no charge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The user defined reason for the hangup. In general, applications should use a set of enumerated values that are predefined to cover all exit points of the Call flows for the given application. | [optional] 

## Example

```python
from freeclimb.models.hangup import Hangup

# TODO update the JSON string below
json = "{}"
# create an instance of Hangup from a JSON string
hangup_instance = Hangup.from_json(json)
# print the JSON string representation of the object
print(Hangup.to_json())

# convert the object into a dict
hangup_dict = hangup_instance.to_dict()
# create an instance of Hangup from a dict
hangup_from_dict = Hangup.from_dict(hangup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


