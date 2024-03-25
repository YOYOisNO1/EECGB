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
# Write a function to find number of odd elements in the given list using lambda function.
#
# SOLUTION CODE
# ============================================
def count_odd(array_nums):

   count_odd = len(list(filter(lambda x: (x%2 != 0) , array_nums)))

   return count_odd

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(array_nums, expected):
    try:
        if validate_solution(count_odd(
            array_nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



