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
# Write a python function to calculate the number of odd days in a given year.
#
# SOLUTION CODE
# ============================================
def odd_days(N): 

    hund1 = N // 100

    hund4 = N // 400

    leap = N >> 2

    ordd = N - leap 

    if (hund1): 

        ordd += hund1 

        leap -= hund1 

    if (hund4): 

        ordd -= hund4 

        leap += hund4 

    days = ordd + leap * 2

    odd = days % 7

    return odd 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(odd_days(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



