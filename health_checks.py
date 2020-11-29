
#!/usr/bin/env python3
import psutil
import shutil
import socket
import emails
disk=shutil.disk_usage('/')
sender='automation@example.com'
reciever='student-04-581017bcfb77@example.com'
Body=' Please check your system and resolve the issue as soon as possible.'
usage_disk=(disk.free/disk.total)*100
memory=psutil.virtual_memory()
usage_cpu=psutil.cpu_percent(1)
if usage_cpu > 80:
        Subject='Error - CPU usage is over 80%'
        message=emails.generate_email1(sender, reciever, Subject, Body)
        emails.send_email(message)
if usage_disk < 20:
        Subject='Error - Available disk space is less than 20%'
        message=emails.generate_email1(sender, reciever, Subject, Body)
        emails.send_email(message)

print(memory[1])
if (memory[1]/(1024*1024)) < 500:
        Subject='Error - Available memory is less than 500MB'
        message=emails.generate_email1(sender, reciever, Subject, Body)
        emails.send_email(message)
try:
        socket.gethostbyname('localhost')
except:
        Subject='Error - localhost cannot be resolved to 127.0.0.1'
        message=emails.generate_email1(sender, reciever, Subject, Body)
        emails.send_email(message)