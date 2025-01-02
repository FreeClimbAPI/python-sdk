# Unpark

The `Unpark` command resumes a parked call.  Execution continues with the first command in the PerCL scripted returned by the actionUrl specified in the Park command as long as the call is still in progress.  If the call is no longer in progress, any returned PerCL will not be executed. Unpark is a terminal command -- any commands following it in the same script are not executed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from freeclimb.models.unpark import Unpark

# TODO update the JSON string below
json = "{}"
# create an instance of Unpark from a JSON string
unpark_instance = Unpark.from_json(json)
# print the JSON string representation of the object
print(Unpark.to_json())

# convert the object into a dict
unpark_dict = unpark_instance.to_dict()
# create an instance of Unpark from a dict
unpark_from_dict = Unpark.from_dict(unpark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


