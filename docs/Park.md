# Park

The `Park` command allows a caller to be put on hold.  You can provide hold music,messages,etc until ready to resume the call. Park is a terminal command.  Actions performed on the Call while on hold are provided in a PerCL script in response to the waitUrl property. Actions performed on the Call after it has been unparked (resumed) will be provided in a PerCL script in response to the actionUrl provided. A Call can be resumed in two ways -- REST API invocation or the Unpark percl command. No actions can be nested within Park and Park cannot be nested in any other actions. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wait_url** | **str** | Specifies a URL pointing to a PerCL script containing actions to be executed while the caller is Parked. Once the script returned by the waitUrl runs out of commands to execute, FreeClimb will re-request the waitUrl and start over, essentially looping the script requests indefinitely. | 
**action_url** | **str** | A request is made to this URL when the Call is resumed, which can occur if the Call is resumed via the Unpark command, the REST API (POST to Call resource), or the caller hangs up. The PerCL script returned in response to the actionUrl will be executed on the resumed call. | 
**notification_url** | **str** | URL to be invoked when the Call is parked. The request to the URL contains the standard request parameters. | [optional] 

## Example

```python
from freeclimb.models.park import Park

# TODO update the JSON string below
json = "{}"
# create an instance of Park from a JSON string
park_instance = Park.from_json(json)
# print the JSON string representation of the object
print(Park.to_json())

# convert the object into a dict
park_dict = park_instance.to_dict()
# create an instance of Park from a dict
park_from_dict = Park.from_dict(park_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


