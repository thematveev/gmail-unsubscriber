from oauth.auth import run_authorization
from gmail.client import GmailClient
import logging_setup


logging_setup.setup_logging()

creds = run_authorization()
client = GmailClient(creds)
messages = client.get_messages()[:100]
for message in messages:
    msg = client.get_message_by_id(message['id'])
    print(msg.unsubscribe_info)
