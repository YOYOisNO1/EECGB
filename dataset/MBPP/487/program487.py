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
# Write a function to sort a list of tuples in increasing order by the last element in each tuple.
#
# SOLUTION CODE
# ============================================
def sort_tuple(tup): 

	lst = len(tup) 

	for i in range(0, lst): 

		for j in range(0, lst-i-1): 

			if (tup[j][-1] > tup[j + 1][-1]): 

				temp = tup[j] 

				tup[j]= tup[j + 1] 

				tup[j + 1]= temp 

	return tup

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(tup, expected):
    try:
        if validate_solution(sort_tuple(
            tup),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



