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
# Write a function to extract specified size of strings from a give list of string values.
#
# SOLUTION CODE
# ============================================
def extract_string(str, l):

    result = [e for e in str if len(e) == l] 

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, l, expected):
    try:
        if validate_solution(extract_string(
            str, l),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



