"""Daily conference-deadline reminder.

Reads deadlines.json and sends an email when a deadline is exactly
14, 7, or 1 days away. Configuration comes from environment variables
(set as GitHub repository secrets in the workflow):

  SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, MY_EMAIL
"""
import json
import os
import smtplib
from datetime import date, datetime
from email.mime.text import MIMEText
from pathlib import Path

REMIND_DAYS = (14, 7, 1)


def main() -> None:
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ["SMTP_USER"]
    smtp_password = os.environ["SMTP_PASSWORD"]
    recipient = os.environ["MY_EMAIL"]

    deadlines = json.loads(Path("deadlines.json").read_text())
    today = date.today()

    for item in deadlines:
        deadline = datetime.strptime(item["deadline"], "%Y-%m-%d").date()
        days_left = (deadline - today).days
        if days_left not in REMIND_DAYS:
            continue

        subject = f"Reminder: {item['conference']} is in {days_left} days!"
        body = (
            f"Deadline reminder\n\n"
            f"{item['conference']}\n"
            f"Deadline: {deadline.isoformat()} ({days_left} days from today)\n\n"
            f"Sent automatically from the SE-conferences-and-journals repository."
        )
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = smtp_user
        msg["To"] = recipient

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, [recipient], msg.as_string())
        print(f"Sent reminder for {item['conference']} ({days_left} days left)")


if __name__ == "__main__":
    main()
