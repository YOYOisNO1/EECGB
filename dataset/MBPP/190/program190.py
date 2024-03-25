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
# Write a python function to count the number of integral co-ordinates that lie inside a square.
#
# SOLUTION CODE
# ============================================
def count_intgral_points(x1,y1,x2,y2): 

    return ((y2 - y1 - 1) * (x2 - x1 - 1)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x1, y1, x2, y2, expected):
    try:
        if validate_solution(count_intgral_points(
            x1, y1, x2, y2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



