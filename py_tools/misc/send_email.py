import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email: str, receiver_email: str, password: str, subject: str, body: str) -> None:
    """Send an email using Yahoo's SMTP server."""
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as server:  # Use SMTP_SSL for Yahoo
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main() -> None:
    send_email(
        sender_email="clearcanvas@myyahoo.com",
        receiver_email="talk2ved11@gmail.com",
        password="WriteGoodCode@@",
        subject="Test Email",
        body="Hello, this is a test email.",
    )

if __name__ == '__main__':
    main()
