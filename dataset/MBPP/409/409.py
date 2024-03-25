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
# Write a function to find the minimum product from the pairs of tuples within a given list.
#
# SOLUTION CODE
# ============================================
def min_product_tuple(list1):

    result_min = min([abs(x * y) for x, y in list1] )

    return result_min

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(min_product_tuple(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



