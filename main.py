"""main module"""
from telegram import BotCommand
from telegram.ext import CommandHandler, MessageHandler, Updater, Dispatcher, Filters

from module.commands import start, report, help_cmd
from module.data import HELP, REPORT

def add_commands(up: Updater) -> None:
    """Adds list of commands with their description to the boy

    Args:
        up(Updater): supplied Updater
    """
    commands = [
        BotCommand("start", "messaggio di benvenuto"),
        BotCommand("help", "ricevi aiuto sui comandi"),
        BotCommand("report", "segnala un problema")
    ]
    up.bot.set_my_commands(commands=commands)

def add_handlers(dp:Dispatcher) -> None:
    """Adds all the handlers the bot will react to

    Args:
        dp:suppplied Dispatcher
    """

    dp.add_handler(CommandHandler("start", start, Filters.chat_type.private))
    dp.add_handler(CommandHandler("chatid", lambda u, c: u.message.reply_text(str(u.message.chat_id))))
    dp.add_handler(CommandHandler("help", help_cmd, Filters.chat_type.private))
    dp.add_handler(MessageHandler(Filters.regex(HELP) & Filters.chat_type.private, help_cmd))
    dp.add_handler(CommandHandler("report", report))
    dp.add_handler(MessageHandler(Filters.regex(REPORT) & Filters.chat_type.private, report))
    dp.add_handler(CommandHandler("chatid", lambda u, c: u.message.reply_text(str(u.message.chat_id))))

def main() -> None:
    """Main function"""
    updater = Updater()
    add_commands(updater)
    add_handlers(updater.dispatcher)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
