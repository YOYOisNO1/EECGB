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
# Write a function to return true if the given number is even else return false.
#
# SOLUTION CODE
# ============================================
def even_num(x):

  if x%2==0:

     return True

  else:

    return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, expected):
    try:
        if validate_solution(even_num(
            x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



