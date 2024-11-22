# PerclScript

A PerCL script to be returned to the FreeClimb servers in FreeClimb applications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[PerclCommand]**](PerclCommand.md) | A JSON array of PerCL commands | [optional] 

## Example

```python
from freeclimb.models.percl_script import PerclScript

# TODO update the JSON string below
json = "{}"
# create an instance of PerclScript from a JSON string
percl_script_instance = PerclScript.from_json(json)
# print the JSON string representation of the object
print(PerclScript.to_json())

# convert the object into a dict
percl_script_dict = percl_script_instance.to_dict()
# create an instance of PerclScript from a dict
percl_script_from_dict = PerclScript.from_dict(percl_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


