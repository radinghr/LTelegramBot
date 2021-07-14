from telegram import InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackQueryHandler
from vocabulary.vocab_handler import vocab_main_menu
from core.base_menu import BaseMenu


class MainMenu(BaseMenu):
    menu_pattern = "main"

    @staticmethod
    def menu_message() -> str:
        return 'This bot will help you to improve your english vocabulary.\r\n What skill do you want to improve? ' \
               'Choose from options:\r\nDeveloped by @raadingh'

    @staticmethod
    def menu_keyboards() -> (list, None):
        keyboard = [
            [InlineKeyboardButton('vocabulary', callback_data=vocab_main_menu.menu_pattern)],
        ]
        return keyboard

    def menu_gui(self, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text=self.menu_message(),
            reply_markup=self.menu_options())

    def add_handler(self, updater, dp=None):
        dp.add_handler(CommandHandler("start", self.start_menu))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_gui, pattern=self.menu_pattern))
        vocab_main_menu.add_handler(updater)

    def start_menu(self, update, context):
        update.message.reply_text(self.menu_message(),
                                  reply_markup=self.menu_options())


main_menu = MainMenu()
