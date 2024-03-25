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
# Write a python function to check whether the sum of divisors are same or not.
#
# SOLUTION CODE
# ============================================
import math 

def divSum(n): 

    sum = 1; 

    i = 2; 

    while(i * i <= n): 

        if (n % i == 0): 

            sum = (sum + i +math.floor(n / i)); 

        i += 1; 

    return sum; 

def are_equivalent(num1,num2): 

    return divSum(num1) == divSum(num2); 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num1, num2, expected):
    try:
        if validate_solution(divSum(
            num1, num2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



