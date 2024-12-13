# RecordUtterance

The `RecordUtterance` command records the caller's voice and returns the URL of a file containing the audio recording. `RecordUtterance` is blocking and is a terminal command. As such, the `actionUrl` property is required, and control of the Call picks up using the PerCL returned in response to the `actionUrl`. Recording information is returned in the `actionUrl` request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** | URL to which information on the completed recording is submitted. The PerCL received in response is then used to continue with Call processing. | 
**silence_timeout_ms** | **int** | Interval of silence that should elapse before ending the recording. | [optional] 
**finish_on_key** | **str** | Key that triggers the end of the recording. any digit, &#39;#&#39;, or &#39;*&#39; | [optional] 
**max_length_sec** | **int** | Maximum length for the command execution in seconds. | [optional] 
**play_beep** | **bool** | Indicates whether to play a beep sound before the start of the recording. If set to &#x60;false&#x60;, no beep is played. | [optional] 
**auto_start** | **bool** | If &#x60;false&#x60;, recording begins immediately after the RecordUtterance command is processed. If &#x60;true&#x60;, recording begins when audio is present and if audio begins before the &#x60;maxLengthSec&#x60; timeout. If no audio begins before &#x60;maxLengthSec&#x60;, no recording is generated. | [optional] 
**privacy_mode** | **bool** | Parameter &#x60;privacyMode&#x60; will not log the &#x60;text&#x60; as required by PCI compliance. | [optional] 

## Example

```python
from freeclimb.models.record_utterance import RecordUtterance

# TODO update the JSON string below
json = "{}"
# create an instance of RecordUtterance from a JSON string
record_utterance_instance = RecordUtterance.from_json(json)
# print the JSON string representation of the object
print(RecordUtterance.to_json())

# convert the object into a dict
record_utterance_dict = record_utterance_instance.to_dict()
# create an instance of RecordUtterance from a dict
record_utterance_from_dict = RecordUtterance.from_dict(record_utterance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


