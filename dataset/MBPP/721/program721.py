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
# Write a function to find a path with the maximum average over all existing paths for the given square matrix of size n*n.
#
# SOLUTION CODE
# ============================================
M = 100

def max_average_of_path(cost, N): 

	dp = [[0 for i in range(N + 1)] for j in range(N + 1)] 

	dp[0][0] = cost[0][0] 

	for i in range(1, N): 

		dp[i][0] = dp[i - 1][0] + cost[i][0] 

	for j in range(1, N): 

		dp[0][j] = dp[0][j - 1] + cost[0][j] 

	for i in range(1, N): 

		for j in range(1, N): 

			dp[i][j] = max(dp[i - 1][j], 

						dp[i][j - 1]) + cost[i][j] 

	return dp[N - 1][N - 1] / (2 * N - 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(cost, n, expected):
    try:
        if validate_solution(max_average_of_path(
            cost, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



