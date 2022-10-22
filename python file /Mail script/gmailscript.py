#  a code to change an email and then resend it in reverse
# Author : Emmanuel Buruvuru 
# Date : 27 june 2022

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

smtp = smtplib.SMTP('mail.yahoo.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('emmauelburuvuru@yahoo.com', 'Nathaneil12')

# send our email message 'msg' to our boss
def message(subject="Python Notification", text=""):
    
    # build message contents
    msg = MIMEMultipart()
      
    # Add Subject
    msg['Subject'] = subject  
      
    # Add text contents
    msg.attach(MIMEText(text))  
  
    return msg
  
  
# Call the message function
msg = message("Good!", "Hi there!")
  
# Make a list of emails, where you wanna send mail
to = ["buruvuruemmanuel@gmail.com"]
  
# Provide some data to the sendmail function!
smtp.sendmail(from_addr="emmanuelburuvuru@gmail.com",
              to_addrs=to, msg=msg.as_string())
  
 # Finally, don't forget to close the connection
smtp.quit()

