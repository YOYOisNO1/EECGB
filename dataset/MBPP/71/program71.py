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
# Write a function to sort a list of elements using comb sort.
#
# SOLUTION CODE
# ============================================
def comb_sort(nums):

    shrink_fact = 1.3

    gaps = len(nums)

    swapped = True

    i = 0

    while gaps > 1 or swapped:

        gaps = int(float(gaps) / shrink_fact)

        swapped = False

        i = 0

        while gaps + i < len(nums):

            if nums[i] > nums[i+gaps]:

                nums[i], nums[i+gaps] = nums[i+gaps], nums[i]

                swapped = True

            i += 1

    return nums

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(comb_sort(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



