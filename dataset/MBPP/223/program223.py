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
# Write a function to check for majority element in the given sorted array.
#
# SOLUTION CODE
# ============================================
def is_majority(arr, n, x):

	i = binary_search(arr, 0, n-1, x)

	if i == -1:

		return False

	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:

		return True

	else:

		return False

def binary_search(arr, low, high, x):

	if high >= low:

		mid = (low + high)//2 

		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):

			return mid

		elif x > arr[mid]:

			return binary_search(arr, (mid + 1), high, x)

		else:

			return binary_search(arr, low, (mid -1), x)

	return -1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, x, expected):
    try:
        if validate_solution(is_majority(
            arr, n, x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



