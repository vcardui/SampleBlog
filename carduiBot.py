# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 27th, 2025
# | Last update..: April 30th, 2025
# | WhatIs.......: EmailBot - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# How to Send HTML Emails in Python using SMTP and email API: https://mailtrap.io/blog/python-send-html-email/#Send-HTML-emails-to-multiple-recipients

# ------------------------- Libraries -------------------------
import time  # time.sleep(1)
import datetime  # datetime.datetime.now()

import smtplib #
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------------------- Variables -------------------------
# Time
now = datetime.datetime.now()
todayDate = now.strftime("%d/%m/%Y")
nowTime = now.strftime("%H:%M")
emailSubject = f"Email test at {todayDate} at {nowTime}"

# SMTP Email connection
carduibotEmail = "carduibot@gmail.com"
carduibotPassword = "dmfq ukdf kmcl wgdp"

myEmail = "vanessa@reteguin.com"
# -------------------------- Class ----------------------------
class EmailBot:
    def __init__(self, data):
        self.data = data
        self.email_body = ""

        with open("mail/submittedData.html") as originalHTML:
            htmlTemplate = originalHTML.read()
            for i in self.data:
                print(f"{i}: {data[i]}")
                htmlTemplate = htmlTemplate.replace(f"[{i}]", f"{data[i]}")

            self.email_body = htmlTemplate


    def sendMail(self):
        # Create email message container
        email = MIMEMultipart('alternative')
        email['Subject'] = emailSubject
        email['From'] = carduibotEmail
        email['To'] = myEmail

        # Record the MIME type email's HTML part
        HTMLPart = MIMEText(self.email_body, 'html')
        email.attach(HTMLPart)

        # Send message with smtplib
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=carduibotEmail, password=carduibotPassword)
        connection.sendmail(from_addr=carduibotEmail,
                            to_addrs=myEmail,
                            msg=email.as_string())
        connection.close()
        print("Email sent")