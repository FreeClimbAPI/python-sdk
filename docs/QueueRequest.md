# QueueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Description for this Queue. Max length is 64 characters. | [optional] 
**max_size** | **int** | Maximum number of calls this queue can hold. Default is 100. Maximum is 1000. **Note:** Reducing the maxSize of a Queue causes the Queue to reject incoming requests until it shrinks below the new value of maxSize. | [optional] [default to 100]

## Example

```python
from freeclimb.models.queue_request import QueueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueueRequest from a JSON string
queue_request_instance = QueueRequest.from_json(json)
# print the JSON string representation of the object
print(QueueRequest.to_json())

# convert the object into a dict
queue_request_dict = queue_request_instance.to_dict()
# create an instance of QueueRequest from a dict
queue_request_from_dict = QueueRequest.from_dict(queue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


