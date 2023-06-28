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
# Write a function to convert a list to a tuple.
#
# SOLUTION CODE
# ============================================
def list_tuple(listx):

  tuplex = tuple(listx)

  return tuplex

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(listx, expected):
    try:
        if validate_solution(list_tuple(
            listx),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



