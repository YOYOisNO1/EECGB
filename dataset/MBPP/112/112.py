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
# Write a python function to find the perimeter of a cylinder.
#
# SOLUTION CODE
# ============================================
def perimeter(diameter,height) : 

    return 2*(diameter+height)  

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(diameter, height, expected):
    try:
        if validate_solution(perimeter(
            diameter, height),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



