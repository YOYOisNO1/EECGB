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
# Write a function to multiply all the numbers in a list and divide with the length of the list.
#
# SOLUTION CODE
# ============================================
def multiply_num(numbers):  

    total = 1

    for x in numbers:

        total *= x  

    return total/len(numbers) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(numbers, expected):
    try:
        if validate_solution(multiply_num(
            numbers),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



