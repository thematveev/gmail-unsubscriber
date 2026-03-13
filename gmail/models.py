from . import utils

class Message:
    def __init__(self, uid, markup, unsubscribe_info):
        self.uid = uid
        self.markup = markup
        self.unsubscribe_info = unsubscribe_info

    @classmethod
    def from_dict(cls, message_dict):
        return cls(
            uid=message_dict['id'],
            markup=utils.extract_body(message_dict['payload']),
            unsubscribe_info=utils.get_unsubscribe_headers(message_dict['payload'])
        )