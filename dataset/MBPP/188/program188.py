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
# Write a python function to check whether the given number can be represented by product of two squares or not.
#
# SOLUTION CODE
# ============================================
def prod_square(n):

    for i in range(2,(n) + 1):

        if (i*i < (n+1)):

            for j in range(2,n + 1):

                if ((i*i*j*j) == n):

                    return True;

    return False;

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(prod_square(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



