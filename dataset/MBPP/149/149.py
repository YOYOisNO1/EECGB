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
# Write a function to find the longest subsequence such that the difference between adjacents is one for the given array.
#
# SOLUTION CODE
# ============================================
def longest_subseq_with_diff_one(arr, n): 

	dp = [1 for i in range(n)] 

	for i in range(n): 

		for j in range(i): 

			if ((arr[i] == arr[j]+1) or (arr[i] == arr[j]-1)): 

				dp[i] = max(dp[i], dp[j]+1) 

	result = 1

	for i in range(n): 

		if (result < dp[i]): 

			result = dp[i] 

	return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(longest_subseq_with_diff_one(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



