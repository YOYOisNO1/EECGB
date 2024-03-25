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
# Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
#
# SOLUTION CODE
# ============================================
def max_product(arr, n ): 

	mpis =[0] * (n) 

	for i in range(n): 

		mpis[i] = arr[i] 

	for i in range(1, n): 

		for j in range(i): 

			if (arr[i] > arr[j] and

					mpis[i] < (mpis[j] * arr[i])): 

						mpis[i] = mpis[j] * arr[i] 

	return max(mpis)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(max_product(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



