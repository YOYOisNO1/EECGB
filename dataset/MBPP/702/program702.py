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
# Write a function to find the minimum number of elements that should be removed such that amax-amin<=k.
#
# SOLUTION CODE
# ============================================
def find_ind(key, i, n, 

			k, arr):

	ind = -1

	start = i + 1

	end = n - 1;

	while (start < end):

		mid = int(start +

				(end - start) / 2)

		if (arr[mid] - key <= k):

			ind = mid

			start = mid + 1

		else:

			end = mid

	return ind

def removals(arr, n, k):

	ans = n - 1

	arr.sort()

	for i in range(0, n):

		j = find_ind(arr[i], i, 

					n, k, arr)

		if (j != -1):

			ans = min(ans, n -

						(j - i + 1))

	return ans

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, k, expected):
    try:
        if validate_solution(find_ind(
            arr, n, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



