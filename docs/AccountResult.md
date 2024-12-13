# AccountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for this resource, relative to /apiserver. | [optional] 
**date_created** | **str** | The date that this resource was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**date_updated** | **str** | The date that this resource was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT). | [optional] 
**revision** | **int** | Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated. | [optional] 
**account_id** | **str** | String that uniquely identifies this account resource. | [optional] 
**api_key** | **str** | The API key assigned to this account. This key must be kept a secret by the customer. | [optional] 
**alias** | **str** | A description for this account. | [optional] 
**label** | **str** | A string that identifies a category or group to which the account belongs. | [optional] 
**type** | [**AccountType**](AccountType.md) |  | [optional] 
**status** | [**AccountStatus**](AccountStatus.md) |  | [optional] 
**subresource_uris** | **object** | The list of subresources for this account. | [optional] 

## Example

```python
from freeclimb.models.account_result import AccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResult from a JSON string
account_result_instance = AccountResult.from_json(json)
# print the JSON string representation of the object
print(AccountResult.to_json())

# convert the object into a dict
account_result_dict = account_result_instance.to_dict()
# create an instance of AccountResult from a dict
account_result_from_dict = AccountResult.from_dict(account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


