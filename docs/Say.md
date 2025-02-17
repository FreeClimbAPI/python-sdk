# Say

The `Say` command provides Text-To-Speech (TTS) support. It converts text to speech and then renders it in a female voice back to the caller. `Say` is useful in cases where it's difficult to pre-record a prompt for any reason. `Say` does not allow barge-in unless nested within a `GetSpeech` command. The file will always be played to completion unless nested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The message to be played to the caller using TTS. The size of the string is limited to 4 KB (or 4,096 bytes). An empty string will cause the command to be skipped. | 
**language** | **str** | Language and (by implication) the locale to use. This implies the accent and pronunciations to be usde for the TTS. The complete list of valid values for the language attribute is shown below. | [optional] 
**loop** | **int** | Number of times the text is said. Specifying &#39;0&#39; causes the &#x60;Say&#x60; action to loop until the Call is hung up. | [optional] [default to 1]
**privacy_mode** | **bool** | Parameter &#x60;privacyMode&#x60; will not log the &#x60;text&#x60; as required by PCI compliance. | [optional] 

## Example

```python
from freeclimb.models.say import Say

# TODO update the JSON string below
json = "{}"
# create an instance of Say from a JSON string
say_instance = Say.from_json(json)
# print the JSON string representation of the object
print(Say.to_json())

# convert the object into a dict
say_dict = say_instance.to_dict()
# create an instance of Say from a dict
say_from_dict = Say.from_dict(say_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


