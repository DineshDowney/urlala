import random
import string

class short:
    token_size=6

    def __init__(self,token_size=None):
        self.token_size=5

    def create_token(self):
        word=string.ascii_letters
        return ''.join(random.choice(word) for i in range(self.token_size))