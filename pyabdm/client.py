import requests
from pyabdm.config import CLIENT_ID, CLIENT_SECRET, GATEWAY_URL

class AuthClient:
    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.gateway_url = GATEWAY_URL
        self.token = None

    def get_access_token(self) -> str:
        if self.token:
            return self.token  # add expiry check later

        url = f"{self.gateway_url}/auth/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }

        response = requests.post(url, json=payload)
        response.raise_for_status()
        self.token = response.json().get("access_token")
        return self.token
