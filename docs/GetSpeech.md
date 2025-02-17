# GetSpeech

The `GetSpeech` command enables the Caller to respond to the application using a supported language. Unlike DTMF entry, which implicitly restricts the user to using the available buttons on the phone key pad, speech input allows for flexible audio inputs based on grammar. FreeClimb supports grammars written using GRXML compatible with the Microsoft Speech Platform. `GetSpeech` is only supported on a single call leg. It is not supported when there are two or more call legs connected (as in within a Conference).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** | When the caller has finished speaking or the command has timed out, FreeClimb will make a POST request to this URL. A PerCL response is expected to continue handling the call. | 
**grammar_type** | [**GrammarType**](GrammarType.md) |  | [optional] 
**grammar_file** | **str** | The grammar file to use for speech recognition. If grammarType is set to URL, this attribute is specified as a download URL. | 
**grammar_rule** | **str** | The grammar rule within the specified grammar file to use for speech recognition. This attribute is optional if &#x60;grammarType&#x60; is &#x60;URL&#x60; and ignored if &#x60;grammarType&#x60; is &#x60;BUILTIN&#x60;. | [optional] 
**play_beep** | **bool** | Indicates whether a beep should be played just before speech recognition is initiated so that the speaker can start to speak. | [optional] 
**prompts** | [**List[PerclCommand]**](PerclCommand.md) | The JSON array of PerCL commands to nest within the &#x60;GetSpeech&#x60; command. The &#x60;Say&#x60;, &#x60;Play&#x60;, and &#x60;Pause&#x60; commands can be used. The nested actions are executed while FreeClimb is waiting for input from the caller. This allows for playing menu options to the caller and to prompt for the expected input. These commands stop executing when the caller begins to input speech. | [optional] 
**no_input_timeout_ms** | **int** | When recognition is started and there is no speech detected for &#x60;noInputTimeoutMs&#x60; milliseconds, the recognizer will terminate the recognition operation. | [optional] 
**recognition_timeout_ms** | **int** | When playback of prompts ends and there is no match for &#x60;recognitionTimeoutMs&#x60; milliseconds, the recognizer will terminate the recognition operation. | [optional] 
**confidence_threshold** | **float** | When a recognition resource recognizes a spoken phrase, it associates a confidence level with that match. Parameter &#x60;confidenceThreshold&#x60; specifies what confidence level is considered a successful match. Values are between 0.0 and 1.0. | [optional] 
**sensitivity_level** | **float** | The speech recognizer supports a variable level of sound sensitivity. The sensitivityLevel attribute allows for filtering out background noise, so it is not mistaken for speech. Values are between 0.0 and 1.0  | [optional] 
**speech_complete_timeout_ms** | **int** | Parameter &#x60;speechCompleteTimeoutMs&#x60; specifies the length of silence required following user speech before the speech recognizer finalizes a result. This timeout applies when the recognizer currently has a complete match against an active grammar. Reasonable speech complete timeout values are typically in the range of 0.3 seconds to 1.0 seconds. | [optional] 
**speech_incomplete_timeout_ms** | **int** | Parameter &#x60;speechIncompleteTimeoutMs&#x60; specifies the length of silence following user speech after which a recognizer finalizes a result. This timeout applies when the speech prior to the silence is an incomplete match of all active grammars. Timeout &#x60;speechIncompleteTimeoutMs&#x60; is usually longer than &#x60;speechCompleteTimeoutMs&#x60; to allow users to pause mid-utterance. | [optional] 
**privacy_mode** | **bool** | Parameter privacyMode will not log the &#x60;text&#x60; as required by PCI compliance. | [optional] 

## Example

```python
from freeclimb.models.get_speech import GetSpeech

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpeech from a JSON string
get_speech_instance = GetSpeech.from_json(json)
# print the JSON string representation of the object
print(GetSpeech.to_json())

# convert the object into a dict
get_speech_dict = get_speech_instance.to_dict()
# create an instance of GetSpeech from a dict
get_speech_from_dict = GetSpeech.from_dict(get_speech_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


