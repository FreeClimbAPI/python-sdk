# GetDigits

The `GetDigits` command collects DTMF inputs from the caller. It is only supported only when there is a single party on the Call. `GetDigits` is a Terminal Command — any actions following it are never executed. When the Caller is done entering the digits, FreeClimb submits that data to the provided `actionUrl` using an HTTP POST request. Your server will be required to respond to the FreeClimb Webhook with PerCL to continue handling the call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** | When the Caller has finished entering digits, FreeClimb will make an HTTP POST request to this URL. A PerCL response is expected to continue handling the Call. Make sure to keep “http://“ in the URL. | 
**digit_timeout_ms** | **int** |  Maximum time in milliseconds that FreeClimb will wait for the Caller to press any digit after the last digit entered, before making a determination that a &#x60;timeout&#x60; has occurred and moving on to make the request to the actionUrl to submit the results of the &#x60;GetDigits&#x60; command. This timeout interval begins and resets after each digit entered. | [optional] 
**finish_on_key** | **str** | Digit that causes the input sequence to be deemed complete. This attribute defers to the &#x60;timeout&#x60; attribute – so, if a &#x60;timeout&#x60; occurs, then the command terminates regardless of the value of &#x60;finishOnKey&#x60;. | [optional] 
**flush_buffer** | **bool** | If set to true, the FreeClimb platform starts with an empty DTMF buffer to store the digits entered by the caller. If set to false, FreeClimb will append the user inputs to the end of the existing digits buffer and will return digits from the start of the digits buffer. | [optional] 
**initial_timeout_ms** | **int** | Maximum time in milliseconds that FreeClimb will wait for the Caller to press the first digit before making a determination that a &#x60;timeout&#x60; has occurred and moving on to make the request to the &#x60;actionUrl&#x60; to submit the results of the &#x60;GetDigits&#x60; command. This timeout interval begins when all nested commands have been fully executed. | [optional] 
**max_digits** | **int** | Maximum number of digits expected in the input. If the terminating digit is not entered and the caller has entered the maximum number of digits allowed, the &#x60;GetDigits&#x60; command terminates regardless of the value of &#x60;finishOnKey&#x60;. | [optional] 
**min_digits** | **int** | Minimum number of digits expected in the input. If specified, FreeClimb will return the collected digits only if the Caller has entered at least that many digits. | [optional] 
**prompts** | [**List[PerclCommand]**](PerclCommand.md) | JSON array of PerCL commands to nest within the &#x60;GetDigits&#x60; command. The &#x60;Say&#x60;, &#x60;Play&#x60;, and &#x60;Pause&#x60; commands can be used. The nested actions are executed while FreeClimb is waiting for input from the Caller. | [optional] 
**privacy_mode** | **bool** | Parameter &#x60;privacyMode&#x60; will not log the &#x60;text&#x60; as required by PCI compliance. | [optional] 

## Example

```python
from freeclimb.models.get_digits import GetDigits

# TODO update the JSON string below
json = "{}"
# create an instance of GetDigits from a JSON string
get_digits_instance = GetDigits.from_json(json)
# print the JSON string representation of the object
print(GetDigits.to_json())

# convert the object into a dict
get_digits_dict = get_digits_instance.to_dict()
# create an instance of GetDigits from a dict
get_digits_from_dict = GetDigits.from_dict(get_digits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


