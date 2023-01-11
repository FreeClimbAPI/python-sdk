# Python SDK Changelog

All notable changes to this project will be documented in this file.

The format of this changelog is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

None

<a name="4.1.0"></a>

## [4.1.0] - 2023-01-06

### Changed

- Enums have been implemented in the python sdk
- Updated README for enum implementation and testing

<a name="4.0.6"></a>

## [4.0.6] - 2022-12-01

### Changed

- Changed `QueueResult` property `current_size` from string to int
- Renamed `QueueResult` property `average_wait_time` to `average_queue_removal_time`

<a name="4.0.5"></a>

## [4.0.5] - 2022-11-01

### Added

- Add `offnet` property in IncomingNumber resource
- Add `offnet` query parameter for listIncomingNumbers

<a name="4.0.4"></a>

## [4.0.4] - 2022-10-07

### Added

- Add `play_ beep` enum to update conference request

### Changed

- Call `status` enum `INPROGRESS` to `IN_PROGRESS`
- Call `status` enum `NOANSWER` to `NO_ANSWER`
- Conference `play_beep` enum `ENTRYONLY` to `ENTRY_ONLY`
- Conference `play_beep` enum `EXITONLY` to `EXIT_ONLY`

<a name="4.0.3"></a>

## [4.0.3] - 2022-08-19

### Added

- Add `Park` PerCL command
- Add `Unpark` PerCL command

<a name="4.0.2"></a>

## [4.0.2] - 2022-08-09

### Added

- Added optional property `campaign_id`

### Changed

- Update default value for `loop` value in Say command to `1`

<a name="4.0.0"></a>

## [4.0.0] - 2022-02-16

### Added

- Add capabilities query functionality for searching AvailableNumbers and IncomingNumbers
- Enable unit testing

### Changed

- Prefer keyword argument initialization for all models
- Rename api->list_an_application to list->list_applications
- Use new openapi-generator version (5.4.0)
- Remove floating `freeclimb.percl_to_json` and added it to `PerclScript` as `to_json` method

<a name="3.0.2"></a>

## [3.0.2] - 2021-12-06

### Changed

-remove alias from accepted query parameters when listing AvailablePhoneNumbers
-Add country, region, smsEnabled, and voiceEnabled as accepted query parameters for AvailablePhoneNumbers
-Add smsEnabled to AvailablePhoneNumbers response schema
-Add applicationId, country, region, smsEnabled, voiceEnabled, and hasApplication as accepted query parameters for IncomingPhoneNumber.

<a name="3.0.1"></a>

## [3.0.1] - 2021-11-01

### Added

- Add `active` property to CallResult

### Changed

- Small instances of `token` to `key`
- Call ID is not required to `AddToConference`

<a name="3.0.0"></a>

## [3.0.0] - 2021-05-05

### Added

- Add `verifyRequest` utility function

<a name="2.2.0"></a>

## [2.2.0] - 2021-04-12

### Changed

- Replace any language instance of `auth_token` or similar speech to `api_key`

<a name="2.1.2"></a>

## [2.1.2] - 2021-03-10

### Added

- Add `callConnectUrl` option to MakeCall Request

<a name="2.1.1"></a>

## [2.1.1] - 2020-12-16

### Added

- Add `privacyMode` option to RecordUtterance PerCL command

<a name="2.1.0"></a>

## [2.1.0] - 2020-12-16

### Added

- Add `Reject` PerCL command
- Add `Hangup` PerCL command

### Fixed

- Updated description and requirement of `action_url` attribute of `Redirect` PerCL command

<a name="2.0.3"></a>

## [2.0.3] - 2020-12-16

### Added

- Additional message statuses for TFN functionality

<a name="2.0.2"></a>

## [2.0.2] - 2020-08-13

### Added

- Add `privacyMode` option

<a name="1.2.1"></a>

## [1.2.1] - 2020-10-14

### Added

- Add `Reject` PerCL command

### Changed

- Rename `setPersyUrl` to `setUrl`

### Fixed

- Properly handle empty response bodies
- Other Minor bug fixes

<a name="1.2"></a>

## [1.2] - 2019-10-16

### Changed

- Persephony is now FreeClimb
- Code cleanup
- Documentation Updates
- Test Update

### Fixed

- Update common response handler to not use bodu twice

<a name="1.1.1"></a>

## [1.1.1] - 2019-06-27

### Changed

- Minor updates to docs and code cleanup

<a name="1.1.0"></a>

## [1.1.0] - 2019-06-07

### Pull Requests

- Merge pull request [#22](https://gitlab.vailsys.com/vail-cloud-services/fc-boilerplates/javascript-sdk/issues/22) from PersephonyAPI/maintenance

<a name="1.0.0"></a>

## [1.0.0] - 2019-06-04

### Changed

- Change default api target

<a name="0.1.0"></a>

## [0.1.0] - 2019-05-30

### Added

- `PlayEarlyMedia` PerCL Command

<a name="0.0.2"></a>

## [0.0.2] - 2018-11-29

### Remove

- Remove `callConnectUrl` and `statusCallbackUrl` from api.calls#create

<a name="0.0.1"></a>

## [0.0.1] - 2018-11-13

### Added

- PerCL Support
- FreeClimb API Support
- README, LICENSE
- docs

### Changed

- Initial Release

[unreleased]: https://github.com/FreeClimbAPI/python-sdk/compare/v1.0.1...HEAD
