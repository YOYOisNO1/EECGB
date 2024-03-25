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
# Write a python function to count lower case letters in a given string.
#
# SOLUTION CODE
# ============================================
def lower_ctr(str):

      lower_ctr= 0

      for i in range(len(str)):

          if str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1     

      return  lower_ctr

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(lower_ctr(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



