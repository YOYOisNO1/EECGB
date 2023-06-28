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
# Write a function to find n-th rencontres number.
#
# SOLUTION CODE
# ============================================
def binomial_coeffi(n, k): 

	if (k == 0 or k == n): 

		return 1

	return (binomial_coeffi(n - 1, k - 1) 

		+ binomial_coeffi(n - 1, k)) 

def rencontres_number(n, m): 

	if (n == 0 and m == 0): 

		return 1

	if (n == 1 and m == 0): 

		return 0

	if (m == 0): 

		return ((n - 1) * (rencontres_number(n - 1, 0)+ rencontres_number(n - 2, 0))) 

	return (binomial_coeffi(n, m) * rencontres_number(n - m, 0))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, m, expected):
    try:
        if validate_solution(binomial_coeffi(
            n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



