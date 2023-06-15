# SMSTenDLCCampaign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** | Alphanumeric identifier assigned by the registry for a campaign. This identifier is required by the NetNumber OSR SMS enabling process of 10DLC. | 
**csp_id** | **str** | Alphanumeric identifier of the CSP associated with this campaign. | 
**brand_id** | **str** | Alphanumeric identifier of the brand associated with this campaign. | 
**usecase** | **str** | Campaign usecase. Must be of defined valid types. Use &#x60;/registry/enum/usecase&#x60; operation to retrieve usecases available for given brand. | 
**sub_usecases** | **[str]** | Campaign sub-usecases. Must be of defined valid sub-usecase types. Use &#x60;/registry/enum/usecase&#x60; operation to retrieve list of valid sub-usecases | 
**description** | **str** | Summary description of this campaign. | 
**mock** | **bool** | Campaign created from mock brand. Mocked campaign cannot be shared with an upstream CNP. | 
**account_id** | **str, none_type** | ID of the account that created this Queue. | [optional] 
**reseller_id** | **str, none_type** | Alphanumeric identifier of the reseller that you want to associate with this campaign. | [optional] 
**status** | **str** | Current campaign status. Possible values: ACTIVE, EXPIRED. A newly created campaign defaults to ACTIVE status.  | [optional] 
**create_date** | **datetime** | Unix timestamp when campaign was created. | [optional] 
**auto_renewal** | **bool** | Campaign subscription auto-renewal status. | [optional] 
**billed_date** | **datetime, none_type** | Campaign recent billed date. | [optional] 
**embedded_link** | **bool** | Does message generated by the campaign include URL link in SMS? | [optional]  if omitted the server will use the default value of False
**embedded_phone** | **bool** | Does message generated by the campaign include phone number in SMS? | [optional]  if omitted the server will use the default value of False
**affiliate_marketing** | **bool** | Does message content controlled by affiliate marketing other than the brand? | [optional] 
**number_pool** | **bool** | Does campaign utilize pool of phone nubers? | [optional]  if omitted the server will use the default value of False
**age_gated** | **bool** | Age gated content in campaign. | [optional] 
**direct_lending** | **bool** |  | [optional] 
**subscriber_optin** | **bool** | Does campaign require subscriber to opt-in before SMS is sent to subscriber? | [optional]  if omitted the server will use the default value of False
**subscriber_optout** | **bool** | Does campaign support subscriber opt-out keyword(s)? | [optional]  if omitted the server will use the default value of False
**subscriber_help** | **bool** | Does campaign responds to help keyword(s)? | [optional]  if omitted the server will use the default value of False
**sample1** | **str** | Message sample. Some campaign tiers require 1 or more message samples. | [optional] 
**sample2** | **str, none_type** | Message sample. Some campaign tiers require 2 or more message samples. | [optional] 
**sample3** | **str, none_type** | Message sample. Some campaign tiers require 3 or more message samples. | [optional] 
**sample4** | **str, none_type** | Message sample. Some campaign tiers require 4 or more message samples. | [optional] 
**sample5** | **str, none_type** | Message sample. Some campaign tiers require 5 or more message samples. | [optional] 
**message_flow** | **str, none_type** | Message flow description. | [optional] 
**help_message** | **str, none_type** | Help message of the campaign. | [optional] 
**reference_id** | **str, none_type** | Caller supplied campaign reference ID. If supplied, the value must be unique across all submitted campaigns. Can be used to prevent duplicate campaign registrations. | [optional] 
**next_renewal_or_expiration_date** | **date, none_type** | When the campaign would be due for its next renew/bill date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

