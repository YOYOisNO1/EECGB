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
# Write a python function to check whether the product of digits of a number at even and odd places is equal or not.
#
# SOLUTION CODE
# ============================================
def product_equal(n): 

    if n < 10: 

        return False

    prodOdd = 1; prodEven = 1

    while n > 0: 

        digit = n % 10

        prodOdd *= digit 

        n = n//10

        if n == 0: 

            break; 

        digit = n % 10

        prodEven *= digit 

        n = n//10

    if prodOdd == prodEven: 

        return True

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(product_equal(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



