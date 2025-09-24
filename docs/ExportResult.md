# ExportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | String that uniquely identifies this account resource. | 
**uri** | **str** |  | 
**date_created** | **str** |  | 
**date_updated** | **str** |  | 
**revision** | **int** |  | 
**export_id** | **str** | String that uniquely identifies this export resource | 
**status** | [**ExportStatus**](ExportStatus.md) |  | 
**size** | **int** |  | 
**resource_type** | [**ExportResourceType**](ExportResourceType.md) |  | 
**query** | **object** | Query params used to filter exported documents | 
**format** | **List[str]** | Desired fields of exported documents | 
**output** | [**ExportResultOutput**](ExportResultOutput.md) |  | 

## Example

```python
from freeclimb.models.export_result import ExportResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExportResult from a JSON string
export_result_instance = ExportResult.from_json(json)
# print the JSON string representation of the object
print(ExportResult.to_json())

# convert the object into a dict
export_result_dict = export_result_instance.to_dict()
# create an instance of ExportResult from a dict
export_result_from_dict = ExportResult.from_dict(export_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


