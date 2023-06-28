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
# Write a function to count repeated items of a tuple.
#
# SOLUTION CODE
# ============================================
def count_tuplex(tuplex,value):  

  count = tuplex.count(value)

  return count

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tuplex, value_arg1, expected):
    try:
        if validate_solution(count_tuplex(
            tuplex, value_arg1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



