from django.core.mail import send_mail
from goodreads.celery import app


def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'rafiqovabulqosim@gmaoil.com',
        recipient_list
    )
    pass
