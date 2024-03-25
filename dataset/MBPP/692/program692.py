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
# Write a python function to find the last two digits in factorial of a given number.
#
# SOLUTION CODE
# ============================================
def last_two_digits(N): 

    if (N >= 10): 

        return

    fac = 1

    for i in range(1,N + 1): 

        fac = (fac * i) % 100

    return (fac) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(last_two_digits(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



