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
# Write a function to find out the minimum no of swaps required for bracket balancing in the given string.
#
# SOLUTION CODE
# ============================================
def swap_count(s):

	chars = s

	count_left = 0

	count_right = 0

	swap = 0

	imbalance = 0; 

	for i in range(len(chars)):

		if chars[i] == '[':

			count_left += 1

			if imbalance > 0:

				swap += imbalance

				imbalance -= 1

		elif chars[i] == ']':

			count_right += 1

			imbalance = (count_right - count_left) 

	return swap

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(s, expected):
    try:
        if validate_solution(swap_count(
            s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



