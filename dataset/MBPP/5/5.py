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
# Write a function to find the number of ways to fill it with 2 x 1 dominoes for the given 3 x n board.
#
# SOLUTION CODE
# ============================================
def count_ways(n): 

	A = [0] * (n + 1) 

	B = [0] * (n + 1) 

	A[0] = 1

	A[1] = 0

	B[0] = 0

	B[1] = 1

	for i in range(2, n+1): 

		A[i] = A[i - 2] + 2 * B[i - 1] 

		B[i] = A[i - 1] + B[i - 2] 

	return A[n] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(count_ways(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



