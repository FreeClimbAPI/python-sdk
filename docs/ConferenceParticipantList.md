# ConferenceParticipantList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total amount of requested resource. | [optional] 
**start** | **int** | Resource index at start of current page | [optional] 
**end** | **int** | Resource index at end of current page | [optional] 
**page** | **int** | Current page | [optional] 
**num_pages** | **int** | Total number of pages | [optional] 
**page_size** | **int** | Number of items per page | [optional] 
**next_page_uri** | **str** | Uri to retrieve the next page of items | [optional] 
**participants** | [**List[ConferenceParticipantResult]**](ConferenceParticipantResult.md) |  | [optional] 

## Example

```python
from freeclimb.models.conference_participant_list import ConferenceParticipantList

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceParticipantList from a JSON string
conference_participant_list_instance = ConferenceParticipantList.from_json(json)
# print the JSON string representation of the object
print(ConferenceParticipantList.to_json())

# convert the object into a dict
conference_participant_list_dict = conference_participant_list_instance.to_dict()
# create an instance of ConferenceParticipantList from a dict
conference_participant_list_from_dict = ConferenceParticipantList.from_dict(conference_participant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


