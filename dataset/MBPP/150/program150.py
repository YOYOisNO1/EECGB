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
# Write a python function to find whether the given number is present in the infinite sequence or not.
#
# SOLUTION CODE
# ============================================
def does_contain_b(a,b,c): 

    if (a == b): 

        return True

    if ((b - a) * c > 0 and (b - a) % c == 0): 

        return True

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, expected):
    try:
        if validate_solution(does_contain_b(
            a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



