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
# Write a function to find numbers divisible by m and n from a list of numbers using lambda function.
#
# SOLUTION CODE
# ============================================
def div_of_nums(nums,m,n):

 result = list(filter(lambda x: (x % m == 0 and x % n == 0), nums)) 

 return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, m, n, expected):
    try:
        if validate_solution(div_of_nums(
            nums, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



