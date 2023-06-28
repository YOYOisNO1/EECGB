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
# Write a function to find the median of two sorted arrays of same size.
#
# SOLUTION CODE
# ============================================
def get_median(arr1, arr2, n):

  i = 0

  j = 0

  m1 = -1

  m2 = -1

  count = 0

  while count < n + 1:

    count += 1

    if i == n:

      m1 = m2

      m2 = arr2[0]

      break

    elif j == n:

      m1 = m2

      m2 = arr1[0]

      break

    if arr1[i] <= arr2[j]:

      m1 = m2

      m2 = arr1[i]

      i += 1

    else:

      m1 = m2

      m2 = arr2[j]

      j += 1

  return (m1 + m2)/2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(arr1, arr2, n, expected):
    try:
        if validate_solution(get_median(
            arr1, arr2, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



