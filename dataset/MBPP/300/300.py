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
# Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
#
# SOLUTION CODE
# ============================================
def count_binary_seq(n): 

	nCr = 1

	res = 1

	for r in range(1, n + 1): 

		nCr = (nCr * (n + 1 - r)) / r 

		res += nCr * nCr 

	return res 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return abs(actual - expected) < 1e-06

def driver(n, expected):
    try:
        if validate_solution(count_binary_seq(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



