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
# Write a python function to find two distinct numbers such that their lcm lies within the given range.
#
# SOLUTION CODE
# ============================================
def answer(L,R): 

    if (2 * L <= R): 

        return (L ,2*L)

    else: 

        return (-1) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, r, expected):
    try:
        if validate_solution(answer(
            l, r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



