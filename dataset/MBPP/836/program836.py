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
# Write a function to find length of the subarray having maximum sum.
#
# SOLUTION CODE
# ============================================
from sys import maxsize 

def max_sub_array_sum(a,size): 

	max_so_far = -maxsize - 1

	max_ending_here = 0

	start = 0

	end = 0

	s = 0

	for i in range(0,size): 

		max_ending_here += a[i] 

		if max_so_far < max_ending_here: 

			max_so_far = max_ending_here 

			start = s 

			end = i 

		if max_ending_here < 0: 

			max_ending_here = 0

			s = i+1

	return (end - start + 1)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, size, expected):
    try:
        if validate_solution(max_sub_array_sum(
            a, size),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



