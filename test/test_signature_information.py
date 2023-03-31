import unittest

from freeclimb.utils.signature_information import SignatureInformation

class TestSignatureInformation(unittest.TestCase):
    """SignatureInformation unit test stubs"""

    def setUp(self):
        requestHeader = "t=1679944186,v1=c3957749baf61df4b1506802579cc69a74c77a1ae21447b930e5a704f9ec4120,v1=1ba18712726898fbbe48cd862dd096a709f7ad761a5bab14bda9ac24d963a6a8"
        self.signatureInformationObject = SignatureInformation(requestHeader)
    
    def tearDown(self):
        pass

    def test_isRequestTimeValid_true(self):
        tolerance = 5 * 60
        self.assertEqual(self.signatureInformationObject.isRequestTimeValid(tolerance), True)
    
    def test_isRequestTimeValid_false(self):
        tolerance = 5 * 60 * 10000
        self.assertEqual(self.signatureInformationObject.isRequestTimeValid(tolerance), False)
    
    def test_isSignatureSafe_true(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7793"
        self.assertEqual(self.signatureInformationObject.isSignatureSafe(requestBody, signingSecret), True)

    def test_isSignatureSafe_false(self):
        requestBody = "{\"accountId\":\"AC1334ffb694cd8d969f51cddf5f7c9b478546d50c\",\"callId\":\"CAccb0b00506553cda09b51c5477f672a49e0b2213\",\"callStatus\":\"ringing\",\"conferenceId\":null,\"direction\":\"inbound\",\"from\":\"+13121000109\",\"parentCallId\":null,\"queueId\":null,\"requestType\":\"inboundCall\",\"to\":\"+13121000096\"}"
        signingSecret = "sigsec_ead6d3b6904196c60835d039e91b3341c77a7794"
        self.assertEqual(self.signatureInformationObject.isSignatureSafe(requestBody, signingSecret), False)
        
    

if __name__ == '__main__':
    unittest.main()