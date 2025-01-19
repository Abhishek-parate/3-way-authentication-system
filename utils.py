import random
import string
from flask import flash

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def flash_messages(messages):
    for category, message in messages:
        flash(message, category)
