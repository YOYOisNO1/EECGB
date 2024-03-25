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
# Write a python function to find the index of an extra element present in one sorted array.
#
# SOLUTION CODE
# ============================================
def find_extra(arr1,arr2,n) : 

    for i in range(0, n) : 

        if (arr1[i] != arr2[i]) : 

            return i 

    return n 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr1, arr2, n, expected):
    try:
        if validate_solution(find_extra(
            arr1, arr2, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



