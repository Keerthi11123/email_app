# app.py
from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
from pytz import timezone, utc
from tasks import send_email_task
import smtplib

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sender = request.form["sender"]
        password = request.form["password"]
        to = request.form["receiver"]
        subject = request.form["subject"]
        body = request.form["body"]
        send_at = request.form["send_at"]  # format: "YYYY-MM-DDTHH:MM"

        try:
            # Authenticate Gmail credentials
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(sender, password)

            # Convert local time to UTC for Celery
            local_tz = timezone("America/New_York")  # adjust as needed
            send_time_local = datetime.fromisoformat(send_at)
            send_time_utc = local_tz.localize(send_time_local).astimezone(utc)

            # Schedule the task
            send_email_task.apply_async(
                args=[sender, password, to, subject, body],
                eta=send_time_utc
            )

            flash("✅ Email scheduled successfully!", "success")

        except smtplib.SMTPAuthenticationError:
            flash("❌ Authentication failed: Invalid email or app password.", "danger")
        except Exception as e:
            flash(f"❌ Failed to schedule email: {str(e)}", "danger")

        return redirect("/")

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
