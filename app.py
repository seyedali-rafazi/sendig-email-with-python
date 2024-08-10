from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import config

message = MIMEMultipart()
message["from"] = "ali rfz"
message["to"] = "****************"
message["subject"] = "test email"
message.attach(MIMEText("Hello ali waht's up"))

with smtplib.SMTP(host="smtp.gmail.com" , port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config.username , config.password)
    smtp.send_message(message)
    print("sent ...")
    print("successful")
            
        
