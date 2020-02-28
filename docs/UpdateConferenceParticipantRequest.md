# UpdateConferenceParticipantRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**talk** | **bool** | (Optional) Default is &#x60;true&#x60;. Setting to &#x60;false&#x60; mutes the Participant. FreeClimb returns an error and ignores any other value. | [optional] 
**listen** | **bool** | (Optional) Default is &#x60;true&#x60;. Setting to &#x60;false&#x60; silences the Conference for this Participant. FreeClimb returns an error and ignores any other value. | [optional] 
**request_id** | **str** | ID of this request starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request include this requestId. If this value is not provided, FreeClimb generates a requestId and returns it as a header in the response (e.g., X-Pulse-Request-Id: &lt;requestId&gt;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


