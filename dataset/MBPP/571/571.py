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
# Write a function to find maximum possible sum of disjoint pairs for the given array of integers and a number k.
#
# SOLUTION CODE
# ============================================
def max_sum_pair_diff_lessthan_k(arr, N, K): 

	arr.sort() 

	dp = [0] * N 

	dp[0] = 0

	for i in range(1, N): 

		dp[i] = dp[i-1] 

		if (arr[i] - arr[i-1] < K): 

			if (i >= 2): 

				dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1]); 

			else: 

				dp[i] = max(dp[i], arr[i] + arr[i-1]); 

	return dp[N - 1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, k, expected):
    try:
        if validate_solution(max_sum_pair_diff_lessthan_k(
            arr, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



