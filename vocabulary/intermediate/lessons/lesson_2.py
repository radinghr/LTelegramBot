from vocabulary.base_lesson import BaseLesson
from ..lessons import lessons_count


class Lesson2(BaseLesson):
    lesson_level = 'inter'
    maximum_lesson = lessons_count
    lesson_num = 2
    vocabs = {
        "keen": "interested in sth and want to do it"
    }


lesson_2 = Lesson2()
