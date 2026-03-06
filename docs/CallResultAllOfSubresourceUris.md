# CallResultAllOfSubresourceUris

The list of subresources for this Call. These include things like logs and recordings associated with the Call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | **str** | The URI for the logs associated with this Call. | [optional] 
**recordings** | **str** | The URI for the recordings associated with this Call. | [optional] 

## Example

```python
from freeclimb.models.call_result_all_of_subresource_uris import CallResultAllOfSubresourceUris

# TODO update the JSON string below
json = "{}"
# create an instance of CallResultAllOfSubresourceUris from a JSON string
call_result_all_of_subresource_uris_instance = CallResultAllOfSubresourceUris.from_json(json)
# print the JSON string representation of the object
print(CallResultAllOfSubresourceUris.to_json())

# convert the object into a dict
call_result_all_of_subresource_uris_dict = call_result_all_of_subresource_uris_instance.to_dict()
# create an instance of CallResultAllOfSubresourceUris from a dict
call_result_all_of_subresource_uris_from_dict = CallResultAllOfSubresourceUris.from_dict(call_result_all_of_subresource_uris_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


