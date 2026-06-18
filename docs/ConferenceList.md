# ConferenceList


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
**conferences** | [**List[ConferenceResult]**](ConferenceResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.conference_list import ConferenceList

json = """{
  "total": 0,
  "start": 0,
  "end": 0,
  "page": 0,
  "numPages": 0,
  "pageSize": 0,
  "nextPageUri": "string",
  "conferences": [
    {
      "uri": "string",
      "dateCreated": "string",
      "dateUpdated": "string",
      "revision": 0,
      "conferenceId": "string",
      "accountId": "string",
      "alias": "string",
      "record": false,
      "status": "empty",
      "waitUrl": "https://www.example.com",
      "actionUrl": "https://www.example.com",
      "statusCallbackUrl": "https://www.example.com"
    }
  ]
}"""
# create an instance of ConferenceList from a JSON string
conference_list_instance = ConferenceList.from_json(json)
# print the JSON string representation of the object
print(ConferenceList.to_json())

# convert the object into a dict
conference_list_dict = conference_list_instance.to_dict()
# create an instance of ConferenceList from a dict
conference_list_from_dict = ConferenceList.from_dict(conference_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


