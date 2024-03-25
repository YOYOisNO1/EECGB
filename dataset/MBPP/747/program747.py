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
# Write a function to find the longest common subsequence for the given three string sequence.
#
# SOLUTION CODE
# ============================================
def lcs_of_three(X, Y, Z, m, n, o): 

	L = [[[0 for i in range(o+1)] for j in range(n+1)] 

		for k in range(m+1)] 

	for i in range(m+1): 

		for j in range(n+1): 

			for k in range(o+1): 

				if (i == 0 or j == 0 or k == 0): 

					L[i][j][k] = 0

				elif (X[i-1] == Y[j-1] and

					X[i-1] == Z[k-1]): 

					L[i][j][k] = L[i-1][j-1][k-1] + 1

				else: 

					L[i][j][k] = max(max(L[i-1][j][k], 

					L[i][j-1][k]), 

									L[i][j][k-1]) 

	return L[m][n][o]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, z, m, n, o, expected):
    try:
        if validate_solution(lcs_of_three(
            x, y, z, m, n, o),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



