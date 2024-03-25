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
# Write a python function to find the smallest missing number from the given array.
#
# SOLUTION CODE
# ============================================
def find_first_missing(array,start,end): 

    if (start > end): 

        return end + 1

    if (start != array[start]): 

        return start; 

    mid = int((start + end) / 2) 

    if (array[mid] == mid): 

        return find_first_missing(array,mid+1,end) 

    return find_first_missing(array,start,mid) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(array, start, end_arg2, expected):
    try:
        if validate_solution(find_first_missing(
            array, start, end_arg2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



