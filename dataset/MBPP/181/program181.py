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
# Write a function to find the longest common prefix in the given set of strings.
#
# SOLUTION CODE
# ============================================
def common_prefix_util(str1, str2): 

	result = ""; 

	n1 = len(str1) 

	n2 = len(str2) 

	i = 0

	j = 0

	while i <= n1 - 1 and j <= n2 - 1: 

		if (str1[i] != str2[j]): 

			break

		result += str1[i] 

		i += 1

		j += 1

	return (result) 

def common_prefix (arr, n): 

	prefix = arr[0] 

	for i in range (1, n): 

		prefix = common_prefix_util(prefix, arr[i]) 

	return (prefix) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(arr, n, expected):
    try:
        if validate_solution(common_prefix_util(
            arr, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



