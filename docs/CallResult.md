# CallResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**call_id** | **str** | String that uniquely identifies this Call resource. | [optional] 
**parent_call_id** | **str** | ID of the Call that created this leg (child Call). | [optional] 
**account_id** | **str** | ID of the account that owns this Call. | [optional] 
**var_from** | **str** | Phone number that initiated this Call. | [optional] 
**to** | **str** | Phone number that received this Call. | [optional] 
**phone_number_id** | **str** | If the Call was inbound, this is the ID of the IncomingPhoneNumber that received the Call (DNIS). If the Call was outbound, this is the ID of the phone number from which the Call was placed (ANI). | [optional] 
**status** | [**CallStatus**](CallStatus.md) |  | [optional] 
**start_time** | **str** | Start time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed. | [optional] 
**connect_time** | **str** | Time the Call was answered (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call has not yet been dialed. | [optional] 
**end_time** | **str** | End time of the Call (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). Empty if the Call did not complete successfully. | [optional] 
**duration** | **int** | Total length of the Call in seconds. Measures time between startTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls. | [optional] 
**connect_duration** | **int** | Length of time that the Call was connected in seconds. Measures time between connectTime and endTime. This value is empty for busy, failed, unanswered or ongoing Calls. | [optional] 
**direction** | [**CallDirection**](CallDirection.md) |  | [optional] 
**answered_by** | [**AnsweredBy**](AnsweredBy.md) |  | [optional] 
**subresource_uris** | **object** | The list of subresources for this Call. These include things like logs and recordings associated with the Call. | [optional] 
**application_id** | **str** | ApplicationId associated with the Call. | [optional] 

## Example

```python
from freeclimb.models.call_result import CallResult

# TODO update the JSON string below
json = "{}"
# create an instance of CallResult from a JSON string
call_result_instance = CallResult.from_json(json)
# print the JSON string representation of the object
print(CallResult.to_json())

# convert the object into a dict
call_result_dict = call_result_instance.to_dict()
# create an instance of CallResult from a dict
call_result_from_dict = CallResult.from_dict(call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


