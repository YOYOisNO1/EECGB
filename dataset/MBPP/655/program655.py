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
# Write a python function to find the sum of fifth power of n natural numbers.
#
# SOLUTION CODE
# ============================================
def fifth_power_sum(n) : 

    sm = 0 

    for i in range(1,n+1) : 

        sm = sm + (i*i*i*i*i) 

    return sm 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(fifth_power_sum(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



