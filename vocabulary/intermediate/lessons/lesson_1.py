from vocabulary.base_lesson import BaseLesson
from vocabulary.intermediate.lessons import lessons_count


class VocabInterLesson1(BaseLesson):
    lesson_level = 'inter'
    lesson_num = 1
    maximum_lesson = lessons_count
    vocabs = {
        "foreign": "from a country that is not your own. a person from another country is a foreigner",
        "basic": "most important and necessary",
        "recognize": "know that sth is or who sb is because you have seen or heard them before",
        "go through sth": "read sth carefully from the beginning to end",
        "identify": "recognize and decide what sth is",
        "context": "the words before and after a new word/phrase that help you to understand the meaning",
        "keep record of sth": "write sth down to help you remember it",
        "formal": "we use formal language to appear serious or official, or in some situations where we don't know people well. OPP informal",
        "translation": "text has been changed from one language into another. translate V.",
        "repeat": "say sth again. repetition N.",
        "explain": "tell sb sth in a way that makes it clear or easy to understand. explanation N.",
        "pronounce": "make the sound of a word or letter. pronunciation N.",
        "function": "the purpose or job that sth is designed to do",
        "opportunity": "a time when it is possible to do th that you want to do. SYN chance",
        "experiment with sth": "try sth to see what result it has",
        "make mistakes": "not do mistakes",
        "revise": "study sth again. do revision N.",
        "method": "a way of doing sth",
        "work": "get or have the result you want"
    }


vocab_inter_lesson_1 = VocabInterLesson1()
