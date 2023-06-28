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
# Write a function to check whether a list contains the given sublist or not.
#
# SOLUTION CODE
# ============================================
def is_sublist(l, s):

	sub_set = False

	if s == []:

		sub_set = True

	elif s == l:

		sub_set = True

	elif len(s) > len(l):

		sub_set = False

	else:

		for i in range(len(l)):

			if l[i] == s[0]:

				n = 1

				while (n < len(s)) and (l[i+n] == s[n]):

					n += 1				

				if n == len(s):

					sub_set = True

	return sub_set

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(l, s, expected):
    try:
        if validate_solution(is_sublist(
            l, s),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



