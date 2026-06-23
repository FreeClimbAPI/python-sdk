# ReplaceBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob** | **object** |  | 

## Example

```python
from freeclimb.models.replace_blob_request import ReplaceBlobRequest

json = """{
  "blob": {
    "firstName": "John",
    "lastName": "Doe"
  }
}"""
# create an instance of ReplaceBlobRequest from a JSON string
replace_blob_request_instance = ReplaceBlobRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceBlobRequest.to_json())

# convert the object into a dict
replace_blob_request_dict = replace_blob_request_instance.to_dict()
# create an instance of ReplaceBlobRequest from a dict
replace_blob_request_from_dict = ReplaceBlobRequest.from_dict(replace_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


