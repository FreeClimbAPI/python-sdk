# PerclCommand

An individual command used in a PerCLScript.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | Name of PerCL Command (this is automatically derived from mapping configuration and should not be manually supplied in any arguments) | [optional] 

## Example

```python
from freeclimb.models.percl_command import PerclCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PerclCommand from a JSON string
percl_command_instance = PerclCommand.from_json(json)
# print the JSON string representation of the object
print(PerclCommand.to_json())

# convert the object into a dict
percl_command_dict = percl_command_instance.to_dict()
# create an instance of PerclCommand from a dict
percl_command_from_dict = PerclCommand.from_dict(percl_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


