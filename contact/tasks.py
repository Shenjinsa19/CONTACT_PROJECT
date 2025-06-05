import logging
from celery import shared_task
from django.core.mail import send_mail
logger = logging.getLogger(__name__)
@shared_task
def send_contact_email(name, email, message):
    logger.info(f"Sending contact email from {name} <{email}>")
    send_mail(
        f"New Contact Message from {name}",
        f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
        'spmacavity@gmail.com',
        ['spmacavity@gmail.com'],
        fail_silently=False,
    )
    logger.info(f"Confirmation email will be sent to {email}")
    send_mail(
        "Thank you for contacting us!",
        f"Hi {name},\n\nThank you for reaching out. We have received your message.\n\nBest regards,\nTeam",
        'spmacavity@gmail.com',
        [email],
        fail_silently=False,
    )
    logger.info("Emails sent successfully")
