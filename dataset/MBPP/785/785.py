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
# Write a function to convert tuple string to integer tuple.
#
# SOLUTION CODE
# ============================================
def tuple_str_int(test_str):

  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_str, expected):
    try:
        if validate_solution(tuple_str_int(
            test_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



