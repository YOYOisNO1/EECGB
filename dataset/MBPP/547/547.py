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
# Write a python function to find the sum of hamming distances of all consecutive numbers from o to n.
#
# SOLUTION CODE
# ============================================
def total_hamming_distance(n):   

    i = 1

    sum = 0

    while (n // i > 0):  

        sum = sum + n // i  

        i = i * 2     

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(total_hamming_distance(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



