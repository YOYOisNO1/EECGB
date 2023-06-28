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
# Write a python function to choose points from two ranges such that no point lies in both the ranges.
#
# SOLUTION CODE
# ============================================
def find_points(l1,r1,l2,r2): 

    x = min(l1,l2) if (l1 != l2) else -1

    y = max(r1,r2) if (r1 != r2) else -1

    return (x,y)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l1, r1, l2, r2, expected):
    try:
        if validate_solution(find_points(
            l1, r1, l2, r2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



