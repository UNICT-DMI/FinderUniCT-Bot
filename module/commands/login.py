"""
    /login mock command to test the login system
"""
from telegram import Update
from telegram.ext import CallbackContext

from module.data import LOGIN_CMD_TEXT

def login(update: Update, context: CallbackContext) -> None:
    """
        Called by the /login command.

        Theoretically, it should send an OTP to the student's email address
        that must be validated. 
        If this check is successfull the user is then logged in and registered
        in the database.

        Args:
            update: update event
            context: context passed by the handler
    """

    context.bot.sendMessage(
        chat_id=update.message.chat_id, text=LOGIN_CMD_TEXT
    )