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
# Write a python function to set the left most unset bit.
#
# SOLUTION CODE
# ============================================
def set_left_most_unset_bit(n): 

    if not (n & (n + 1)): 

        return n 

    pos, temp, count = 0, n, 0 

    while temp: 

        if not (temp & 1): 

            pos = count      

        count += 1; temp>>=1

    return (n | (1 << (pos))) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(set_left_most_unset_bit(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



