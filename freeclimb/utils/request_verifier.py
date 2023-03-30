import sys

from freeclimb.utils.signature_information import SignatureInformation

class RequestVerifier:
    
    DEFAULT_TOLERANCE = 5*60*1000

    def verifyRequestSignature(self, requestBody, requestHeader, signingSecret, tolerance=DEFAULT_TOLERANCE):
        self.checkRequestBody(requestBody)
        self.checkRequestHeader(requestHeader)
        self.checkSigningSecret(signingSecret)
        self.checkTolerance(tolerance)
        info = SignatureInformation(requestHeader)
        self.verifyTolerance(info, tolerance)
        self.verifySignature(info, requestBody, signingSecret)
    
    def checkRequestBody(self, requestBody):
        if requestBody == "" or requestBody == None:
            raise Exception("Request Body cannot be empty or null")

    def checkRequestHeader(self, requestHeader): 
        if requestHeader == "" or requestHeader == None: 
            raise Exception("Error with request header, Request header is empty")
        
        elif not("t" in requestHeader) :
            raise Exception("Error with request header, timestamp is not present")
        
        elif not("v1" in requestHeader) :
            raise Exception("Error with request header, signatures are not present")
        

    def checkSigningSecret(self, signingSecret):
        if signingSecret == "" or signingSecret == None:
            raise Exception("Signing secret cannot be empty or null")
        
    def checkTolerance(self, tolerance):
        if tolerance <= 0 or tolerance >= sys.maxsize:
            raise Exception("Tolerance value must be a positive integer")
        
    def verifyTolerance(self, info, tolerance):
        currentTime = info.getCurrentUnixTime()
        if not(info.isRequestTimeValid(tolerance)):
            raise Exception("Request time exceeded tolerance threshold. Request: " + info.requestTimestamp
            + ", CurrentTime: " + str(currentTime) + ", tolerance: " + str(tolerance))

    def verifySignature(self, info, requestBody, signingSecret):
         if not(info.isSignatureSafe(requestBody, signingSecret)):
            raise Exception("Unverified signature request, If this request was unexpected, it may be from a bad actor. Please proceed with caution. If the request was exepected, please check any typos or issues with the signingSecret")

