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
# Write a function to find kth element from the given two sorted arrays.
#
# SOLUTION CODE
# ============================================
def find_kth(arr1, arr2, m, n, k):

	sorted1 = [0] * (m + n)

	i = 0

	j = 0

	d = 0

	while (i < m and j < n):

		if (arr1[i] < arr2[j]):

			sorted1[d] = arr1[i]

			i += 1

		else:

			sorted1[d] = arr2[j]

			j += 1

		d += 1

	while (i < m):

		sorted1[d] = arr1[i]

		d += 1

		i += 1

	while (j < n):

		sorted1[d] = arr2[j]

		d += 1

		j += 1

	return sorted1[k - 1]

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr1, arr2, m, n, k, expected):
    try:
        if validate_solution(find_kth(
            arr1, arr2, m, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



