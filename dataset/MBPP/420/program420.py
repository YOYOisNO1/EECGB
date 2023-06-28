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
# Write a python function to find the cube sum of first n even natural numbers.
#
# SOLUTION CODE
# ============================================
def cube_sum(n): 

    sum = 0

    for i in range(1,n + 1): 

        sum += (2*i)*(2*i)*(2*i) 

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(cube_sum(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



