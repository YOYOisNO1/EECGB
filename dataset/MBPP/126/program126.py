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
# Write a python function to find the sum of common divisors of two given numbers.
#
# SOLUTION CODE
# ============================================
def sum(a,b): 

    sum = 0

    for i in range (1,min(a,b)): 

        if (a % i == 0 and b % i == 0): 

            sum += i 

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, expected):
    try:
        if validate_solution(sum(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



