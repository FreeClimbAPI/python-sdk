# CallResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**call_id** | **str, none_type** | String that uniquely identifies this Call resource. | [optional] 
**parent_call_id** | **str, none_type** | ID of the Call that created this leg (child Call). | [optional] 
**account_id** | **str, none_type** | ID of the account that owns this Call. | [optional] 
**_from** | **str, none_type** | Phone number that initiated this Call. | [optional] 
**to** | **str, none_type** | Phone number that received this Call. | [optional] 
**phone_number_id** | **str, none_type** | If the Call was inbound, this is the ID of the IncomingPhoneNumber that received the Call (DNIS). If the Call was outbound, this is the ID of the phone number from which the Call was placed (ANI). | [optional] 
**status** | [**CallStatus**](CallStatus.md) |  | [optional] 
**start_time** | **str, none_type** | Start time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed. | [optional] 
**connect_time** | **str, none_type** | Time the Call was answered (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed. | [optional] 
**end_time** | **str, none_type** | End time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call did not complete successfully. | [optional] 
**duration** | **int, none_type** | Total length of the Call in seconds. Measures time between startTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls. | [optional] 
**connect_duration** | **int, none_type** | Length of time that the Call was connected in seconds. Measures time between connectTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls. | [optional] 
**direction** | [**CallDirection**](CallDirection.md) |  | [optional] 
**answered_by** | [**AnsweredBy**](AnsweredBy.md) |  | [optional] 
**subresource_uris** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The list of subresources for this Call. These include things like logs and recordings associated with the Call. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


