# CreateConferenceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A description for this Conference. Maximum 64 characters. | [optional] 
**play_beep** | **str** | Controls when a beep is played. Valid values: &#x60;always&#x60;, &#x60;never&#x60;, &#x60;entryOnly&#x60;, &#x60;exitOnly&#x60;. | [optional]  if omitted the server will use the default value of "always"
**record** | **bool** | Setting to &#x60;true&#x60; records the entire Conference. | [optional] 
**wait_url** | **str** | If specified, a URL for the audio file that provides custom hold music for the Conference when it is in the populated state. Otherwise, FreeClimb uses a system default audio file. This is always fetched using HTTP GET and is fetched just once &amp;mdash; when the Conference is created. | [optional] 
**status_callback_url** | **str** | This URL is invoked when the status of the Conference changes. For more information, see **statusCallbackUrl** (below). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


