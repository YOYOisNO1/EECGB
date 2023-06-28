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
# Write a function to calculate the sum of the positive numbers of a given list of numbers using lambda function.
#
# SOLUTION CODE
# ============================================
def sum_positivenum(nums):

  sum_positivenum = list(filter(lambda nums:nums>0,nums))

  return sum(sum_positivenum)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(sum_positivenum(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



