# ExportRequestOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExportOutputType**](ExportOutputType.md) |  | 

## Example

```python
from freeclimb.models.export_request_output import ExportRequestOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRequestOutput from a JSON string
export_request_output_instance = ExportRequestOutput.from_json(json)
# print the JSON string representation of the object
print(ExportRequestOutput.to_json())

# convert the object into a dict
export_request_output_dict = export_request_output_instance.to_dict()
# create an instance of ExportRequestOutput from a dict
export_request_output_from_dict = ExportRequestOutput.from_dict(export_request_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


