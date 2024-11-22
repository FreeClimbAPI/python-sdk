# PlayEarlyMedia

`PlayEarlyMedia` is relevant only when present as the very first command in the PerCL script returned for an incoming Call. In such cases, the command is executed before FreeClimb attempts to connect the call. The audio file it uses can be stored in any location that is accessible via URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | RL of the audio file to be played to the caller. The URL can be the &#x60;recordingUrl&#x60; generated from the &#x60;RecordUtterance&#x60; or &#x60;StartRecordCall&#x60; PerCL commands or any accessible URL. FreeClimb will respect Cache-Control headers for this file. Use these to limit repeated requests for unchanged audio. If no Cache-Control header is provided, the file will be cached for seven days by default. | 

## Example

```python
from freeclimb.models.play_early_media import PlayEarlyMedia

# TODO update the JSON string below
json = "{}"
# create an instance of PlayEarlyMedia from a JSON string
play_early_media_instance = PlayEarlyMedia.from_json(json)
# print the JSON string representation of the object
print(PlayEarlyMedia.to_json())

# convert the object into a dict
play_early_media_dict = play_early_media_instance.to_dict()
# create an instance of PlayEarlyMedia from a dict
play_early_media_from_dict = PlayEarlyMedia.from_dict(play_early_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


