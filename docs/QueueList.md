# QueueList


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
**queues** | [**List[QueueResult]**](QueueResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.queue_list import QueueList

# TODO update the JSON string below
json = "{}"
# create an instance of QueueList from a JSON string
queue_list_instance = QueueList.from_json(json)
# print the JSON string representation of the object
print(QueueList.to_json())

# convert the object into a dict
queue_list_dict = queue_list_instance.to_dict()
# create an instance of QueueList from a dict
queue_list_from_dict = QueueList.from_dict(queue_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


