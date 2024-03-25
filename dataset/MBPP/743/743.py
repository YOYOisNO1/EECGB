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
# Write a function to rotate a given list by specified number of items to the right direction.
#
# SOLUTION CODE
# ============================================
def rotate_right(list1,m,n):

  result =  list1[-(m):]+list1[:-(n)]

  return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list1, m, n, expected):
    try:
        if validate_solution(rotate_right(
            list1, m, n),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



