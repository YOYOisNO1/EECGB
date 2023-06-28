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
# Write a function to check if all values are same in a dictionary.
#
# SOLUTION CODE
# ============================================
def check_value(dict, n):

    result = all(x == n for x in dict.values()) 

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(dict, n, expected):
    try:
        if validate_solution(check_value(
            dict, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



