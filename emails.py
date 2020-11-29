#!/usr/bin/env python3
from email.message import EmailMessage
import os
import smtplib
def generate_email(sender, reciever, Subject, Body, attachment_path):
        message=EmailMessage()
        message['From']=sender
        message['To']=reciever
        message['Subject']=Subject
        message.set_content(Body)
        with open(attachment_path, 'rb') as attachment:
                message.add_attachment(attachment.read(),maintype='application',subtype='json',filename=os.path.basename(attachment_path))
        attachment.close()
        return message
def generate_email1(sender, reciever, Subject, Body):
        message=EmailMessage()
        message['From']=sender
        message['To']=reciever
        message['Subject']=Subject
        message.set_content(Body)
        return message
def send_email(message):
        mail_server=smtplib.SMTP('localhost')
        mail_server.send_message(message)
        mail_server.quit()