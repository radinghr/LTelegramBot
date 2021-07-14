from telegram import InlineKeyboardMarkup, InlineKeyboardButton


class BaseMenu:
    menu_pattern = None
    prev_menu = None

    @staticmethod
    def menu_keyboards() -> (list, None):
        """
        Return menu's keyboard
        :return:
        """
        return None

    @staticmethod
    def menu_message() -> str:
        """
        Return menu's message
        :return:
        """
        raise NotImplementedError("You should implement this function")

    def back_button(self) -> (list, None):
        """
        Return menu's back button or None
        :return:
        """
        if self.prev_menu is None:
            return None
        back_menu = [InlineKeyboardButton('◀️ Back️', callback_data=self.prev_menu)]
        return back_menu

    def next_button(self) -> (list, None):
        """
        Return menu's next button or None
        :return:
        """
        return None

    def menu_options(self) -> (list, None):
        """
        Return menu's options
        :return:
        """
        keyboard = self.menu_keyboards()
        if keyboard is not None:
            next_button = self.next_button()
            if next_button is not None:
                keyboard.append(next_button)
            back_button = self.back_button()
            if back_button is not None:
                keyboard.insert(0, back_button)
            return InlineKeyboardMarkup(keyboard)
        else:
            return None

    def menu_gui(self, update, context):
        pass

    def add_handler(self, updater, **kwargs):
        pass
