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
# Write a python function to remove the characters which have odd index values of a given string.
#
# SOLUTION CODE
# ============================================
def odd_values_string(str):

  result = "" 

  for i in range(len(str)):

    if i % 2 == 0:

      result = result + str[i]

  return result

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(str, expected):
    try:
        if validate_solution(odd_values_string(
            str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



