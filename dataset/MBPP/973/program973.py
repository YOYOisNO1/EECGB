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
# Write a python function to left rotate the string.
#
# SOLUTION CODE
# ============================================
def left_rotate(s,d):

    tmp = s[d : ] + s[0 : d]

    return tmp  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, d, expected):
    try:
        if validate_solution(left_rotate(
            s, d),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



