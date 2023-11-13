"""
    /register command
"""
import re
import hashlib
from enum import Enum

from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, CommandHandler, ConversationHandler, filters

from sqlalchemy import select
from data.db import Session
from data.db.models import User

class State(Enum):
    """
        States of the register procedure
    """
    EMAIL = 1
    OTP = 2

async def register_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State:
    """
        Called by the /register command.

        Starts the registration procedure.

        Args:
            update: Update event
            context: context passed by the handler

        Returns:
            State: the next state of the conversation
    """

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Invia la tua email studium"
    )

    return State.EMAIL

async def email_checker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State | int:
    """
        Checks if the user isn't already registered.

        Args:
            update: Update event
            context: context passed by the handler

        Returns:
            State: the next state of the conversation
            int: constant ConversationHandler.END (if the user is already registered)
    """
    email = update.message.text.strip()
    email_digest = hashlib.sha256(email.encode()).hexdigest()

    with Session() as session:
        stmt = select(User).where((User.chat_id == update.effective_chat.id) | (User.email == email_digest))
        result = session.scalars(stmt).first()

    if result is not None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Sei gia' registrato!"
        )

        return ConversationHandler.END

    context.user_data["email"] = email
    context.user_data["otp"] = "123456"
    context.user_data["tries"] = 0

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Invia l'OTP che ti e' stato inviato all'email da te indicata"
    )

    return State.OTP

async def otp_checker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State | int:
    """
        Checks if the OTP sent to the email is valid.

        Args:
            update: Update event
            context: context passed by the handler

        Returns:
            State: returns State.OTP if the OTP wasn't correct.
            int: constant ConversationHandler.END (if the OTP was correct or too many wrong tries)
    """
    if context.user_data["tries"] >= 3:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hai esaurito il numero di tentativi, riprova piu' tardi"
        )

        return ConversationHandler.END

    otp = update.message.text.strip()
    if otp != context.user_data["otp"]:
        context.user_data["tries"] += 1

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="OTP non corretto, controlla la tua mail"
        )

        return State.OTP

    with Session() as session:
        session.add(User=context.user_data["email"], chat_id=update.effective_chat.id)
        session.commit()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Registrazione completata!"
    )

    return ConversationHandler.END

def register_conv_handler() -> ConversationHandler:
    """
        Creates the /register ConversationHandler.

        States of the command:
            - State.EMAIL: Waits for a text message containing the email (should match the regex)
            - State.OTP: Waits for a text message containing the OTP sent to the email address.

        Returns:
            ConversationHandler: the created handler
    """
    email_regex = re.compile(r"^[a-z]+\.[a-z]+@studium\.unict\.it$")
    otp_regex = re.compile(r"^\d{6}$")

    async def invalid_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Email non valida, riprova"
        )

        return State.EMAIL

    async def invalid_otp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="OTP non valido, riprova"
        )

        return State.OTP

    async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Registrazione annullata!"
        )

        return ConversationHandler.END

    return ConversationHandler(
        entry_points=[CommandHandler("register", register_entry)],
        states={
            State.EMAIL: [
                MessageHandler(filters.Regex(email_regex), email_checker),
                MessageHandler(filters.TEXT & ~filters.Regex(email_regex), invalid_email)
            ],
            State.OTP: [
                MessageHandler(filters.Regex(otp_regex), otp_checker),
                MessageHandler(filters.TEXT & ~filters.Regex(otp_regex), invalid_otp)
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
