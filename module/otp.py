"""
    OTP module.
"""
import os
import random
import smtplib
from email.mime.text import MIMEText

from module.data import MAIL_TEMPLATE

#: Define the following in settings.yaml
HOST = 'HOST'
USER = "USER"
PASSWORD = "PASSWORD"

class OTPException(Exception):
    pass

class OTPConnectionFailed(OTPException):
    pass

class OTPLoginFailed(OTPException):
    pass

class OTPNotAuthenticated(OTPException):
    pass

class OTPCodeNotSent(OTPException):
    pass

class OTPSender:
    """
        OTP sender class.

        Attributes:
            authenticated (bool): True if the user is authenticated, False otherwise.

        Methods:
            login() -> None: 
                Logs in to the SMTP server. Modifies the authenticated attribute.
            send(to: str) -> str | None:
                Sends a randomly generated OTP to the specified email address.
                Returns the OTP sent to the specified email address.
    """
    def __init__(self):
        try:
            self.__server = smtplib.SMTP_SSL(HOST, smtplib.SMTP_SSL_PORT)
        except Exception as e:
            raise OTPConnectionFailed('Connection failed.') from e

        self.authenticated = False
        self.login()

    def login(self) -> None:
        """
            Logs in to the SMTP server.

            Returns:
                None: check self.authenticated for login status.
        """
        if self.authenticated:
            return

        try:
            self.__server.login(USER, PASSWORD)
            self.authenticated = True
        except Exception as e:
            raise OTPLoginFailed('Login failed.') from e

    def send(self, to: str) -> str:
        """
            Sends a randomly generated OTP to the specified email address.

            Args:
                to (str): The email address of the recipient.

            Returns:
                str: The OTP sent to the specified email address.
        """
        if not self.authenticated:
            raise OTPNotAuthenticated('Not authenticated.')

        random.seed(os.urandom(64))
        otp = str(random.randint(100000, 999999))

        message = MIMEText(MAIL_TEMPLATE.format(otp=otp))
        message['From'] = USER
        message['To'] = to
        message['Subject'] = "FinderUniCT-Bot - Codice OTP"

        try:
            self.__server.send_message(message)
            return otp
        except Exception as e:
            raise OTPCodeNotSent('OTP code not sent.') from e
