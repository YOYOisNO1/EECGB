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
# Write a function to find eulerian number a(n, m).
#
# SOLUTION CODE
# ============================================
def eulerian_num(n, m): 

	if (m >= n or n == 0): 

		return 0 

	if (m == 0): 

		return 1 

	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, m, expected):
    try:
        if validate_solution(eulerian_num(
            n, m),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



