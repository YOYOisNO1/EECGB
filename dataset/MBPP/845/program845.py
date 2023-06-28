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
# Write a python function to count the number of digits in factorial of a given number.
#
# SOLUTION CODE
# ============================================
import math 

def find_digits(n): 

    if (n < 0): 

        return 0;

    if (n <= 1): 

        return 1; 

    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0)); 

    return math.floor(x) + 1; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(find_digits(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



