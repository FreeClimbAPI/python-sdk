# ConferenceResultAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **str, none_type** | A string that uniquely identifies this Conference resource. | [optional] 
**account_id** | **str, none_type** | ID of the account that created this Conference. | [optional] 
**alias** | **str, none_type** | A description for this Conference. | [optional] 
**play_beep** | [**PlayBeep**](PlayBeep.md) |  | [optional] 
**record** | **bool, none_type** | Flag indicating whether recording is enabled for this Conference. | [optional] 
**status** | [**ConferenceStatus**](ConferenceStatus.md) |  | [optional] 
**wait_url** | **str, none_type** | URL referencing the audio file to be used as default wait music for the Conference when it is in the populated state. | [optional] 
**action_url** | **str, none_type** | URL invoked once the Conference is successfully created. | [optional] 
**status_callback_url** | **str, none_type** | URL to inform that the Conference status has changed. | [optional] 
**subresource_uris** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The list of subresources for this Conference. This includes participants and/or recordings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


