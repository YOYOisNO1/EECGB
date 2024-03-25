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
# Write a function to find the length of the shortest string that has both str1 and str2 as subsequences.
#
# SOLUTION CODE
# ============================================
def super_seq(X, Y, m, n):

	if (not m):

		return n

	if (not n):

		return m

	if (X[m - 1] == Y[n - 1]):

		return 1 + super_seq(X, Y, m - 1, n - 1)

	return 1 + min(super_seq(X, Y, m - 1, n),	super_seq(X, Y, m, n - 1))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, m, n, expected):
    try:
        if validate_solution(super_seq(
            x, y, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



