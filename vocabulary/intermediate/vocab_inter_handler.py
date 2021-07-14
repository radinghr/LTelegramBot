from telegram import InlineKeyboardButton
from telegram.ext import CallbackQueryHandler
from core.base_menu import BaseMenu
from .lesson_handler import add_lessons_handler


class VocabIntermediateMainMenu(BaseMenu):
    menu_pattern = "vocab_inter"

    @staticmethod
    def menu_keyboards() -> (list, None):
        keyboard = [
            [InlineKeyboardButton('Lesson 1', callback_data='inter_1')],
        ]
        return keyboard

    @staticmethod
    def menu_message():
        return 'Choose your lesson:'

    def menu_gui(self, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text=self.menu_message(),
            reply_markup=self.menu_options())

    def add_handler(self, update, prev_menu=None):
        self.prev_menu = prev_menu
        update.dispatcher.add_handler(CallbackQueryHandler(self.menu_gui, pattern=self.menu_pattern))
        add_lessons_handler(update)


vocab_inter_menu = VocabIntermediateMainMenu()
