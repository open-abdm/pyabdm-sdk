import os
from dotenv import load_dotenv

load_dotenv()  # Load env variables from .env

ENV = os.getenv("ENV", "sbx").lower()  # default to sandbox
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

GATEWAY_URLS = {
    "sandbox": "https://sandbox.abdm.gov.in/gateway",
    "production": "https://prod.abdm.gov.in/gateway"
}

GATEWAY_URL = GATEWAY_URLS.get(ENV)
