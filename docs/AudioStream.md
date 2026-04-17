# AudioStream

The `AudioStream` command transfers control of the call to a gRPC session.  Upon completion of the gRPC session, if the actionUrl is specified, control can be returned to percl usage or the call will simply be hung up if the actionUrl is not specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The gRPC server location that will receive the grpc stream as a uri and must be port 80 or 443. | 
**action_url** | **str** | A request is made to this URL when the gRPC session is concluded. The PerCL script returned in response to the actionUrl will be executed on the call. | [optional] 
**content_type** | **str** | The type and sample rate of the audio being received over the channel must match the environmental sample rate. | [optional] 
**meta_data** | **List[str]** | An arbitrary array of strings passed through FC to the GRPC server can be used to pass state or other information about the call. | [optional] 
**privacy_mode** | **bool** | Enables audio redaction with full call recording while gRPC session is running and blocks logging of any DTMFs received by FreeClimb. | [optional] 

## Example

```python
from freeclimb.models.audio_stream import AudioStream

# TODO update the JSON string below
json = "{}"
# create an instance of AudioStream from a JSON string
audio_stream_instance = AudioStream.from_json(json)
# print the JSON string representation of the object
print(AudioStream.to_json())

# convert the object into a dict
audio_stream_dict = audio_stream_instance.to_dict()
# create an instance of AudioStream from a dict
audio_stream_from_dict = AudioStream.from_dict(audio_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


