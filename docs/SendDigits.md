# SendDigits

The `SendDigits` command plays DTMF tones on a live Call. This is useful for navigating through IVR menus or dialing extensions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digits** | **str** | String containing the digits to be played. The string cannot be empty and can include any digit, plus &#x60;#&#x60;, or &#x60;*&#x60;, and allows embedding specification for delay or pause between the output of individual digits. | 
**pause_ms** | **int** | Pause between digits in milliseconds. Valid values are 100-1000 milliseconds and will be adjusted by FreeClimb to satisfy the constraint. | [optional] 
**privacy_mode** | **bool** | Parameter &#x60;privacyMode&#x60; will not log the &#x60;text&#x60; as required by PCI compliance. | [optional] 

## Example

```python
from freeclimb.models.send_digits import SendDigits

# TODO update the JSON string below
json = "{}"
# create an instance of SendDigits from a JSON string
send_digits_instance = SendDigits.from_json(json)
# print the JSON string representation of the object
print(SendDigits.to_json())

# convert the object into a dict
send_digits_dict = send_digits_instance.to_dict()
# create an instance of SendDigits from a dict
send_digits_from_dict = SendDigits.from_dict(send_digits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


