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
# Write a function to find whether all the given tuples have equal length or not.
#
# SOLUTION CODE
# ============================================
def find_equal_tuple(Input, k):

  flag = 1

  for tuple in Input:

    if len(tuple) != k:

      flag = 0

      break

  return flag

def get_equal(Input, k):

  if find_equal_tuple(Input, k) == 1:

    return ("All tuples have same length")

  else:

    return ("All tuples do not have same length")

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(input, k, expected):
    try:
        if validate_solution(find_equal_tuple(
            input, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



