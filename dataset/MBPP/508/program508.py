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
# Write a function to check if the common elements between two given lists are in the same order or not.
#
# SOLUTION CODE
# ============================================
def same_order(l1, l2):

    common_elements = set(l1) & set(l2)

    l1 = [e for e in l1 if e in common_elements]

    l2 = [e for e in l2 if e in common_elements]

    return l1 == l2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l1, l2, expected):
    try:
        if validate_solution(same_order(
            l1, l2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



