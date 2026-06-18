# AvailableNumberList


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
**available_phone_numbers** | [**List[AvailableNumber]**](AvailableNumber.md) |  | [optional] 

## Example

```python
from freeclimb.models.available_number_list import AvailableNumberList

json = """{
  "total": 0,
  "start": 0,
  "end": 0,
  "page": 0,
  "numPages": 0,
  "pageSize": 0,
  "nextPageUri": "string",
  "availablePhoneNumbers": [
    {
      "capabilities": {
        "voice": false,
        "sms": false,
        "tollFree": false,
        "tenDLC": false,
        "shortCode": false
      },
      "campaignId": "string",
      "phoneNumber": "string",
      "alias": "string",
      "region": "string",
      "country": "string"
    }
  ]
}"""
# create an instance of AvailableNumberList from a JSON string
available_number_list_instance = AvailableNumberList.from_json(json)
# print the JSON string representation of the object
print(AvailableNumberList.to_json())

# convert the object into a dict
available_number_list_dict = available_number_list_instance.to_dict()
# create an instance of AvailableNumberList from a dict
available_number_list_from_dict = AvailableNumberList.from_dict(available_number_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


