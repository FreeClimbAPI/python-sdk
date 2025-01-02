# TranscribeUtteranceRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save_recording** | **bool** |  | [optional] [default to False]
**max_length_sec** | **int** |  | [optional] [default to 60]
**rcrd_termination_silence_time_ms** | **int** |  | [optional] 

## Example

```python
from freeclimb.models.transcribe_utterance_record import TranscribeUtteranceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TranscribeUtteranceRecord from a JSON string
transcribe_utterance_record_instance = TranscribeUtteranceRecord.from_json(json)
# print the JSON string representation of the object
print(TranscribeUtteranceRecord.to_json())

# convert the object into a dict
transcribe_utterance_record_dict = transcribe_utterance_record_instance.to_dict()
# create an instance of TranscribeUtteranceRecord from a dict
transcribe_utterance_record_from_dict = TranscribeUtteranceRecord.from_dict(transcribe_utterance_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


