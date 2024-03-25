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
# Write a function to find the longest bitonic subsequence for the given array.
#
# SOLUTION CODE
# ============================================
def lbs(arr): 

	n = len(arr) 

	lis = [1 for i in range(n+1)] 

	for i in range(1 , n): 

		for j in range(0 , i): 

			if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 

				lis[i] = lis[j] + 1

	lds = [1 for i in range(n+1)] 

	for i in reversed(range(n-1)): 

		for j in reversed(range(i-1 ,n)): 

			if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 

				lds[i] = lds[j] + 1

	maximum = lis[0] + lds[0] - 1

	for i in range(1 , n): 

		maximum = max((lis[i] + lds[i]-1), maximum) 

	return maximum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, expected):
    try:
        if validate_solution(lbs(
            arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



