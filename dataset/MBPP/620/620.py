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
# Write a function to find the largest subset where each pair is divisible.
#
# SOLUTION CODE
# ============================================
def largest_subset(a, n):

	dp = [0 for i in range(n)]

	dp[n - 1] = 1; 

	for i in range(n - 2, -1, -1):

		mxm = 0;

		for j in range(i + 1, n):

			if a[j] % a[i] == 0 or a[i] % a[j] == 0:

				mxm = max(mxm, dp[j])

		dp[i] = 1 + mxm

	return max(dp)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, expected):
    try:
        if validate_solution(largest_subset(
            a, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



