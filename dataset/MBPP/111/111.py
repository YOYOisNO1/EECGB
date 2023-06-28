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
# Write a function to find common elements in given nested lists. * list item * list item * list item * list item
#
# SOLUTION CODE
# ============================================
def common_in_nested_lists(nestedlist):

    result = list(set.intersection(*map(set, nestedlist)))

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(nestedlist, expected):
    try:
        if validate_solution(common_in_nested_lists(
            nestedlist),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



