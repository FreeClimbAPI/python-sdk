# BlobListResponse


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
**blobs** | [**List[BlobResult]**](BlobResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.blob_list_response import BlobListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlobListResponse from a JSON string
blob_list_response_instance = BlobListResponse.from_json(json)
# print the JSON string representation of the object
print(BlobListResponse.to_json())

# convert the object into a dict
blob_list_response_dict = blob_list_response_instance.to_dict()
# create an instance of BlobListResponse from a dict
blob_list_response_from_dict = BlobListResponse.from_dict(blob_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


