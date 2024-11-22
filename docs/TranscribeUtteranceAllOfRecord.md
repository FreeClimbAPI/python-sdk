# TranscribeUtteranceAllOfRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save_recording** | **bool** |  | [optional] [default to False]
**max_length_sec** | **int** |  | [optional] [default to 60]
**rcrd_termination_silence_time_ms** | **int** |  | [optional] 

## Example

```python
from freeclimb.models.transcribe_utterance_all_of_record import TranscribeUtteranceAllOfRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TranscribeUtteranceAllOfRecord from a JSON string
transcribe_utterance_all_of_record_instance = TranscribeUtteranceAllOfRecord.from_json(json)
# print the JSON string representation of the object
print(TranscribeUtteranceAllOfRecord.to_json())

# convert the object into a dict
transcribe_utterance_all_of_record_dict = transcribe_utterance_all_of_record_instance.to_dict()
# create an instance of TranscribeUtteranceAllOfRecord from a dict
transcribe_utterance_all_of_record_from_dict = TranscribeUtteranceAllOfRecord.from_dict(transcribe_utterance_all_of_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


