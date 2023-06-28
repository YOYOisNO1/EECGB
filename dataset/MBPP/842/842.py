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
# Write a function to find the number which occurs for odd number of times in the given array.
#
# SOLUTION CODE
# ============================================
def get_odd_occurence(arr, arr_size):

  for i in range(0, arr_size):

    count = 0

    for j in range(0, arr_size):

      if arr[i] == arr[j]:

        count += 1

    if (count % 2 != 0):

      return arr[i]

  return -1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, arr_size, expected):
    try:
        if validate_solution(get_odd_occurence(
            arr, arr_size),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



