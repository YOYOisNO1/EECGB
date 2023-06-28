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
# Write a function to find the inversions of tuple elements in the given tuple list.
#
# SOLUTION CODE
# ============================================
def inversion_elements(test_tup):

  res = tuple(list(map(lambda x: ~x, list(test_tup))))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, expected):
    try:
        if validate_solution(inversion_elements(
            test_tup),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



