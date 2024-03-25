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
# Write a python function to access multiple elements of specified index from a given list.
#
# SOLUTION CODE
# ============================================
def access_elements(nums, list_index):

    result = [nums[i] for i in list_index]

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nums, list_index, expected):
    try:
        if validate_solution(access_elements(
            nums, list_index),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



