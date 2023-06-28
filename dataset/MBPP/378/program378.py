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
# Write a python function to shift last element to first position in the given list.
#
# SOLUTION CODE
# ============================================
def move_first(test_list):

  test_list = test_list[-1:] + test_list[:-1]  

  return test_list

# TESTING CODE 
# ============================================
def validate_solution(actual, expected):
    return actual == expected

def driver(test_list, expected):
    try:
        if validate_solution(move_first(
            test_list),
            expected
        ):
            return "PASSED"
        return "FAILED"
    except Exception as exception_obj:
        return type(exception_obj).__name__
    



