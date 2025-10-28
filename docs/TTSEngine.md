# TTSEngine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**TTSEngineName**](TTSEngineName.md) |  | [optional] 
**parameters** | **Dict[str, object]** | Parameters for the TTS engine. The parameters are specific to the engine and are documented in the engine&#39;s documentation. | [optional] 

## Example

```python
from freeclimb.models.tts_engine import TTSEngine

# TODO update the JSON string below
json = "{}"
# create an instance of TTSEngine from a JSON string
tts_engine_instance = TTSEngine.from_json(json)
# print the JSON string representation of the object
print(TTSEngine.to_json())

# convert the object into a dict
tts_engine_dict = tts_engine_instance.to_dict()
# create an instance of TTSEngine from a dict
tts_engine_from_dict = TTSEngine.from_dict(tts_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


