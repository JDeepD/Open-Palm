# MIT License

# Copyright (c) 2020 Jdeep

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
            return True
        except:
            return False

if __name__ == '__main__':
    body = """#Enter your email here """
    ml = Mail("Receiver mail", body,
              "sender mail", "********************")
    ml.send_mail()



