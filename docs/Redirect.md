# Redirect

The `Redirect` command transfers control of a Call to the PerCL at a different URL. `Redirect` is a terminal command, so any actions following it are never executed. The maximum number of redirections allowed during the life time of a Call is 256. This is intended to prevent a Call from possibly looping infinitely due to errors in PerCL being generated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** | URL to request a new PerCL script to continue with the current Call&#39;s processing. When &#x60;Redirect&#x60; invokes the &#x60;actionUrl&#x60;, an &#x60;inbound&#x60; Webhook is sent. This request therefore looks identical to the initial request (made to the &#x60;voiceUrl&#x60; of the number that was called) for an inbound Call. | 

## Example

```python
from freeclimb.models.redirect import Redirect

# TODO update the JSON string below
json = "{}"
# create an instance of Redirect from a JSON string
redirect_instance = Redirect.from_json(json)
# print the JSON string representation of the object
print(Redirect.to_json())

# convert the object into a dict
redirect_dict = redirect_instance.to_dict()
# create an instance of Redirect from a dict
redirect_from_dict = Redirect.from_dict(redirect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


