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
# Write a python function to find the smallest prime divisor of a number.
#
# SOLUTION CODE
# ============================================
def smallest_divisor(n): 

    if (n % 2 == 0): 

        return 2; 

    i = 3;  

    while (i*i <= n): 

        if (n % i == 0): 

            return i; 

        i += 2; 

    return n; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(smallest_divisor(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



