# AccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Description for this account. | [optional] 
**label** | **str** | Group to which this account belongs. | [optional] 

## Example

```python
from freeclimb.models.account_request import AccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRequest from a JSON string
account_request_instance = AccountRequest.from_json(json)
# print the JSON string representation of the object
print(AccountRequest.to_json())

# convert the object into a dict
account_request_dict = account_request_instance.to_dict()
# create an instance of AccountRequest from a dict
account_request_from_dict = AccountRequest.from_dict(account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


