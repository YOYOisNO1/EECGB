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
# Write a function to sort a list in increasing order by the last element in each tuple from a given list of non-empty tuples.
#
# SOLUTION CODE
# ============================================
def last(n):

   return n[-1]

def sort_list_last(tuples):

  return sorted(tuples, key=last)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tuples, expected):
    try:
        if validate_solution(last(
            tuples),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



