# BlobResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob_id** | **str** | Identifier which can be used to reference this blob in future interations. | [optional] 
**account_id** | **str** |  | [optional] 
**alias** | **str** | Custom identifier for this blob that is unique for the owning account. It will be set to the blobId by default if not provided in the creation request. | [optional] 
**revision** | **int** |  | [optional] 
**date_created** | **datetime** | An RFC3339 timestamp with millisecond resolution. It represents the time this blob was created. | [optional] 
**date_updated** | **datetime** | An RFC3339 timestamp with millisecond resolution. It represents the time this blob was last modified, which at creation will always equal dateCreated. | [optional] 
**expires_at** | **datetime** | An RFC3339 timestamp with millisecond resolution. It represents the time at which this blob will expire and self delete. | [optional] 
**blob** | **object** | Blob content | [optional] 

## Example

```python
from freeclimb.models.blob_result import BlobResult

# TODO update the JSON string below
json = "{}"
# create an instance of BlobResult from a JSON string
blob_result_instance = BlobResult.from_json(json)
# print the JSON string representation of the object
print(BlobResult.to_json())

# convert the object into a dict
blob_result_dict = blob_result_instance.to_dict()
# create an instance of BlobResult from a dict
blob_result_from_dict = BlobResult.from_dict(blob_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


