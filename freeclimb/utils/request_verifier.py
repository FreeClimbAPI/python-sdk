import sys

from freeclimb.utils.signature_information import SignatureInformation

class RequestVerifier:
    
    DEFAULT_TOLERANCE = 5*60*1000

    @staticmethod
    def verify_request_signature(request_body:str, request_header:str, signing_secret:str, tolerance:int=DEFAULT_TOLERANCE):
        RequestVerifier.check_request_body(request_body)
        RequestVerifier.check_request_header(request_header)
        RequestVerifier.check_signing_secret(signing_secret)
        RequestVerifier.check_tolerance(tolerance)
        info = SignatureInformation(request_header)
        RequestVerifier.verify_tolerance(info, tolerance)
        RequestVerifier.verify_signature(info, request_body, signing_secret)
    
    def check_request_body(request_body:str):
        if request_body == "" or request_body == None:
            raise Exception("Request Body cannot be empty or null")

    def check_request_header(request_header:str): 
        if request_header == "" or request_header == None: 
            raise Exception("Error with request header, Request header is empty")
        
        elif not("t" in request_header) :
            raise Exception("Error with request header, timestamp is not present")
        
        elif not("v1" in request_header) :
            raise Exception("Error with request header, signatures are not present")
        

    def check_signing_secret(signing_secret:str):
        if signing_secret == "" or signing_secret == None:
            raise Exception("Signing secret cannot be empty or null")
        
    def check_tolerance(tolerance:int):
        if tolerance <= 0 or tolerance >= sys.maxsize:
            raise Exception("Tolerance value must be a positive integer")
        
    def verify_tolerance(info:SignatureInformation, tolerance:int):
        currentTime = info.get_current_unix_time()
        if not(info.is_request_time_valid(tolerance)):
            raise Exception("Request time exceeded tolerance threshold. Request: " + str(info.request_timestamp)
            + ", CurrentTime: " + str(currentTime) + ", tolerance: " + str(tolerance))

    def verify_signature(info:SignatureInformation, request_body:str, signing_secret:str):
         if not(info.is_signature_safe(request_body, signing_secret)):
            raise Exception("Unverified signature request, If this request was unexpected, it may be from a bad actor. Please proceed with caution. If the request was exepected, please check any typos or issues with the signingSecret")

