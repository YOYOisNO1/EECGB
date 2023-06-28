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
# Write a function to extract maximum and minimum k elements in the given tuple.
#
# SOLUTION CODE
# ============================================


def extract_min_max(test_tup, K):

  res = []

  test_tup = list(test_tup)

  temp = sorted(test_tup)

  for idx, val in enumerate(temp):

    if idx < K or idx >= len(temp) - K:

      res.append(val)

  res = tuple(res)

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, k, expected):
    try:
        if validate_solution(extract_min_max(
            test_tup, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



