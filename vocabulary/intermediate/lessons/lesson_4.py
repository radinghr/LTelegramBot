from vocabulary.base_lesson import BaseLesson
from vocabulary.intermediate.lessons import lessons_count


class VocabInterLesson4(BaseLesson):
    lesson_level = 'inter'
    maximum_lesson = lessons_count
    lesson_num = 4
    vocabs = {
        "abbreviation": "a short form of a word\. tv is and abbreviation of televison",
        "capital letters": "A B C are capital letters",
        "pause": "a short period of time when sb stops talking",
        "separate": "keep people or thing away from each other",
        "list": "a series of names, items or numbers",
        "omit": "if you omit sth, you dont include it",
        "interrupt": "stop sth or sb so that it or they can not continue",
        "further": "more, extra",
        "details": "small pieces of information about sth in the place of sb/sth",
        "instead of sb/sth": "in the place of sb/sth",
        "connect": "put two or more things together",
        "such as": "you use suck as ro introduce an example"
    }


vocab_inter_lesson_4 = VocabInterLesson4()
