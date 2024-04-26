import smtplib
from email.mime.text import MIMEText

subject = "Test"
body = "Hej Casper ring når du ser det her\nVenlig hilsen Casper"
sender = "persson1201@gmail.com"
recipients = ["klapssk@gmail.com", "stammis@hotmail.com"]
password = "ybyy qbxl xcsc ptuv +"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)