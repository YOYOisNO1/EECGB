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
# Write a function to replace characters in a string.
#
# SOLUTION CODE
# ============================================
def replace_char(str1,ch,newch):

 str2 = str1.replace(ch, newch)

 return str2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, ch, newch, expected):
    try:
        if validate_solution(replace_char(
            str1, ch, newch),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



