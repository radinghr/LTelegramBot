from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('vocabulary', callback_data='vocabulary')],
    ]
    return InlineKeyboardMarkup(keyboard)


def vocabulary_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('Intermediate', callback_data='vocab_inter')],
    ]
    return InlineKeyboardMarkup(keyboard)


def vocabulary_intermediate_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('Lesson 1', callback_data='vocab_inter_1')],
    ]
    return InlineKeyboardMarkup(keyboard)
