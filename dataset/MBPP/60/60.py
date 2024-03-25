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
# Write a function to find the maximum length of the subsequence with difference between adjacent elements for the given array.
#
# SOLUTION CODE
# ============================================
def max_len_sub( arr, n): 

	mls=[] 

	max = 0

	for i in range(n): 

		mls.append(1) 

	for i in range(n): 

		for j in range(i): 

			if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1): 

				mls[i] = mls[j] + 1

	for i in range(n): 

		if (max < mls[i]): 

			max = mls[i] 

	return max

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(max_len_sub(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



