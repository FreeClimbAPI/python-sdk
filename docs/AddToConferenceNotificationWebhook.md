# AddToConferenceNotificationWebhook

A Call has been bridged to a Conference and the AddToConference command’s notificationUrl is being invoked. This is a notification only; any PerCL returned will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | **str** | Context or reason why this request is being made. Will be addToConferenceNotification - A Call has been bridged to a conference and the addToConference command’s notificationUrl is being invoked. | [optional] 
**call_id** | **str** | Unique ID for this Call, generated by FreeClimb. | [optional] 
**account_id** | **str** | Account ID associated with your account. | [optional] 
**var_from** | **str** | Phone number of the party that initiated the Call (in E.164 format). | [optional] 
**to** | **str** | Phone number provisioned to you and to which this Call is directed (in E.164 format). | [optional] 
**call_status** | [**CallStatus**](CallStatus.md) |  | [optional] 
**direction** | [**CallDirection**](CallDirection.md) |  | [optional] 
**conference_id** | **str** | Unique ID of the Conference. | [optional] 
**queue_id** | **str** | This is only populated if the request pertains to a Queue. Otherwise, it is set to null. | [optional] 
**status** | [**ConferenceStatus**](ConferenceStatus.md) |  | [optional] 
**recording_url** | **str** | URL of the Conference’s recorded audio. Populated only if a Recording exists and the Conference was emptied. | [optional] 
**recording_id** | **str** | Unique ID of the Recording from this Conference. Populated only if a recording exists and the Conference was emptied. | [optional] 
**recording_duration_sec** | **int** | Duration of the recorded audio (in seconds), rounded up to the nearest second. Populated only if a Recording exists and the Conference was emptied. | [optional] 

## Example

```python
from freeclimb.models.add_to_conference_notification_webhook import AddToConferenceNotificationWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of AddToConferenceNotificationWebhook from a JSON string
add_to_conference_notification_webhook_instance = AddToConferenceNotificationWebhook.from_json(json)
# print the JSON string representation of the object
print(AddToConferenceNotificationWebhook.to_json())

# convert the object into a dict
add_to_conference_notification_webhook_dict = add_to_conference_notification_webhook_instance.to_dict()
# create an instance of AddToConferenceNotificationWebhook from a dict
add_to_conference_notification_webhook_from_dict = AddToConferenceNotificationWebhook.from_dict(add_to_conference_notification_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

