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
# Write a function to sort a list of elements using pancake sort.
#
# SOLUTION CODE
# ============================================
def pancake_sort(nums):

    arr_len = len(nums)

    while arr_len > 1:

        mi = nums.index(max(nums[0:arr_len]))

        nums = nums[mi::-1] + nums[mi+1:len(nums)]

        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]

        arr_len -= 1

    return nums

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, expected):
    try:
        if validate_solution(pancake_sort(
            nums),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



