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
# Write a function to find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times.
#
# SOLUTION CODE
# ============================================
def max_sub_array_sum_repeated(a, n, k): 

	max_so_far = -2147483648

	max_ending_here = 0

	for i in range(n*k): 

		max_ending_here = max_ending_here + a[i%n] 

		if (max_so_far < max_ending_here): 

			max_so_far = max_ending_here 

		if (max_ending_here < 0): 

			max_ending_here = 0

	return max_so_far

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, k, expected):
    try:
        if validate_solution(max_sub_array_sum_repeated(
            a, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



