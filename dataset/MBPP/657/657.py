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
# Write a python function to find the first digit in factorial of a given number.
#
# SOLUTION CODE
# ============================================
import math 

def first_digit(n) : 

    fact = 1

    for i in range(2,n + 1) : 

        fact = fact * i 

        while (fact % 10 == 0) :  

            fact = int(fact / 10) 

    while (fact >= 10) : 

        fact = int(fact / 10) 

    return math.floor(fact) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(first_digit(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



