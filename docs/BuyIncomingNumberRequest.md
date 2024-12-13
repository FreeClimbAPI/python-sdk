# BuyIncomingNumberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number to purchase in E.164 format (as returned in the list of Available Phone Numbers). | 
**alias** | **str** | Description for this new incoming phone number (max 64 characters). | [optional] 
**application_id** | **str** | ID of the application that should handle phone calls to the number. | [optional] 

## Example

```python
from freeclimb.models.buy_incoming_number_request import BuyIncomingNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyIncomingNumberRequest from a JSON string
buy_incoming_number_request_instance = BuyIncomingNumberRequest.from_json(json)
# print the JSON string representation of the object
print(BuyIncomingNumberRequest.to_json())

# convert the object into a dict
buy_incoming_number_request_dict = buy_incoming_number_request_instance.to_dict()
# create an instance of BuyIncomingNumberRequest from a dict
buy_incoming_number_request_from_dict = BuyIncomingNumberRequest.from_dict(buy_incoming_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


