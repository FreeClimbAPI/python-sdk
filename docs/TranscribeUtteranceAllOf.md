# TranscribeUtteranceAllOf

The `TranscribeUtterance` command transcribes the caller’s voice and returns transcription of the audio and optionally returns the recording of the audio transcribed.  `TranscribeUtterance` is blocking and is a terminal command. As such, the actionUrl property is required, and control of the Call picks up using the `PerCL` returned in response of the `actionUrl`. Recording and Transcription information is returned in the actionUrl request. If the reason this command ended was due to the call hanging up, any PerCL returned will not execute.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** |  | 
**play_beep** | **bool** |  | [optional]  if omitted the server will use the default value of False
**record** | [**TranscribeUtteranceAllOfRecord**](TranscribeUtteranceAllOfRecord.md) |  | [optional] 
**privacy_for_logging** | **bool** |  | [optional]  if omitted the server will use the default value of False
**privacy_for_recording** | **bool** |  | [optional]  if omitted the server will use the default value of False
**prompts** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


