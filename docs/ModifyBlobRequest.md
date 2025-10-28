# ModifyBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob** | **object** |  | 
**alias** | **str** | Custom identifier for this blob that is unique for the owning account. It will be set to the blobId by default if not provided. | [optional] 

## Example

```python
from freeclimb.models.modify_blob_request import ModifyBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyBlobRequest from a JSON string
modify_blob_request_instance = ModifyBlobRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyBlobRequest.to_json())

# convert the object into a dict
modify_blob_request_dict = modify_blob_request_instance.to_dict()
# create an instance of ModifyBlobRequest from a dict
modify_blob_request_from_dict = ModifyBlobRequest.from_dict(modify_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


