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
# Write a function to convert a tuple of string values to a tuple of integer values.
#
# SOLUTION CODE
# ============================================
def tuple_int_str(tuple_str):

    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tuple_str, expected):
    try:
        if validate_solution(tuple_int_str(
            tuple_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



