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
# Write a function to find the length of the longest sub-sequence such that elements in the subsequences are consecutive integers.
#
# SOLUTION CODE
# ============================================
def find_longest_conseq_subseq(arr, n): 

	ans = 0

	count = 0

	arr.sort() 

	v = [] 

	v.append(arr[0]) 

	for i in range(1, n): 

		if (arr[i] != arr[i - 1]): 

			v.append(arr[i]) 

	for i in range(len(v)): 

		if (i > 0 and v[i] == v[i - 1] + 1): 

			count += 1

		else: 

			count = 1

		ans = max(ans, count) 

	return ans 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(find_longest_conseq_subseq(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



