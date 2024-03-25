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
# Write a function to find if the given number is abundant or not.
#
# SOLUTION CODE
# ============================================
import math 

def get_sum(n): 

	sum = 0

	i = 1

	while i <= (math.sqrt(n)): 

		if n%i == 0: 

			if n/i == i : 

				sum = sum + i 

			else: 

				sum = sum + i 

				sum = sum + (n / i ) 

		i = i + 1

	sum = sum - n 

	return sum

def check_abundant(n): 

	if (get_sum(n) > n): 

		return True

	else: 

		return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(get_sum(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



