from . import utils

class Message:
    def __init__(self, uid, markup):
        self.uid = uid
        self.markup = markup

    @classmethod
    def from_dict(cls, message_dict):
        return cls(
            uid=message_dict['id'],
            markup=utils.extract_body(message_dict['payload'])
        )