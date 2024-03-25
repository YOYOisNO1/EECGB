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
# Write a function to find the maximum of similar indices in two lists of tuples.
#
# SOLUTION CODE
# ============================================
def max_similar_indices(test_list1, test_list2):

  res = [(max(x[0], y[0]), max(x[1], y[1]))

   for x, y in zip(test_list1, test_list2)]

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list1, test_list2, expected):
    try:
        if validate_solution(max_similar_indices(
            test_list1, test_list2),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



