# SMSTenDLCPartnerCampaignBrand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account that created this Queue. | [optional] 
**brand_id** | **str** | Unique identifier assigned to the brand by the registry. | [optional] [readonly] 
**first_name** | **str** | First or given name.  | [optional] 
**last_name** | **str** | Last or Surname. | [optional] 
**display_name** | **str** | Display or marketing name of the brand. | [optional] 
**company_name** | **str** | (Required for Non-profit/private/public) Legal company name. | [optional] 
**phone** | **str** | Valid phone number in e.164 international format. | 
**email** | **str** | Valid email address of brand support contact. | 
**website** | **str** | Brand website URL. | [optional] 
**optional_attributes** | **Dict[str, object]** | Optional brand attributes. Please refer to GET /enum/optionalAttributeNames for dictionary of optional attribute names. | [optional] 
**evp_vetting_score** | **int** | External vetting score. | [optional] 

## Example

```python
from freeclimb.models.sms_ten_dlc_partner_campaign_brand import SMSTenDLCPartnerCampaignBrand

# TODO update the JSON string below
json = "{}"
# create an instance of SMSTenDLCPartnerCampaignBrand from a JSON string
sms_ten_dlc_partner_campaign_brand_instance = SMSTenDLCPartnerCampaignBrand.from_json(json)
# print the JSON string representation of the object
print(SMSTenDLCPartnerCampaignBrand.to_json())

# convert the object into a dict
sms_ten_dlc_partner_campaign_brand_dict = sms_ten_dlc_partner_campaign_brand_instance.to_dict()
# create an instance of SMSTenDLCPartnerCampaignBrand from a dict
sms_ten_dlc_partner_campaign_brand_from_dict = SMSTenDLCPartnerCampaignBrand.from_dict(sms_ten_dlc_partner_campaign_brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


