from oauth.auth import run_authorization
from gmail.client import GmailClient

creds = run_authorization()
client = GmailClient(creds)
print(client.get_messages())
