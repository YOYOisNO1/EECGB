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
# Write a python function to count characters at same position in a given string (lower and uppercase characters) as in english alphabet.
#
# SOLUTION CODE
# ============================================
def count_char_position(str1): 

    count_chars = 0

    for i in range(len(str1)):

        if ((i == ord(str1[i]) - ord('A')) or 

            (i == ord(str1[i]) - ord('a'))): 

            count_chars += 1

    return count_chars 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(count_char_position(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



