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
# Write a python function to count the occurrence of a given character in a string.
#
# SOLUTION CODE
# ============================================
def count(s,c) : 

    res = 0 

    for i in range(len(s)) : 

        if (s[i] == c): 

            res = res + 1

    return res 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, c, expected):
    try:
        if validate_solution(count(
            s, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



