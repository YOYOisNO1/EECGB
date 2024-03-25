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
# Write a python function to find the sum of even numbers at even positions.
#
# SOLUTION CODE
# ============================================
def sum_even_and_even_index(arr,n):  

    i = 0

    sum = 0

    for i in range(0,n,2): 

        if (arr[i] % 2 == 0) : 

            sum += arr[i]  

    return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(sum_even_and_even_index(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



