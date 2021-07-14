from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from bot_commands import start, main_menu, vocabulary_menu, inter_vocabulary_menu
import os


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    bot_token = os.getenv("BOT_TOKEN")
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(vocabulary_menu, pattern='vocabulary'))
    updater.dispatcher.add_handler(CallbackQueryHandler(inter_vocabulary_menu, pattern='Intermediate'))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
