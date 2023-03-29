import time, hmac, hashlib

class SignatureInformation:
    requestTimestamp = 0
    signatures = []

    def __init__(self, requestHeader):
        signatureHeaders = requestHeader.split(",")
        for signature in signatureHeaders:
            header = signature.split("=")[0]
            value = signature.split("=")[1]
            if header == "t":
                self.requestTimestamp = value
            elif header == "v1":
                self.signatures.append(value) 
    
    def isRequestTimeValid(self, tolerance):
        currentTime = self.getCurrentUnixTime()
        return float(self.requestTimestamp) + float(tolerance) < currentTime

    def isSignatureSafe(self, requestBody, signingSecret):
        hashValue = self.computeHash(requestBody, signingSecret)
        return hashValue in self.signatures

    def computeHash(self, requestBody, signingSecret):
        data = self.requestTimestamp + "." + requestBody
        return hmac.new(bytes(signingSecret, 'utf-8'), data.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

    def getCurrentUnixTime(self):
        return int(time.time())
