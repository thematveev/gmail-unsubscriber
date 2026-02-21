from googleapiclient.discovery import build
from .models import Message
import logging


logger = logging.getLogger(__name__)

class GmailClient:
    def __init__(self, creds):
        self.service = build('gmail', 'v1', credentials=creds)
        logger.debug('Service "gmail" created')

    def get_messages(self):
        result = self.service.users().messages().list(maxResults=500, userId='me').execute()
        messages = result.get('messages', [])
        logger.info(f'Messages received. Total {len(messages)} received!')
        return messages

    def get_message_by_id(self, message_id) -> Message | None:
        result = self.service.users().messages().get(userId='me', id=message_id).execute()
        msg = Message.from_dict(result) if result else None
        if msg:
            logger.info(f'Message with id {msg.uid} fetched')
        else:
            logger.info(f'Message with id {message_id} not found')
        return msg