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
# Write a python function to count the number of equal numbers from three given integers.
#
# SOLUTION CODE
# ============================================
def test_three_equal(x,y,z):

  result= set([x,y,z])

  if len(result)==3:

    return 0

  else:

    return (4-len(result))

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(x, y, z, expected):
    try:
        if validate_solution(test_three_equal(
            x, y, z),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



