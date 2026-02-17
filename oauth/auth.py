from google.auth.transport.requests import Request
from .scopes import SCOPES
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os

def _perform_authorization():
    flow = InstalledAppFlow.from_client_secrets_file(
        "./artifacts/credentials.json",
        scopes=SCOPES
    )

    creds = flow.run_local_server(port=0)
    return creds


def _save_token(creds):
    with open("./token.json", "w") as token:
        token.write(creds.to_json())


def run_authorization():
    if os.path.exists("./token.json"):
        creds = Credentials.from_authorized_user_file(
            "./token.json", scopes=SCOPES )
        if not creds.valid:
            creds.refresh(Request())
    else:
        creds = _perform_authorization()
    _save_token(creds)
    return creds