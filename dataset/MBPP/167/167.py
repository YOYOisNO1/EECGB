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
# Write a python function to find smallest power of 2 greater than or equal to n.
#
# SOLUTION CODE
# ============================================
def next_power_of_2(n): 

    count = 0; 

    if (n and not(n & (n - 1))): 

        return n   

    while( n != 0): 

        n >>= 1

        count += 1

    return 1 << count; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(next_power_of_2(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



