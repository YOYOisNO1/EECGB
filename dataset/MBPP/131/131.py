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
# Write a python function to reverse only the vowels of a given string.
#
# SOLUTION CODE
# ============================================
def reverse_vowels(str1):

	vowels = ""

	for char in str1:

		if char in "aeiouAEIOU":

			vowels += char

	result_string = ""

	for char in str1:

		if char in "aeiouAEIOU":

			result_string += vowels[-1]

			vowels = vowels[:-1]

		else:

			result_string += char

	return result_string

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str1, expected):
    try:
        if validate_solution(reverse_vowels(
            str1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



