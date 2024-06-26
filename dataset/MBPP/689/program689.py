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
# ## write a function to find the minimum number of jumps to reach the end of the array for the given array of integers where each element represents the max number of steps that can be made forward from that element. > indented block > indented block
#
# SOLUTION CODE
# ============================================
def min_jumps(arr, n):

	jumps = [0 for i in range(n)]

	if (n == 0) or (arr[0] == 0):

		return float('inf')

	jumps[0] = 0

	for i in range(1, n):

		jumps[i] = float('inf')

		for j in range(i):

			if (i <= j + arr[j]) and (jumps[j] != float('inf')):

				jumps[i] = min(jumps[i], jumps[j] + 1)

				break

	return jumps[n-1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(min_jumps(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



