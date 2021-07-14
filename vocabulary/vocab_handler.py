from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton
from core.base_menu import BaseMenu
from .intermediate.vocab_inter_handler import vocab_inter_menu


class VocabMainMenu(BaseMenu):
    menu_pattern = "vocabulary"

    @staticmethod
    def menu_message():
        return 'Choose your level:'

    @staticmethod
    def menu_keyboards() -> (list, None):
        keyboard = [
            [InlineKeyboardButton('Intermediate', callback_data=vocab_inter_menu.menu_pattern)],
        ]
        return keyboard

    def menu_gui(self, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text=self.menu_message(),
            reply_markup=self.menu_options())

    def add_handler(self, update, prev_menu=None):
        self.prev_menu = prev_menu
        update.dispatcher.add_handler(CallbackQueryHandler(self.menu_gui, pattern=self.menu_pattern))
        vocab_inter_menu.add_handler(update, prev_menu=self.menu_pattern)


vocab_main_menu = VocabMainMenu()
