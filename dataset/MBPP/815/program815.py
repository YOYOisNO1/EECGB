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
# Write a function to sort the given array without using any sorting algorithm. the given array consists of only 0, 1, and 2.
#
# SOLUTION CODE
# ============================================
def sort_by_dnf(arr, n):

  low=0

  mid=0

  high=n-1

  while mid <= high:

    if arr[mid] == 0:

      arr[low], arr[mid] = arr[mid], arr[low]

      low = low + 1

      mid = mid + 1

    elif arr[mid] == 1:

      mid = mid + 1

    else:

      arr[mid], arr[high] = arr[high], arr[mid]

      high = high - 1

  return arr

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(sort_by_dnf(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



