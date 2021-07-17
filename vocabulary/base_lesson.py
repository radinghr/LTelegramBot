from telegram import InlineKeyboardButton
from telegram.ext import CallbackQueryHandler

from core.base_menu import BaseMenu


class BaseLesson(BaseMenu):
    lesson_level = None
    lesson_num = None
    maximum_lesson = 100
    vocabs = {}

    def menu_message(self):
        title = f'*Lesson {self.lesson_num}:*'
        words = ''.join('\r\n*{}*:{}'.format(key, val) for key, val in self.vocabs.items())
        return title + words

    def back_button(self) -> (list, None):
        """
        Return menu's back button or None
        :return:
        """
        if self.lesson_num <= 1:
            return None
        prev_data = self.lesson_level + "_" + str(self.lesson_num - 1)
        back_menu = [InlineKeyboardButton('◀️ Previous', callback_data=prev_data)]
        return back_menu

    def next_button(self) -> (list, None):
        """
        Return menu's back button or None
        :return:
        """
        if self.lesson_num >= self.maximum_lesson:
            return None
        next_data = self.lesson_level + "_" + str(self.lesson_num + 1)
        back_menu = [InlineKeyboardButton('Next ➡️', callback_data=next_data)]
        return back_menu

    @staticmethod
    def menu_keyboards() -> (list, None):
        from main_handler import main_menu
        keyboard = [
            [InlineKeyboardButton('Main Menu', callback_data=main_menu.menu_pattern)],
        ]
        return keyboard

    def menu_gui(self, update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text=self.reformat_texts(self.menu_message()),
            reply_markup=self.menu_options(),
            parse_mode='MarkdownV2')

    def add_handler(self, update, prev_menu=None):
        self.menu_pattern = self.lesson_level + "_" + str(self.lesson_num)
        update.dispatcher.add_handler(CallbackQueryHandler(self.menu_gui, pattern=self.menu_pattern))
