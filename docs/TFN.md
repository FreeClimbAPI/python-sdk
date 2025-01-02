# TFN

TollFree Campaign details for this number

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** | alphanumeric identifier for the TollFree campaign associated with this number | 

## Example

```python
from freeclimb.models.tfn import TFN

# TODO update the JSON string below
json = "{}"
# create an instance of TFN from a JSON string
tfn_instance = TFN.from_json(json)
# print the JSON string representation of the object
print(TFN.to_json())

# convert the object into a dict
tfn_dict = tfn_instance.to_dict()
# create an instance of TFN from a dict
tfn_from_dict = TFN.from_dict(tfn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


