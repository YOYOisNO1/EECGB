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
# Write a function to find the maximum sum in the given right triangle of numbers.
#
# SOLUTION CODE
# ============================================
def max_sum(tri, n): 

	if n > 1: 

		tri[1][1] = tri[1][1]+tri[0][0] 

		tri[1][0] = tri[1][0]+tri[0][0] 

	for i in range(2, n): 

		tri[i][0] = tri[i][0] + tri[i-1][0] 

		tri[i][i] = tri[i][i] + tri[i-1][i-1] 

		for j in range(1, i): 

			if tri[i][j]+tri[i-1][j-1] >= tri[i][j]+tri[i-1][j]: 

				tri[i][j] = tri[i][j] + tri[i-1][j-1] 

			else: 

				tri[i][j] = tri[i][j]+tri[i-1][j] 

	return (max(tri[n-1]))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tri, n, expected):
    try:
        if validate_solution(max_sum(
            tri, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



