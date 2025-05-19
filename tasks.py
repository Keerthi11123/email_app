# tasks.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from celery_config import celery  # Use the separate Celery config

@celery.task
def send_email_task(sender, password, to, subject, body):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
            print(f"✅ Email sent to {to}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
