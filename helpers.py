import random
import string

def generate_random_email():
    domain = random.choice(["mail.ru", "gmail.com", "yandex.ru"])
    prefix = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{prefix}@{domain}"