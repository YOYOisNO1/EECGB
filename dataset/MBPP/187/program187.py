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
# Write a function to find the longest common subsequence for the given two sequences.
#
# SOLUTION CODE
# ============================================
def longest_common_subsequence(X, Y, m, n): 

    if m == 0 or n == 0: 

       return 0 

    elif X[m-1] == Y[n-1]: 

       return 1 + longest_common_subsequence(X, Y, m-1, n-1) 

    else: 

       return max(longest_common_subsequence(X, Y, m, n-1), longest_common_subsequence(X, Y, m-1, n))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, m, n, expected):
    try:
        if validate_solution(longest_common_subsequence(
            x, y, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



