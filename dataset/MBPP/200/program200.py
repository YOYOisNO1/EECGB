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
# Write a function to find all index positions of the maximum values in a given list.
#
# SOLUTION CODE
# ============================================
def position_max(list1):

    max_val = max(list1)

    max_result = [i for i, j in enumerate(list1) if j == max_val]

    return max_result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, expected):
    try:
        if validate_solution(position_max(
            list1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



