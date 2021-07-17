from vocabulary.base_lesson import BaseLesson
from vocabulary.intermediate.lessons import lessons_count


class VocabInterLesson3(BaseLesson):
    lesson_level = 'inter'
    maximum_lesson = lessons_count
    lesson_num = 3
    vocabs = {
        "definition": "an exact statement of what a word or phrase means",
        "provide": "give sth to sb or make sth available for sb",
        "avoid doing sth": "if you avoid doing sth, you try not to do it",
        "idiom": "a group of words with a special meaning",
        "entry": "one item that is written in a dictionary, list etc\.",
        "symbol": "a letter, number or sign that has a particular meaning",
        "syllable": "a part of word which contains vowel sound",
        "related (do sth)": "connected to sth",
        "build": "make sth bigger, increase sth",
        "style": "they way sth is written or spoken",
        "for instance": "SYN for example",
        "slang": "very informal words or phrases used in spoken language"
    }


vocab_inter_lesson_3 = VocabInterLesson3()
