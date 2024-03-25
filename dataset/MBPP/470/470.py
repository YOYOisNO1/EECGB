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
# Write a function to find the pairwise addition of the elements of the given tuples.
#
# SOLUTION CODE
# ============================================
def add_pairwise(test_tup):

  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, expected):
    try:
        if validate_solution(add_pairwise(
            test_tup),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



