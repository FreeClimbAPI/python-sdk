# ApplicationList


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
**applications** | [**List[ApplicationResult]**](ApplicationResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.application_list import ApplicationList

json = """{
  "total": 0,
  "start": 0,
  "end": 0,
  "page": 0,
  "numPages": 0,
  "pageSize": 0,
  "nextPageUri": "string",
  "applications": [
    {
      "uri": "string",
      "dateCreated": "string",
      "dateUpdated": "string",
      "revision": 0,
      "accountId": "string",
      "applicationId": "string",
      "alias": "string",
      "voiceUrl": "https://www.example.com",
      "voiceFallbackUrl": "https://www.example.com",
      "callConnectUrl": "https://www.example.com",
      "statusCallbackUrl": "https://www.example.com",
      "smsUrl": "https://www.example.com",
      "smsFallbackUrl": "https://www.example.com"
    }
  ]
}"""
# create an instance of ApplicationList from a JSON string
application_list_instance = ApplicationList.from_json(json)
# print the JSON string representation of the object
print(ApplicationList.to_json())

# convert the object into a dict
application_list_dict = application_list_instance.to_dict()
# create an instance of ApplicationList from a dict
application_list_from_dict = ApplicationList.from_dict(application_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


