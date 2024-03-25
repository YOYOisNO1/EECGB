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
# Write a python function to print duplicants from a list of integers.
#
# SOLUTION CODE
# ============================================
def repeat(x): 

    _size = len(x) 

    repeated = [] 

    for i in range(_size): 

        k = i + 1

        for j in range(k, _size): 

            if x[i] == x[j] and x[i] not in repeated: 

                repeated.append(x[i]) 

    return repeated 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(repeat(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



