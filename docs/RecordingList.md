# RecordingList


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
**recordings** | [**List[RecordingResult]**](RecordingResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.recording_list import RecordingList

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingList from a JSON string
recording_list_instance = RecordingList.from_json(json)
# print the JSON string representation of the object
print(RecordingList.to_json())

# convert the object into a dict
recording_list_dict = recording_list_instance.to_dict()
# create an instance of RecordingList from a dict
recording_list_from_dict = RecordingList.from_dict(recording_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


