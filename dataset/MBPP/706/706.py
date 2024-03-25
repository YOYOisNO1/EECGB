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
# Write a function to find whether an array is subset of another array.
#
# SOLUTION CODE
# ============================================
def is_subset(arr1, m, arr2, n): 

	hashset = set() 

	for i in range(0, m): 

		hashset.add(arr1[i]) 

	for i in range(0, n): 

		if arr2[i] in hashset: 

			continue

		else: 

			return False

	return True		

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr1, m, arr2, n, expected):
    try:
        if validate_solution(is_subset(
            arr1, m, arr2, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



