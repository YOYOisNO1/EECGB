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
# Write a python function to check whether the given two numbers have same number of digits or not.
#
# SOLUTION CODE
# ============================================
def same_length(A,B): 

    while (A > 0 and B > 0): 

        A = A / 10; 

        B = B / 10; 

    if (A == 0 and B == 0): 

        return True; 

    return False; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, expected):
    try:
        if validate_solution(same_length(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



