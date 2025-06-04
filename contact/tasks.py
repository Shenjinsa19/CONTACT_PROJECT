from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_contact_email(name, email, message):
    subject = f"New Contact Message from {name}"
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    send_mail(
        subject,
        body,
        'spmacavity@gmail.com.com',  # replace with your from-email
        ['recipient@example.com'],  # replace with recipient(s)
        fail_silently=False,
    )
