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
# Write a function to find the maximum number of segments of lengths a, b and c that can be formed from n.
#
# SOLUTION CODE
# ============================================
def maximum_segments(n, a, b, c) : 

	dp = [-1] * (n + 10) 

	dp[0] = 0

	for i in range(0, n) : 

		if (dp[i] != -1) : 

			if(i + a <= n ): 

				dp[i + a] = max(dp[i] + 1, 

							dp[i + a]) 

			if(i + b <= n ): 

				dp[i + b] = max(dp[i] + 1, 

							dp[i + b]) 

			if(i + c <= n ): 

				dp[i + c] = max(dp[i] + 1, 

							dp[i + c]) 

	return dp[n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, a, b, c, expected):
    try:
        if validate_solution(maximum_segments(
            n, a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



