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
# Write a function to check if the given number is woodball or not.
#
# SOLUTION CODE
# ============================================
def is_woodall(x): 

	if (x % 2 == 0): 

		return False

	if (x == 1): 

		return True

	x = x + 1 

	p = 0

	while (x % 2 == 0): 

		x = x/2

		p = p + 1

		if (p == x): 

			return True

	return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(is_woodall(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



