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
# Write a function to find the minimum total path sum in the given triangle.
#
# SOLUTION CODE
# ============================================
def min_sum_path(A): 

	memo = [None] * len(A) 

	n = len(A) - 1

	for i in range(len(A[n])): 

		memo[i] = A[n][i] 

	for i in range(len(A) - 2, -1,-1): 

		for j in range( len(A[i])): 

			memo[j] = A[i][j] + min(memo[j], 

									memo[j + 1]) 

	return memo[0]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, expected):
    try:
        if validate_solution(min_sum_path(
            a),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



