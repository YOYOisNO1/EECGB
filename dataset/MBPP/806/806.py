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
# Write a function to find maximum run of uppercase characters in the given string.
#
# SOLUTION CODE
# ============================================
def max_run_uppercase(test_str):

  cnt = 0

  res = 0

  for idx in range(0, len(test_str)):

    if test_str[idx].isupper():

      cnt += 1

    else:

      res = cnt

      cnt = 0

  if test_str[len(test_str) - 1].isupper():

    res = cnt

  return (res)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_str, expected):
    try:
        if validate_solution(max_run_uppercase(
            test_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



