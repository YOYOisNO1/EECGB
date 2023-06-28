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
# Write a function to sort a given list of elements in ascending order using heap queue algorithm.
#
# SOLUTION CODE
# ============================================
import heapq as hq

def heap_assending(nums):

  hq.heapify(nums)

  s_result = [hq.heappop(nums) for i in range(len(nums))]

  return s_result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(heap_assending(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



