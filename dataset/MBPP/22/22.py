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
# Write a function to find the first duplicate element in a given array of integers.
#
# SOLUTION CODE
# ============================================
def find_first_duplicate(nums):

    num_set = set()

    no_duplicate = -1



    for i in range(len(nums)):



        if nums[i] in num_set:

            return nums[i]

        else:

            num_set.add(nums[i])



    return no_duplicate

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(find_first_duplicate(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



