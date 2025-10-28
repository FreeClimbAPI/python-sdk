# PlatformError

Standard error structure returned by platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**call** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**details** | **object** |  | [optional] 

## Example

```python
from freeclimb.models.platform_error import PlatformError

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformError from a JSON string
platform_error_instance = PlatformError.from_json(json)
# print the JSON string representation of the object
print(PlatformError.to_json())

# convert the object into a dict
platform_error_dict = platform_error_instance.to_dict()
# create an instance of PlatformError from a dict
platform_error_from_dict = PlatformError.from_dict(platform_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


