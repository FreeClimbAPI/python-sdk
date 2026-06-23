# ExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**ExportResourceType**](ExportResourceType.md) |  | 
**format** | **List[str]** |  | [optional] 
**output** | [**ExportRequestOutput**](ExportRequestOutput.md) |  | 
**query** | **object** |  | [optional] 

## Example

```python
from freeclimb.models.export_request import ExportRequest

json = """{
  "resourceType": "Messages",
  "format": [
    "messageId",
    "dateUpdated",
    "status"
  ],
  "output": {
    "type": "csv"
  },
  "query": {
    "direction": "inbound"
  }
}"""
# create an instance of ExportRequest from a JSON string
export_request_instance = ExportRequest.from_json(json)
# print the JSON string representation of the object
print(ExportRequest.to_json())

# convert the object into a dict
export_request_dict = export_request_instance.to_dict()
# create an instance of ExportRequest from a dict
export_request_from_dict = ExportRequest.from_dict(export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


