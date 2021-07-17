from vocabulary.base_lesson import BaseLesson
from ..lessons import lessons_count


class Lesson2(BaseLesson):
    lesson_level = 'inter'
    maximum_lesson = lessons_count
    lesson_num = 2
    vocabs = {
        "keen": "interested in sth and want to do it",
        "motivated": "if you are motivated(to do sth), you realy want to do sth",
        "find it difficult to (do sth)": "be difficult for sb",
        "after a while": "after a period of time",
        "get better": "get better",
        "express": "say or show what think or feel",
        "effectively": "in a way that gives you the result you want",
        "obvious": "easy to see and understand",
        "encouraging": "if sth/sb is encouraging, they give you hope and make you want to continue",
        "slow down": "start to go more slowly",
        "be aware of sth": "if you are aware of sth, you know about it",
        "frustrating": "making you angry because you can not be successful at sth you want to do",
        "goal": "sth you want to be able to do in the future",
        "native speaker": "sb who speak a language as their first language",
        "expand": "become bigger or make sth bigger",
        "a (wide) range (of sth)": "a (large) number of different things",
        "complex": "having a lot of details that make sth difficult",
        "fluent": "able to speak easily and well",
        "in detail": "fully and including a lot of information",
        "suitable": "right for sth or sb",
        "achieve": "do or finish sth well after trying hard",
        "be to do with sth/sb": "be connected with sth/sb"
    }


lesson_2 = Lesson2()
