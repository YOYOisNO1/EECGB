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
# Write a function to find the number of flips required to make the given binary string a sequence of alternate characters.
#
# SOLUTION CODE
# ============================================
def make_flip(ch): 

	return '1' if (ch == '0') else '0'

def get_flip_with_starting_charcter(str, expected): 

	flip_count = 0

	for i in range(len( str)): 

		if (str[i] != expected): 

			flip_count += 1

		expected = make_flip(expected) 

	return flip_count 

def min_flip_to_make_string_alternate(str): 

	return min(get_flip_with_starting_charcter(str, '0'),get_flip_with_starting_charcter(str, '1')) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(make_flip(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



