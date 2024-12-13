# Dequeue

The `Dequeue` command transfers control of a Call that is in a Queue so that the waiting caller exits the Queue. Execution continues with the first command in the PerCL script returned by the `actionUrl` specified in the `Enqueue` command.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from freeclimb.models.dequeue import Dequeue

# TODO update the JSON string below
json = "{}"
# create an instance of Dequeue from a JSON string
dequeue_instance = Dequeue.from_json(json)
# print the JSON string representation of the object
print(Dequeue.to_json())

# convert the object into a dict
dequeue_dict = dequeue_instance.to_dict()
# create an instance of Dequeue from a dict
dequeue_from_dict = Dequeue.from_dict(dequeue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


