# SMSTollFreeCampaignsListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total amount of requested resource. | [optional] 
**start** | **int** | Resource index at start of current page | [optional] 
**end** | **int** | Resource index at end of current page | [optional] 
**page** | **int** | Current page | [optional] 
**num_pages** | **int** | Total number of pages | [optional] 
**page_size** | **int** | Number of items per page | [optional] 
**next_page_uri** | **str** | Uri to retrieve the next page of items | [optional] 
**brands** | [**List[SMSTollFreeCampaign]**](SMSTollFreeCampaign.md) |  | [optional] 

## Example

```python
from freeclimb.models.sms_toll_free_campaigns_list_result import SMSTollFreeCampaignsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of SMSTollFreeCampaignsListResult from a JSON string
sms_toll_free_campaigns_list_result_instance = SMSTollFreeCampaignsListResult.from_json(json)
# print the JSON string representation of the object
print(SMSTollFreeCampaignsListResult.to_json())

# convert the object into a dict
sms_toll_free_campaigns_list_result_dict = sms_toll_free_campaigns_list_result_instance.to_dict()
# create an instance of SMSTollFreeCampaignsListResult from a dict
sms_toll_free_campaigns_list_result_from_dict = SMSTollFreeCampaignsListResult.from_dict(sms_toll_free_campaigns_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


