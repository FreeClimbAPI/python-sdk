# MessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**var_from** | **str** | Phone number to use as the sender. This must be an incoming phone number that you have purchased from FreeClimb. | 
**to** | **str** | Phone number to receive the message. Must be within FreeClimb&#39;s service area. | 
**text** | **str** | Text contained in the message (maximum 160 characters).   **Note:** For text, only ASCII characters are supported. | 
**notification_url** | **str** | When the Message changes status, this URL is invoked using HTTP POST with the messageStatus parameters.  **Note:** This is a notification only; any PerCL returned is ignored. | [optional] 
**media_urls** | **List[str]** | an array of HTTP URLs which are to be used as attachments to the message. This will force the message into being an MMS message and must be done using a from number which is MMS capabile. | [optional] 

## Example

```python
from freeclimb.models.message_request import MessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageRequest from a JSON string
message_request_instance = MessageRequest.from_json(json)
# print the JSON string representation of the object
print(MessageRequest.to_json())

# convert the object into a dict
message_request_dict = message_request_instance.to_dict()
# create an instance of MessageRequest from a dict
message_request_from_dict = MessageRequest.from_dict(message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


