# MutableResourceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 

## Example

```python
from freeclimb.models.mutable_resource_model import MutableResourceModel

# TODO update the JSON string below
json = "{}"
# create an instance of MutableResourceModel from a JSON string
mutable_resource_model_instance = MutableResourceModel.from_json(json)
# print the JSON string representation of the object
print(MutableResourceModel.to_json())

# convert the object into a dict
mutable_resource_model_dict = mutable_resource_model_instance.to_dict()
# create an instance of MutableResourceModel from a dict
mutable_resource_model_from_dict = MutableResourceModel.from_dict(mutable_resource_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


