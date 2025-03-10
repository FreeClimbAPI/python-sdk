# AddToConference

The `AddToConference` command adds a Participant to a Conference. Two Call legs can be bridged together by creating a Conference and adding both Call legs to it via `AddToConference`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_call_control** | **bool** | If &#x60;true&#x60;, Call control will be enabled for this Participant&#39;s Call leg. | [optional] 
**call_control_sequence** | **str** | Defines a sequence of digits that, when entered by this caller, invokes the &#x60;callControlUrl&#x60;. Only digits plus &#39;*&#39;, and &#39;#&#39; may be used. | [optional] 
**call_control_url** | **str** | URL to be invoked when this Participant enters the digit sequence defined in the &#x60;callControlSequence&#x60; attribute. | [optional] 
**conference_id** | **str** | ID of the Conference to which to add the Participant (Call leg). Conference must exist or an error will result. | 
**leave_conference_url** | **str** | URL to be invoked when the Participant leaves the Conference.  | [optional] 
**listen** | **bool** | If &#x60;true&#x60;, the Participant joins the Conference with listen privileges. This may be modified later via the REST API or &#x60;SetListen&#x60; PerCL command. | [optional] 
**notification_url** | **str** | When the Participant enters the Conference, this URL will be invoked using an HTTP POST request with the standard request parameters. | [optional] 
**start_conf_on_enter** | **bool** | Flag that indicates whether a Conference starts upon entry of this particular Participant. This is usually set to &#x60;true&#x60; for moderators and &#x60;false&#x60; for all other Participants. | [optional] 
**talk** | **bool** | If &#x60;true&#x60;, the Participant joins the Conference with talk privileges. This may be modified later via the REST API or &#x60;SetTalk&#x60; PerCL command.  | [optional] 
**dtmf_pass_through** | **bool** | If &#x60;true&#x60;, the Participant joins the Conference with dtmfPassThrough privileges. This may be modified later via the REST API or &#x60;SetDTMFPassThrough&#x60; PerCL command.  | [optional] 

## Example

```python
from freeclimb.models.add_to_conference import AddToConference

# TODO update the JSON string below
json = "{}"
# create an instance of AddToConference from a JSON string
add_to_conference_instance = AddToConference.from_json(json)
# print the JSON string representation of the object
print(AddToConference.to_json())

# convert the object into a dict
add_to_conference_dict = add_to_conference_instance.to_dict()
# create an instance of AddToConference from a dict
add_to_conference_from_dict = AddToConference.from_dict(add_to_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


