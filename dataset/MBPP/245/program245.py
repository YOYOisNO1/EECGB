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
# Write a function to find the maximum sum of bi-tonic sub-sequence for the given array.
#
# SOLUTION CODE
# ============================================
def max_sum(arr, n): 

	MSIBS = arr[:] 

	for i in range(n): 

		for j in range(0, i): 

			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 

				MSIBS[i] = MSIBS[j] + arr[i] 

	MSDBS = arr[:] 

	for i in range(1, n + 1): 

		for j in range(1, i): 

			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 

				MSDBS[-i] = MSDBS[-j] + arr[-i] 

	max_sum = float("-Inf") 

	for i, j, k in zip(MSIBS, MSDBS, arr): 

		max_sum = max(max_sum, i + j - k) 

	return max_sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(max_sum(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



