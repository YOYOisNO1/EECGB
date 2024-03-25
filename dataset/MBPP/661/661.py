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
# Write a function to find the maximum sum that can be formed which has no three consecutive elements present.
#
# SOLUTION CODE
# ============================================
def max_sum_of_three_consecutive(arr, n): 

	sum = [0 for k in range(n)] 

	if n >= 1: 

		sum[0] = arr[0] 

	if n >= 2: 

		sum[1] = arr[0] + arr[1] 

	if n > 2: 

		sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2])) 

	for i in range(3, n): 

		sum[i] = max(max(sum[i-1], sum[i-2] + arr[i]), arr[i] + arr[i-1] + sum[i-3]) 

	return sum[n-1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(max_sum_of_three_consecutive(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



