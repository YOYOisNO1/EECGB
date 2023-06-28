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
# Write a python function to check for odd parity of a given number.
#
# SOLUTION CODE
# ============================================
def check_odd_parity(x): 

    parity = 0

    while (x != 0): 

        x = x & (x - 1) 

        parity += 1

    if (parity % 2 == 1): 

        return True

    else: 

        return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(check_odd_parity(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



