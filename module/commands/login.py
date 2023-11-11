"""
    /login command
"""
from telegram import Update
from telegram.ext import ContextTypes

from module.data import LOGIN_CMD_TEXT

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=LOGIN_CMD_TEXT
    )
