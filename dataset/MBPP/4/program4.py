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
# Write a function to find the largest integers from a given list of numbers using heap queue algorithm.
#
# SOLUTION CODE
# ============================================
import heapq as hq

def heap_queue_largest(nums,n):

  largest_nums = hq.nlargest(n, nums)

  return largest_nums

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, n, expected):
    try:
        if validate_solution(heap_queue_largest(
            nums, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



