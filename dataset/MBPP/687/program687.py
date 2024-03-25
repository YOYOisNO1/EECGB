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
# Write a function to find the greatest common divisor (gcd) of two integers by using recursion.
#
# SOLUTION CODE
# ============================================
def recur_gcd(a, b):

	low = min(a, b)

	high = max(a, b)

	if low == 0:

		return high

	elif low == 1:

		return 1

	else:

		return recur_gcd(low, high%low)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, expected):
    try:
        if validate_solution(recur_gcd(
            a, b),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



