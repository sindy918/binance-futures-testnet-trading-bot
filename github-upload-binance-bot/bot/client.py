import time
import hmac
import hashlib
import requests
import logging

class BinanceClient:
    def __init__(self, api_key, api_secret, base_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def get_signature(self, query_string):
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def send_signed_request(self, method, endpoint, params):
        url = f"{self.base_url}{endpoint}"
        
        # Add timestamp
        params["timestamp"] = int(time.time() * 1000)
        
        # Create query string
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        
        # Generate signature
        signature = self.get_signature(query_string)
        
        # Build query string with signature
        query_string_with_sig = f"{query_string}&signature={signature}"
        
        headers = {
            "X-MBX-APIKEY": self.api_key
        }
        
        try:
            if method.upper() == "POST":
                response = requests.post(f"{url}?{query_string_with_sig}", headers=headers)
            elif method.upper() == "GET":
                response = requests.get(f"{url}?{query_string_with_sig}", headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            return response
        except Exception as e:
            logging.error(f"Request failed: {str(e)}")
            raise e
