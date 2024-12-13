# CreateWebRTCToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | E.164 formatted phone number to which calls using this token will be made. | 
**var_from** | **str** | E.164 formatted phone number owned by the reqeusting account from which calls using this token will be made. | 
**uses** | **int** | number of times this token may be used for a WebRTC call | 

## Example

```python
from freeclimb.models.create_web_rtc_token import CreateWebRTCToken

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebRTCToken from a JSON string
create_web_rtc_token_instance = CreateWebRTCToken.from_json(json)
# print the JSON string representation of the object
print(CreateWebRTCToken.to_json())

# convert the object into a dict
create_web_rtc_token_dict = create_web_rtc_token_instance.to_dict()
# create an instance of CreateWebRTCToken from a dict
create_web_rtc_token_from_dict = CreateWebRTCToken.from_dict(create_web_rtc_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


