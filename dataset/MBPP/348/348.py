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
# Write a function to count sequences of given length having non-negative prefix sums that can be generated by given values.
#
# SOLUTION CODE
# ============================================
def bin_coff(n, r): 

	val = 1

	if (r > (n - r)): 

		r = (n - r) 

	for i in range(0, r): 

		val *= (n - i) 

		val //= (i + 1) 

	return val 

def find_ways(M): 

	n = M // 2

	a = bin_coff(2 * n, n) 

	b = a // (n + 1) 

	return (b) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(m, expected):
    try:
        if validate_solution(bin_coff(
            m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



