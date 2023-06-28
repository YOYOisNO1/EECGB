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
# Write a function to find the product of it’s kth index in the given tuples.
#
# SOLUTION CODE
# ============================================
def get_product(val) : 

	res = 1

	for ele in val: 

		res *= ele 

	return res 

def find_k_product(test_list, K):

  res = get_product([sub[K] for sub in test_list])

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, k, expected):
    try:
        if validate_solution(get_product(
            test_list, k),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



