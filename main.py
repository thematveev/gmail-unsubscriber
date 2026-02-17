from oauth.auth import run_authorization
from gmail.client import GmailClient

creds = run_authorization()
client = GmailClient(creds)
messages = client.get_messages()[:10]
for message in messages:
    print("Message:", message['id'])
    msg = client.get_message_by_id(message['id'])
    if msg['payload']['mimeType'] == 'text/html':
        print(msg['payload'])
