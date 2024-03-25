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
# Write function to find the sum of all items in the given dictionary.
#
# SOLUTION CODE
# ============================================
def return_sum(dict):

  sum = 0

  for i in dict.values():

    sum = sum + i

  return sum

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(dict, expected):
    try:
        if validate_solution(return_sum(
            dict),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



