# CreateBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Custom identifier for this blob that is unique for the owning account. It will be set to the blobId by default if not provided. | [optional] 
**expires_at** | **str** | An RFC3339 timestamp with millisecond resolution. This timestamp defines the time at which this blob will delete itself. It must not be more than 48 hours in the future and will default to 9 hours in the future if not provided. | [optional] 
**blob** | **object** |  | 

## Example

```python
from freeclimb.models.create_blob_request import CreateBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlobRequest from a JSON string
create_blob_request_instance = CreateBlobRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBlobRequest.to_json())

# convert the object into a dict
create_blob_request_dict = create_blob_request_instance.to_dict()
# create an instance of CreateBlobRequest from a dict
create_blob_request_from_dict = CreateBlobRequest.from_dict(create_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


