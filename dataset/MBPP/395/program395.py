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
# Write a python function to find the first non-repeated character in a given string.
#
# SOLUTION CODE
# ============================================
def first_non_repeating_character(str1):

  char_order = []

  ctr = {}

  for c in str1:

    if c in ctr:

      ctr[c] += 1

    else:

      ctr[c] = 1 

      char_order.append(c)

  for c in char_order:

    if ctr[c] == 1:

      return c

  return None

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(first_non_repeating_character(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



