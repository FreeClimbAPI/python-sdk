# ExportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total amount of requested resource. | [optional] 
**start** | **int** | Resource index at start of current page | [optional] 
**end** | **int** | Resource index at end of current page | [optional] 
**page** | **int** | Current page | [optional] 
**num_pages** | **int** | Total number of pages | [optional] 
**page_size** | **int** | Number of items per page | [optional] 
**next_page_uri** | **str** | Uri to retrieve the next page of items | [optional] 
**exports** | [**List[ExportResult]**](ExportResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.export_list import ExportList

# TODO update the JSON string below
json = "{}"
# create an instance of ExportList from a JSON string
export_list_instance = ExportList.from_json(json)
# print the JSON string representation of the object
print(ExportList.to_json())

# convert the object into a dict
export_list_dict = export_list_instance.to_dict()
# create an instance of ExportList from a dict
export_list_from_dict = ExportList.from_dict(export_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


