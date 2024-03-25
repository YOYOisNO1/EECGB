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
# Write a python function to find lcm of two positive integers.
#
# SOLUTION CODE
# ============================================
def lcm(x, y):

   if x > y:

       z = x

   else:

       z = y

   while(True):

       if((z % x == 0) and (z % y == 0)):

           lcm = z

           break

       z += 1

   return lcm

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, expected):
    try:
        if validate_solution(lcm(
            x, y),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



