#
#
#
#


# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
  
# creates SMTP session
s = smtplib.SMTP('mail.yahoo.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("emmanuelbururvuru@yahoo.com", "Nathaneil12")
  
# message to be sent
message = "You are right"
  
# sending the mail
s.sendmail("emmanuelbururvuru@yahoo.com", "20750194@student.curtin.edu.au", message)
  
# terminating the session
s.quit()