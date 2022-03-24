# QueueRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Description for this Queue. Max length is 64 characters. | [optional] 
**max_size** | **int** | Maximum number of calls this queue can hold. Default is 100. Maximum is 1000. **Note:** Reducing the maxSize of a Queue causes the Queue to reject incoming requests until it shrinks below the new value of maxSize. | [optional]  if omitted the server will use the default value of 100

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


