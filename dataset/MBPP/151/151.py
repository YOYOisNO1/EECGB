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
# Write a python function to check whether the given number is co-prime or not.
#
# SOLUTION CODE
# ============================================
def gcd(p,q):

    while q != 0:

        p, q = q,p%q

    return p

def is_coprime(x,y):

    return gcd(x,y) == 1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(gcd(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



