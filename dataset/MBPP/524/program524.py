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
# Write a function to find the sum of maximum increasing subsequence of the given array.
#
# SOLUTION CODE
# ============================================
def max_sum_increasing_subsequence(arr, n): 

	max = 0

	msis = [0 for x in range(n)] 

	for i in range(n): 

		msis[i] = arr[i] 

	for i in range(1, n): 

		for j in range(i): 

			if (arr[i] > arr[j] and

				msis[i] < msis[j] + arr[i]): 

				msis[i] = msis[j] + arr[i] 

	for i in range(n): 

		if max < msis[i]: 

			max = msis[i] 

	return max

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(max_sum_increasing_subsequence(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



