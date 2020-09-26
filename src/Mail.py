import smtplib
from email.mime.text import MIMEText


class Mail:
    def __init__(self, receiver_mail, body, emailid, password):
        self.emailid = emailid
        # Constructs the receiver email address for entire class
        self.receiver_mail = receiver_mail
        # port number for Gmail is 587
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        # Email Id and Respective password
        self.server.login("{}".format(emailid), "{}".format(password))
        self.body = body

    def send_mail(self):
        self.message = MIMEText(self.body)
        self.message['From'] = self.emailid
        self.message['To'] = self.receiver_mail
        self.message['Subject'] = 'This is the subject of the a mail'
        try:
            self.server.send_message(self.message)
            print('Done')
        except:
            return ('There is some error. PLease check the email address again')


if __name__ == '__main__':
    body = """#Enter your email here """
    ml = Mail("receiver@gmail.com", body,
              "sender@gmail.com", "passwd_of_sender")
    ml.send_mail()
