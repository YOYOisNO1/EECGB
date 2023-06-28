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
# Write a function to find entringer number e(n, k).
#
# SOLUTION CODE
# ============================================
def zigzag(n, k): 

	if (n == 0 and k == 0): 

		return 1

	if (k == 0): 

		return 0

	return zigzag(n, k - 1) + zigzag(n - 1, n - k)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, k, expected):
    try:
        if validate_solution(zigzag(
            n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



