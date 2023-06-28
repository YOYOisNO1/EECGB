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
# Write a function to extract all the adjacent coordinates of the given coordinate tuple.
#
# SOLUTION CODE
# ============================================
def adjac(ele, sub = []): 

  if not ele: 

     yield sub 

  else: 

     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 

                for idx in adjac(ele[1:], sub + [j])] 

def get_coordinates(test_tup):

  res = list(adjac(test_tup))

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, expected):
    try:
        if validate_solution(adjac(
            test_tup),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



