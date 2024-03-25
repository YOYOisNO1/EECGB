import array
import bisect
import collections
import datetime
import functools
import heapq
import itertools
import math
import queue
import re
import string
import sys
from typing import Any, Dict, List, Optional, Set

# Question Prompt (NOT what is passed to the model)
# Write a function to replace blank spaces with any character in a string.
#
# SOLUTION CODE
# ============================================
def replace_blank(str1,char):

 str2 = str1.replace(' ', char)

 return str2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, char_arg1, expected):
    try:
        if validate_solution(replace_blank(
            str1, char_arg1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



