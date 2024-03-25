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
# Write a function to find the nth jacobsthal-lucas number.
#
# SOLUTION CODE
# ============================================
def jacobsthal_lucas(n): 

	dp=[0] * (n + 1) 

	dp[0] = 2

	dp[1] = 1

	for i in range(2, n+1): 

		dp[i] = dp[i - 1] + 2 * dp[i - 2]; 

	return dp[n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(jacobsthal_lucas(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



