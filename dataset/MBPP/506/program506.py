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
# Write a function to calculate the permutation coefficient of given p(n, k).
#
# SOLUTION CODE
# ============================================
def permutation_coefficient(n, k): 

	P = [[0 for i in range(k + 1)] 

			for j in range(n + 1)] 

	for i in range(n + 1): 

		for j in range(min(i, k) + 1): 

			if (j == 0): 

				P[i][j] = 1

			else: 

				P[i][j] = P[i - 1][j] + ( 

						j * P[i - 1][j - 1]) 

			if (j < k): 

				P[i][j + 1] = 0

	return P[n][k] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, k, expected):
    try:
        if validate_solution(permutation_coefficient(
            n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



