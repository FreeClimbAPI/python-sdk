# CreateConference

The `CreateConference` command does exactly what its name implies — it creates an unpopulated Conference (one without any Participants). Once created, a Conference remains in FreeClimb until explicitly terminated by a customer. Once a Conference has been terminated, it can no longer be used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** |  This URL is invoked once the Conference is successfully created. Actions on the Conference, such as adding Participants, can be performed via the PerCL script returned in the response.  | 
**alias** | **str** | Descriptive name for the Conference.  | [optional] 
**play_beep** | [**PlayBeep**](PlayBeep.md) |  | [optional] 
**record** | **bool** | When set to &#x60;true&#x60;, the entire Conference is recorded. The &#x60;statusCallbackUrl&#x60; of the Conference will receive a &#x60;conferenceRecordingEnded&#x60; Webhook when the Conference transitions from the &#x60;inProgress&#x60; to empty state. | [optional] 
**status_callback_url** | **str** | This URL is invoked when the status of the Conference changes or when a recording of the Conference has become available. | [optional] 
**wait_url** | **str** | If specified, this URL provides the custom hold music for the Conference when it is in the populated state. This attribute is always fetched using HTTP GET and is fetched just once – when the Conference is created. The URL must be an audio file that is reachable and readable by FreeClimb. | [optional] 
**parent_call_id** | **str** | ID of the Call that created this leg (child call). | [optional] 

## Example

```python
from freeclimb.models.create_conference import CreateConference

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConference from a JSON string
create_conference_instance = CreateConference.from_json(json)
# print the JSON string representation of the object
print(CreateConference.to_json())

# convert the object into a dict
create_conference_dict = create_conference_instance.to_dict()
# create an instance of CreateConference from a dict
create_conference_from_dict = CreateConference.from_dict(create_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


