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
# Write a function to calculate the nth pell number.
#
# SOLUTION CODE
# ============================================
def get_pell(n): 

	if (n <= 2): 

		return n 

	a = 1

	b = 2

	for i in range(3, n+1): 

		c = 2 * b + a 

		a = b 

		b = c 

	return b 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(get_pell(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



