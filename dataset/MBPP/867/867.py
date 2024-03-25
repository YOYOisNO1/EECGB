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
# Write a python function to add a minimum number such that the sum of array becomes even.
#
# SOLUTION CODE
# ============================================
def min_num(arr,n):  

    odd = 0

    for i in range(n): 

        if (arr[i] % 2): 

            odd += 1 

    if (odd % 2): 

        return 1

    return 2

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(min_num(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



