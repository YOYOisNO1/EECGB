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
# Write a function to flatten the given tuple matrix into the tuple list with each tuple representing each column.
#
# SOLUTION CODE
# ============================================
def matrix_to_list(test_list):

  temp = [ele for sub in test_list for ele in sub]

  res = list(zip(*temp))

  return (str(res))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(matrix_to_list(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



