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
# Write a python function to find minimum sum of factors of a given number.
#
# SOLUTION CODE
# ============================================
def find_min_sum(num): 

    sum = 0

    i = 2

    while(i * i <= num): 

        while(num % i == 0): 

            sum += i 

            num /= i 

        i += 1

    sum += num 

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(num, expected):
    try:
        if validate_solution(find_min_sum(
            num),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



