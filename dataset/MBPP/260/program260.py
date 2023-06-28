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
# Write a function to find the nth newman–shanks–williams prime number.
#
# SOLUTION CODE
# ============================================
def newman_prime(n): 

	if n == 0 or n == 1: 

		return 1

	return 2 * newman_prime(n - 1) + newman_prime(n - 2)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(newman_prime(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



