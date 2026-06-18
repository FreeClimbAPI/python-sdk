# CallList


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
**calls** | [**List[CallResult]**](CallResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.call_list import CallList

json = """{
  "total": 0,
  "start": 0,
  "end": 0,
  "page": 0,
  "numPages": 0,
  "pageSize": 0,
  "nextPageUri": "string",
  "calls": [
    {
      "uri": "string",
      "dateCreated": "string",
      "dateUpdated": "string",
      "revision": 0,
      "dateCreatedISO": "2022-01-01T00:00:00Z",
      "dateUpdatedISO": "2022-01-01T00:00:00Z",
      "callId": "string",
      "parentCallId": "string",
      "accountId": "string",
      "from": "string",
      "to": "string",
      "phoneNumberId": "string",
      "status": "queued",
      "startTime": "string",
      "startTimeISO": "2022-01-01T00:00:00Z",
      "connectTime": "string",
      "connectTimeISO": "2022-01-01T00:00:00Z",
      "endTime": "string",
      "endTimeISO": "2022-01-01T00:00:00Z",
      "duration": 0,
      "connectDuration": 0,
      "audioStreamDuration": 0,
      "direction": "inbound",
      "answeredBy": "human",
      "callerName": "string",
      "webRTC": false,
      "subresourceUris": {
        "logs": "string",
        "recordings": "string"
      },
      "applicationId": "string"
    }
  ]
}"""
# create an instance of CallList from a JSON string
call_list_instance = CallList.from_json(json)
# print the JSON string representation of the object
print(CallList.to_json())

# convert the object into a dict
call_list_dict = call_list_instance.to_dict()
# create an instance of CallList from a dict
call_list_from_dict = CallList.from_dict(call_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


