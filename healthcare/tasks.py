from celery import shared_task

@shared_task
def send_email_task(email):
    # Simulate sending email
    print(f"Sending email to {email}")
