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
# Write a function to generate a two-dimensional array.
#
# SOLUTION CODE
# ============================================
def multi_list(rownum,colnum):

  multi_list = [[0 for col in range(colnum)] for row in range(rownum)]

  for row in range(rownum):

    for col in range(colnum):

        multi_list[row][col]= row*col

  return multi_list



# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(rownum, colnum, expected):
    try:
        if validate_solution(multi_list(
            rownum, colnum),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



