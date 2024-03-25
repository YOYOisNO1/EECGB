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
# Write a function to convert the given binary tuple to integer.
#
# SOLUTION CODE
# ============================================
def binary_to_integer(test_tup):

  res = int("".join(str(ele) for ele in test_tup), 2)

  return (str(res)) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, expected):
    try:
        if validate_solution(binary_to_integer(
            test_tup),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



