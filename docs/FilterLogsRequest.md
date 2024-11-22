# FilterLogsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pql** | **str** | The filter query for retrieving logs. See **Performance Query Language** below. | 

## Example

```python
from freeclimb.models.filter_logs_request import FilterLogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilterLogsRequest from a JSON string
filter_logs_request_instance = FilterLogsRequest.from_json(json)
# print the JSON string representation of the object
print(FilterLogsRequest.to_json())

# convert the object into a dict
filter_logs_request_dict = filter_logs_request_instance.to_dict()
# create an instance of FilterLogsRequest from a dict
filter_logs_request_from_dict = FilterLogsRequest.from_dict(filter_logs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


