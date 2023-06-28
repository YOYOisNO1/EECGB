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
# Write a function to find the largest possible value of k such that k modulo x is y.
#
# SOLUTION CODE
# ============================================
import sys 

def find_max_val(n, x, y): 

	ans = -sys.maxsize 

	for k in range(n + 1): 

		if (k % x == y): 

			ans = max(ans, k) 

	return (ans if (ans >= 0 and

					ans <= n) else -1) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, x, y, expected):
    try:
        if validate_solution(find_max_val(
            n, x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



