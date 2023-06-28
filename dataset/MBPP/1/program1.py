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
# Write a function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].
#
# SOLUTION CODE
# ============================================
R = 3

C = 3

def min_cost(cost, m, n): 

	tc = [[0 for x in range(C)] for x in range(R)] 

	tc[0][0] = cost[0][0] 

	for i in range(1, m+1): 

		tc[i][0] = tc[i-1][0] + cost[i][0] 

	for j in range(1, n+1): 

		tc[0][j] = tc[0][j-1] + cost[0][j] 

	for i in range(1, m+1): 

		for j in range(1, n+1): 

			tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] 

	return tc[m][n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(cost, m, n, expected):
    try:
        if validate_solution(min_cost(
            cost, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



