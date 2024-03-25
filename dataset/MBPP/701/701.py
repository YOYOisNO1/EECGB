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
# Write a function to find the equilibrium index of the given array.
#
# SOLUTION CODE
# ============================================
def equilibrium_index(arr):

  total_sum = sum(arr)

  left_sum=0

  for i, num in enumerate(arr):

    total_sum -= num

    if left_sum == total_sum:

      return i

    left_sum += num

  return -1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, expected):
    try:
        if validate_solution(equilibrium_index(
            arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



