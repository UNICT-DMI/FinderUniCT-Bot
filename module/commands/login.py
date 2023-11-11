"""
    /login command
"""
import hashlib

from telegram import Update
from telegram.ext import ContextTypes

from sqlalchemy import select
from data.db import Session
from data.db.models import User

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
    args = update.message.text.strip().split()[1:]

    if len(args) != 1:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Utilizzo sbagliato. /login <email>"
        )

        return

    email = args[0]
    if not email.endswith("@studium.unict.it"):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                "Questo bot e' solo per gli studenti di UNICT.\n"
                "Se sei uno studente controlla di aver scritto bene l'email "
                "(deve finire con @studium.unict.it)"
            )
        )

        return

    with Session() as session:
        stmt = select(User).where(User.chat_id == update.effective_chat.id)
        result = session.scalars(stmt).first()
        if result is None:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Non sei registrato, procedo alla registrazione.."
            )

            session.add(User(email=email, chat_id=update.effective_chat.id))
            session.commit()

            return

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sei gia' registrato! Controllo se i dati corrispondono..."
    )

    if result.chat_id != update.effective_chat.id:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Il chat_id non corrisponde..."
        )

        return

    email_digest = hashlib.sha256(email.encode()).hexdigest()
    if result.email != email_digest:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="L'email non corrisponde..."
        )

        return

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Bentornato!"
    )
