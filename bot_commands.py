from bot_messages import (
    main_menu_message,
    vocabulary_menu_message,
)
from bot_keyboards import (
    main_menu_keyboard,
    vocabulary_menu_keyboard,
    vocabulary_intermediate_menu_keyboard,
)


def start(update, context):
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())


def main_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=main_menu_message(),
        reply_markup=main_menu_keyboard())


def vocabulary_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=vocabulary_menu_message(),
        reply_markup=vocabulary_menu_keyboard())


def inter_vocabulary_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=vocabulary_menu_message(),
        reply_markup=vocabulary_intermediate_menu_keyboard())
