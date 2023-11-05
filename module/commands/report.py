"""/report command"""
from telegram import Update
from telegram.ext import CallbackContext

def report(update: Update, context: CallbackContext) -> None:
    """Called by the /report command
    Sends a report to the admin group

    Args:
        update: update event
        context: context passed by the handler
    """
