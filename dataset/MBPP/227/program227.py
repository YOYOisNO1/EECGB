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
# Write a function to find minimum of three numbers.
#
# SOLUTION CODE
# ============================================
def min_of_three(a,b,c): 

      if (a <= b) and (a <= c): 

        smallest = a 

      elif (b <= a) and (b <= c): 

        smallest = b 

      else: 

        smallest = c 

      return smallest 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(a, b, c, expected):
    try:
        if validate_solution(min_of_three(
            a, b, c),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



