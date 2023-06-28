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
# Write a function to find the longest palindromic subsequence in the given string.
#
# SOLUTION CODE
# ============================================
def lps(str): 

	n = len(str) 

	L = [[0 for x in range(n)] for x in range(n)] 

	for i in range(n): 

		L[i][i] = 1

	for cl in range(2, n+1): 

		for i in range(n-cl+1): 

			j = i+cl-1

			if str[i] == str[j] and cl == 2: 

				L[i][j] = 2

			elif str[i] == str[j]: 

				L[i][j] = L[i+1][j-1] + 2

			else: 

				L[i][j] = max(L[i][j-1], L[i+1][j]); 

	return L[0][n-1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(lps(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



