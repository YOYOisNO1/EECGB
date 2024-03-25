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
# Write a function to convert tuple to a string.
#
# SOLUTION CODE
# ============================================
def tup_string(tup1):

  str =  ''.join(tup1)

  return str

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tup1, expected):
    try:
        if validate_solution(tup_string(
            tup1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



