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
# Write a function to print check if the triangle is isosceles or not.
#
# SOLUTION CODE
# ============================================
def check_isosceles(x,y,z):

  if x==y or y==z or z==x:

	   return True

  else:

     return False

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, z, expected):
    try:
        if validate_solution(check_isosceles(
            x, y, z),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



