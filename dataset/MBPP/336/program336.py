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
# Write a function to check whether the given month name contains 28 days or not.
#
# SOLUTION CODE
# ============================================
def check_monthnum(monthname1):

  if monthname1 == "February":

    return True

  else:

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(monthname1, expected):
    try:
        if validate_solution(check_monthnum(
            monthname1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



