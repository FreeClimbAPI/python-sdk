# IncomingNumberResultAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** | String that uniquely identifies this phone number resource. | [optional] 
**account_id** | **str** | ID of the account that owns this phone number. | [optional] 
**application_id** | **str** | ID of the Application that FreeClimb should contact if a Call or SMS arrives for this phone number or a Call from this number is placed. An incoming phone number is not useful until associated with an applicationId. | [optional] 
**phone_number** | **str** | Phone number in E.164 format. | [optional] 
**alias** | **str** | Description for this phone number. Typically the conventionally-formatted version of the phone number. | [optional] 
**region** | **str** | State or province of this phone number. | [optional] 
**country** | **str** | Country of this phone number. | [optional] 
**voice_enabled** | **bool** | Indicates whether the phone number can handle Calls. Typically set to true for all numbers. | [optional] 
**sms_enabled** | **bool** | Indication of whether the phone number can handle sending and receiving SMS messages. Typically set to true for all numbers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


