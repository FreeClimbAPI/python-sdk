# MessagesList


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
**messages** | [**List[MessageResult]**](MessageResult.md) | Array of messages | [optional] 

## Example

```python
from freeclimb.models.messages_list import MessagesList

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesList from a JSON string
messages_list_instance = MessagesList.from_json(json)
# print the JSON string representation of the object
print(MessagesList.to_json())

# convert the object into a dict
messages_list_dict = messages_list_instance.to_dict()
# create an instance of MessagesList from a dict
messages_list_from_dict = MessagesList.from_dict(messages_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


