# Sms

The `Sms` command can be used to send an SMS message to a phone number during a phone call. International SMS is disabled by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | E.164 representation of the phone number to which the message will be sent. Must be within FreeClimb&#39;s service area and E.164 formatting (e.g., +18003608245). | 
**var_from** | **str** | E.164 representation of the phone number to use as the sender. This must be an incoming phone number you have purchased from FreeClimb. | 
**text** | **str** | Text contained in the message (maximum 160 characters). | 
**notification_url** | **str** | When the message changes status, this URL will be invoked using HTTP POST with the messageStatus parameters. This is a notification only; any PerCL returned will be ignored. | [optional] 

## Example

```python
from freeclimb.models.sms import Sms

# TODO update the JSON string below
json = "{}"
# create an instance of Sms from a JSON string
sms_instance = Sms.from_json(json)
# print the JSON string representation of the object
print(Sms.to_json())

# convert the object into a dict
sms_dict = sms_instance.to_dict()
# create an instance of Sms from a dict
sms_from_dict = Sms.from_dict(sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


