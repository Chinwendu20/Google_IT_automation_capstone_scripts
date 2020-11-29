#!/usr/bin/env python3
import emails
import reports
sender='automation@example.com'
reciever='student-04-581017bcfb77@example.com'
Subject='Upload Completed - Online Fruit Store'
Body='All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
attachment_path='/tmp/processed.pdf'
if __name__=='__main__':
        message=emails.generate_email(sender, reciever, Subject, Body, attachment_path)
        emails.send_email(message)