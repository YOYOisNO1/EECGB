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
# Write a function to count all the distinct pairs having a difference of k in any array.
#
# SOLUTION CODE
# ============================================
def count_pairs(arr, n, k):

  count=0;

  for i in range(0,n):

    for j in range(i+1, n):

      if arr[i] - arr[j] == k or arr[j] - arr[i] == k:

        count += 1

  return count

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, k, expected):
    try:
        if validate_solution(count_pairs(
            arr, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



