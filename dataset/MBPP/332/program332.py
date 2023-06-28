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
# Write a function to count character frequency of a given string.
#
# SOLUTION CODE
# ============================================
def char_frequency(str1):

    dict = {}

    for n in str1:

        keys = dict.keys()

        if n in keys:

            dict[n] += 1

        else:

            dict[n] = 1

    return dict

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(char_frequency(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



