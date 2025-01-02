# Capabilities

Details for which features this number may be used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice** | **bool** | Indicates whether a number can be used for voice calls. Replaces voiceEnabled. | 
**sms** | **bool** | Indicates whether a number can be used SMS messaging. Replaces smsEnabled. | 
**toll_free** | **bool** | Indicates that a number is toll-free and will make toll-free calls, and when enabled, toll-free messages. | 
**ten_dlc** | **bool** | Indicates that a number, if sms is true, will be used for 10DLC messaging | 
**short_code** | **bool** | Indicates that a number is a short code and can be used for short code messaging | 

## Example

```python
from freeclimb.models.capabilities import Capabilities

# TODO update the JSON string below
json = "{}"
# create an instance of Capabilities from a JSON string
capabilities_instance = Capabilities.from_json(json)
# print the JSON string representation of the object
print(Capabilities.to_json())

# convert the object into a dict
capabilities_dict = capabilities_instance.to_dict()
# create an instance of Capabilities from a dict
capabilities_from_dict = Capabilities.from_dict(capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


