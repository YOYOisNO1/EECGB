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
# Write a function to find the next smallest palindrome of a specified number.
#
# SOLUTION CODE
# ============================================
import sys

def next_smallest_palindrome(num):

    numstr = str(num)

    for i in range(num+1,sys.maxsize):

        if str(i) == str(i)[::-1]:

            return i

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num, expected):
    try:
        if validate_solution(next_smallest_palindrome(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



