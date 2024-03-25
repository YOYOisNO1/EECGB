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
# Write a python function to find the first natural number whose factorial is divisible by x.
#
# SOLUTION CODE
# ============================================
def first_factorial_divisible_number(x): 

    i = 1;

    fact = 1; 

    for i in range(1,x): 

        fact = fact * i 

        if (fact % x == 0): 

            break

    return i 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(first_factorial_divisible_number(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



