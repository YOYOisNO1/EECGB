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
# Write a python function to check whether the triangle is valid or not if 3 points are given.
#
# SOLUTION CODE
# ============================================
def check_triangle(x1,y1,x2,y2,x3,y3): 

    a = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))   

    if a == 0: 

        return ('No') 

    else: 

        return ('Yes') 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x1, y1, x2, y2, x3, y3, expected):
    try:
        if validate_solution(check_triangle(
            x1, y1, x2, y2, x3, y3),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



