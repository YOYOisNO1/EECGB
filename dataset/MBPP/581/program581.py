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
# Write a python function to find the surface area of the square pyramid.
#
# SOLUTION CODE
# ============================================
def surface_area(b,s): 

    return 2 * b * s + pow(b,2) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(b, s, expected):
    try:
        if validate_solution(surface_area(
            b, s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



