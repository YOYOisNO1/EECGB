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
# Write a python function to find the largest prime factor of a given number.
#
# SOLUTION CODE
# ============================================
import math 

def max_prime_factors (n): 

    maxPrime = -1 

    while n%2 == 0: 

        maxPrime = 2

        n >>= 1    

    for i in range(3,int(math.sqrt(n))+1,2): 

        while n % i == 0: 

            maxPrime = i 

            n = n / i 

    if n > 2: 

        maxPrime = n  

    return int(maxPrime)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution((
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



