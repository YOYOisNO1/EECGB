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
# Write a function to substract the elements of the given nested tuples.
#
# SOLUTION CODE
# ============================================
def substract_elements(test_tup1, test_tup2):

  res = tuple(tuple(a - b for a, b in zip(tup1, tup2))

   for tup1, tup2 in zip(test_tup1, test_tup2))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup1, test_tup2, expected):
    try:
        if validate_solution(substract_elements(
            test_tup1, test_tup2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



