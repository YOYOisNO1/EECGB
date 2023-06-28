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
# Write a python function to find the length of the last word in a given string.
#
# SOLUTION CODE
# ============================================
def length_of_last_word(a): 

    l = 0

    x = a.strip() 

    for i in range(len(x)): 

        if x[i] == " ": 

            l = 0

        else: 

            l += 1

    return l 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, expected):
    try:
        if validate_solution(length_of_last_word(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



