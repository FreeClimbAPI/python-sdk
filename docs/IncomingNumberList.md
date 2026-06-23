# IncomingNumberList


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
**incoming_phone_numbers** | [**List[IncomingNumberResult]**](IncomingNumberResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.incoming_number_list import IncomingNumberList

json = """{
  "total": 0,
  "start": 0,
  "end": 0,
  "page": 0,
  "numPages": 0,
  "pageSize": 0,
  "nextPageUri": "string",
  "incomingPhoneNumbers": [
    {
      "uri": "string",
      "dateCreated": "string",
      "dateUpdated": "string",
      "revision": 0,
      "capabilities": {
        "voice": false,
        "sms": false,
        "tollFree": false,
        "tenDLC": false,
        "shortCode": false
      },
      "campaignId": "string",
      "phoneNumberId": "string",
      "accountId": "string",
      "applicationId": "string",
      "phoneNumber": "string",
      "alias": "string",
      "region": "string",
      "country": "string",
      "offnet": false,
      "tfn": {
        "campaignId": "string"
      }
    }
  ]
}"""
# create an instance of IncomingNumberList from a JSON string
incoming_number_list_instance = IncomingNumberList.from_json(json)
# print the JSON string representation of the object
print(IncomingNumberList.to_json())

# convert the object into a dict
incoming_number_list_dict = incoming_number_list_instance.to_dict()
# create an instance of IncomingNumberList from a dict
incoming_number_list_from_dict = IncomingNumberList.from_dict(incoming_number_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


