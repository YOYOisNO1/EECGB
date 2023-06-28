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
# Write a function to count the longest repeating subsequences such that the two subsequences don’t have same string characters at same positions.
#
# SOLUTION CODE
# ============================================
def find_longest_repeating_subseq(str): 

	n = len(str) 

	dp = [[0 for k in range(n+1)] for l in range(n+1)] 

	for i in range(1, n+1): 

		for j in range(1, n+1): 

			if (str[i-1] == str[j-1] and i != j): 

				dp[i][j] = 1 + dp[i-1][j-1] 

			else: 

				dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 

	return dp[n][n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(find_longest_repeating_subseq(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



