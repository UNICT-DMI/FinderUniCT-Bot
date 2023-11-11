"""
    main module
"""
from module.commands import start, report, help
from module.data import HELP, REPORT

from telegram import BotCommand, Update
from telegram.ext import filters, Application, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

async def add_commands(app: Application) -> None:
    """
        Adds a list of commands with their description to the bot

        Args:
            app (Application): the built application
    """
    commands = [
        BotCommand("start", "messaggio di benvenuto"),
        BotCommand("help", "ricevi aiuto sui comandi"),
        BotCommand("report", "segnala un problema"),
        BotCommand("login", "procedura di autenticazione")
    ]

    await app.bot.set_my_commands(commands)

def add_handlers(app: Application) -> None:
    """
        Adds all the handlers to the bot

        Args:
            app (Application): the built application
    """
    async def chatid(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=str(update.effective_chat.id)
        )

    handlers = [
        CommandHandler("start", start, filters.ChatType.PRIVATE),
        CommandHandler("chatid", chatid),
        CommandHandler("help", help, filters.ChatType.PRIVATE),
        MessageHandler(filters.Regex(HELP) & filters.ChatType.PRIVATE, help),
        CommandHandler("report", report),
        MessageHandler(filters.Regex(REPORT) & filters.ChatType.PRIVATE, report),
    ]

    app.add_handlers(handlers)

def main():
    app = ApplicationBuilder().token("TOKEN").build()
    add_commands(app)
    add_handlers(app)

    app.run_polling()

if __name__ == "__main__":
    main()
