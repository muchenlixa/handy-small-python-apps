import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))

def generate_daily_report():
    # Generate your daily report here
    today = datetime.date.today()
    report = f"Daily Report - {today}\n\n"
    report += "This is where you put your daily report content."

    return report

if __name__ == "__main__":
    # Email configuration
    subject = "Daily Report"
    to_email = "recipient@example.com"
    from_email = "your_email@example.com"
    password = "your_email_password"
    smtp_server = "smtp.example.com"  # SMTP server address
    smtp_port = 587  # SMTP server port (587 for TLS)

    # Generate daily report
    body = generate_daily_report()

    # Send email
    send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port)