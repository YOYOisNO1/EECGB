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
# Write a python function to find the slope of a line.
#
# SOLUTION CODE
# ============================================
def slope(x1,y1,x2,y2): 

    return (float)(y2-y1)/(x2-x1)  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(x1, y1, x2, y2, expected):
    try:
        if validate_solution(slope(
            x1, y1, x2, y2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



