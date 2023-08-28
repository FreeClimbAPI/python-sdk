# Python SDK Testing

## Manually added arguments

| Class                                                                 | Arguments                                                                                                                                                                                                         |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AddToConferenceAllOf                                                  | `conference_id="TEST_ID"`                                                                                                                                                                                         |
| AddToConference                                                       | `conference_id="TEST_ID"`                                                                                                                                                                                         |
| AvailableNumber - test_capabilities                                   | `sms=False, voice=False,toll_free=False, ten_dlc=False, short_code=False`                                                                                                                                         |
| BuyIncomingPhoneNumberRequest                                         | `phone_number="+11231231234"`                                                                                                                                                                                     |
| Capabilities                                                          | `sms=False, voice=False,toll_free=False, ten_dlc=False, short_code=False`                                                                                                                                         |
| CreateConferenceAllOf                                                 | `action_url="TEST_URL"`                                                                                                                                                                                           |
| CreateConference                                                      | `action_url="TEST_URL"`                                                                                                                                                                                           |
| EnqueueAllOf                                                          | `action_url="TEST_URL", queue_id="TEST_ID", wait_url="TEST_URL"`                                                                                                                                                  |
| Enqueue                                                               | `action_url="TEST_URL", queue_id="TEST_ID", wait_url="TEST_URL"`                                                                                                                                                  |
| FilterLogsRequest                                                     | `pql="TEST_PQL"`                                                                                                                                                                                                  |
| GetDigitsAllOf                                                        | `action_url="TEST_URL"`                                                                                                                                                                                           |
| GetDigits                                                             | `action_url="TEST_URL"`                                                                                                                                                                                           |
| GetSpeechAllOf                                                        | `action_url="TEST_URL", grammar_file="TEST_STRING"`                                                                                                                                                               |
| GetSpeech                                                             | `action_url="TEST_URL", grammar_file="TEST_STRING"`                                                                                                                                                               |
| IncomingNumberResultAllOf - test_capabilities                         | `sms=False, voice=False,toll_free=False, ten_dlc=False, short_code=False`                                                                                                                                         |
| IncomingNumberResult - test_capabilities                              | `sms=False, voice=False,toll_free=False, ten_dlc=False, short_code=False`                                                                                                                                         |
| MakeCallRequest                                                       | `_from="+11231231234", to="+11231231234"`                                                                                                                                                                         |
| MessageRequestAllOf                                                   | `_from="+11231231234", to="+11231231234", text="TEST_STRING"`                                                                                                                                                     |
| MessageRequest                                                        | `_from="+11231231234", to="+11231231234"`                                                                                                                                                                         |
| OutDialAllOf                                                          | `action_url="TEST_URL", call_connect_url="TEST_URL", calling_number="+11231231234", destination="+11231231234"`                                                                                                   |
| OutDial                                                               | `action_url="TEST_URL", call_connect_url="TEST_URL", calling_number="+11231231234", destination="+11231231234"`                                                                                                   |
| ParkAllOf                                                             | `wait_url="TEST_URL", action_url="TEST_URL"`                                                                                                                                                                      |
| Park                                                                  | `wait_url="TEST_URL", action_url="TEST_URL"`                                                                                                                                                                      |
| PauseAllOf                                                            | `length=1`                                                                                                                                                                                                        |
| Pause                                                                 | `length=1`                                                                                                                                                                                                        |
| PlayAllOf                                                             | `file="TEST_STRING"`                                                                                                                                                                                              |
| PlayEarlyMediaAllOf                                                   | `file="TEST_STRING"`                                                                                                                                                                                              |
| PlayEarlyMedia                                                        | `file="TEST_STRING"`                                                                                                                                                                                              |
| Play                                                                  | `file="TEST_STRING"`                                                                                                                                                                                              |
| RecordUtteranceAllOf                                                  | `action_url="TEST_URL"`                                                                                                                                                                                           |
| RecordUtterance                                                       | `action_url="TEST_URL"`                                                                                                                                                                                           |
| RedirectAllOf                                                         | `action_url="TEST_URL"`                                                                                                                                                                                           |
| Redirect                                                              | `action_url="TEST_URL"`                                                                                                                                                                                           |
| RemoveFromConferenceAllOf                                             | `call_id="TEST_ID"`                                                                                                                                                                                               |
| RemoveFromConference                                                  | `call_id="TEST_ID"`                                                                                                                                                                                               |
| SayAllOf                                                              | `text="TEST_STRING"`                                                                                                                                                                                              |
| Say                                                                   | `text="TEST_STRING"`                                                                                                                                                                                              |
| SendDigitsAllOf                                                       | `digits="TEST_STRING"`                                                                                                                                                                                            |
| SendDigits                                                            | `digits="TEST_STRING"`                                                                                                                                                                                            |
| SetListenAllOf                                                        | `call_id="TEST_ID"`                                                                                                                                                                                               |
| SetListen                                                             | `call_id="TEST_ID"`                                                                                                                                                                                               |
| SetTalkAllOf                                                          | `call_id="TEST_ID"`                                                                                                                                                                                               |
| SetTalk                                                               | `call_id="TEST_ID"`                                                                                                                                                                                               |
| SmsAllOf                                                              | `to="+11231231234", _from= "+11231231234", text="TEST_STRING"`                                                                                                                                                    |
| Sms                                                                   | `to="+11231231234", _from= "+11231231234", text="TEST_STRING"`                                                                                                                                                    |
| SMSTenDLCBrand                                                        | `entity_type="PRIVATE_PROFIT", display_name="TEST_STRING,phone="TEST_STRING",country="TS", email="TEST_STRING", brand_relationship="BASIC_ACCOUNT", vertical="TEST_STRING", mock=True, identity_status="VERIFIED` |
| SMSTenDLCCampaign                                                     | `campaign_id="TET_STRING", csp_id="TEST_STRING", brand_id="TEST_STR", usecase="TEST_STRING", sub_usecases=[], description="TEST_STRING", mock=True`                                                               |
| SMSTenDLCPartnerCampaignBrand                                         | `phone="TEST_STRING", email="TEST_STRING"`                                                                                                                                                                        |
| SMSTenDLCPartnerCampaign                                              | `campaign_id="TEST_STRING", brand_id="TEST_STR", usecase="TEST_STRING", description="TEST_STRING"`                                                                                                                |
| SMSTenDLCPartnerCampaign - test_brand (SMSTenDLCPartnerCampaignBrand) | `phone="TEST_STRING", email="TEST_STRING"`                                                                                                                                                                        |
| TerminateConferenceAllOf                                              | `conference_id="TEST_STRING"`                                                                                                                                                                                     |
| TerminateConference                                                   | `conference_id="TEST_STRING"`                                                                                                                                                                                     |
| UpdateCallRequest                                                     | `status="TEST_STRING"`                                                                                                                                                                                            |