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
# Write a python function to find the largest triangle that can be inscribed in the semicircle.
#
# SOLUTION CODE
# ============================================
def triangle_area(r) :  

    if r < 0 : 

        return -1

    return r * r 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(r, expected):
    try:
        if validate_solution(triangle_area(
            r),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



