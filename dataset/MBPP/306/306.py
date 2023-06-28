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
# Write a function to find the maximum sum of increasing subsequence from prefix till ith index and also including a given kth element which is after i, i.e., k > i .
#
# SOLUTION CODE
# ============================================
def max_sum_increasing_subseq(a, n, index, k):

	dp = [[0 for i in range(n)] 

			for i in range(n)]

	for i in range(n):

		if a[i] > a[0]:

			dp[0][i] = a[i] + a[0]

		else:

			dp[0][i] = a[i]

	for i in range(1, n):

		for j in range(n):

			if a[j] > a[i] and j > i:

				if dp[i - 1][i] + a[j] > dp[i - 1][j]:

					dp[i][j] = dp[i - 1][i] + a[j]

				else:

					dp[i][j] = dp[i - 1][j]

			else:

				dp[i][j] = dp[i - 1][j]

	return dp[index][k]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, index, k, expected):
    try:
        if validate_solution(max_sum_increasing_subseq(
            a, n, index, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



