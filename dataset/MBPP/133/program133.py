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
# Write a function to calculate the sum of the negative numbers of a given list of numbers using lambda function.
#
# SOLUTION CODE
# ============================================
def sum_negativenum(nums):

  sum_negativenum = list(filter(lambda nums:nums<0,nums))

  return sum(sum_negativenum)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(sum_negativenum(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



