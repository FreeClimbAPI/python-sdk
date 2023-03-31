import time, hmac, hashlib

class SignatureInformation:
    requestTimestamp:int = 0
    signatures = []

    def __init__(self, requestHeader:str):
        signatureHeaders = requestHeader.split(",")
        for signature in signatureHeaders:
            header, value = signature.split("=")
            if header == "t":
                self.requestTimestamp = int(value)
            elif header == "v1":
                self.signatures.append(value) 
    
    def isRequestTimeValid(self, tolerance:int) -> bool:
        currentTime = self.getCurrentUnixTime()
        timeCalculation:int = self.requestTimestamp + tolerance
        return (timeCalculation) < currentTime

    def isSignatureSafe(self, requestBody:str, signingSecret:str) -> bool:
        hashValue = self.computeHash(requestBody, signingSecret)
        return hashValue in self.signatures

    def computeHash(self, requestBody:str, signingSecret:str) -> str:
        data = str(self.requestTimestamp) + "." + requestBody
        return hmac.new(bytes(signingSecret, 'utf-8'), data.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

    def getCurrentUnixTime(self) -> int:
        return int(time.time())
