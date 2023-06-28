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
# Write a function to repeat the given tuple n times.
#
# SOLUTION CODE
# ============================================
def repeat_tuples(test_tup, N):

  res = ((test_tup, ) * N)

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, n, expected):
    try:
        if validate_solution(repeat_tuples(
            test_tup, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



