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
# Write a function to count the same pair in two given lists using map function.
#
# SOLUTION CODE
# ============================================
from operator import eq

def count_same_pair(nums1, nums2):

    result = sum(map(eq, nums1, nums2))

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums1, nums2, expected):
    try:
        if validate_solution(count_same_pair(
            nums1, nums2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



