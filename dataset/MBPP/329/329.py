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
# Write a python function to count negative numbers in a list.
#
# SOLUTION CODE
# ============================================
def neg_count(list):

  neg_count= 0

  for num in list: 

    if num <= 0: 

      neg_count += 1

  return neg_count 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(list, expected):
    try:
        if validate_solution(neg_count(
            list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



