# Enqueue

The `Enqueue` command adds the current Call to a call Queue. If the specified Queue does not exist, it is created and then the Call is added to it. The default maximum length of the queue is 100. This can be modified using the REST API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** | A request is made to this URL when the Call leaves the Queue, which can occur if enqueue of the Call fails or when the call is dequeued via the &#x60;Dequeue&#x60; command, the REST API (POST to Queue Member resource), or the caller hangs up. | 
**notification_url** | **str** | URL to be invoked when the call enters the queue. The request to the URL contains the standard request parameters.This is a notification only; any PerCL returned will be ignored. | [optional] 
**queue_id** | **str** | ID of the Queue to which to add the Call. If the Queue does not exist, it will be created. The ID must start with QU followed by 40 hex characters. | 
**wait_url** | **str** | A request is made to this URL when the Call leaves the Queue, which can occur if enqueue of the Call fails or when the call is dequeued via the &#x60;Dequeue&#x60; command, the REST API (POST to Queue Member resource), or the caller hangs up. | 

## Example

```python
from freeclimb.models.enqueue import Enqueue

# TODO update the JSON string below
json = "{}"
# create an instance of Enqueue from a JSON string
enqueue_instance = Enqueue.from_json(json)
# print the JSON string representation of the object
print(Enqueue.to_json())

# convert the object into a dict
enqueue_dict = enqueue_instance.to_dict()
# create an instance of Enqueue from a dict
enqueue_from_dict = Enqueue.from_dict(enqueue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


