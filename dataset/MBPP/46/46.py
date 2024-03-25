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
# Write a python function to determine whether all the numbers are different from each other are not.
#
# SOLUTION CODE
# ============================================
def test_distinct(data):

  if len(data) == len(set(data)):

    return True

  else:

    return False;

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(data_arg0, expected):
    try:
        if validate_solution(test_distinct(
            data_arg0),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



