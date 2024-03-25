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
# Write a python function to find the first missing positive number.
#
# SOLUTION CODE
# ============================================
def first_missing_positive(arr,n): 

    ptr = 0

    for i in range(n):

        if arr[i] == 1:

            ptr = 1

            break

    if ptr == 0:

        return(1)

    for i in range(n):

        if arr[i] <= 0 or arr[i] > n:

            arr[i] = 1

    for i in range(n):

        arr[(arr[i] - 1) % n] += n

    for i in range(n):

        if arr[i] <= n:

            return(i + 1)

    return(n + 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(first_missing_positive(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



