# CallStatus

* `queued` &ndash; Call is ready and waiting in line before going out. * `ringing` &ndash; Call is currently ringing. * `inProgress` &ndash; Call was answered and is currently in progress. * `canceled` &ndash; Call was hung up while it was queued or ringing. * `completed` &ndash; Call was answered and has ended normally. * `busy` &ndash; Caller received a busy signal. * `failed` &ndash; Call could not be completed as dialed, most likely because the phone number was non-existent. * `noAnswer` &ndash; Call ended without being answered.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
| **QUEUED** | **CallStatus** |  | Represented in Python as "queued" |
| **RINGING** | **CallStatus** |  | Represented in Python as "ringing" |
| **IN_PROGRESS** | **CallStatus** |  | Represented in Python as "inProgress" |
| **CANCELED** | **CallStatus** |  | Represented in Python as "canceled" |
| **COMPLETED** | **CallStatus** |  | Represented in Python as "completed" |
| **FAILED** | **CallStatus** |  | Represented in Python as "failed" |
| **BUSY** | **CallStatus** |  | Represented in Python as "busy" |
| **NO_ANSWER** | **CallStatus** |  | Represented in Python as "noAnswer" |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


