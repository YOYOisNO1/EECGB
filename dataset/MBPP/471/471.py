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
# Write a python function to find remainder of array multiplication divided by n.
#
# SOLUTION CODE
# ============================================
def find_remainder(arr, lens, n): 

    mul = 1

    for i in range(lens):  

        mul = (mul * (arr[i] % n)) % n 

    return mul % n 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, lens, n, expected):
    try:
        if validate_solution(find_remainder(
            arr, lens, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



