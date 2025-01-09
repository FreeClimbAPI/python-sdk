# StartRecordCall

The `StartRecordCall` command records the current call and returns the URL of a file containing the audio recording when recording completes. `StartRecordCall` is non-blocking. After recording of the current call begins, control of the call moves to the PerCL command that follows `StartRecordCall` in the current PerCL script.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from freeclimb.models.start_record_call import StartRecordCall

# TODO update the JSON string below
json = "{}"
# create an instance of StartRecordCall from a JSON string
start_record_call_instance = StartRecordCall.from_json(json)
# print the JSON string representation of the object
print(StartRecordCall.to_json())

# convert the object into a dict
start_record_call_dict = start_record_call_instance.to_dict()
# create an instance of StartRecordCall from a dict
start_record_call_from_dict = StartRecordCall.from_dict(start_record_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


