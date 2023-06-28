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
# Write a python function to find the product of non-repeated elements in a given array.
#
# SOLUTION CODE
# ============================================
def find_product(arr,n): 

    arr.sort() 

    prod = 1

    for i in range(0,n,1): 

        if (arr[i - 1] != arr[i]): 

            prod = prod * arr[i] 

    return prod; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_product(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



