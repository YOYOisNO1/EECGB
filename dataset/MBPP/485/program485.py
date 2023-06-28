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
# Write a function to find the largest palindromic number in the given array.
#
# SOLUTION CODE
# ============================================
def is_palindrome(n) : 

	divisor = 1

	while (n / divisor >= 10) : 

		divisor *= 10

	while (n != 0) : 

		leading = n // divisor 

		trailing = n % 10

		if (leading != trailing) : 

			return False

		n = (n % divisor) // 10

		divisor = divisor // 100

	return True

def largest_palindrome(A, n) : 

	A.sort() 

	for i in range(n - 1, -1, -1) : 

		if (is_palindrome(A[i])) : 

			return A[i] 

	return -1

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, n, expected):
    try:
        if validate_solution(is_palindrome(
            a, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



