# SMSTollFreeCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account that created this toll-free campaign | 
**campaign_id** | **str** | Alphanumeric identifier used by the platform to identify this toll-free campaign | 
**use_case** | **str** |  | 
**registration_status** | [**SMSTollFreeCampaignRegistrationStatus**](SMSTollFreeCampaignRegistrationStatus.md) |  | 
**date_created** | **str** |  | 
**date_updated** | **str** |  | 
**revision** | **int** |  | 

## Example

```python
from freeclimb.models.sms_toll_free_campaign import SMSTollFreeCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of SMSTollFreeCampaign from a JSON string
sms_toll_free_campaign_instance = SMSTollFreeCampaign.from_json(json)
# print the JSON string representation of the object
print(SMSTollFreeCampaign.to_json())

# convert the object into a dict
sms_toll_free_campaign_dict = sms_toll_free_campaign_instance.to_dict()
# create an instance of SMSTollFreeCampaign from a dict
sms_toll_free_campaign_from_dict = SMSTollFreeCampaign.from_dict(sms_toll_free_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


