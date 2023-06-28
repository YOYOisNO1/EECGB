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
# Write a function to find the combinations of sums with tuples in the given tuple list.
#
# SOLUTION CODE
# ============================================
from itertools import combinations 

def find_combinations(test_list):

  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(find_combinations(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



