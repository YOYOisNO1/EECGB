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
# Write a function to count the number of inversions in the given array.
#
# SOLUTION CODE
# ============================================
def get_inv_count(arr, n): 

	inv_count = 0

	for i in range(n): 

		for j in range(i + 1, n): 

			if (arr[i] > arr[j]): 

				inv_count += 1

	return inv_count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(get_inv_count(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



