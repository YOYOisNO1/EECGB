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
# Write a python function to find the frequency of a number in a given array.
#
# SOLUTION CODE
# ============================================
def frequency(a,x): 

    count = 0  

    for i in a: 

        if i == x: count += 1

    return count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, x, expected):
    try:
        if validate_solution(frequency(
            a, x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



