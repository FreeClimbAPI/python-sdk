# MessageResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**account_id** | **str, none_type** | String that uniquely identifies this account resource. | [optional] 
**message_id** | **str, none_type** | String that uniquely identifies this message resource | [optional] 
**status** | [**MessageStatus**](MessageStatus.md) |  | [optional] 
**_from** | **str, none_type** | Phone number in E.164 format that sent the message. | [optional] 
**to** | **str, none_type** | Phone number in E.164 format that received the message. | [optional] 
**text** | **str, none_type** | Message contents | [optional] 
**direction** | **str, none_type** | Noting whether the message was inbound or outbound | [optional] 
**notification_url** | **str, none_type** | URL invoked when message sent | [optional] 
**brand_id** | **str, none_type** | The unique identifier for the brand associated with the message | [optional] 
**campaign_id** | **str, none_type** | The unique identifier for the campaign associated with the message | [optional] 
**segment_count** | **float, none_type** | The number of segments into which the message was split | [optional] 
**media_urls** | **[str], none_type** | an array of HTTP URLs which were attached this this message | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


