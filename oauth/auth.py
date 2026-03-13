from google.auth.transport.requests import Request
from .scopes import SCOPES
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os
from logging_setup import setup_logging

logger = setup_logging()

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
    logger.info('Auth process started')
    if os.path.exists("./token.json"):
        logger.info('Saved token exists')
        creds = Credentials.from_authorized_user_file(
            "./token.json", scopes=SCOPES )
        if not creds.valid:
            logger.info('Saved token expired, refreshing...')
            creds.refresh(Request())
    else:
        logger.info('Saved token not exists, performing full auth')
        creds = _perform_authorization()

    logger.info('Auth performed')
    _save_token(creds)
    logger.info('Auth token saved')
    return creds