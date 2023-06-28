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
# Write a function to convert the given string of integers into a tuple.
#
# SOLUTION CODE
# ============================================
def str_to_tuple(test_str):

  res = tuple(map(int, test_str.split(', ')))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_str, expected):
    try:
        if validate_solution(str_to_tuple(
            test_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



