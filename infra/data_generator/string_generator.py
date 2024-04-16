import random
import string


class StringGenerator:
    def __init__(self, length):
        self.length = length

    def string_generate(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(self.length))

    def number_generate(self):
        characters = string.digits
        return ''.join(random.choice(characters) for _ in range(self.length))

