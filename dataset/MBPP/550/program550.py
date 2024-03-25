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
# Write a python function to find the maximum element in a sorted and rotated array.
#
# SOLUTION CODE
# ============================================
def find_max(arr,low,high): 

    if (high < low): 

        return arr[0] 

    if (high == low): 

        return arr[low] 

    mid = low + (high - low) // 2 

    if (mid < high and arr[mid + 1] < arr[mid]): 

        return arr[mid] 

    if (mid > low and arr[mid] < arr[mid - 1]): 

        return arr[mid - 1]  

    if (arr[low] > arr[mid]): 

        return find_max(arr,low,mid - 1) 

    else: 

        return find_max(arr,mid + 1,high) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, low, high, expected):
    try:
        if validate_solution(find_max(
            arr, low, high),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



