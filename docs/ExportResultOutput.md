# ExportResultOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExportOutputType**](ExportOutputType.md) |  | 

## Example

```python
from freeclimb.models.export_result_output import ExportResultOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ExportResultOutput from a JSON string
export_result_output_instance = ExportResultOutput.from_json(json)
# print the JSON string representation of the object
print(ExportResultOutput.to_json())

# convert the object into a dict
export_result_output_dict = export_result_output_instance.to_dict()
# create an instance of ExportResultOutput from a dict
export_result_output_from_dict = ExportResultOutput.from_dict(export_result_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


