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
# Write a function to find the maximum sum we can make by dividing number in three parts recursively and summing them up together for the given number.
#
# SOLUTION CODE
# ============================================
MAX = 1000000

def break_sum(n): 

	dp = [0]*(n+1) 

	dp[0] = 0

	dp[1] = 1

	for i in range(2, n+1): 

		dp[i] = max(dp[int(i/2)] + dp[int(i/3)] + dp[int(i/4)], i); 

	return dp[n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(break_sum(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



