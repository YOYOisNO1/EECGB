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
# Write a function to check whether the given key is present in the dictionary or not.
#
# SOLUTION CODE
# ============================================
def is_key_present(d,x):

  if x in d:

    return True

  else:

     return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(d, x, expected):
    try:
        if validate_solution(is_key_present(
            d, x),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



