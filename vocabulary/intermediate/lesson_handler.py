from .lessons import import_modules


def add_lessons_handler(update):
    for module in import_modules:
        module.add_handler(update)

