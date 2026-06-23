# ExportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | String that uniquely identifies this account resource. | 
**uri** | **str** |  | 
**date_created** | **str** |  | 
**date_updated** | **str** |  | 
**revision** | **int** |  | 
**export_id** | **str** | String that uniquely identifies this export resource | 
**status** | [**ExportStatus**](ExportStatus.md) |  | 
**size** | **int** |  | 
**resource_type** | [**ExportResourceType**](ExportResourceType.md) |  | 
**query** | **object** | Query params used to filter exported documents | 
**format** | **List[str]** | Desired fields of exported documents | 
**output** | [**ExportResultOutput**](ExportResultOutput.md) |  | 

## Example

```python
from freeclimb.models.export_result import ExportResult

json = """{
  "accountId": "AC0123456789abcdefABCDEF0123456789abcdef07",
  "uri": "/Accounts/AC0123456789abcdefABCDEF0123456789abcdef07/Exports/EX0123456789abcdefABCDEF0123456789abcdef08",
  "dateCreated": "Wed, 26 Jun 2024 15:45:06 UTC",
  "dateUpdated": "Wed, 26 Jun 2024 15:45:06 UTC",
  "revision": 1,
  "exportId": "EX0123456789abcdefABCDEF0123456789abcdef08",
  "status": "completed",
  "size": 12893786,
  "resourceType": "Messages",
  "query": {
    "direction": "inbound"
  },
  "format": [
    "messageId",
    "dateUpdated",
    "segmentCount",
    "status"
  ],
  "output": {
    "type": "csv"
  }
}"""
# create an instance of ExportResult from a JSON string
export_result_instance = ExportResult.from_json(json)
# print the JSON string representation of the object
print(ExportResult.to_json())

# convert the object into a dict
export_result_dict = export_result_instance.to_dict()
# create an instance of ExportResult from a dict
export_result_from_dict = ExportResult.from_dict(export_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


