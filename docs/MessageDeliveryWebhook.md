# MessageDeliveryWebhook

An SMS has been received by the platform and is being delivered to the smsUrl of the customer application that is associated with the destination number. A PerCL response will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Value will be messageDelivery - An SMS message has been received by the platform and is being delivered to the customer application associated with the destination number. | [optional] 
**account_id** | **str** | Account ID associated with your account. | [optional] 
**var_from** | **str** | Phone number of the party that initiated the Call (in E.164 format). | [optional] 
**to** | **str** | Phone number provisioned to you and to which this Call is directed (in E.164 format). | [optional] 
**text** | **str** | Body of the SMS message. | [optional] 
**direction** | **str** | Value will be inbound to indicate the receipt of a message into the FreeClimb platform. | [optional] 
**application_id** | **str** | ID of the application to which the destination number is assigned. | [optional] 
**status** | **str** | Value will be received to indicate that the platform has successfully received the incoming message. | [optional] 
**phone_number_id** | **str** | ID of the destination phone number. | [optional] 
**uri** | **str** | The URI for this resource, relative to the API base URL | [optional] 

## Example

```python
from freeclimb.models.message_delivery_webhook import MessageDeliveryWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of MessageDeliveryWebhook from a JSON string
message_delivery_webhook_instance = MessageDeliveryWebhook.from_json(json)
# print the JSON string representation of the object
print(MessageDeliveryWebhook.to_json())

# convert the object into a dict
message_delivery_webhook_dict = message_delivery_webhook_instance.to_dict()
# create an instance of MessageDeliveryWebhook from a dict
message_delivery_webhook_from_dict = MessageDeliveryWebhook.from_dict(message_delivery_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


