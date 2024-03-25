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
# Write a function to push all values into a heap and then pop off the smallest values one at a time.
#
# SOLUTION CODE
# ============================================
import heapq as hq

def heap_sort(iterable):

    h = []

    for value in iterable:

        hq.heappush(h, value)

    return [hq.heappop(h) for i in range(len(h))]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(iterable, expected):
    try:
        if validate_solution(heap_sort(
            iterable),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



