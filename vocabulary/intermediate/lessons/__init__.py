import os, glob

parent_dir = os.path.dirname(__file__)
lessons_count = len(glob.glob1(parent_dir, '*.py')) - 1

from .lesson_1 import lesson_1
from .lesson_2 import lesson_2
