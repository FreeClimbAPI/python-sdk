import sys
import time
import unittest

from freeclimb.utils.request_verifier import RequestVerifier


class TestRequestVerifier(unittest.TestCase):
    """RequestVerifier unit test stubs"""

    def setUp(self):
        self.request_verifier = RequestVerifier()

    def tearDown(self):
        pass

    def test_check_request_body(self):
        request_body = ""
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60 * 1000
        request_header = "t=1679944186,v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(str(exc.exception), "Request Body cannot be empty or null")

    def test_check_request_header_no_signatures(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60 * 1000
        request_header = "t=1679944186,"
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception), "Error with request header, signatures are not present"
        )

    def test_check_request_header_no_timestamp(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60 * 1000
        request_header = "v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception), "Error with request header, timestamp is not present"
        )

    def test_check_request_header_empty_request_header(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60 * 1000
        request_header = ""
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception), "Error with request header, Request header is empty"
        )

    def test_check_signing_secret(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = ""
        tolerance = 5 * 60 * 1000
        request_header = "t=1679944186,v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(str(exc.exception), "Signing secret cannot be empty or null")

    def test_check_tolerance_max_int(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = sys.maxsize
        request_header = "t=1679944186,v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception), "Tolerance value must be a positive integer"
        )

    def test_check_tolerance_zero_value(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 0
        request_header = "t=1679944186,v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            self.request_verifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception), "Tolerance value must be a positive integer"
        )

    def test_check_tolerance_negative_value(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = -5
        request_header = "t=1679944186,v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception), "Tolerance value must be a positive integer"
        )

    def test_verify_tolerance(self):
        current_time = int(time.time())
        request_header_time = current_time - (6 * 60 * 1000)
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60 * 1000
        request_header = (
            "t="
            + str(request_header_time)
            + ",v1=1d798c86e977ff734dec3a8b8d67fe8621dcc1df46ef4212e0bfe2e122b01bfd,v1=78e363373f8a9f6fddc2e3ca3a1ed9dc94efa44d378363adf52434e78f32d8fb"
        )
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception),
            "Request time exceeded tolerance threshold. Request: "
            + str(request_header_time)
            + ", CurrentTime: "
            + str(current_time)
            + ", tolerance: "
            + str(tolerance),
        )

    def test_verify_signature(self):
        current_time = int(time.time())
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7794"
        tolerance = 5 * 60 * 1000
        request_header = (
            "t="
            + str(current_time)
            + ",v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        )
        with self.assertRaises(Exception) as exc:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        self.assertEqual(
            str(exc.exception),
            "Unverified signature request, If this request was unexpected, it may be from a bad actor. Please proceed with caution. If the request was exepected, please check any typos or issues with the signingSecret",
        )

    def test_verify_request_signature(self):
        request_body = '{"accountId":"AC0123456789abcdefABCDEF0123456789abcdef00","callId":"CA0123456789abcdefABCDEF0123456789abcdef00","callStatus":"ringing","conferenceId":null,"direction":"inbound","from":"+13121000109","parentCallId":null,"queueId":null,"requestType":"inboundCall","to":"+13121000096"}'
        signing_secret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60 * 1000
        request_header = "t=3795106129,v1=2f33654710a27e57828fa8556c2ed47c7a324aca88f155e296579e2ae851ce7b,v1=f1003cbf329694be4802907289fff9838cd5ea2894860a66bba00adc0e1fa73e"
        raised = False
        try:
            RequestVerifier.verify_request_signature(
                request_body, request_header, signing_secret, tolerance
            )
        except:
            raised = True
            self.assertFalse(raised, "Exception has been raised")


if __name__ == "__main__":
    unittest.main()
