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
# Write a python function to check whether the two numbers differ at one bit position only or not.
#
# SOLUTION CODE
# ============================================
def is_Power_Of_Two (x): 

    return x and (not(x & (x - 1))) 

def differ_at_one_bit_pos(a,b): 

    return is_Power_Of_Two(a ^ b)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, expected):
    try:
        if validate_solution(differ_at_one_bit_pos(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



