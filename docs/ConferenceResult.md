# ConferenceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**conference_id** | **str** | A string that uniquely identifies this Conference resource. | [optional] 
**account_id** | **str** | ID of the account that created this Conference. | [optional] 
**alias** | **str** | A description for this Conference. | [optional] 
**play_beep** | [**PlayBeep**](PlayBeep.md) |  | [optional] 
**record** | **bool** | Flag indicating whether recording is enabled for this Conference. | [optional] 
**status** | [**ConferenceStatus**](ConferenceStatus.md) |  | [optional] 
**wait_url** | **str** | URL referencing the audio file to be used as default wait music for the Conference when it is in the populated state. | [optional] 
**action_url** | **str** | URL invoked once the Conference is successfully created. | [optional] 
**status_callback_url** | **str** | URL to inform that the Conference status has changed. | [optional] 
**subresource_uris** | **object** | The list of subresources for this Conference. This includes participants and/or recordings. | [optional] 

## Example

```python
from freeclimb.models.conference_result import ConferenceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceResult from a JSON string
conference_result_instance = ConferenceResult.from_json(json)
# print the JSON string representation of the object
print(ConferenceResult.to_json())

# convert the object into a dict
conference_result_dict = conference_result_instance.to_dict()
# create an instance of ConferenceResult from a dict
conference_result_from_dict = ConferenceResult.from_dict(conference_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


