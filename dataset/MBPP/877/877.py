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
# Write a python function to sort the given string.
#
# SOLUTION CODE
# ============================================
def sort_string(str) : 

    str = ''.join(sorted(str)) 

    return (str) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(sort_string(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



