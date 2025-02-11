# TFNCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account that created this participant. | 
**campaign_id** | **str** | TFNCampaignId | 
**use_case** | **str** |  | 
**registration_status** | [**SMSTollFreeCampaignRegistrationStatus**](SMSTollFreeCampaignRegistrationStatus.md) |  | 
**date_created** | **str** |  | 
**date_updated** | **str** |  | 
**date_created_iso** | **str** |  | 
**date_updated_iso** | **str** |  | 
**revision** | **int** |  | 

## Example

```python
from freeclimb.models.tfn_campaign import TFNCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of TFNCampaign from a JSON string
tfn_campaign_instance = TFNCampaign.from_json(json)
# print the JSON string representation of the object
print(TFNCampaign.to_json())

# convert the object into a dict
tfn_campaign_dict = tfn_campaign_instance.to_dict()
# create an instance of TFNCampaign from a dict
tfn_campaign_from_dict = TFNCampaign.from_dict(tfn_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


