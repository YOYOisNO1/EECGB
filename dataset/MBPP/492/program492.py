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
# Write a function to search an element in the given array by using binary search.
#
# SOLUTION CODE
# ============================================
def binary_search(item_list,item):

	first = 0

	last = len(item_list)-1

	found = False

	while( first<=last and not found):

		mid = (first + last)//2

		if item_list[mid] == item :

			found = True

		else:

			if item < item_list[mid]:

				last = mid - 1

			else:

				first = mid + 1	

	return found

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(item_list, item, expected):
    try:
        if validate_solution(binary_search(
            item_list, item),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



