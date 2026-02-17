from googleapiclient.discovery import build


class GmailClient:
    def __init__(self, creds):
        self.service = build('gmail', 'v1', credentials=creds)

    def get_messages(self):
        result = self.service.users().messages().list(maxResults=500, userId='me').execute()
        return result.get('messages', [])