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
# Write a python function to find the volume of a triangular prism.
#
# SOLUTION CODE
# ============================================
def find_volume(l,b,h) : 

    return ((l * b * h) / 2) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, b, h, expected):
    try:
        if validate_solution(find_volume(
            l, b, h),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



