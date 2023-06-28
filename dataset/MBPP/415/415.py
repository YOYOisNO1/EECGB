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
# Write a python function to find a pair with highest product from a given array of integers.
#
# SOLUTION CODE
# ============================================
def max_product(arr): 

    arr_len = len(arr) 

    if (arr_len < 2): 

        return ("No pairs exists")           

    x = arr[0]; y = arr[1]      

    for i in range(0,arr_len): 

        for j in range(i + 1,arr_len): 

            if (arr[i] * arr[j] > x * y): 

                x = arr[i]; y = arr[j] 

    return x,y    

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, expected):
    try:
        if validate_solution(max_product(
            arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



