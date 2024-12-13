# PaginationModel


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

## Example

```python
from freeclimb.models.pagination_model import PaginationModel

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationModel from a JSON string
pagination_model_instance = PaginationModel.from_json(json)
# print the JSON string representation of the object
print(PaginationModel.to_json())

# convert the object into a dict
pagination_model_dict = pagination_model_instance.to_dict()
# create an instance of PaginationModel from a dict
pagination_model_from_dict = PaginationModel.from_dict(pagination_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


