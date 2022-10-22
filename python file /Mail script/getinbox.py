# Get inbox 

import imaplib
import email

host = "imap.mail.yahoo.com"

def get_inbox():
    mail = imaplib.IMAP4_SSL(host) 
    mail.login('emmanuelburuvuru@yahoo.com','Nathaneil12')
    mail.select('inbox')

    searched_data = mail.search(None, 'UNSEEN') 

    print(searched_data) 

if __name__ == "__main__":
    returned = get_inbox()
    print(returned)