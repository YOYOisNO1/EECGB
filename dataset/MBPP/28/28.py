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
# Write a python function to find binomial co-efficient.
#
# SOLUTION CODE
# ============================================
def binomial_coeff(n,k): 

    if k > n : 

       return 0

    if k==0 or k ==n : 

        return 1 

    return binomial_coeff(n-1,k-1) + binomial_coeff(n-1,k) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, k, expected):
    try:
        if validate_solution(binomial_coeff(
            n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



