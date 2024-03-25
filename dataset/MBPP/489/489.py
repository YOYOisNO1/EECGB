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
# Write a python function to find the frequency of the largest value in a given array.
#
# SOLUTION CODE
# ============================================
def frequency_of_largest(n,arr): 

    mn = arr[0] 

    freq = 1

    for i in range(1,n): 

        if (arr[i] >mn): 

            mn = arr[i] 

            freq = 1

        elif (arr[i] == mn): 

            freq += 1

    return freq 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, arr, expected):
    try:
        if validate_solution(frequency_of_largest(
            n, arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



