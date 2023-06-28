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
# Write a python function to find the minimun number of subsets with distinct elements.
#
# SOLUTION CODE
# ============================================
def subset(ar, n): 

    res = 0

    ar.sort() 

    for i in range(0, n) : 

        count = 1

        for i in range(n - 1): 

            if ar[i] == ar[i + 1]: 

                count+=1

            else: 

                break 

        res = max(res, count)  

    return res 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(ar, n, expected):
    try:
        if validate_solution(subset(
            ar, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



