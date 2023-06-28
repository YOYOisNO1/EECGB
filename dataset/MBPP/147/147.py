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
# Write a function to find the maximum total path sum in the given triangle.
#
# SOLUTION CODE
# ============================================
def max_path_sum(tri, m, n): 

	for i in range(m-1, -1, -1): 

		for j in range(i+1): 

			if (tri[i+1][j] > tri[i+1][j+1]): 

				tri[i][j] += tri[i+1][j] 

			else: 

				tri[i][j] += tri[i+1][j+1] 

	return tri[0][0]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tri, m, n, expected):
    try:
        if validate_solution(max_path_sum(
            tri, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



