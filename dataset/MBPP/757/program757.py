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
# Write a function to count the pairs of reverse strings in the given string list.
#
# SOLUTION CODE
# ============================================
def count_reverse_pairs(test_list):

  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 

	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 

  return str(res)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(count_reverse_pairs(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



