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
# Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.
#
# SOLUTION CODE
# ============================================
def count_no_of_ways(n, k): 

	dp = [0] * (n + 1) 

	total = k 

	mod = 1000000007

	dp[1] = k 

	dp[2] = k * k	 

	for i in range(3,n+1): 

		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 

	return dp[n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, k, expected):
    try:
        if validate_solution(count_no_of_ways(
            n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



