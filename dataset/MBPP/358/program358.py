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
# Write a function to find modulo division of two lists using map and lambda function.
#
# SOLUTION CODE
# ============================================
def moddiv_list(nums1,nums2):

  result = map(lambda x, y: x % y, nums1, nums2)

  return list(result)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums1, nums2, expected):
    try:
        if validate_solution(moddiv_list(
            nums1, nums2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



