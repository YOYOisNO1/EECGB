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
# Write a function to find the item with maximum frequency in a given list.
#
# SOLUTION CODE
# ============================================
from collections import defaultdict

def max_occurrences(nums):

    dict = defaultdict(int)

    for i in nums:

        dict[i] += 1

    result = max(dict.items(), key=lambda x: x[1]) 

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(max_occurrences(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



