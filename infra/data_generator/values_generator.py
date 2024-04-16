import random

from faker import Faker


class FakeGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_name(self):
        return self.faker.name()

    def generate_first_name(self):
        return self.faker.first_name()

    def generate_last_name(self):
        return self.faker.last_name()

    def generate_email(self):
        return self.faker.ascii_email()

    def generate_string_with_length(self, length):
        return "".join(self.faker.random_letters(length=length))

    def generate_title(self):
        return " ".join(self.faker.text().split()[:random.randint(1, 3)])

    def generate_text(self):
        return self.faker.text()
