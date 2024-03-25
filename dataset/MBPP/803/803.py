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
# Write a python function to check whether the given number is a perfect square or not.
#
# SOLUTION CODE
# ============================================
def is_perfect_square(n) :

    i = 1

    while (i * i<= n):

        if ((n % i == 0) and (n / i == i)):

            return True     

        i = i + 1

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(is_perfect_square(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



