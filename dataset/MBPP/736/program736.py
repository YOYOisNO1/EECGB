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
# Write a function to locate the left insertion point for a specified value in sorted order.
#
# SOLUTION CODE
# ============================================
import bisect

def left_insertion(a, x):

    i = bisect.bisect_left(a, x)

    return i

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, x, expected):
    try:
        if validate_solution(left_insertion(
            a, x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



