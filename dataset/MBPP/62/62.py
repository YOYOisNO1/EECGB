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
# Write a python function to find smallest number in a list.
#
# SOLUTION CODE
# ============================================
def smallest_num(xs):
  return min(xs)


# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(xs, expected):
    try:
        if validate_solution(smallest_num(
            xs),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



