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
# Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
#
# SOLUTION CODE
# ============================================
def find_length(string, n): 

	current_sum = 0

	max_sum = 0

	for i in range(n): 

		current_sum += (1 if string[i] == '0' else -1) 

		if current_sum < 0: 

			current_sum = 0

		max_sum = max(current_sum, max_sum) 

	return max_sum if max_sum else 0

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(string_arg0, n, expected):
    try:
        if validate_solution(find_length(
            string_arg0, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



