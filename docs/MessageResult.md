# MessageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**account_id** | **str** | String that uniquely identifies this account resource. | [optional] 
**message_id** | **str** | String that uniquely identifies this message resource | [optional] 
**status** | [**MessageStatus**](MessageStatus.md) |  | [optional] 
**var_from** | **str** | Phone number in E.164 format that sent the message. | [optional] 
**to** | **str** | Phone number in E.164 format that received the message. | [optional] 
**text** | **str** | Message contents | [optional] 
**direction** | **str** | Noting whether the message was inbound or outbound | [optional] 
**notification_url** | **str** | URL invoked when message sent | [optional] 
**brand_id** | **str** | The unique identifier for the brand associated with the message | [optional] 
**campaign_id** | **str** | The unique identifier for the campaign associated with the message | [optional] 
**segment_count** | **float** | The number of segments into which the message was split | [optional] 
**media_urls** | **List[str]** | an array of HTTP URLs which were attached this this message | [optional] 
**tfn** | [**TFN**](TFN.md) |  | [optional] 
**phone_number_id** | **str** | String that uniquely identifies the phoneNumber resource used to send this Message | [optional] 
**application_id** | **str** | String that uniquely identifies the Application resource used to send this Message | [optional] 

## Example

```python
from freeclimb.models.message_result import MessageResult

# TODO update the JSON string below
json = "{}"
# create an instance of MessageResult from a JSON string
message_result_instance = MessageResult.from_json(json)
# print the JSON string representation of the object
print(MessageResult.to_json())

# convert the object into a dict
message_result_dict = message_result_instance.to_dict()
# create an instance of MessageResult from a dict
message_result_from_dict = MessageResult.from_dict(message_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


