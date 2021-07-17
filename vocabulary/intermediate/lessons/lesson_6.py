from vocabulary.base_lesson import BaseLesson
from vocabulary.intermediate.lessons import lessons_count


class VocabInterLesson6(BaseLesson):
    lesson_level = 'inter'
    maximum_lesson = lessons_count
    lesson_num = 6
    vocabs = {
        "see sb as sth": "imagine or think of sb in a particular way",
        "character": "the qualities that sb different from other people",
        "ambitious": "an ambitious person want to be successful, to have power, etc",
        "outgoing": "friendly and interested in other people and new experiences",
        "generous": "always ready to give people thing or to spend money",
        "confident": "feeling sure about your own ability",
        "patient": "able to stay calm and wait for sth/sb",
        "practical": "making sensible decisions and good at dealing with problems",
        "organized": "good at planning and arranging thing",
        "hard-working": "able to work with effort and for a long time",
        "sensible": "able to think carefully about sth and do the right thing",
        "shy": "not able to talk easily to people you do not know",
        "dull": "not interested or exciting",
        "cheerful": "feeling happy",
        "easy-going": "relaxed and not worried by what what others do",
        "energy": "the ability to be very active without getting tired",
        "responsible": "able to act sensibly and intelligently"
    }


vocab_inter_lesson_6 = VocabInterLesson6()
