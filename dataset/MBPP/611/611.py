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
# Write a function to find the maximum of nth column from the given tuple list.
#
# SOLUTION CODE
# ============================================
def max_of_nth(test_list, N):

  res = max([sub[N] for sub in test_list])

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, n, expected):
    try:
        if validate_solution(max_of_nth(
            test_list, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



