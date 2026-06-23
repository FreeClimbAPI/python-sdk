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

json = """{
  "total": 0,
  "start": 0,
  "end": 0,
  "page": 0,
  "numPages": 0,
  "pageSize": 0,
  "nextPageUri": "string",
  "brands": [
    {
      "mock": true,
      "optionalAttributes": {},
      "accountId": "AC0123456789abcdefABCDEF0123456789abcdef06",
      "brandId": "BVCEBIJ",
      "cspId": "SKGC6G0",
      "firstName": "",
      "lastName": "",
      "displayName": "FreeClimb LLC(mock)",
      "companyName": "FreeClimb LLC",
      "ein": "843793747",
      "einIssuingCountry": "US",
      "phone": "+18475722071",
      "street": "570 Lake Cook Rd Ste 400",
      "city": "Deerfield",
      "state": "IL",
      "postalCode": "60015",
      "country": "US",
      "email": "bmabry@vailsys.com",
      "stockSymbol": "",
      "stockExchange": "NASDAQ",
      "ipAddress": "127.0.0.1",
      "website": "https://www.freeclimb.com/",
      "vertical": "TECHNOLOGY",
      "universalEin": "US_843793747",
      "referenceId": "ACdeadbeef",
      "entityType": "PRIVATE_PROFIT",
      "brandRelationship": "SMALL_ACCOUNT",
      "identityStatus": "VERIFIED",
      "createDate": "2022-07-01T20:29:23Z"
    }
  ]
}"""
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


