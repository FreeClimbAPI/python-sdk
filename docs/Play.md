# Play

The `Play` command plays an audio file back to the caller. The audio file may be located at any location accessible via a URL. `Play` can exist as a stand-alone command or as a nested command. It does not allow barge-in unless nested within a `GetSpeech` command. The file will always be played to completion unless nested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | RL of the audio file to be played to the caller. The URL can be the &#x60;recordingUrl&#x60; generated from the &#x60;RecordUtterance&#x60; or &#x60;StartRecordCall&#x60; PerCL commands.  | 
**loop** | **int** | Number of times the audio file is played. Specifying &#39;0&#39; causes the Play action to loop until the Call is hung up. | [optional] 
**privacy_mode** | **bool** | Parameter &#x60;privacyMode&#x60; will not log the &#x60;text&#x60; as required by PCI compliance. | [optional] 

## Example

```python
from freeclimb.models.play import Play

# TODO update the JSON string below
json = "{}"
# create an instance of Play from a JSON string
play_instance = Play.from_json(json)
# print the JSON string representation of the object
print(Play.to_json())

# convert the object into a dict
play_dict = play_instance.to_dict()
# create an instance of Play from a dict
play_from_dict = Play.from_dict(play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


