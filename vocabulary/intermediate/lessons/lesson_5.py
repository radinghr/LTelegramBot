from vocabulary.base_lesson import BaseLesson
from ..lessons import lessons_count


class Lesson5(BaseLesson):
    lesson_level = 'inter'
    maximum_lesson = lessons_count
    lesson_num = 5
    vocabs = {
        "male": "Men and boys are male",
        "dark skin": "OPP pale/fair skin",
        "broad": "larger from side to side",
        "appearance": "the way that sb or sth looks or seems",
        "in a good/bad shape": "in good/bad physical condition",
        "(sun)tan": "when you have a (sun)tan you skin is brown from the sun",
        "medium build": "not big or small, not fat or thin ALSO of medium build",
        "be pregnant": "if a woman is pregnant, she has baby growing in her body",
        "medium height": "not tall or short",
        "at the time": "then",
        "smooth": "with a completely flat surface",
        "figure": "the shape of the body specially that of a woman",
        "hairstyle": "the way that your hair is cut and arranged",
        "neat": "tidy and carefully arranged",
        "contact lenses": "small round pieces of plastic you wear in your eyes to help you see better",
        "tell": "know or guess"
    }


lesson_5 = Lesson5()
