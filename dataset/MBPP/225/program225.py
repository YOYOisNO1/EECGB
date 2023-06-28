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
# Write a python function to find the minimum element in a sorted and rotated array.
#
# SOLUTION CODE
# ============================================
def find_min(arr,low,high): 

    while (low < high): 

        mid = low + (high - low) // 2;   

        if (arr[mid] == arr[high]): 

            high -= 1; 

        elif (arr[mid] > arr[high]): 

            low = mid + 1; 

        else: 

            high = mid; 

    return arr[high]; 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, low, high, expected):
    try:
        if validate_solution(find_min(
            arr, low, high),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



