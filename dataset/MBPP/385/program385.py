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
# Write a function to find the n'th perrin number using recursion.
#
# SOLUTION CODE
# ============================================
def get_perrin(n):

  if (n == 0):

    return 3

  if (n == 1):

    return 0

  if (n == 2):

    return 2 

  return get_perrin(n - 2) + get_perrin(n - 3)

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(n, expected):
    try:
        if validate_solution(get_perrin(
            n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



