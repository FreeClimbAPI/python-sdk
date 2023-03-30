import sys
import time
import unittest

from freeclimb.utils.request_verifier import RequestVerifier

class TestRequestVerifier(unittest.TestCase):
    """RequestVerifier unit test stubs"""

    def setUp(self):
        self.model = RequestVerifier()
    
    def tearDown(self):
        pass

    def test_checkRequestBody(self):
        requestBody = ""
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Request Body cannot be empty or null")
    
    def test_checkRequestHeader_noSignatures(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60
        requestHeader = "t=1679944186,"
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Error with request header, signatures are not present")
    
    def test_checkRequestHeader_noTimestamp(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60
        requestHeader = "v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Error with request header, timestamp is not present")
    
    def test_checkRequestHeader_emptyRequestHeader(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60
        requestHeader = ""        
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Error with request header, Request header is empty")

    def test_checkSigningSecret(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = ""
        tolerance = 5 * 60
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"        
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Signing secret cannot be empty or null")
    
    def test_checkTolerance_toleranceMaxInt(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = sys.maxsize
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"        
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Tolerance value must be a positive integer")
    
    def test_checkTolerance_toleranceZeroValue(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 0
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"        
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Tolerance value must be a positive integer")
    
    def test_checkTolerance_toleranceNegativeValue(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = -5
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"        
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Tolerance value must be a positive integer")
    
    def test_verifyTolerance(self):
        currentTime = int(time.time())
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60
        requestHeader = "t=1900871395,v1=1d798c86e977ff734dec3a8b8d67fe8621dcc1df46ef4212e0bfe2e122b01bfd,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"        
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Request time exceeded tolerance threshold. Request: 1900871395" 
                + ", CurrentTime: " + str(currentTime) + ", tolerance: " + str(tolerance))
    
    def test_verifySignature(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7794"
        tolerance = 5 * 60
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"        
        with self.assertRaises(Exception) as exc:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        self.assertEqual(str(exc.exception), "Unverified signature request, If this request was unexpected, it may be from a bad actor. Please proceed with caution. If the request was exepected, please check any typos or issues with the signingSecret")
    
    def test_verifyRequestSignature(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        tolerance = 5 * 60
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"        
        raised = False
        try:
            self.model.verifyRequestSignature(requestBody, requestHeader, signingSecret, tolerance)
        except:
            raised = True
        self.assertFalse(raised, 'Exception has been raised')
    
    

if __name__ == '__main__':
    unittest.main()