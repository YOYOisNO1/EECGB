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
# Write a function to count array elements having modular inverse under given prime number p equal to itself.
#
# SOLUTION CODE
# ============================================
def modular_inverse(arr, N, P):

	current_element = 0

	for i in range(0, N):

		if ((arr[i] * arr[i]) % P == 1):

			current_element = current_element + 1

	return current_element

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, p, expected):
    try:
        if validate_solution(modular_inverse(
            arr, n, p),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



