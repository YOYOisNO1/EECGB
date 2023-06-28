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
# Write a function to find the previous palindrome of a specified number.
#
# SOLUTION CODE
# ============================================
def previous_palindrome(num):

    for x in range(num-1,0,-1):

        if str(x) == str(x)[::-1]:

            return x

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num, expected):
    try:
        if validate_solution(previous_palindrome(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



