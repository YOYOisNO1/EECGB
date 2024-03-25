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
# Write a function to find the number of subsequences having product smaller than k for the given non negative array.
#
# SOLUTION CODE
# ============================================
def no_of_subsequences(arr, k): 

	n = len(arr) 

	dp = [[0 for i in range(n + 1)] 

			for j in range(k + 1)] 

	for i in range(1, k + 1): 

		for j in range(1, n + 1): 

			dp[i][j] = dp[i][j - 1] 

			if arr[j - 1] <= i and arr[j - 1] > 0: 

				dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1

	return dp[k][n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, k, expected):
    try:
        if validate_solution(no_of_subsequences(
            arr, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



