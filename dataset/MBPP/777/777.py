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
# Write a python function to find the sum of non-repeated elements in a given array.
#
# SOLUTION CODE
# ============================================
def find_sum(arr,n): 

    arr.sort() 

    sum = arr[0] 

    for i in range(0,n-1): 

        if (arr[i] != arr[i+1]): 

            sum = sum + arr[i+1]   

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_sum(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



