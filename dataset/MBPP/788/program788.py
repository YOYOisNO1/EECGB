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
# Write a function to create a new tuple from the given string and list.
#
# SOLUTION CODE
# ============================================
def new_tuple(test_list, test_str):

  res = tuple(test_list + [test_str])

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, test_str, expected):
    try:
        if validate_solution(new_tuple(
            test_list, test_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



