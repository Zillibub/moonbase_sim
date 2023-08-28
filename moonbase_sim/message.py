@dataclass
class Message:
    """
    Class representing a message sent or received from Earth.
    """
    message_id: str
    content: str
    sent_at: str = datetime.datetime.now().isoformat()
    received_at: str = None

    def send_message(self, content):
        """
        Sends a message to Earth.
        """
        self.content = content
        self.sent_at = datetime.datetime.now().isoformat()

    def receive_message(self, content):
        """
        Receives a message from Earth.
        """
        self.content = content
        self.received_at = datetime.datetime.now().isoformat()

    def get_message(self):
        """
        Returns the message.
        """
        return {
            'message_id': self.message_id,
            'content': self.content,
            'sent_at': self.sent_at,
            'received_at': self.received_at
        }