"""This function will be used for sending mails"""   # noqa E501 pylint: disable=invalid-name


import smtplib
from email.mime.text import MIMEText


class Mail:  # pylint: disable=all
    """This class will handle the sending of mails. It has the
    following methods:
    1. constructor(__init__) which takes in the following parameters
       as input:
            (i) receiver_mail ---> Email Id of the receiver
            (ii) body ----> The body of the mail.
            (iii) emailid ----> Email id of the sender
            (iv) password ----> password of the sender's mail id

    2. `send_mail()`. This does not take any parameter.
        Its task is to successfully send the mail.
        If the mail is successfully sent, it returns True.
        Else it returns False.
    """
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
        """See class docstrings"""
        self.message = MIMEText(self.body)
        self.message['From'] = self.emailid
        self.message['To'] = self.receiver_mail
        self.message['Subject'] = 'This is the subject of the a mail'
        try:
            self.server.send_message(self.message)
            return True
        except:  # noqa
            return False


# if __name__ == '__main__':
#     Body = """#Enter your email here """
#     ml = Mail("Receiver mail", Body,
#               "sender mail", "********************")
#     ml.send_mail()
