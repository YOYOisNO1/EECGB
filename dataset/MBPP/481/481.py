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
# Write a function to determine if there is a subset of the given set with sum equal to the given sum.
#
# SOLUTION CODE
# ============================================
def is_subset_sum(set, n, sum):

	if (sum == 0):

		return True

	if (n == 0):

		return False

	if (set[n - 1] > sum):

		return is_subset_sum(set, n - 1, sum)

	return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(set_arg0, n, sum, expected):
    try:
        if validate_solution(is_subset_sum(
            set_arg0, n, sum),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



