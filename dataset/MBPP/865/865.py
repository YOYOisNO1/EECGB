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
# Write a function to print n-times a list using map function.
#
# SOLUTION CODE
# ============================================
def ntimes_list(nums,n):

    result = map(lambda x:n*x, nums) 

    return list(result)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, n, expected):
    try:
        if validate_solution(ntimes_list(
            nums, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



