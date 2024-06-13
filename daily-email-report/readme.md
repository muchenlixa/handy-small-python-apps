A basic Python script using the smtplib module to send an email with a daily report. 

This script assumes you have an SMTP server to send emails through, such as Gmail, and that you're okay with storing your email credentials in the script (although it's not recommended for security reasons).

Make sure to replace "recipient@example.com", "your_email@example.com", "your_email_password", "smtp.example.com", and 587 with your recipient's email address, your email address, your email password, your SMTP server address, and SMTP server port respectively.

This script can be scheduled to run daily using tools like cron on Unix-like systems or Task Scheduler on Windows.