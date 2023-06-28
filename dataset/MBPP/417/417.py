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
# Write a function to find common first element in given list of tuple.
#
# SOLUTION CODE
# ============================================
def group_tuples(Input): 

	out = {} 

	for elem in Input: 

		try: 

			out[elem[0]].extend(elem[1:]) 

		except KeyError: 

			out[elem[0]] = list(elem) 

	return [tuple(values) for values in out.values()] 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(input, expected):
    try:
        if validate_solution(group_tuples(
            input),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



