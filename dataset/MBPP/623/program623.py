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
# Write a function to find the n-th power of individual elements in a list using lambda function.
#
# SOLUTION CODE
# ============================================
def nth_nums(nums,n):

 nth_nums = list(map(lambda x: x ** n, nums))

 return nth_nums

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, n, expected):
    try:
        if validate_solution(nth_nums(
            nums, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



