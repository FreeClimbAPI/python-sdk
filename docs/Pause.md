# Pause

The `Pause` command halts execution of the current PerCL script for a specified number of milliseconds. If `Pause` is the first command in a PerCL document, FreeClimb will wait for the specified time to elapse before picking up the call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Length in milliseconds. FreeClimb will wait silently before continuing on. | 

## Example

```python
from freeclimb.models.pause import Pause

# TODO update the JSON string below
json = "{}"
# create an instance of Pause from a JSON string
pause_instance = Pause.from_json(json)
# print the JSON string representation of the object
print(Pause.to_json())

# convert the object into a dict
pause_dict = pause_instance.to_dict()
# create an instance of Pause from a dict
pause_from_dict = Pause.from_dict(pause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


