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
# Write a function to find the number of possible sequences of length n such that each of the next element is greater than or equal to twice of the previous element but less than or equal to m.
#
# SOLUTION CODE
# ============================================
def get_total_number_of_sequences(m,n): 

	T=[[0 for i in range(n+1)] for i in range(m+1)] 

	for i in range(m+1): 

		for j in range(n+1): 

			if i==0 or j==0: 

				T[i][j]=0

			elif i<j: 

				T[i][j]=0

			elif j==1: 

				T[i][j]=i 

			else: 

				T[i][j]=T[i-1][j]+T[i//2][j-1] 

	return T[m][n]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(m, n, expected):
    try:
        if validate_solution(get_total_number_of_sequences(
            m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



