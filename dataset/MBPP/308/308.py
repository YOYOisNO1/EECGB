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
# Write a function to find the specified number of largest products from two given lists.
#
# SOLUTION CODE
# ============================================
def large_product(nums1, nums2, N):

    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums1, nums2, n, expected):
    try:
        if validate_solution(large_product(
            nums1, nums2, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



