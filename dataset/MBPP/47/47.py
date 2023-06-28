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
# Write a python function to find the last digit when factorial of a divides factorial of b.
#
# SOLUTION CODE
# ============================================
def compute_last_digit(A,B): 

    variable = 1

    if (A == B): 

        return 1

    elif ((B - A) >= 5):  

        return 0

    else:   

        for i in range(A + 1,B + 1): 

            variable = (variable * (i % 10)) % 10

        return variable % 10

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, expected):
    try:
        if validate_solution(compute_last_digit(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



