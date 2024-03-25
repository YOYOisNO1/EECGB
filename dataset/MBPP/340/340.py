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
# Write a python function to find the sum of the three lowest positive numbers from a given list of numbers.
#
# SOLUTION CODE
# ============================================
def sum_three_smallest_nums(lst):

	return sum(sorted([x for x in lst if x > 0])[:3])

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(lst, expected):
    try:
        if validate_solution(sum_three_smallest_nums(
            lst),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



