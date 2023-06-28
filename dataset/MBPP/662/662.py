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
# Write a function to sort a list in a dictionary.
#
# SOLUTION CODE
# ============================================
def sorted_dict(dict1):

  sorted_dict = {x: sorted(y) for x, y in dict1.items()}

  return sorted_dict

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(dict1, expected):
    try:
        if validate_solution(sorted_dict(
            dict1),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



