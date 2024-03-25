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
# Write a function to find the length of the longest increasing subsequence of the given sequence.
#
# SOLUTION CODE
# ============================================
def longest_increasing_subsequence(arr): 

	n = len(arr) 

	longest_increasing_subsequence = [1]*n 

	for i in range (1 , n): 

		for j in range(0 , i): 

			if arr[i] > arr[j] and longest_increasing_subsequence[i]< longest_increasing_subsequence[j] + 1 : 

				longest_increasing_subsequence[i] = longest_increasing_subsequence[j]+1

	maximum = 0

	for i in range(n): 

		maximum = max(maximum , longest_increasing_subsequence[i]) 

	return maximum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, expected):
    try:
        if validate_solution(longest_increasing_subsequence(
            arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



