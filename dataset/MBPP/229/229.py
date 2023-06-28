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
# Write a function to re-arrange the elements of the given array so that all negative elements appear before positive ones.
#
# SOLUTION CODE
# ============================================
def re_arrange_array(arr, n):

  j=0

  for i in range(0, n):

    if (arr[i] < 0):

      temp = arr[i]

      arr[i] = arr[j]

      arr[j] = temp

      j = j + 1

  return arr

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(re_arrange_array(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



