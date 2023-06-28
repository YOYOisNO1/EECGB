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
# Write a function to extract the ranges that are missing from the given list with the given start range and end range values.
#
# SOLUTION CODE
# ============================================
def extract_missing(test_list, strt_val, stop_val):

  res = []

  for sub in test_list:

    if sub[0] > strt_val:

      res.append((strt_val, sub[0]))

      strt_val = sub[1]

    if strt_val < stop_val:

      res.append((strt_val, stop_val))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, strt_val, stop_val, expected):
    try:
        if validate_solution(extract_missing(
            test_list, strt_val, stop_val),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



