# TranscribeUtterance

The `TranscribeUtterance` command transcribes the caller’s voice and returns transcription of the audio and optionally returns the recording of the audio transcribed.  `TranscribeUtterance` is blocking and is a terminal command. As such, the actionUrl property is required, and control of the Call picks up using the `PerCL` returned in response of the `actionUrl`. Recording and Transcription information is returned in the actionUrl request. If the reason this command ended was due to the call hanging up, any PerCL returned will not execute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** |  | 
**play_beep** | **bool** |  | [optional] [default to False]
**record** | [**TranscribeUtteranceRecord**](TranscribeUtteranceRecord.md) |  | [optional] 
**privacy_for_logging** | **bool** |  | [optional] [default to False]
**privacy_for_recording** | **bool** |  | [optional] [default to False]
**prompts** | [**List[PerclCommand]**](PerclCommand.md) |  | [optional] 

## Example

```python
from freeclimb.models.transcribe_utterance import TranscribeUtterance

# TODO update the JSON string below
json = "{}"
# create an instance of TranscribeUtterance from a JSON string
transcribe_utterance_instance = TranscribeUtterance.from_json(json)
# print the JSON string representation of the object
print(TranscribeUtterance.to_json())

# convert the object into a dict
transcribe_utterance_dict = transcribe_utterance_instance.to_dict()
# create an instance of TranscribeUtterance from a dict
transcribe_utterance_from_dict = TranscribeUtterance.from_dict(transcribe_utterance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


