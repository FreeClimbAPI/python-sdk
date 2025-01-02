# QueueMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | URI for this Queue Member resource, relative to the API base URL. | [optional] 
**call_id** | **str** | ID of the Call associated with this Queue Member. | [optional] 
**wait_time** | **int** | Number of seconds the Member has been in the queue. | [optional] 
**position** | **int** | Member&#39;s current position in the Queue, 1 indexed. | [optional] 
**date_enqueued** | **str** | Date that the Member was enqueued (GMT), given in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 

## Example

```python
from freeclimb.models.queue_member import QueueMember

# TODO update the JSON string below
json = "{}"
# create an instance of QueueMember from a JSON string
queue_member_instance = QueueMember.from_json(json)
# print the JSON string representation of the object
print(QueueMember.to_json())

# convert the object into a dict
queue_member_dict = queue_member_instance.to_dict()
# create an instance of QueueMember from a dict
queue_member_from_dict = QueueMember.from_dict(queue_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


