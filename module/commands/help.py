"""/help command"""
from telegram import Update
from telegram.ext import ContextTypes

from module.data.constants import HELP_CMD_TEXT

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
        Called by the /help command
        Sends a list of the avaible bot's commands

        Args:
            update: update event
            context: context passed by the handler
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=HELP_CMD_TEXT
    )
