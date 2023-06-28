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
# Write a function to sort a list of elements using radix sort.
#
# SOLUTION CODE
# ============================================
def radix_sort(nums):

    RADIX = 10

    placement = 1

    max_digit = max(nums)



    while placement < max_digit:

      buckets = [list() for _ in range( RADIX )]

      for i in nums:

        tmp = int((i / placement) % RADIX)

        buckets[tmp].append(i)

      a = 0

      for b in range( RADIX ):

        buck = buckets[b]

        for i in buck:

          nums[a] = i

          a += 1

      placement *= RADIX

    return nums

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(radix_sort(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



