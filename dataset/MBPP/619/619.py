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
# Write a function to move all the numbers in it to the given string.
#
# SOLUTION CODE
# ============================================
def move_num(test_str):

  res = ''

  dig = ''

  for ele in test_str:

    if ele.isdigit():

      dig += ele

    else:

      res += ele

  res += dig

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_str, expected):
    try:
        if validate_solution(move_num(
            test_str),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



