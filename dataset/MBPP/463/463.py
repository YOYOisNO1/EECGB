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
# Write a function to find the maximum product subarray of the given array.
#
# SOLUTION CODE
# ============================================
def max_subarray_product(arr):

	n = len(arr)

	max_ending_here = 1

	min_ending_here = 1

	max_so_far = 0

	flag = 0

	for i in range(0, n):

		if arr[i] > 0:

			max_ending_here = max_ending_here * arr[i]

			min_ending_here = min (min_ending_here * arr[i], 1)

			flag = 1

		elif arr[i] == 0:

			max_ending_here = 1

			min_ending_here = 1

		else:

			temp = max_ending_here

			max_ending_here = max (min_ending_here * arr[i], 1)

			min_ending_here = temp * arr[i]

		if (max_so_far < max_ending_here):

			max_so_far = max_ending_here

	if flag == 0 and max_so_far == 0:

		return 0

	return max_so_far

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, expected):
    try:
        if validate_solution(max_subarray_product(
            arr),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



