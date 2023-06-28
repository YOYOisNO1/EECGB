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
# Write a function to verify validity of a string of parentheses.
#
# SOLUTION CODE
# ============================================
def is_valid_parenthese( str1):

        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}

        for parenthese in str1:

            if parenthese in pchar:

                stack.append(parenthese)

            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:

                return False

        return len(stack) == 0

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(is_valid_parenthese(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



