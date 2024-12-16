# ConferenceParticipantResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**account_id** | **str, none_type** | ID of the account that created this participant. | [optional] 
**conference_id** | **str, none_type** | ID of the conference this participant is in. | [optional] 
**call_id** | **str, none_type** | ID of the Call associated with this Participant. | [optional] 
**talk** | **bool, none_type** | True if this Participant has talk privileges in the Conference. False otherwise. | [optional] 
**listen** | **bool, none_type** | True if this Participant has listen privileges in the Conference. False otherwise. | [optional] 
**dtmf_pass_through** | **bool, none_type** | True if this Participant had dtmfPassThrough privileges in the Conference. False otherwise. | [optional] 
**start_conf_on_enter** | **bool, none_type** | True if this Participant joining the Conference caused the Conference to start (status &#x3D; inProgress). False otherwise. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


