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
# Write a function to calculate the number of digits and letters in a string.
#
# SOLUTION CODE
# ============================================
def dig_let(s):

 d=l=0

 for c in s:

    if c.isdigit():

        d=d+1

    elif c.isalpha():

        l=l+1

    else:

        pass

 return (l,d)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(dig_let(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



