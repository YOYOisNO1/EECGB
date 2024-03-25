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
# Write a function to find the peak element in the given array.
#
# SOLUTION CODE
# ============================================
def find_peak_util(arr, low, high, n): 

	mid = low + (high - low)/2

	mid = int(mid) 

	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and

		(mid == n - 1 or arr[mid + 1] <= arr[mid])): 

		return mid 

	elif (mid > 0 and arr[mid - 1] > arr[mid]): 

		return find_peak_util(arr, low, (mid - 1), n) 

	else: 

		return find_peak_util(arr, (mid + 1), high, n) 

def find_peak(arr, n): 

	return find_peak_util(arr, 0, n - 1, n) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_peak_util(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



