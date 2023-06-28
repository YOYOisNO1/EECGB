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
# Write a python function to find the highest power of 2 that is less than or equal to n.
#
# SOLUTION CODE
# ============================================
def highest_power_of_2(n): 

    res = 0; 

    for i in range(n, 0, -1): 

        if ((i & (i - 1)) == 0): 

            res = i; 

            break; 

    return res; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(highest_power_of_2(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



