# SMSTenDLCBrandsListResult


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
**brands** | [**List[SMSTenDLCBrand]**](SMSTenDLCBrand.md) |  | [optional] 

## Example

```python
from freeclimb.models.sms_ten_dlc_brands_list_result import SMSTenDLCBrandsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of SMSTenDLCBrandsListResult from a JSON string
sms_ten_dlc_brands_list_result_instance = SMSTenDLCBrandsListResult.from_json(json)
# print the JSON string representation of the object
print(SMSTenDLCBrandsListResult.to_json())

# convert the object into a dict
sms_ten_dlc_brands_list_result_dict = sms_ten_dlc_brands_list_result_instance.to_dict()
# create an instance of SMSTenDLCBrandsListResult from a dict
sms_ten_dlc_brands_list_result_from_dict = SMSTenDLCBrandsListResult.from_dict(sms_ten_dlc_brands_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


