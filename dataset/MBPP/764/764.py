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
# Write a python function to count numeric values in a given string.
#
# SOLUTION CODE
# ============================================
def number_ctr(str):

      number_ctr= 0

      for i in range(len(str)):

          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     

      return  number_ctr

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(number_ctr(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



