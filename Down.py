#!/usr/bin/env python
import pantilthat
import time
import smtplib
from email.mime.text import MIMEText

angle = pantilthat.get_pan()
pantilthat.pan(angle+5)

msg = MIMEText("Camera is going down")
msg['Subject'] = "Camera Status"
msg['From'] = "jimmy.python@outlook.com"
msg['To'] = "yinyouyang.byyy@gmail.com"
s = smtplib.SMTP('smtp-mail.outlook.com', 587)
s.set_debuglevel(1)
s.ehlo()
s.starttls()
s.login("jimmy.python@outlook.com", "12345qwert")
s.send_message(msg)
s.quit()
