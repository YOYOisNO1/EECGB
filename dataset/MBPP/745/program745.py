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
# Write a function to find numbers within a given range where every number is divisible by every digit it contains.
#
# SOLUTION CODE
# ============================================
def divisible_by_digits(startnum, endnum):

    return [n for n in range(startnum, endnum+1) \

                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(startnum, endnum, expected):
    try:
        if validate_solution(divisible_by_digits(
            startnum, endnum),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



