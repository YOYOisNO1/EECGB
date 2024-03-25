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
# Write a function to convert a roman numeral to an integer.
#
# SOLUTION CODE
# ============================================
def roman_to_int(s):

        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        int_val = 0

        for i in range(len(s)):

            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:

                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]

            else:

                int_val += rom_val[s[i]]

        return int_val

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(roman_to_int(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



