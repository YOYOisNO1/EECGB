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
# Write a function to calculate the sum of perrin numbers.
#
# SOLUTION CODE
# ============================================
def cal_sum(n): 

	a = 3

	b = 0

	c = 2

	if (n == 0): 

		return 3

	if (n == 1): 

		return 3

	if (n == 2): 

		return 5

	sum = 5

	while (n > 2): 

		d = a + b 

		sum = sum + d 

		a = b 

		b = c 

		c = d 

		n = n-1

	return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(cal_sum(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



