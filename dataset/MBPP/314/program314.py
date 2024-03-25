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
# Write a function to find out the maximum sum such that no two chosen numbers are adjacent for the given rectangular grid of dimension 2 x n.
#
# SOLUTION CODE
# ============================================
def max_sum_rectangular_grid(grid, n) : 

	incl = max(grid[0][0], grid[1][0]) 

	excl = 0

	for i in range(1, n) : 

		excl_new = max(excl, incl) 

		incl = excl + max(grid[0][i], grid[1][i]) 

		excl = excl_new 

	return max(excl, incl)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(grid, n, expected):
    try:
        if validate_solution(max_sum_rectangular_grid(
            grid, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



