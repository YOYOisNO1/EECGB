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
# Write a function to check if any list element is present in the given list.
#
# SOLUTION CODE
# ============================================
def check_element(test_tup, check_list):

  res = False

  for ele in check_list:

    if ele in test_tup:

      res = True

      break

  return (res) 

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_tup, check_list, expected):
    try:
        if validate_solution(check_element(
            test_tup, check_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



