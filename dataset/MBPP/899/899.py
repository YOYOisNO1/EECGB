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
# Write a python function to check whether an array can be sorted or not by picking only the corner elements.
#
# SOLUTION CODE
# ============================================
def check(arr,n): 

    g = 0 

    for i in range(1,n): 

        if (arr[i] - arr[i - 1] > 0 and g == 1): 

            return False

        if (arr[i] - arr[i] < 0): 

            g = 1

    return True

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(check(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



