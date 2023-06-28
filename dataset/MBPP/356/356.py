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
# Write a function to find the third angle of a triangle using two angles.
#
# SOLUTION CODE
# ============================================
def find_angle(a,b):

 c = 180 - (a + b)

 return c



# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, expected):
    try:
        if validate_solution(find_angle(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



