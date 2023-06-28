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
# Write a function to find the kth element in the given array.
#
# SOLUTION CODE
# ============================================
def kth_element(arr, n, k):

  for i in range(n):

    for j in range(0, n-i-1):

      if arr[j] > arr[j+1]:

        arr[j], arr[j+1] == arr[j+1], arr[j]

  return arr[k-1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, k, expected):
    try:
        if validate_solution(kth_element(
            arr, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



