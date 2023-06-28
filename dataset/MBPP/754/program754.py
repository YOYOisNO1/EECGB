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
# Write a function to find common index elements from three lists.
#
# SOLUTION CODE
# ============================================
def extract_index_list(l1, l2, l3):

    result = []

    for m, n, o in zip(l1, l2, l3):

        if (m == n == o):

            result.append(m)

    return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l1, l2, l3, expected):
    try:
        if validate_solution(extract_index_list(
            l1, l2, l3),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



